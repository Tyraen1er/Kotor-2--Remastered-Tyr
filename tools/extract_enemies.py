"""Extrait l'état des lieux défensif des ennemis (UTC) : immunités, résistances, dons défensifs.

Phases :
  1: scanne tous les UTC (chitin.key + modules), filtre les hostiles (FactionID=1),
     résout dons (feat.2da), équipement (items.json), race (racialtype.2da) -> enemies.json
  2: agrège et génère datas_kotor/ennemis_defenses_etat_des_lieux.md
"""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

from pykotor.extract.installation import Installation
from pykotor.resource.formats.erf import read_erf
from pykotor.resource.formats.gff import read_gff
from pykotor.resource.formats.rim import read_rim
from pykotor.resource.formats.tlk import read_tlk
from pykotor.resource.formats.twoda import read_2da
from pykotor.resource.type import ResourceType

GAME = Path(r"C:\Program Files (x86)\Steam\steamapps\common\Knights of the Old Republic II")
ROOT = Path(__file__).resolve().parent.parent
CACHE = Path(r"C:\Users\emman\AppData\Local\Temp\opencode\itemdb")
DATAS = ROOT / "datas_kotor"
RT = ResourceType

# dons défensifs -> catégorie d'analyse (labels feat.2da)
DEF_FEATS = {
    "FEAT_FORCE_IMMUNITY_FEAR": "Immunité mentale (Peur)",
    "FEAT_FORCE_IMMUNITY_STUN": "Immunité mentale (Étourdissement)",
    "FEAT_FORCE_IMMUNITY_PARALYSIS": "Immunité mentale (Paralysie)",
    "FEAT_IMMUNITY_FEAR": "Immunité mentale (Peur)",
    "FEAT_IMMUNITY_MIND": "Immunité mentale (Esprit)",
    "FEAT_CONDITIONING": "Sauvegardes (+1)",
    "FEAT_IMPROVED_CONDITIONING": "Sauvegardes (+2)",
    "FEAT_MASTER_CONDITIONING": "Sauvegardes (+3)",
    "FEAT_TOUGHNESS": "PV/RD (Robustesse)",
    "FEAT_IMPROVED_TOUGHNESS": "PV/RD (Robustesse II)",
    "FEAT_MASTER_TOUGHNESS": "PV/RD (Robustesse III)",
    "FEAT_ARMOUR_PROFICIENCY_LIGHT": "Port d'armure légère",
    "FEAT_ARMOUR_PROFICIENCY_MEDIUM": "Port d'armure intermédiaire",
    "FEAT_ARMOUR_PROFICIENCY_HEAVY": "Port d'armure lourde",
    "FEAT_JEDI_DEFENSE": "Déviation de tirs (Jedi)",
    "FEAT_ADVANCED_JEDI_DEFENSE": "Déviation de tirs (avancée)",
    "FEAT_MASTER_JEDI_DEFENSE": "Déviation de tirs (maîtrise)",
    "FEAT_UNCANNY_DODGE_1": "Esquive instinctive I",
    "FEAT_UNCANNY_DODGE_2": "Esquive instinctive II",
    "FEAT_EVASION": "Esquive (Evasion)",
    "FEAT_IGNORE_PAIN_I": "Réduction dégâts % (Ignorer douleur I)",
    "FEAT_IGNORE_PAIN_II": "Réduction dégâts % (Ignorer douleur II)",
    "FEAT_IGNORE_PAIN_III": "Réduction dégâts % (Ignorer douleur III)",
    "FEAT_INNER_STRENGTH_I": "Réduction dégâts % (Force intérieure I)",
    "FEAT_INNER_STRENGTH_II": "Réduction dégâts % (Force intérieure II)",
    "FEAT_INNER_STRENGTH_III": "Réduction dégâts % (Force intérieure III)",
    "FEAT_WOOKIEE_TOUGHNESS": "RD naturelle (Wookiee)",
    "FEAT_WOOKIEE_TOUGHNESS_II": "RD naturelle (Wookiee II)",
    "FEAT_WOOKIEE_TOUGHNESS_III": "RD naturelle (Wookiee III)",
    "FEAT_DEFLECT": "Dévier sans sabre",
    "FEAT_MINE_IMMUNITY": "Immunité aux mines",
    "FEAT_WEAPON_FINESSE": "Finesse (défense DEX)",
    "FEAT_DROID_UPGRADE": "Upgrade droïde",
    "FEAT_DROID_SHIELD": "Bouclier droïde",
    "FEAT_COMBAT_EXPERTISE": "Expertise au combat (CA)",
    "FEAT_IMPROVED_COMBAT_EXPERTISE": "Expertise au combat (CA+)",
}

