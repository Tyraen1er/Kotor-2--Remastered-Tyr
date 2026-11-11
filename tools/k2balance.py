"""KotOR 2 Balance & Simulation Engine + Star Wars d20 (RCR) Converter.

Provides mathematical models for:
1. KotOR 2 enemy stat scaling (`autobalance.2da` Sets 1-5) and named solo boss benchmarks.
2. Star Wars d20 (Revised Core Rulebook) enemy stat progression (Levels 1-20).
3. DPR (Damage Per Round), Hit Chance, Save DC Success Probability, and TTK (Time-To-Kill) simulator
   to evaluate custom feats, Force powers, and weapon changes across levels.
4. Star Wars d20 (RCR) -> KotOR 2 Converter that eliminates the VP/WP split while preserving
   tactical identity (weapons, armors, powers/feats, and NPC statblocks).
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass

# ==============================================================================
# 1. AUTOBALANCE.2DA & ENEMY MATHEMATICAL MODELS (KOTOR 2 vs SW d20 RCR)
# ==============================================================================


@dataclass(frozen=True)
class AutobalanceSet:
    name: str
    vpmult: float
    tohitmult: float
    armormult: float
    damagemult: float
    savemult: float
    crmod: int
    levelmult: float = 0.75


AUTOBALANCE_SETS: dict[str, AutobalanceSet] = {
    "Set_0": AutobalanceSet("No_Auto_Balance", 0.00, 0.00, 0.00, 0.000, 0.00, 0, 0.00),
    "Set_1": AutobalanceSet("Sbire faible (Set_1)", 0.65, 0.90, 0.60, 0.065, 0.80, -3),
    "Set_2": AutobalanceSet("Soldat standard (Set_2)", 0.65, 0.90, 0.70, 0.090, 0.90, -2),
    "Set_3": AutobalanceSet("Soldat d'elite (Set_3)", 0.65, 0.95, 0.80, 0.110, 1.00, -1),
    "Set_4": AutobalanceSet("Lieutenant / Sous-boss (Set_4)", 0.70, 1.00, 0.90, 0.135, 1.00, 1),
    "Set_5": AutobalanceSet("Boss Majeur (Set_5)", 0.80, 1.10, 1.00, 0.175, 1.05, 4),
}


@dataclass(frozen=True)
class EnemyStats:
    name: str
    player_level: int
    effective_level: int
    hp: int
    defense: int
    attack: int
    damage_per_hit: float
    fort_save: int
    ref_save: int
    will_save: int


# Base archetype templates (before autobalance scaling) for generic Set_1..Set_5 enemies
BASE_ARCHETYPES: dict[str, dict[str, float]] = {
    "Set_1": {"vp": 10, "def": 12, "att": 4, "dmg": 4.5, "save": 3, "str_dmg": 1},
    "Set_2": {"vp": 14, "def": 14, "att": 6, "dmg": 5.5, "save": 4, "str_dmg": 2},
    "Set_3": {"vp": 18, "def": 16, "att": 8, "dmg": 6.5, "save": 6, "str_dmg": 3},
    "Set_4": {"vp": 24, "def": 17, "att": 9, "dmg": 8.0, "save": 7, "str_dmg": 4},
    "Set_5": {"vp": 42, "def": 19, "att": 11, "dmg": 11.0, "save": 9, "str_dmg": 6},
}

# Named solo bosses from datas_kotor/ennemis_reference_kotor2.md at their typical encounter level
NAMED_BOSS_PRESETS: dict[str, EnemyStats] = {
    "brianna": EnemyStats("La Servante / Brianna (Telos 1v1)", 8, 8, 78, 16, 11, 9.0, 6, 7, 4),
    "visas": EnemyStats("Visas Marr (Ebon Hawk 1v1)", 11, 10, 110, 23, 15, 14.0, 9, 12, 11),
    "kelborn": EnemyStats("Kelborn / Bralor (Dxun 1v1 sans Force)", 15, 14, 150, 26, 20, 20.0, 15, 12, 10),
    "atris": EnemyStats("Atris (Telos Academie 1v1)", 24, 21, 252, 43, 32, 30.0, 34, 33, 34),
    "nihilus": EnemyStats("Darth Nihilus (Ravager)", 24, 21, 420, 37, 33, 35.0, 33, 34, 32),
    "stormbeast": EnemyStats("Grande Bete d'Orage (Malachor Solo)", 26, 24, 480, 30, 35, 45.0, 36, 24, 22),
    "sion": EnemyStats("Darth Sion (Trayus 1v1 - 4 phases)", 28, 26, 1200, 48, 40, 48.0, 44, 32, 35),
    "traya": EnemyStats("Darth Traya (Noyau de Trayus 1v1)", 28, 28, 1180, 51, 42, 55.0, 42, 40, 58),
}


def kotor2_enemy_stats(level: int, set_key: str = "Set_5") -> EnemyStats:
    """Compute KotOR 2 enemy statistics at player level `L` using autobalance.2da formulas."""
    ab = AUTOBALANCE_SETS[set_key]
    base = BASE_ARCHETYPES[set_key]

    eff_lvl = 1 + max(math.floor(level * ab.levelmult) - 1, 1)
    if set_key in ("Set_1", "Set_2", "Set_3"):
        vp_scalar = max(math.floor((level + 1) * ab.vpmult) - 1, 1)
    else:
        vp_scalar = max(round(level * ab.vpmult) - 1, 1)

    hp = int(base["vp"] * vp_scalar)
    defense = int(base["def"] + math.floor(level * ab.armormult) + (2 if ab.armormult > 0 else 0))
    attack = int(base["att"] + math.floor(level * ab.tohitmult))
    dmg_mult = 1 + max(math.ceil((level - 1) * ab.damagemult), 1)
    damage = round(base["dmg"] * dmg_mult + base["str_dmg"], 1)
    save = int(base["save"] + math.floor(level * ab.savemult))

    return EnemyStats(
        name=f"KotOR 2 {ab.name} (Niv. joueur {level})",
        player_level=level,
        effective_level=eff_lvl,
        hp=hp,
        defense=defense,
        attack=attack,
        damage_per_hit=damage,
        fort_save=save + 2,
        ref_save=save,
        will_save=save + (4 if set_key == "Set_5" else 0),
    )


def swd20_enemy_stats(level: int, is_boss: bool = True) -> EnemyStats:
    """Compute Star Wars d20 (RCR) tabletop enemy statistics at character level `L` (1..20)."""
    lvl = min(max(level, 1), 20)
    if is_boss:
        # Boss / Jedi Master / Sith Lord progression
        hp = int(15 + 8.0 * lvl)  # VP (d10 + CON) + WP (CON ~15)
        defense = int(round(15 + 0.75 * lvl))  # 10 + Class + DEX + Lightsaber Defense
        attack = int(3 + 1.0 * lvl)  # Full BAB + STR/DEX + Focus
        damage = round(9.0 + 1.125 * lvl, 1)  # Lightsaber scaling 2d8 -> 6d8 + STR
        save = int(round(4 + 0.60 * lvl))
        label = f"JdR SW d20 Boss/Sith (Niv. {lvl})"
    else:
        # Standard Soldier / Trooper progression
        hp = int(11 + 5.5 * lvl)
        defense = int(round(12 + 0.45 * lvl))
        attack = int(1 + 0.85 * lvl)
        damage = round(10.5 + 0.3 * lvl, 1)
        save = int(round(2 + 0.45 * lvl))
        label = f"JdR SW d20 Soldat (Niv. {lvl})"

    return EnemyStats(
        name=label,
        player_level=level,
        effective_level=lvl,
        hp=hp,
        defense=defense,
        attack=attack,
        damage_per_hit=damage,
        fort_save=save + 1,
        ref_save=save,
        will_save=save,
    )


# ==============================================================================
# 2. COMBAT, FEAT & FORCE POWER EFFECTIVENESS SIMULATOR
# ==============================================================================


@dataclass
class BuildConfig:
    name: str
    style: str  # "single", "dual", "double", "ranged_pistol", "ranged_rifle", "unarmed"
    base_weapon_dmg: float  # Average base + upgrade damage of main hand
    offhand_weapon_dmg: float = 0.0  # Average base + upgrade damage of off-hand
    str_or_dex_mod: int = 4  # Primary attack/damage attribute modifier
    bonus_attack_mod: int = 0  # Extra attack bonus from feats/buffs (e.g. Dueling +3, Focus +1)
    bonus_flat_dmg: float = 0.0  # Extra flat damage per hit (Specialization +2, Power Attack +12)
    duel_str_scaling: float = 0.0  # Custom mod: +0.25 / +0.50 / +1.00 of STR/DEX mod added on single weapon
    extra_attacks: int = 0  # Extra attacks at full BAB (Master Speed +2, Flurry +1, Juyo +1)
    crit_range: int = 2  # Threat range count out of 20 (e.g., 20-20 -> 1, 19-20 -> 2, 17-20 -> 4)
    crit_mult: int = 2  # Critical multiplier (x2, x3, x4)
    on_hit_stun_dc: int = 0  # If > 0, evaluates stun probability against enemy Fortitude/Will


def clamp(val: float, low: float, high: float) -> float:
    return max(low, min(high, val))


def hit_probability(attack_bonus: int, target_defense: int) -> float:
    """Compute d20 hit probability with natural 1 (miss) and natural 20 (hit) rules."""
    # Roll r in 1..20 hits if r + attack_bonus >= target_defense
    needed_roll = target_defense - attack_bonus
    raw_prob = (21 - needed_roll) / 20.0
    return clamp(raw_prob, 0.05, 0.95)


def save_fail_probability(dc: int, enemy_save: int) -> float:
    """Probability that an enemy FAILS a saving throw against difficulty class `dc`."""
    # Enemy rolls 1d20 + enemy_save >= dc to succeed (1 always fails, 20 always succeeds)
    fail_count = dc - enemy_save - 1
    return clamp(fail_count / 20.0, 0.05, 0.95)


def evaluate_build_vs_enemy(level: int, build: BuildConfig, enemy: EnemyStats) -> dict[str, float]:
    """Calculate full DPR, hit chance, crit contribution, TTK, and stun chance against an enemy."""
    base_bab = level  # Standard combat progression in KotOR 2
    total_att = base_bab + build.str_or_dex_mod + build.bonus_attack_mod

    p_hit = hit_probability(total_att, enemy.defense)
    t_crit = build.crit_range / 20.0
    # In KotOR, a critical threat must be confirmed by a second roll against target Defense
    crit_factor = 1.0 + p_hit * t_crit * (build.crit_mult - 1)

    # Attribute damage bonus based on weapon style
    if build.style == "single":
        attr_dmg = build.str_or_dex_mod * (1.0 + build.duel_str_scaling)
        main_hit_dmg = build.base_weapon_dmg + attr_dmg + build.bonus_flat_dmg
        n_main = 1 + build.extra_attacks
        dpr = n_main * main_hit_dmg * p_hit * crit_factor
        total_attacks = n_main
        avg_dmg_per_hit = main_hit_dmg
    elif build.style in ("dual", "double"):
        # Vanilla KotOR 2 bug/feature: double-bladed gets 1.5x STR on main hand; dual gets 1.0x main, 0.5x offhand
        main_str_mult = 1.5 if build.style == "double" else 1.0
        off_str_mult = 0.5
        main_hit_dmg = build.base_weapon_dmg + (build.str_or_dex_mod * main_str_mult) + build.bonus_flat_dmg
        off_hit_dmg = (build.offhand_weapon_dmg or build.base_weapon_dmg) + (build.str_or_dex_mod * off_str_mult) + build.bonus_flat_dmg

        n_main = 1 + build.extra_attacks
        p_hit_main = hit_probability(total_att, enemy.defense)
        p_hit_off = hit_probability(total_att - 2, enemy.defense)  # TWF III offhand is -2

        dpr_main = n_main * main_hit_dmg * p_hit_main * (1.0 + p_hit_main * t_crit * (build.crit_mult - 1))
        dpr_off = 1 * off_hit_dmg * p_hit_off * (1.0 + p_hit_off * t_crit * (build.crit_mult - 1))
        dpr = dpr_main + dpr_off
        total_attacks = n_main + 1
        avg_dmg_per_hit = (n_main * main_hit_dmg + off_hit_dmg) / total_attacks
    else:
        # Ranged or Unarmed
        attr_dmg = build.str_or_dex_mod * (1.0 + build.duel_str_scaling) if build.style == "unarmed" else (build.str_or_dex_mod * build.duel_str_scaling)
        main_hit_dmg = build.base_weapon_dmg + attr_dmg + build.bonus_flat_dmg
        n_main = 1 + build.extra_attacks
        dpr = n_main * main_hit_dmg * p_hit * crit_factor
        total_attacks = n_main
        avg_dmg_per_hit = main_hit_dmg

    ttk = enemy.hp / dpr if dpr > 0 else 999.0

    # Stun probability per round (at least one hit lands AND triggers failed save)
    p_stun_single_hit = 0.0
    p_stun_round = 0.0
    if build.on_hit_stun_dc > 0:
        p_fail_save = save_fail_probability(build.on_hit_stun_dc, enemy.fort_save)
        p_stun_single_hit = p_hit * p_fail_save
        p_stun_round = 1.0 - ((1.0 - p_stun_single_hit) ** total_attacks)

    return {
        "attack_bonus": total_att,
        "p_hit_pct": round(p_hit * 100, 1),
        "attacks_per_round": total_attacks,
        "avg_dmg_per_hit": round(avg_dmg_per_hit, 1),
        "dpr": round(dpr, 1),
        "ttk_rounds": round(ttk, 2),
        "p_stun_hit_pct": round(p_stun_single_hit * 100, 1),
        "p_stun_round_pct": round(p_stun_round * 100, 1),
    }


# ==============================================================================
# 3. CONVERTER: JdR STAR WARS d20 (RCR) -> KOTOR 2 (OCCULTING VP / WP)
# ==============================================================================


def convert_jdr_health_to_kotor(vp: int, wp: int, level: int, role: str = "elite") -> dict[str, int | float]:
    """Convert tabletop VP/WP health into a single KotOR 2 Hit Point pool and base `.utc` VP.

    Why we occult VP/WP:
    In SWd20 RCR, Wounds (WP) equal Constitution (~12-16) and critical hits bypass Vitality (VP)
    to strike Wounds directly, causing instant one-shots. KotOR 2 merges health into a single HP
    pool, multiplies crit damage normally (x2/x3), and scales enemy HP via `autobalance.2da`
    to absorb KotOR 2's full-BAB extra attacks.
    """
    raw_tabletop_hp = vp + wp
    # In KotOR 2, players deal 2x to 4.5x more DPR than in tabletop because extra attacks
    # (Master Speed, Flurry, TWF) do not suffer the tabletop -5/-10/-15 iterative penalty.
    role_set_map = {
        "minion": ("Set_1", 1.0),
        "soldier": ("Set_2", 1.15),
        "elite": ("Set_3", 1.35),
        "subboss": ("Set_4", 1.75),
        "boss": ("Set_5", 2.50),
    }
    set_key, action_economy_factor = role_set_map.get(role, ("Set_3", 1.35))
    ab = AUTOBALANCE_SETS[set_key]

    # Scale factor grows with level (1.0x at level 6 up to action_economy_factor at level 24+)
    progression_ratio = clamp((level - 6) / 18.0, 0.0, 1.5)
    kotor_hp_multiplier = 1.0 + (action_economy_factor - 1.0) * progression_ratio
    target_kotor_hp = int(round(raw_tabletop_hp * kotor_hp_multiplier))

    # Compute the base `.utc` Vitality needed before `autobalance.2da` multiplies it at `level`
    if set_key in ("Set_1", "Set_2", "Set_3"):
        vp_scalar = max(math.floor((level + 1) * ab.vpmult) - 1, 1)
    else:
        vp_scalar = max(round(level * ab.vpmult) - 1, 1)
    utc_base_vp = max(int(round(target_kotor_hp / vp_scalar)), 8)

    return {
        "tabletop_total_hp": raw_tabletop_hp,
        "kotor_target_hp": target_kotor_hp,
        "utc_base_vp": utc_base_vp,
        "autobalance_set": set_key,
        "hp_scaling_factor": round(kotor_hp_multiplier, 2),
    }


def convert_jdr_weapon_to_kotor(
    dice_count: int,
    die_faces: int,
    crit_threat_min: int = 20,
    has_multifire: bool = False,
    has_autofire: bool = False,
) -> dict[str, str | float | int]:
    """Convert a Star Wars d20 (RCR) weapon into balanced KotOR 2 `baseitems.2da` / `.uti` stats.

    Tabletop blasters roll massive base dice (3d6=10.5 for pistols, 3d8=13.5 for rifles, 5d8=22.5
    for heavy repeating) because tabletop armor grants DR 4-9 and crits go straight to Wounds (14 WP)
    without multiplying dice.
    In KotOR 2, weapon base damage is ~55-65% of tabletop dice, while crits use standard multipliers
    (x2, or x3 to compensate for high-lethality/Multifire weapons).
    """
    tabletop_avg = dice_count * (die_faces + 1) / 2.0

    # Convert tabletop dice (e.g. 3d8 = 13.5) to KotOR 2 base damage scale (~0.55x)
    target_kotor_avg = tabletop_avg * 0.55
    # Suggest standard KotOR dice (d4, d6, d8, d10, d12)
    best_dice = (1, 8, 4.5)
    min_err = 999.0
    for n_dice in range(1, 5):
        for faces in (4, 6, 8, 10, 12):
            avg = n_dice * (faces + 1) / 2.0
            err = abs(avg - target_kotor_avg)
            if err < min_err:
                min_err = err
                best_dice = (n_dice, faces, avg)

    # Convert Wound-bypass crit and Multifire/Autofire into KotOR crit multiplier / bonus attacks
    crit_mult = 2
    special_notes = []
    if has_multifire and has_autofire:
        crit_mult = 3
        special_notes.append("Multifire/Autofire JdR -> Crit x3 ou +1 attaque à -2 via don Tir Multiple")
    elif has_multifire:
        special_notes.append("Multifire JdR -> Plage critique élargie (+1) ou +1 attaque à -4")
    elif has_autofire:
        crit_mult = 3
        special_notes.append("Autofire JdR -> Effet de zone (AoE 2m) ou dégât bonus massif")

    return {
        "tabletop_dice": f"{dice_count}d{die_faces}",
        "tabletop_avg_dmg": round(tabletop_avg, 1),
        "kotor_suggested_dice": f"{best_dice[0]}d{best_dice[1]} ({best_dice[0]}-{best_dice[0] * best_dice[1]})",
        "kotor_avg_dmg": round(best_dice[2], 1),
        "kotor_crit": f"{crit_threat_min}-20, x{crit_mult}",
        "adaptation_notes": " | ".join(special_notes) if special_notes else "Conversion standard 1:1",
    }


def convert_jdr_armor_to_kotor(
    armor_category: str,
    tabletop_dr: int,
    max_dex: int,
    armor_check_penalty: int,
) -> dict[str, str | int]:
    """Convert a Star Wars d20 (RCR) armor (which only gave Wound DR) into a viable KotOR 2 armor.

    In SWd20 RCR, armor gave 0 Defense and only applied DR to Wounds (making armor useless).
    In KotOR 2, armor gives Defense (AC) + can grant permanent Damage Immunity / Damage Reduction
    against all HP to compensate for losing Force Speed and uncapped DEX.
    """
    base_ac_map = {"light": 5, "medium": 7, "heavy": 9}
    base_ac = base_ac_map.get(armor_category.lower(), 6)

    # Convert tabletop Wound DR (2..9) into KotOR 2 all-HP Damage Reduction + Damage Immunity %
    kotor_flat_dr = max(tabletop_dr - 1, 1)
    kotor_immunity_pct = tabletop_dr * 5  # e.g. DR 4 -> 20% physical/energy immunity; DR 8 -> 40%

    return {
        "category": armor_category,
        "tabletop_stats": f"DR {tabletop_dr} (Wounds only), Max DEX +{max_dex}, ACP {armor_check_penalty}",
        "kotor_armor_ac": base_ac,
        "kotor_max_dex": max_dex,
        "kotor_flat_dr_all_hp": kotor_flat_dr,
        "kotor_damage_immunity_pct": f"{kotor_immunity_pct}% (Tranchant/Contondant/Perforant/Énergie)",
        "force_restriction_note": (
            "Dans le JdR, le malus d'armure ("
            f"{armor_check_penalty}) s'applique seulement aux pouvoirs physiques (Control), "
            "sans interdire les pouvoirs mentaux/télékinétiques (Sense/Alter)."
        ),
    }


def convert_jdr_power_to_kotor(
    vp_cost: int,
    tabletop_skill_dc: int = 20,
    is_Save_based: bool = True,
) -> dict[str, str | int]:
    """Convert a Star Wars d20 Force Skill (VP cost + skill check DC) to KotOR 2 FP cost and Save DC."""
    # In SWd20, powers cost 1 to 10 Vitality Points. In KotOR 2, powers cost 10 to 40 Force Points.
    kotor_fp_cost = max(vp_cost * 5, 10)
    return {
        "tabletop_vp_cost": vp_cost,
        "kotor_fp_cost": kotor_fp_cost,
        "tabletop_dc_mechanic": f"Jet de compétence DD {tabletop_skill_dc}",
        "kotor_save_dc_formula": (
            "DD = 5 + Niveau_Lanceur + Mod_SAG + Mod_CHA (obligatoire pour suivre savemult = 1.05*L)"
            if is_Save_based
            else "Buff direct sans jet de sauvegarde (Durée via Sp_CalcDuration)"
        ),
    }


# ==============================================================================
# 4. CLI COMMAND HANDLERS (CALLED BY k2mod.py OR DIRECTLY)
# ==============================================================================


def cmd_enemy_curve(args: argparse.Namespace) -> None:
    levels = [int(x) for x in args.levels.split(",")]
    print(f"\n=== COURBES STATISTIQUES DES ENNEMIS (Palier KotOR 2 : {args.set} vs JdR SW d20) ===")
    header = f"{'Niv(L)':>6} | {'Système':<24} | {'PV (HP)':>8} | {'Déf(CA)':>7} | {'Attaque':>7} | {'Dég/Coup':>8} | {'Vig/Réf/Vol':>13}"
    print(header)
    print("-" * len(header))
    for lvl in levels:
        k2 = kotor2_enemy_stats(lvl, args.set)
        jdr = swd20_enemy_stats(lvl, is_boss=(args.set in ("Set_4", "Set_5")))
        print(
            f"{lvl:>6} | {'KotOR 2 ' + args.set:<24} | {k2.hp:>8} | {k2.defense:>7} | "
            f"{'+' + str(k2.attack):>7} | {k2.damage_per_hit:>8.1f} | "
            f"+{k2.fort_save}/+{k2.ref_save}/+{k2.will_save}"
        )
        print(
            f"{lvl:>6} | {'JdR SW d20 (VP+WP)':<24} | {jdr.hp:>8} | {jdr.defense:>7} | "
            f"{'+' + str(jdr.attack):>7} | {jdr.damage_per_hit:>8.1f} | "
            f"+{jdr.fort_save}/+{jdr.ref_save}/+{jdr.will_save}"
        )
        print("-" * len(header))


def cmd_sim_duel(args: argparse.Namespace) -> None:
    """Compare Single-Weapon Duelist (Vanilla vs Modded STR scaling) against Two-Weapon Fighting."""
    levels = [8, 11, 15, 22, 24, 28]
    print("\n=== SIMULATION : DUEL (1 ARME) vs COMBAT À 2 ARMES vs BOSS SOLO ===")
    print(f"Bonus Duel testé : +{int(args.duel_scale * 100)}% du modificateur FOR/DEX aux dégâts (+3 Att/Déf)\n")
    header = (
        f"{'Niv':>3} | {'Cible / Boss':<26} | {'Build':<26} | "
        f"{'Toucher':>7} | {'Att/rd':>6} | {'Dég/hit':>7} | {'DPR':>6} | {'TTK (rds)':>9}"
    )
    print(header)
    print("-" * len(header))

    boss_by_level = {
        8: NAMED_BOSS_PRESETS["brianna"],
        11: NAMED_BOSS_PRESETS["visas"],
        15: NAMED_BOSS_PRESETS["kelborn"],
        22: kotor2_enemy_stats(22, "Set_5"),
        24: NAMED_BOSS_PRESETS["atris"],
        28: NAMED_BOSS_PRESETS["traya"],
    }

    for lvl in levels:
        enemy = boss_by_level[lvl]
        # Progressive player stats across the campaign (STR mod, weapon avg damage, Master Speed extra attacks)
        str_mod = 4 + (lvl - 6) // 3  # +4 at lvl 8 -> +11 at lvl 28 (with gear/buffs)
        wpn_dmg = 10.0 + (lvl - 6) * 1.4  # ~13 at lvl 8 -> ~41 at lvl 28 (upgraded lightsaber/sword)
        extra_att = 1 if lvl < 15 else (2 if lvl < 21 else 3)  # Flurry (+1) + Knight/Master Speed (+1/+2)

        builds = [
            BuildConfig(
                name="1 Arme (Duel III Vanilla)",
                style="single",
                base_weapon_dmg=wpn_dmg,
                str_or_dex_mod=str_mod,
                bonus_attack_mod=3,  # Duel III +3 Attack
                duel_str_scaling=0.0,
                extra_attacks=extra_att,
            ),
            BuildConfig(
                name=f"1 Arme (Duel +{int(args.duel_scale * 100)}% FOR)",
                style="single",
                base_weapon_dmg=wpn_dmg,
                str_or_dex_mod=str_mod,
                bonus_attack_mod=3,
                duel_str_scaling=args.duel_scale,
                extra_attacks=extra_att,
            ),
            BuildConfig(
                name="2 Armes / Double Lame",
                style="double",
                base_weapon_dmg=wpn_dmg + 2.0,
                offhand_weapon_dmg=wpn_dmg + 2.0,
                str_or_dex_mod=str_mod,
                bonus_attack_mod=0,
                extra_attacks=extra_att,
            ),
        ]

        for b in builds:
            res = evaluate_build_vs_enemy(lvl, b, enemy)
            print(
                f"{lvl:>3} | {enemy.name[:26]:<26} | {b.name:<26} | "
                f"{res['p_hit_pct']:>6.1f}% | {res['attacks_per_round']:>6} | "
                f"{res['avg_dmg_per_hit']:>7.1f} | {res['dpr']:>6.1f} | {res['ttk_rounds']:>9.2f}"
            )
        print("-" * len(header))


def cmd_sim_stun(args: argparse.Namespace) -> None:
    """Compare Unarmed Stun DC formulas (Tabletop 10 + 1/2 Lvl vs KotOR 5 + 1.0 Lvl) across levels."""
    levels = [8, 12, 16, 20, 24, 28]
    print(f"\n=== SIMULATION : PROBABILITÉ D'ÉTOURDISSEMENT (STUN MAINS NUES) CONTRE {args.set} ===")
    header = (
        f"{'Niv(L)':>6} | {'Vig Ennemi':>10} | {'DD JdR (10+L/2+Mod)':>20} | "
        f"{'Stun/hit (JdR)':>14} | {'DD KotOR (5+L+Mod)':>19} | {'Stun/hit (KotOR)':>16} | {'Stun/round (KotOR)':>18}"
    )
    print(header)
    print("-" * len(header))

    for lvl in levels:
        enemy = kotor2_enemy_stats(lvl, args.set)
        stat_mod = 4 + (lvl - 6) // 3
        dc_jdr = 10 + (lvl // 2) + stat_mod
        dc_kotor = 5 + lvl + stat_mod
        extra_att = 1 if lvl < 15 else 3

        b_jdr = BuildConfig("Mains Nues (DD JdR)", "unarmed", 12.0, str_or_dex_mod=stat_mod, extra_attacks=extra_att, on_hit_stun_dc=dc_jdr)
        b_k2 = BuildConfig("Mains Nues (DD KotOR)", "unarmed", 12.0, str_or_dex_mod=stat_mod, extra_attacks=extra_att, on_hit_stun_dc=dc_kotor)

        r_jdr = evaluate_build_vs_enemy(lvl, b_jdr, enemy)
        r_k2 = evaluate_build_vs_enemy(lvl, b_k2, enemy)

        print(
            f"{lvl:>6} | {'+' + str(enemy.fort_save):>10} | {'DD ' + str(dc_jdr):>20} | "
            f"{r_jdr['p_stun_hit_pct']:>13.1f}% | {'DD ' + str(dc_kotor):>19} | "
            f"{r_k2['p_stun_hit_pct']:>15.1f}% | {r_k2['p_stun_round_pct']:>17.1f}%"
        )


def cmd_convert_jdr(args: argparse.Namespace) -> None:
    """Run the JdR Star Wars d20 -> KotOR 2 converter on an NPC, Weapon, Armor, or Force Power."""
    print("\n=== CONVERTISSEUR JdR STAR WARS d20 (RCR) -> KOTOR 2 (Sans VP/WP) ===")
    if args.type == "npc":
        res = convert_jdr_health_to_kotor(args.vp, args.wp, args.level, args.role)
        print(f"• Entrée JdR       : {args.vp} VP + {args.wp} WP (Total = {res['tabletop_total_hp']} PV papier) | Niveau {args.level} ({args.role})")
        print(f"• Palier KotOR 2   : {res['autobalance_set']} (Multiplicateur d'économie d'actions : x{res['hp_scaling_factor']})")
        print(f"• PV Cibles en jeu : {res['kotor_target_hp']} PV")
        print(f"• Valeur .utc Base : Base Vitality = {res['utc_base_vp']} (avant multiplication par autobalance.2da)")
    elif args.type == "weapon":
        res = convert_jdr_weapon_to_kotor(args.dice, args.faces, args.crit, args.multifire, args.autofire)
        print(f"• Arme JdR Papier  : {res['tabletop_dice']} (Moyenne : {res['tabletop_avg_dmg']} dég, Crit {args.crit}-20 -> Wounds)")
        print(f"• Dés KotOR 2      : {res['kotor_suggested_dice']} (Moyenne : {res['kotor_avg_dmg']} dég)")
        print(f"• Critique KotOR 2 : {res['kotor_crit']}")
        print(f"• Adaptation       : {res['adaptation_notes']}")
    elif args.type == "armor":
        res = convert_jdr_armor_to_kotor(args.category, args.dr, args.max_dex, args.acp)
        print(f"• Armure JdR Papier: {res['tabletop_stats']}")
        print(f"• Défense KotOR 2  : +{res['kotor_armor_ac']} CA | Bonus DEX Max : +{res['kotor_max_dex']}")
        print(f"• Réduction Dégâts : RD {res['kotor_flat_dr_all_hp']} sur tous les PV (ou Immunité {res['kotor_damage_immunity_pct']})")
        print(f"• Note Pouvoirs    : {res['force_restriction_note']}")
    elif args.type == "power":
        res = convert_jdr_power_to_kotor(args.vp_cost, args.dc, not args.no_save)
        print(f"• Pouvoir JdR      : Coût {res['tabletop_vp_cost']} VP | {res['tabletop_dc_mechanic']}")
        print(f"• Coût PF KotOR 2  : {res['kotor_fp_cost']} PF")
        print(f"• Formule DD KotOR : {res['kotor_save_dc_formula']}")


def register_balance_subparsers(subparsers: argparse._SubParsersAction) -> None:
    """Register balance and converter subcommands into an existing argparse subparsers object."""
    p_curve = subparsers.add_parser("enemy-curve", help="Afficher les courbes de stats ennemies (KotOR 2 vs JdR SW d20)")
    p_curve.add_argument("-s", "--set", default="Set_5", choices=["Set_1", "Set_2", "Set_3", "Set_4", "Set_5"], help="Palier autobalance.2da")
    p_curve.add_argument("-l", "--levels", default="6,8,11,15,19,22,24,28", help="Niveaux à calculer (séparés par des virgules)")
    p_curve.set_defaults(func=cmd_enemy_curve)

    p_duel = subparsers.add_parser("sim-duel", help="Simuler l'efficacité du don Duel (+%% FOR/DEX) face au Combat à 2 armes")
    p_duel.add_argument("--duel-scale", type=float, default=1.0, help="Bonus FOR/DEX ajouté aux dégâts en Duel (ex: 0.5 pour +50%%, 1.0 pour +100%%)")
    p_duel.set_defaults(func=cmd_sim_duel)

    p_stun = subparsers.add_parser("sim-stun", help="Simuler la probabilité d'étourdissement (Stun Mains Nues) selon la formule de DD")
    p_stun.add_argument("-s", "--set", default="Set_3", choices=["Set_1", "Set_2", "Set_3", "Set_4", "Set_5"], help="Palier ennemi cible")
    p_stun.set_defaults(func=cmd_sim_stun)

    p_conv = subparsers.add_parser("convert-jdr", help="Convertir un élément du JdR Star Wars d20 (RCR) vers KotOR 2 en occultant VP/WP")
    conv_sub = p_conv.add_subparsers(dest="type", required=True)

    c_npc = conv_sub.add_parser("npc", help="Convertir les VP/WP d'un PNJ/Boss JdR en PV et Base Vitality KotOR 2")
    c_npc.add_argument("--vp", type=int, required=True, help="Vitality Points dans le JdR")
    c_npc.add_argument("--wp", type=int, required=True, help="Wound Points (CON) dans le JdR")
    c_npc.add_argument("--level", type=int, default=15, help="Niveau de rencontre dans KotOR 2")
    c_npc.add_argument("--role", default="boss", choices=["minion", "soldier", "elite", "subboss", "boss"])
    c_npc.set_defaults(func=cmd_convert_jdr)

    c_wpn = conv_sub.add_parser("weapon", help="Convertir une arme JdR (ex: 3d8 Multifire) en arme KotOR 2")
    c_wpn.add_argument("--dice", type=int, required=True, help="Nombre de dés (ex: 3 pour 3d8)")
    c_wpn.add_argument("--faces", type=int, required=True, help="Faces du dé (ex: 8 pour 3d8)")
    c_wpn.add_argument("--crit", type=int, default=20, help="Seuil critique minimum (ex: 19 pour 19-20)")
    c_wpn.add_argument("--multifire", action="store_true", help="Possède le mode Multifire dans le JdR")
    c_wpn.add_argument("--autofire", action="store_true", help="Possède le mode Autofire dans le JdR")
    c_wpn.set_defaults(func=cmd_convert_jdr)

    c_arm = conv_sub.add_parser("armor", help="Convertir une armure JdR (DR sur Wounds) en armure KotOR 2")
    c_arm.add_argument("--category", default="heavy", choices=["light", "medium", "heavy"])
    c_arm.add_argument("--dr", type=int, required=True, help="Réduction de Dégâts (DR) dans le JdR")
    c_arm.add_argument("--max-dex", type=int, default=1, help="Bonus DEX Max")
    c_arm.add_argument("--acp", type=int, default=-6, help="Malus d'armure aux compétences (ACP)")
    c_arm.set_defaults(func=cmd_convert_jdr)

    c_pwr = conv_sub.add_parser("power", help="Convertir un pouvoir JdR (Coût VP) en pouvoir KotOR 2 (Coût PF & DD)")
    c_pwr.add_argument("--vp-cost", type=int, required=True, help="Coût en Points de Vitalité (VP) dans le JdR")
    c_pwr.add_argument("--dc", type=int, default=20, help="DD du test de compétence dans le JdR")
    c_pwr.add_argument("--no-save", action="store_true", help="Le pouvoir est un buff sans jet de sauvegarde ennemi")
    c_pwr.set_defaults(func=cmd_convert_jdr)


def main() -> None:
    parser = argparse.ArgumentParser(description="KotOR 2 Balance Simulator & SWd20 Converter")
    sub = parser.add_subparsers(dest="cmd", required=True)
    register_balance_subparsers(sub)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