BOSS_TAGS = {
    "atris": "Atris", "a_atris": "Atris", "nihilus": "Darth Nihilus", "n_nihilus": "Darth Nihilus",
    "sion": "Darth Sion", "n_sion": "Darth Sion", "traya": "Darth Traya", "n_traya": "Darth Traya",
    "kreia": "Kreia / Traya", "visas": "Visas Marr", "n_visasmarr": "Visas Marr",
    "handmaiden": "Servante (Brianna)", "kelborn": "Kelborn", "bralor": "Bralor",
    "n_darkjedi": "Jedi Obscur", "sithlord": "Seigneur Sith", "vicious": "Vicious",
    "dxa_": "Dxun", "stormbeast": "Bête d'Orage", "rancor": "Rancor", "drexl": "Drexl",
    "kraytdragon": "Dragon Krayt", "zakkeg": "Zakkeg", "nihlius": "Darth Nihilus",
}


def twoda_rows(data: bytes) -> list[dict]:
    td = read_2da(data)
    cols = list(td.get_columns().keys()) if isinstance(td.get_columns(), dict) else list(td.get_columns())
    out = []
    for i in range(len(td)):
        row = td.get_row(i)
        d = {"_row": str(i)}
        for c in cols:
            try:
                d[c] = row.get_string(c) or ""
            except Exception:
                d[c] = ""
        out.append(d)
    return out


def gval(node, key):
    try:
        v = node[key]
        return v.value if hasattr(v, "value") else v
    except Exception:
        return None


def phase1():
    inst = Installation(GAME)
    tlk = read_tlk(GAME / "dialog.tlk")

    def tlk_text(sr):
        try:
            sr = int(sr)
        except (TypeError, ValueError):
            return ""
        if sr < 0:
            return ""
        e = tlk.get(sr)
        return (e.text or "").strip() if e else ""

    # tables de référence (pas de racialtype.2da dans TSL : Race 5 = droïde, 6 = organique)
    feat_res = inst.resource("feat", RT.TwoDA)
    feats = {r["_row"]: r for r in twoda_rows(feat_res.data)}
    def race_label(rid: int) -> str:
        return {5: "Droïde", 6: "Organique"}.get(rid, f"Race {rid}")
    class_res = inst.resource("classes", RT.TwoDA)
    classes = {r["_row"]: r for r in twoda_rows(class_res.data)}
    items = json.loads((CACHE / "items.json").read_text(encoding="utf-8"))

    from pykotor.resource.formats.key import read_key
    key = read_key(GAME / "chitin.key")
    resrefs = {str(e.resref).lower() for e in key.key_entries if str(e.restype).upper() == "UTC"}
    nmod = 0
    for mf in sorted((GAME / "modules").glob("*.mod")) + sorted((GAME / "modules").glob("*.rim")):
        try:
            arch = read_rim(mf) if mf.suffix == ".rim" else read_erf(mf)
        except Exception:
            continue
        for r in arch:
            try:
                if str(r.restype).upper() == "UTC":
                    if str(r.resref).lower() not in resrefs:
                        resrefs.add(str(r.resref).lower())
                        nmod += 1
            except Exception:
                pass
    print("UTC total (key + modules):", len(resrefs), f"(+{nmod} des modules)")

    out = {}
    bosses = {}
    for rr in sorted(resrefs):
        res = inst.resource(rr, RT.UTC)
        if not res:
            continue
        try:
            root = read_gff(res.data).root
        except Exception:
            continue
        faction = gval(root, "FactionID")
        if faction is None:
            continue
        faction = int(faction)
        tag = str(gval(root, "Tag") or rr)
        is_boss = any(k in rr.lower() or k in tag.lower() for k in BOSS_TAGS)
        if faction != 1 and not is_boss:  # 1 = hostile
            continue
        race_id = gval(root, "Race")
        race_id = int(race_id) if race_id is not None else -1
        race_label_ = race_label(race_id)
        is_droid = race_id == 5
        feats_ids = []
        if "FeatList" in root:
            for f in root["FeatList"]:
                v = gval(f, "Feat")
                if v is not None:
                    feats_ids.append(int(v))
        feat_labels = [feats.get(str(i), {}).get("constant", f"feat_{i}") for i in feats_ids]
        def_feats = sorted({DEF_FEATS[l] for l in feat_labels if l in DEF_FEATS})
        classes_l = []
        if "ClassList" in root:
            for c in root["ClassList"]:
                cid = gval(c, "Class")
                lvl = gval(c, "ClassLevel")
                classes_l.append((classes.get(str(cid), {}).get("label", str(cid)), int(lvl) if lvl else 0))
        # équipement + inventaire complet
        equip = []
        inv = []
        if "Equip_ItemList" in root:
            for s in root["Equip_ItemList"]:
                rrf = gval(s, "EquippedRes") or gval(s, "InventoryRes") or ""
                rrf = str(rrf).lower()
                if rrf:
                    equip.append(rrf)
        if "ItemList" in root:
            for s in root["ItemList"]:
                rrf = str(gval(s, "InventoryRes") or "").lower()
                if not rrf:
                    continue
                x = gval(s, "Repos_PosX")
                y = gval(s, "Repos_Posy") or gval(s, "Repos_PosY")
                drop = gval(s, "Dropable")
                rec = (rrf, int(drop) if drop is not None else -1)
                if x is None or int(x) == 0:
                    if rrf not in equip:
                        equip.append(rrf)
                else:
                    inv.append(rec)
        eq_info = []
        for itrr in equip:
            it = items.get(itrr)
            if not it:
                continue
            eq_info.append({"resref": itrr, "cat": it["categorie"], "props": it["props"]})
        inv_info = [{"resref": r, "cat": items.get(r, {}).get("categorie", "?"), "drop": d} for r, d in inv]
        # immunités / résistances venant des objets
        item_immunities, item_dr, armor_ac = [], [], None
        for info in eq_info:
            cat = info["cat"]
            if cat.startswith("Armor_Class") or "Robe" in cat or "Plating" in cat or "Zeison" in cat:
                try:
                    armor_ac = int(info.get("props") and items[info["resref"]]["baseac"] or 0)
                except Exception:
                    armor_ac = None
            for p in info["props"]:
                if "Immunité" in p:
                    m = re.search(r"\((\w+)\)", p)
                    item_immunities.append(m.group(1) if m else p)
                if "Résistance aux dégâts" in p:
                    item_dr.append(p)
        name = tlk_text(gval(root, "Firstname")) or tlk_text(gval(root, "Lastname"))
        cr = gval(root, "ChallengeRating")
        abilities = {a: int(gval(root, a) or 0) for a in ("Str", "Dex", "Con", "Int", "Wis", "Cha")}
        rec = {
            "resref": rr, "tag": tag, "nom": name,
            "race": race_label_, "droid": is_droid,
            "cr": float(cr) if cr else 0.0,
            "naturalac": int(gval(root, "NaturalAC") or 0),
            "pv": int(gval(root, "MaxHitPoints") or 0),
            "abilities": abilities,
            "classes": classes_l,
            "niveau": sum(l for _, l in classes_l),
            "feats": feat_labels, "def_feats": def_feats,
            "equip": eq_info,
            "inv": inv_info,
            "item_immunities": sorted(set(item_immunities)),
            "item_dr": item_dr,
            "faction": faction,
        }
        if faction == 1:
            out[rr] = rec
        else:
            bosses[rr] = rec
    p = CACHE / "enemies.json"
    p.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    pb = CACHE / "bosses.json"
    pb.write_text(json.dumps(bosses, ensure_ascii=False, indent=1), encoding="utf-8")
    print("ennemis hostiles:", len(out), "| boss/compagnons notables:", len(bosses), "->", p)


def phase2():
    enemies = json.loads((CACHE / "enemies.json").read_text(encoding="utf-8"))
    bosses = json.loads((CACHE / "bosses.json").read_text(encoding="utf-8"))
    es = list(enemies.values())
    n = len(es)
    droids = [e for e in es if e["droid"]]
    organics = [e for e in es if not e["droid"]]

    def zero_def(e):
        return not e["def_feats"] and not e["item_immunities"] and not e["item_dr"]

    zero_all = [e for e in es if zero_def(e)]
    zero_org = [e for e in organics if zero_def(e)]
    n_armor = sum(1 for e in es for i in e["equip"]
                  if i["cat"].startswith("Armor_Class") or "Robe" in i["cat"] or "Plating" in i["cat"] or "Zeison" in i["cat"])
    feat_count = Counter(f for e in es for f in e["def_feats"])
    imm_count = Counter(i for e in es for i in e["item_immunities"])
    n_dr = sum(1 for e in es if e["item_dr"])

    def block(e):
        eq_txt = ", ".join(f"{i['cat']} ({i['resref']})" for i in e["equip"]) if e["equip"] else "—"
        imms = sorted(set(e["def_feats"] + e["item_immunities"]))
        return "\n".join([
            f"**{e['nom'] or e['tag']}** (`{e['resref']}`) — {e['race']}, CR {e['cr']:g}, niv. {e['niveau']}, CA naturelle {e['naturalac']}",
            f"- Dons défensifs : {', '.join(e['def_feats']) if e['def_feats'] else '— AUCUN —'}",
            f"- Immunités (dons + objets) : {', '.join(imms) if imms else '— AUCUNE —'}",
            f"- Résistances objets : {'; '.join(e['item_dr']) if e['item_dr'] else '—'}",
            f"- Équipement : {eq_txt}",
            "",
        ])

    L = []
    A = L.append
    A("# État des Lieux Défensif des Ennemis — Immunités, Résistances, Dons défensifs")
    A("")
    A("> Extrait de **tous les templates de créatures hostiles** (`FactionID = 1`) des fichiers du jeu")
    A("> (chitin.key + modules, installation telle que jouée) par [`tools/extract_enemies.py`](file:///C:/Users/emman/Desktop/dev/Kotor%202%20Mods/tools/extract_enemies.py).")
    A("> Compagnon de [`ennemis_reference_kotor2.md`](ennemis_reference_kotor2.md) (autobalance, PV/CA des boss).")
    A("> **Limites :** les bonus appliqués par scripts (`OnSpawn`, dialogues) ne sont pas comptés ; stats des templates *avant* scaling autobalance.")
    A("")
    A("## 1. Vue d'ensemble")
    A("")
    A(f"- **{n}** templates hostiles : **{len(organics)}** organiques + **{len(droids)}** droïdes ({100 * len(droids) / n:.0f} %).")
    A(f"- **{len(zero_all)}/{n} ({100 * len(zero_all) / n:.0f} %)** n'ont **aucune** défense identifiée (ni don, ni immunité, ni résistance).")
    A(f"- Chez les **organiques** seulement : **{len(zero_org)}/{len(organics)} ({100 * len(zero_org) / len(organics):.0f} %)** sans rien ;")
    A(f"  **{len(organics) - len(zero_org)}** ont au moins un élément défensif (souvent un simple don de port d'armure).")
    A(f"- **Armures réellement portées : {n_armor} pièces** sur l'ensemble des {n} templates — la quasi-totalité combat à CA naturelle.")
    A("")
    A("## 2. Dons défensifs recensés (fréquence)")
    A("")
    A("| Don défensif | Ennemis | % des hostiles |")
    A("| :-- | :--: | :--: |")
    for f, c in feat_count.most_common():
        A(f"| {f} | {c} | {100 * c / n:.0f} % |")
    if not feat_count:
        A("| — aucun — | 0 | 0 % |")
    A("")
    A("> Les « Port d'armure L/I/L » (102 templates, soldats) sont des dons de **classe**, mais seuls ~15 portent réellement une armure.")
    A("")
    A("## 3. Immunités & résistances d'équipement")
    A("")
    A("| Immunité (objet) | Ennemis | Portés par |")
    A("| :-- | :--: | :-- |")
    src = Counter()
    for e in es:
        for i in e["item_immunities"]:
            hide = next((x["resref"] for x in e["equip"] if any("Immunité" in p and i in p for p in x["props"])), "?")
            src[(i, hide)] += 1
    rows = {}
    for (imm, hide), c in src.items():
        rows.setdefault(imm, []).append((hide, c))
    for imm, lst in sorted(rows.items(), key=lambda kv: -sum(c for _, c in kv[1])):
        tot = sum(c for _, c in lst)
        wearers = ", ".join(f"`{h}` ×{c}" for h, c in sorted(lst, key=lambda x: -x[1])[:3])
        A(f"| {imm} | {tot} | {wearers} |")
    A("")
    A(f"**Résistances aux dégâts d'équipement : {n_dr} ennemis sur {n} ({100 * n_dr / n:.0f} %)** — essentiellement des peaux de droïde (`Résist 15/-` physique).")
    A("")
    A("## 4. Droïdes : la seule « adaptation forcée » du jeu")
    A("")
    A("Les droïdes cumulent **trois couches d'immunités** :")
    A("1. **Raciales moteur** (vérifications `GetRacialType != RACIAL_TYPE_DROID` dans `k_inc_force.nss`) : esprit (*Peur, Folie, Stase, Dominance*), poison, drain de vie/Force, ligne *Blessure/Étranglement* ;")
    A("2. **Peaux de droïde** (`g_i_crhide008` ×61, etc.) : *Immunité Esprit + Paralysie + Poison* — redondant avec le moteur ;")
    A("3. Certaines peaux d'assaut ajoutent `Résist 15/-` contondant/perforant/tranchant.")
    A("")
    A("→ Face aux droïdes, le joueur **doit** changer de plan (pouvoirs Biologiques inutiles, *Destruction de droïde* devient requis).")
    A(f"**{len(droids)} templates** concernés ({100 * len(droids) / n:.0f} % des hostiles) — mais la réponse est *binaire* : droïde ou pas.")
    A("")
    A("## 5. Boss & duels notables — profils défensifs détaillés")
    A("")
    A("*(Y compris les UTC non hostiles au sens strict — compagnons/duels scriptés hostiles — identifiés par nom.)*")
    A("")
    notable = sorted(list(bosses.values()) + [e for e in es if e["cr"] >= 15],
                     key=lambda x: -x["cr"])[:24]
    seen = set()
    for e in notable:
        key = (e["nom"] or e["tag"], e["cr"])
        if key in seen:
            continue
        seen.add(key)
        A(block(e))
    A("## 6. Verdict — pourquoi le combat ne s'adapte jamais")
    A("")
    A(f"1. **{100 * len(zero_org) / len(organics):.0f} % des ennemis organiques n'ont aucun profil défensif** (pas d'immunité, pas de résistance, pas de don défensif utile).")
    A("2. Les seules immunités de masse sont **raciales et binaires** : droïde ou organique. Aucun spectre intermédiaire.")
    A("3. Les résistances d'équipement sont anecdotiques (peaux de droïde mises à part) et les immunités d'objets organiques se comptent **en unités** (quelques casques `a_helmet_02`).")
    A("4. Les boss majeurs (Traya, Nihilus, Jedi obscurs) ne portent **aucun objet défensif** : leur résistance vient uniquement de l'autobalance (PV/CA/sauvegardes) — jamais d'une mécanique à contourner.")
    A("5. **Conséquence gameplay** : la réponse optimale est *toujours la même* — même pouvoir, même type de dégâts, du Péragus à Malachor. Rien n'incite à :")
    A("   - diversifier les types de dégâts (aucune résistance sélective),")
    A("   - préparer un anti-soin (aucun boss ne se soigne),")
    A("   - contourner une immunité (sauf droïdes),")
    A("   - gérer une phase de bouclier (aucun boss n'active de bouclier énergétique scripté).")
    A("")
    A("## 7. Ce que ça implique pour l'overhaul (pistes, non décisions)")
    A("")
    A("- Donner des **profils défensifs thématiques par faction** (Sith = immunités mentales partielles + Résistance à la Force ; Mandaloriens = armures réelles + boucliers ; bêtes = RD physique ; assassins = Esquive).")
    A("- Utiliser les **leviers déjà existants** : peaux de créature (immunités/RD), `EffectForceResistance`, boucliers énergétiques scriptés, RD physique (nos boss `3/7/12` actés).")
    A("- Étendre la logique droïde à d'autres « familles » sans la copier binairement : résistances *partielles* (50 %) plutôt qu'immunités totales.")
    A("- Notre *Esquive Totale* accordée aux Jedi/Sith 20+ (décision §7) est déjà un premier pas : les AoE perdent de la valeur contre les élites.")
    A("")
    p = DATAS / "ennemis_defenses_etat_des_lieux.md"
    p.write_text("\n".join(L), encoding="utf-8")
    print("écrit:", p)
    print(f"{n} hostiles | {len(zero_org)}/{len(organics)} organiques sans défense | {len(droids)} droïdes")


CAT_FR = {
    "Armor_Class_4": "Arm. légère", "Armor_Class_5": "Arm. légère", "Armor_Class_6": "Arm. interm.",
    "Armor_Class_7": "Arm. interm.", "Armor_Class_8": "Arm. lourde", "Armor_Class_9": "Arm. lourde",
    "Armor_Armd_Flight_Suit": "Arm. légère (ubese)", "Armor_Zeison_Sha": "Arm. Zeison Sha",
    "Jedi_Robe": "Robe", "Jedi_Knight_Robe": "Robe", "Jedi_Master_Robe": "Robe",
    "Basic_Clothing": "Vêtements", "Miner_Uniform": "Tenue de mineur", "Slave_Outfit": "Tenue",
    "Droid_Light_Plating": "Blindage dr. léger", "Droid_Medium_Plating": "Blindage dr. moyen",
    "Droid_Heavy_Plating": "Blindage dr. lourd",
    "Creature_Hide_Item": "Peau", "Creature_Item_Slash": "Griffes", "Creature_Item_Pierce": "Crocs",
    "Creature_Weapon_Sl_Prc": "Arme naturelle",
    "Blaster_Pistol": "Pistolet", "Heavy_Blaster": "Pistolet lourd", "Hold_Out_Blaster": "Pistolet de poche",
    "Sonic_Pistol": "Pistolet sonique", "Ion_Blaster": "Blaster ion", "Disrupter_Pistol": "Disrupteur",
    "Blaster_Rifle": "Fusil", "Ion_Rifle": "Fusil ion", "Blaster_Carbine": "Carabine",
    "Sonic_Rifle": "Fusil sonique", "Disrupter_Rifle": "Fusil disrupteur",
    "Repeating_Blaster": "Blaster répétition", "Heavy_Repeating_Blaster": "Blaster lourd rép.",
    "Bowcaster": "Arbalète wookie", "Wrist_Launcher": "Lance-poignet",
    "Lightsaber": "Sabre laser", "Short_Lightsaber": "Sabre court", "Double_Bladed_Lightsaber": "Sabre double",
    "Vibro_Sword": "Vibro-épée", "Long_Sword": "Épée longue", "Short_Sword": "Épée courte",
    "Vibro_Blade": "Vibrolame", "Vibro_Double_Blade": "Vibro-lame double",
    "Quarter_Staff": "Bâton", "Stun_Baton": "Matraque sonique", "Force_Pike": "Pique de Force",
    "Gammorean_Battleaxe": "Hache de guerre", "Wookie_Warblade": "Lame wookie",
    "Mask": "Casque/Masque", "Belt": "Ceinture", "Forearm_Bands": "Brassard",
    "Implant_1": "Implant T1", "Implant_2": "Implant T2", "Implant_3": "Implant T3", "Implant_4": "Implant T4",
    "Gauntlets": "Gants", "Droid_Utility_Device": "Module droïde", "Droid_Shield": "Bouclier droïde",
    "Droid_Targeting_Computers": "Visée droïde", "Droid_Computer_Spike_Mount_x": "Pointes droïde",
    "Droid_Repair_Equipment": "Kit réparation",
    "Fragmentation_Grenades": "Grenade frag.", "Sonic_Grenade": "Grenade sonique",
    "Fire_Grenade": "Grenade incend.", "Poison_Grenade": "Grenade poison", "Ion_Grenade": "Grenade ion",
    "Cryoban_Grenade": "Grenade cryo", "Adhesive_Grenade": "Grenade adhésive",
    "Thermal_Detonator": "Détonateur thermique", "Stun_Grenades": "Grenade étourdissante",
    "Medical_Equipment": "Medpac", "Squad_Recovery_kit": "Kit de récup.",
    "Adrenaline": "Stim", "Combat_Shots": "Injection", "Trap_Kit": "Mine", "Rocket": "Fusée",
    "Aesthetic_Item": "Déco", "Data_Pad": "Datapad", "Plot_Useable_Items": "Objet de quête",
    "Stealth_Unit": "Furtivité", "Credits": "Crédits", "Components": "Composants",
    "Chemicals": "Produits chim.", "Programming_Spikes": "Pointes prog.",
    "Security_Spikes": "Pointes sécurité", "Pazaak_Card": "Cartes pazaak",
}


def phase3():
    """Tableau complet ennemi par ennemi -> section annexe de equilibrage_ennemis.md (entre marqueurs)."""
    enemies = json.loads((CACHE / "enemies.json").read_text(encoding="utf-8"))
    bosses = json.loads((CACHE / "bosses.json").read_text(encoding="utf-8"))
    ITEMS = json.loads((CACHE / "items.json").read_text(encoding="utf-8"))

    # --- sauvegardes : base par classe (cls_st_*) + modificateur de caractéristique
    inst = Installation(GAME)

    def rows_2da(res):
        td = read_2da(res.data)
        cols = list(td.get_columns().keys()) if isinstance(td.get_columns(), dict) else list(td.get_columns())
        out = []
        for i in range(len(td)):
            row = td.get_row(i)
            d = {}
            for c in cols:
                try:
                    d[c] = row.get_string(c) or ""
                except Exception:
                    d[c] = ""
            out.append(d)
        return out

    class_tables: dict[str, list[dict]] = {}
    for cr_ in rows_2da(inst.resource("classes", ResourceType.TwoDA)):
        lab = cr_.get("label", "")
        stbl = cr_.get("savingthrowtable", "")
        if lab and stbl:
            res = inst.resource(stbl.lower(), ResourceType.TwoDA)
            if res:
                class_tables[lab] = rows_2da(res)

    def _int(v, d=0):
        try:
            return int(v)
        except (TypeError, ValueError):
            return d

    def compute_saves(classes: list, ab: dict) -> tuple[int, int, int]:
        fort = ref = will = 0
        for cname, lvl in classes:
            t = class_tables.get(cname)
            if not t:
                continue
            i = max(0, min(lvl - 1, len(t) - 1))
            fort += _int(t[i].get("fortsave"))
            ref += _int(t[i].get("refsave"))
            will += _int(t[i].get("willsave"))

        def mod(k):
            s = _int(ab.get(k), 10)
            return (s - 10) // 2

        return fort + mod("Con"), ref + mod("Dex"), will + mod("Wis")

    CLASS_FR = {
        "Soldier": "Soldat", "Scout": "Éclaireur", "Scoundrel": "Voyou",
        "JediGuardian": "Gardien Jedi", "JediConsular": "Consulaire", "JediSentinel": "Sentinelle",
        "CombatDroid": "Droïde de combat", "ExpertDroid": "Droïde expert", "Minion": "Sbire",
        "TechSpecialist": "Technicien", "JediWeaponmaster": "Maître d'Armes", "JediMaster": "Maître Jedi",
        "JediWatchman": "Veilleur", "SithMarauder": "Maraudeur Sith", "SithLord": "Seigneur Sith",
        "SithAssassin": "Assassin Sith",
    }
    AB_FR = {"Str": "FOR", "Dex": "DEX", "Con": "CON", "Int": "INT", "Wis": "SAG", "Cha": "CHA"}
    ARMOR_CATS = {
        "Armor_Class_4", "Armor_Class_5", "Armor_Class_6", "Armor_Class_7", "Armor_Class_8",
        "Armor_Class_9", "Jedi_Robe", "Jedi_Knight_Robe", "Jedi_Master_Robe",
        "Armor_Armd_Flight_Suit", "Armor_Zeison_Sha", "Basic_Clothing", "Miner_Uniform",
    }

    def shield_desc(rr: str) -> str:
        it = ITEMS.get(rr, {})
        nm = it.get("nom") or rr
        desc = it.get("desc", "")
        micro = ""
        m = re.search(r"(?:Absorbe|Parade)\s*:\s*(.*?)(?:Durée|Charges|$)", desc, re.S)
        if m:
            micro = re.sub(r"\s+", " ", m.group(1)).strip().rstrip(",• ")
            micro = micro.replace(" points au total", " pts").replace(" points", " pts")
            micro = micro.replace("dégâts ", "")
        return f"{nm} ({micro})" if micro else nm

    def fam(e):
        t = (e["resref"] + " " + e["tag"]).lower()
        if e["droid"]:
            return "Droïdes"
        if any(k in t for k in ["mandalor", "bralor", "kelborn"]):
            return "Mandaloriens"
        if any(k in t for k in ["sith", "jedi", "dark", "sion", "traya", "atris", "nihilus",
                                 "revan", "malak", "visas", "kreia", "maiden", "servant"]):
            return "Sith / Jedi / Duels"
        if any(i["cat"] in ("Creature_Hide_Item",) for i in e["equip"]) or any(
            k in t for k in ["beast", "rakghoul", "kinrath", "laigrek", "hssiss", "boma", "kath",
                              "tukata", "maalrass", "wraid", "zakkeg", "drexl", "rancor", "krayt",
                              "verkaal", "mykal", "brith", "gizka", "cannok", "storm", "seabeast",
                              "tarentatek", "shyrack", "hssiss"]):
            return "Bêtes"
        return "Soldats / Divers"

    def cat_fr(c):
        return CAT_FR.get(c, c)

    SHIELD_CATS = {"Droid_Shield"}

    def row(e):
        # stats : CR, classe, CA nat, PV, sauvegardes (base classe + mod. car.), caractéristiques libellées
        cls = " / ".join(f"{CLASS_FR.get(c, c)} {l}" for c, l in e["classes"]) or "—"
        ab = e.get("abilities", {})
        ab_lbl = " ".join(f"{AB_FR[a]} {ab.get(a, '?')}" for a in ("Str", "Dex", "Con", "Int", "Wis", "Cha"))
        sv = compute_saves(e["classes"], ab)
        s1, s2, s3 = (f"{'+' if v >= 0 else ''}{v}" for v in sv)
        stats = (f"CR {e['cr']:g} · {cls} · CA nat {e['naturalac']} · PV {e.get('pv', '?')} · "
                 f"Vig {s1} / Réf {s2} / Vol {s3} · {ab_lbl}")
        # équipement (porté) — armes/armures/peaux/hides
        eq_parts = []
        for i in e["equip"]:
            if i["cat"] in SHIELD_CATS or "shield" in i["resref"]:
                continue
            lbl = cat_fr(i["cat"])
            if i["cat"] in ARMOR_CATS:
                nm_item = (ITEMS.get(i["resref"]) or {}).get("nom") or i["resref"]
                lbl = f"{lbl} ({nm_item})"
            eq_parts.append(lbl)
        equip = ", ".join(eq_parts[:6]) if eq_parts else "—"
        if len(eq_parts) > 6:
            equip += f" (+{len(eq_parts) - 6})"
        # objets utilisables : boucliers équipés + inventaire
        usable = []
        for i in e["equip"]:
            if i["cat"] in SHIELD_CATS or "shield" in i["resref"]:
                usable.append(f"**Bouclier : {shield_desc(i['resref'])}**")
        inv_g = {}
        for r in e.get("inv", []):
            key = cat_fr(r["cat"])
            inv_g[key] = inv_g.get(key, 0) + 1
        for k, c in sorted(inv_g.items(), key=lambda kv: -kv[1]):
            usable.append(f"{k} ×{c}" if c > 1 else k)
        usable_s = ", ".join(usable) if usable else "—"
        # dons
        feats = [f.replace("FEAT_", "") for f in e.get("feats", [])]
        feats_s = "; ".join(feats[:12])
        if len(feats) > 12:
            feats_s += f" (+{len(feats) - 12})"
        nom = e["nom"] or e["tag"]
        return (f"| {fam(e)} | **{nom[:30]}** (`{e['resref']}`) | {stats} | {equip} | {usable_s} | "
                f"{feats_s if feats_s else '—'} |")

    rows = []
    for e in sorted(list(enemies.values()) + list(bosses.values()),
                    key=lambda x: (fam(x), -x["cr"], x["resref"])):
        rows.append(row(e))

    header = [
        "## 9. Annexe — Tableau complet des ennemis (état actuel du jeu)",
        "",
        ">*Généré automatiquement par `tools/extract_enemies.py --phase 3` (367 templates : 313 hostiles + 54 boss/duels notables).*",
        ">*Stats : CR · classe/niveau · CA naturelle · PV de base (avant autobalance ×0,65–0,80) · **sauvegardes** (base de classe `cls_st_*` + mod. de CON/DEX/SAG — avant autobalance, hors dons et objets) · caractéristiques.*",
        "",
        "| Famille | Ennemi | Stats | Équipement porté | Objets utilisables (boucliers/inventaire) | Dons |",
        "| :-- | :-- | :-- | :-- | :-- | :-- |",
    ]
    block = "\n".join(header + rows) + "\n"
    target = ROOT / "equilibrage_ennemis.md"
    txt = target.read_text(encoding="utf-8")
    BEGIN = "<!-- TABLEAU_ENNEMIS_DEBUT -->"
    END = "<!-- TABLEAU_ENNEMIS_FIN -->"
    if BEGIN in txt and END in txt:
        pre = txt.split(BEGIN)[0]
        post = txt.split(END)[1]
        txt = pre + BEGIN + "\n" + block + END + post
    else:
        txt = txt.rstrip() + "\n\n" + BEGIN + "\n" + block + END + "\n"
    target.write_text(txt, encoding="utf-8")
    print("tableau:", len(rows), "ennemis ->", target)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--phase", type=int, required=True)
    args = ap.parse_args()
    {1: phase1, 2: phase2, 3: phase3}[args.phase]()


if __name__ == "__main__":
    main()
