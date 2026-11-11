"""Extract ALL game equipment (items, stats, loot rules, sure locations) into datas_kotor/.

Phases (run with --phase):
  1: dump needed 2DA tables to JSON/CSV cache
  2: build item database (all UTI: names, categories, base stats, decoded properties) -> items.json
  3: scan modules (.mod/.rim) for fixed placements (GIT placeables, UTC creatures, UTM merchants) -> locations.json
  4: random-loot mapping (k_inc_treas_k2 prefix system -> level bands) -> loot.json
  5: generate markdown tables into datas_kotor/
"""
from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path

from pykotor.extract.installation import Installation
from pykotor.resource.formats.erf import read_erf
from pykotor.resource.formats.gff import read_gff
from pykotor.resource.formats.rim import read_rim
from pykotor.resource.formats.tlk import read_tlk
from pykotor.resource.formats.twoda import read_2da
from pykotor.resource.generics.uti import read_uti, UTI, UTIProperty
from pykotor.resource.type import ResourceType

GAME = Path(r"C:\Program Files (x86)\Steam\steamapps\common\Knights of the Old Republic II")
ROOT = Path(__file__).resolve().parent.parent
CACHE = Path(r"C:\Users\emman\AppData\Local\Temp\opencode\itemdb")
DATAS = ROOT / "datas_kotor"

TWO_DA_TABLES = [
    "itemprops", "itempropdef", "itemvalue", "iprp_amount", "iprp_abilities",
    "iprp_acmodtype", "iprp_damagecost", "iprp_damagetype", "iprp_immunity",
    "iprp_saveelement", "iprp_savingthrow", "iprp_protection", "iprp_onhit",
    "iprp_combatdam", "iprp_feats", "iprp_poison", "iprp_costtable",
    "iprp_attribcost", "iprp_bonuscost", "iprp_durcost", "iprp_srcost",
    "iprp_lightcost", "iprp_meleecost", "iprp_spellshl", "iprp_soakcost",
    "iprp_resistcost", "iprp_weightcost", "iprp_weightinc", "iprp_spellcost",
    "iprp_spelllvcost", "iprp_base1", "iprp_damagepen", "iprp_monsterdam",
]

RT = ResourceType


def twoda_to_dicts(data: bytes) -> list[dict]:
    td = read_2da(data)
    cols = list(td.get_columns().keys()) if isinstance(td.get_columns(), dict) else list(td.get_columns())
    out = []
    for i in range(len(td)):
        row = td.get_row(i)
        lab = row.label() if callable(getattr(row, "label", None)) else str(getattr(row, "label", i))
        d = {"_row": str(lab)}
        for c in cols:
            try:
                d[c] = row.get_string(c) or ""
            except Exception:
                d[c] = ""
        out.append(d)
    return out


class Ctx:
    def __init__(self):
        self.inst = Installation(GAME)
        self.tlk = read_tlk(GAME / "dialog.tlk")
        CACHE.mkdir(parents=True, exist_ok=True)
        self._prop_cache = None

    def tlk_text(self, strref) -> str:
        try:
            strref = int(strref)
        except (TypeError, ValueError):
            return ""
        if strref < 0:
            return ""
        e = self.tlk.get(strref)
        return (e.text or "").strip() if e else ""

    def twoda(self, name: str) -> list[dict]:
        p = CACHE / f"{name}.json"
        if p.exists():
            return json.loads(p.read_text(encoding="utf-8"))
        res = self.inst.resource(name, RT.TwoDA)
        rows = twoda_to_dicts(res.data) if res else []
        p.write_text(json.dumps(rows, ensure_ascii=False), encoding="utf-8")
        return rows


# ---------------------------------------------------------------- phase 1
def phase1(ctx: Ctx):
    for t in TWO_DA_TABLES:
        rows = ctx.twoda(t)
        print(f"[{t}] {len(rows)} lignes")
    print("cache ->", CACHE)


# ---------------------------------------------------------------- phase 2
# subtype table per property label (Kotor Tool mapping, main families)
SUBTYPE_TABLES = {
    "Ability_Bonus": "iprp_abilities",
    "Immunity": "iprp_immunity",
    "SavingThrow_Bonus": "iprp_savingthrow",
    "Damage_Bonus": "iprp_damagetype",
    "Damage_Resistance": "iprp_damagetype",
    "Damage_Vulnerability": "iprp_damagetype",
    "Skill_Bonus": None,
    "AC_Bonus_vs_Damage_Type": "iprp_damagetype",
    "Attack_Bonus_vs_Damage_Type": "iprp_damagetype",
}
PROP_LABEL_FR = {
    "Ability_Bonus": "Bonus de caractéristique",
    "AC_Bonus": "Bonus de CA",
    "AC_Bonus_vs_Alignment_Group": "CA vs alignement",
    "AC_Bonus_vs_Damage_Type": "CA vs type de dégâts",
    "AC_Bonus_vs_Racial_Group": "CA vs groupe racial",
    "Enhancement_Bonus": "Bonus d'enchantement",
    "Enhancement_Bonus_vs__Alignment_Group": "Enchantement vs alignement",
    "Enchancement_Bonus_vs_Racial_Group": "Enchantement vs race",
    "Damage_Bonus": "Bonus de dégâts",
    "Damage_Bonus_vs_Alignment_Group": "Dégâts vs alignement",
    "Damage_Bonus_vs_Racial_Group": "Dégâts vs race",
    "Damage_Vulnerability": "Vulnérabilité aux dégâts",
    "Damage_Reduction": "Réduction de dégâts",
    "Damage_Resistance": "Résistance aux dégâts",
    "Immunity": "Immunité",
    "SavingThrow_Bonus": "Bonus aux sauvegardes",
    "Keen": "Arme acérée (critique élargi)",
    "Massive_Crits": "Critiques massifs",
    "Attack_Bonus": "Bonus d'attaque",
    "Attack_Bonus_vs_Alignment_Group": "Attaque vs alignement",
    "Attack_Bonus_vs_Racial_Group": "Attaque vs race",
    "Attack_Bonus_vs_Damage_Type": "Attaque vs type de dégâts",
    "Force_Point_Bonus": "Bonus de PF",
    "Vitality_Point_Bonus": "Bonus de PV",
    "Regeneration": "Régénération",
    "Skill_Bonus": "Bonus de compétence",
    "Strength_Bonus": "Bonus de Force",
    "Dexterity_Bonus": "Bonus de Dextérité",
    "Constitution_Bonus": "Bonus de Constitution",
    "Intelligence_Bonus": "Bonus d'Intelligence",
    "Wisdom_Bonus": "Bonus de Sagesse",
    "Charisma_Bonus": "Bonus de Charisme",
    "Force_Resistant": "Résistance à la Force",
    "Haste": "Célérité",
    "Additional_Attack": "Attaque supplémentaire",
    "Stun": "Étourdissement (on-hit)",
    "OnHitCastSpell": "Effet au contact (sort)",
    "Weight_Increase": "Poids augmenté",
    "Weight_Reduction": "Poids réduit",
    "Upgrade": "Amélioration (slot)",
    "Bludgeoning_Weapon": None,
}


class PropDecoder:
    def __init__(self, ctx: Ctx):
        self.ctx = ctx
        self.itemprops = ctx.twoda("itemprops")
        self.costtables = ctx.twoda("iprp_costtable")
        self.subs = {n: ctx.twoda(n) for n in set(SUBTYPE_TABLES.values()) if n}
        # per-table label lookup from iprp_costtable rows (row -> table name)
        self.cost_by_name = {}
        for r in self.costtables:
            self.cost_by_name[r["_row"]] = r

    def decode(self, ip: UTIProperty) -> str:
        pn = ip.property_name
        row = self.itemprops[pn] if 0 <= pn < len(self.itemprops) else None
        label_en = (row.get("label") or "") if row else ""
        label = PROP_LABEL_FR.get(label_en, label_en or f"Propriété#{pn}")
        # French display name from itemprops stringref if available
        fr = self.ctx.tlk_text(row.get("stringref")) if row else ""
        if fr and len(fr) < 40:
            label = fr
        sub = ""
        tname = SUBTYPE_TABLES.get(label_en)
        if tname and self.subs.get(tname) and ip.subtype is not None and ip.subtype >= 0:
            t = self.subs[tname]
            if ip.subtype < len(t):
                lab = t[ip.subtype].get("label", "")
                sub = lab
        # magnitude: resolve cost table name then row label
        mag = ""
        try:
            ct = ip.cost_table
            cv = ip.cost_value
            if ct and ct >= 0 and cv is not None and cv >= 0:
                ctrow = self.costtables[ct] if ct < len(self.costtables) else None
                if ctrow:
                    tname2 = ctrow.get("name") or ctrow.get("label") or ""
                    t2 = self.ctx.twoda(tname2) if tname2 else []
                    if t2 and cv < len(t2):
                        lab2 = t2[cv].get("label") or t2[cv].get("name") or ""
                        mag = lab2 or str(cv)
                    else:
                        mag = str(cv)
        except Exception:
            mag = str(ip.cost_value) if ip.cost_value is not None else ""
        parts = [label]
        if sub:
            parts.append(f"({sub})")
        if mag:
            parts.append(mag if mag.startswith(("+", "-")) else f"+{mag}")
        return " ".join(parts)


def load_baseitems(ctx: Ctx) -> dict[int, dict]:
    p = CACHE / "baseitems.json"
    if p.exists():
        return {int(k): v for k, v in json.loads(p.read_text(encoding="utf-8")).items()}
    res = ctx.inst.resource("baseitems", RT.TwoDA)
    rows = twoda_to_dicts(res.data)
    out = {}
    for r in rows:
        try:
            out[int(r["_row"])] = r
        except ValueError:
            pass
    p.write_text(json.dumps(out, ensure_ascii=False), encoding="utf-8")
    return out


def load_feats(ctx: Ctx) -> dict[str, str]:
    rows = ctx.twoda("feat")
    return {r["_row"]: r.get("label", "") for r in rows}


def phase2(ctx: Ctx):
    baseitems = load_baseitems(ctx)
    feats = load_feats(ctx)
    dec = PropDecoder(ctx)

    from pykotor.resource.formats.key import read_key
    key = read_key(GAME / "chitin.key")
    resrefs = {str(e.resref).lower() for e in key.key_entries if str(e.restype).upper() == "UTI"}
    print("UTI in chitin.key:", len(resrefs))
    for mf in sorted((GAME / "modules").glob("*.rim")) + sorted((GAME / "modules").glob("*.mod")):
        try:
            arch = read_rim(mf) if mf.suffix == ".rim" else read_erf(mf)
        except Exception:
            continue
        for r in arch:
            try:
                if str(r.restype).upper() == "UTI":
                    resrefs.add(str(r.resref).lower())
            except Exception:
                pass
    print("UTI total (key + modules):", len(resrefs))

    items = {}
    for i, rr in enumerate(sorted(resrefs)):
        res = ctx.inst.resource(rr, RT.UTI)
        if not res:
            continue
        try:
            uti: UTI = read_uti(res.data)
        except Exception as ex:
            print("  parse fail", rr, ex)
            continue
        bi = baseitems.get(uti.base_item, {})
        name = ctx.tlk_text(uti.name.stringref) if uti.name is not None else ""
        desc = ctx.tlk_text(uti.description.stringref) if uti.description is not None else ""
        props = []
        for p in uti.properties:
            try:
                props.append(dec.decode(p))
            except Exception:
                props.append(f"propriété #{p.property_name}")
        reqfeats = []
        for k in ("reqfeat0", "reqfeat1", "reqfeat2", "reqfeat3", "reqfeat4"):
            fv = bi.get(k, "")
            if fv and fv not in ("", "****"):
                try:
                    reqfeats.append(feats.get(str(int(fv)), fv))
                except ValueError:
                    reqfeats.append(fv)
        items[rr] = {
            "resref": rr,
            "nom": name,
            "baseitem": uti.base_item,
            "categorie": bi.get("label", ""),
            "itemclass": bi.get("itemclass", ""),
            "itemtype": bi.get("itemtype", ""),
            "reqfeats": reqfeats,
            "baseac": bi.get("baseac", ""),
            "dexbonus": bi.get("dexbonus", ""),
            "numdice": bi.get("numdice", ""),
            "dietoroll": bi.get("dietoroll", ""),
            "critthreat": bi.get("critthreat", ""),
            "crithitmult": bi.get("crithitmult", ""),
            "desc": desc[:500],
            "props": props,
            "cout": uti.cost,
            "stack": uti.stack_size,
        }
        if i % 250 == 0:
            print("  ...", i)
    out = CACHE / "items.json"
    out.write_text(json.dumps(items, ensure_ascii=False, indent=1), encoding="utf-8")
    print("items:", len(items), "->", out)


# ---------------------------------------------------------------- phase 3
def as_str(v) -> str:
    """Tolerant conversion of GFF values (ResRef objects, ints, strings)."""
    if v is None:
        return ""
    if isinstance(v, str):
        return v
    for attr in ("resref", "value"):
        if hasattr(v, attr):
            try:
                return str(getattr(v, attr))
            except Exception:
                pass
    s = str(v)
    # ResRef(g_i_parts01) -> g_i_parts01
    m = re.match(r"^ResRef\((.*)\)$", s)
    return m.group(1) if m else s


def as_int(v, default=-1) -> int:
    try:
        return int(as_str(v))
    except (TypeError, ValueError):
        try:
            return int(v)
        except Exception:
            return default


def phase3(ctx: Ctx):
    placements: dict[str, list[dict]] = {}
    module_names: dict[str, str] = {}

    def add(item: str, module: str, kind: str, owner: str, qty: int, extra: str = ""):
        placements.setdefault(item.lower(), []).append(
            {"module": module, "type": kind, "owner": owner, "qte": qty, "info": extra}
        )

    mdir = GAME / "modules"
    files = sorted(mdir.glob("*.mod")) + sorted(mdir.glob("*.rim")) + sorted(mdir.glob("*.erf"))
    for mf in files:
        modname = re.sub(r"_s$", "", mf.stem)
        try:
            arch = read_rim(mf) if mf.suffix == ".rim" else read_erf(mf)
        except Exception as ex:
            print("skip", mf.name, ex)
            continue
        placed: set[str] | None = None  # None = unknown (no GIT parsed)
        for r in arch:
            try:
                rt = str(r.restype).upper()
                rr = str(r.resref)
            except Exception:
                continue
            if rt not in ("GIT", "UTC", "UTM", "UTP", "ARE"):
                continue
            try:
                data = arch.get(rr, r.restype)
            except Exception:
                data = None
            if not data:
                continue
            try:
                root = read_gff(data).root
            except Exception:
                continue
            if rt == "GIT":
                for holder in ("Placeable List", "Creature List"):
                    try:
                        lst = root[holder]
                        ents = list(iter(lst))
                    except Exception:
                        continue
                    if placed is None:
                        placed = set()
                    for ent in ents:
                        try:
                            placed.add(as_str(ent["TemplateResRef"]).lower())
                        except Exception:
                            pass
                continue
            if rt == "ARE":
                try:
                    ls = root["Name"]
                    sr = getattr(ls, "stringref", -1)
                    fr = ctx.tlk_text(sr)
                    if fr:
                        module_names.setdefault(modname, fr)
                except Exception:
                    pass
                continue
            # UTP / UTC / UTM : templates with inventory
            is_placed = placed is None or rr.lower() in placed or any(
                rr.lower().startswith(p) for p in placed if p
            )
            kind = {"UTP": "conteneur", "UTC": "créature", "UTM": "marchand"}[rt]
            try:
                tag = as_str(root["Tag"]) if "Tag" in root else rr
            except Exception:
                tag = rr
            try:
                ientries = list(iter(root["ItemList"]))
            except Exception:
                continue
            for it3 in ientries:
                try:
                    inv = as_str(it3["InventoryRes"]).lower()
                    if not inv:
                        continue
                    if "Infinite" in it3:
                        inf = as_int(it3["Infinite"], 0)
                        add(inv, modname, kind, tag, 1, f"infini={'oui' if inf else 'non'}")
                    else:
                        drop = as_int(it3["Dropable"], -1) if "Dropable" in it3 else -1
                        x = as_int(it3["Repos_PosX"], 0) if "Repos_PosX" in it3 else 0
                        y = as_int(it3["Repos_Posy"], 0) if "Repos_Posy" in it3 else 0
                        eq = "équipé" if rt == "UTC" and x == 0 and y == 0 else ""
                        info = "; ".join(s for s in [f"drop={'oui' if drop == 1 else 'non'}" if drop >= 0 else "", eq] if s)
                        add(inv, modname, kind, tag, 1, info)
                except Exception:
                    pass

    out = CACHE / "locations.json"
    out.write_text(
        json.dumps({"module_names": module_names, "placements": placements}, ensure_ascii=False),
        encoding="utf-8",
    )
    total = sum(len(v) for v in placements.values())
    print("placements:", total, "| items distincts:", len(placements), "| modules nommés:", len(module_names))


# ---------------------------------------------------------------- phase 4
PREFIXES = {
    "w_blaste_": ("Arme à distance", "Pistolet blaster", 1),
    "w_brifle_": ("Arme à distance", "Fusil blaster", 1),
    "w_melee_": ("Arme de mêlée", "Mêlée", 1),
    "u_r_targ_": ("Amélioration", "Lunette de visée", 2),
    "u_r_firi_": ("Amélioration", "Chambre de tir", 2),
    "u_r_powe_": ("Amélioration", "Pack d'énergie (distance)", 2),
    "u_m_grip_": ("Amélioration", "Poignée (mêlée)", 2),
    "u_m_edge_": ("Amélioration", "Lame (mêlée)", 2),
    "u_m_cell_": ("Amélioration", "Cellule d'énergie (mêlée)", 2),
    "u_a_over_": ("Amélioration", "Overlay (armure)", 2),
    "u_a_unde_": ("Amélioration", "Underlay (armure)", 2),
    "u_l_emit_": ("Amélioration", "Émetteur (sabre)", 7),
    "u_l_lens_": ("Amélioration", "Lentille (sabre)", 7),
    "u_l_cell_": ("Amélioration", "Cellule d'énergie (sabre)", 7),
    "u_l_crys_": ("Amélioration", "Cristal (sabre)", 6),
    "u_l_colo_": ("Amélioration", "Cristal de couleur", 8),
    "a_belt_": ("Accessoire", "Ceinture", 2),
    "a_gloves_": ("Accessoire", "Gants", 2),
    "a_helmet_": ("Accessoire", "Casque/Masque", 2),
    "a_robe_": ("Armure", "Robe Jedi", 2),
    "a_light_": ("Armure", "Légère", 2),
    "a_medium_": ("Armure", "Intermédiaire", 2),
    "a_heavy_": ("Armure", "Lourde", 2),
    "e_imp1_": ("Implant", "Niveau 1", 3),
    "e_imp2_": ("Implant", "Niveau 2", 3),
    "e_imp3_": ("Implant", "Niveau 3", 3),
    "e_imp4_": ("Implant", "Niveau 4", 3),
    "d_utility_": ("Droïde", "Utilitaire", 2),
    "d_interface_": ("Droïde", "Interface", 2),
    "d_armor_": ("Droïde", "Blindage", 2),
    "d_shield_": ("Droïde", "Bouclier", 4),
    "d_device_": ("Droïde", "Arme spéciale", 2),
}
# curve id: how k_inc_treas_k2 converts itemLevel -> tier number
# 1: tier = itemLevel (weapons); 2: tier = itemLevel/2; 3: tier = itemLevel/3;
# 4: tier = itemLevel/3 (min 1, minus 4 if >6); 6: tier = itemLevel-5; 7: (itemLevel-6)/2; 8: special color


def phase4(ctx: Ctx):
    items = json.loads((CACHE / "items.json").read_text(encoding="utf-8"))
    loot = {}
    for rr, it in items.items():
        m = re.match(r"^(.*?_)(\d+)$", rr)
        if not m:
            continue
        prefix, num = m.group(1), int(m.group(2))
        if prefix not in PREFIXES:
            continue
        cat, sub, curve = PREFIXES[prefix]
        # invert: minimal PC level such that tier can be reached. itemLevel = PC + Random(8)-5 -> min itemLevel = PC-4
        if curve == 1:
            plvl_min = num + 4
        elif curve == 2:
            plvl_min = num * 2 + 4
        elif curve == 3:
            plvl_min = num * 3 + 4
        elif curve == 4:
            # shield: tier = lvl/3, >6 -> -4 ; keep simple
            plvl_min = num * 3 + 4 if num <= 6 else (num + 4) * 3 + 4
        elif curve == 6:
            plvl_min = num + 5 + 4
        elif curve == 7:
            plvl_min = (num * 2 + 6) + 4
        elif curve == 8:
            plvl_min = 10
        else:
            plvl_min = None
        loot[rr] = {
            "cat": cat, "sub": sub, "tier": num,
            "plvl_normal": min(30, max(1, plvl_min)) if plvl_min is not None else None,
            "plvl_rare": min(30, max(1, plvl_min - 5)) if plvl_min is not None else None,
            "nom": it.get("nom", ""),
        }
    out = CACHE / "loot.json"
    out.write_text(json.dumps(loot, ensure_ascii=False, indent=1), encoding="utf-8")
    print("loot entries:", len(loot), "->", out)


def phase5(ctx: Ctx):
    items = json.loads((CACHE / "items.json").read_text(encoding="utf-8"))
    loot = json.loads((CACHE / "loot.json").read_text(encoding="utf-8"))
    locdata = json.loads((CACHE / "locations.json").read_text(encoding="utf-8"))
    module_names = locdata["module_names"]
    placements = locdata["placements"]
    DATAS.mkdir(exist_ok=True)

    def clean_mag(p: str) -> str:
        for pre in ("Penalty_", "Resist_", "Bonus_", "Cost_"):
            p = p.replace(" +" + pre, " +").replace(pre, "")
        p = p.replace("+>=", "≥ ").replace("+Single_Use", "(usage unique)")
        p = p.replace(">=12", "≥ 12").replace(">=14", "≥ 14").replace(">=16", "≥ 16").replace(">=18", "≥ 18")
        return p

    def props_of(rr: str) -> str:
        ps = [clean_mag(x) for x in items.get(rr, {}).get("props", [])]
        if len(ps) > 6:
            return ", ".join(ps[:6]) + f" *(+{len(ps) - 6} autres, slots d'amélioration)*"
        return ", ".join(ps) if ps else "—"

    def loot_of(rr: str) -> str:
        l = loot.get(rr)
        if not l:
            return "—"
        parts = [f"palier {l['tier']}"]
        if l.get("plvl_normal"):
            parts.append(f"niv. {l['plvl_normal']}+")
        if l.get("plvl_rare") and l["plvl_rare"] != l.get("plvl_normal"):
            parts.append(f"(rare dès {l['plvl_rare']})")
        return " ".join(parts)

    def locs_of(rr: str) -> str:
        ps = placements.get(rr, [])
        if not ps:
            return "—"
        bymod: dict[str, int] = {}
        for p in ps:
            m = p["module"]
            bymod[m] = bymod.get(m, 0) + 1
        mods = sorted(bymod, key=lambda m: -bymod[m])
        out = []
        for m in mods[:4]:
            fr = module_names.get(m, m)
            fr = fr if len(fr) <= 26 else fr[:24] + "…"
            out.append(f"{fr} ×{bymod[m]}" if bymod[m] > 1 else fr)
        s = ", ".join(out)
        if len(mods) > 4:
            s += f" (+{len(mods) - 4} lieux)"
        return s

    def reqs_of(rr: str) -> str:
        it = items.get(rr, {})
        r = []
        if it.get("reqfeats"):
            r.append(" / ".join(it["reqfeats"]).replace("FEAT_ARMOUR_PROFICIENCY_", "Port d'armure ").lower()
                     .replace("FEAT_", ""))
        for p in it.get("props", []):
            if "Restriction de caractéristique" in p:
                m = re.search(r">=(\d+)", p)
                r.append("Caract. ≥ " + m.group(1) if m else "Caract. requise")
            if "Restriction d'alignement" in p:
                r.append("Alignement")
            if "Restriction PJ" in p:
                r.append("PNJ only")
        return ", ".join(r) if r else "—"

    # category -> file/section mapping
    CATS = {
        "armes_distance": {
            "title": "Équipement — Armes à Distance (pistolets, fusils, grenades, fusées)",
            "cats": ["Adhesive_Grenade", "Blaster_Carbine", "Blaster_Pistol", "Blaster_Rifle", "Bowcaster",
                      "Cryoban_Grenade", "Disrupter_Pistol", "Disrupter_Rifle", "Fire_Grenade",
                      "Fragmentation_Grenades", "Heavy_Blaster", "Heavy_Repeating_Blaster", "Hold_Out_Blaster",
                      "Ion_Blaster", "Ion_Grenade", "Ion_Rifle", "Poison_Grenade", "Repeating_Blaster",
                      "Rocket", "Sonic_Grenade", "Sonic_Pistol", "Sonic_Rifle", "Stun_Grenades",
                      "Thermal_Detonator", "Wrist_Launcher"],
            "stats": "weapon",
        },
        "armes_melee": {
            "title": "Équipement — Armes de Mêlée (vibro-armes, sabres laser, haches)",
            "cats": ["Double_Bladed_Lightsaber", "Double_Bladed_Sword", "Force_Pike", "Gammorean_Battleaxe",
                      "Lightsaber", "Long_Sword", "Quarter_Staff", "Short_Lightsaber", "Short_Sword",
                      "Stun_Baton", "Vibro_Blade", "Vibro_Double_Blade", "Vibro_Sword", "Wookie_Warblade",
                      "Creature_Item_Slash", "Creature_Item_Pierce", "Creature_Weapon_Sl_Prc"],
            "stats": "weapon",
        },
        "armures": {
            "title": "Équipement — Armures & Robes (légères / intermédiaires / lourdes / droïdes)",
            "cats": ["Armor_Class_4", "Armor_Class_5", "Armor_Class_6", "Armor_Class_7", "Armor_Class_8",
                      "Armor_Class_9", "Armor_Armd_Flight_Suit", "Armor_Zeison_Sha", "Basic_Clothing",
                      "Jedi_Robe", "Jedi_Knight_Robe", "Jedi_Master_Robe", "Miner_Uniform", "Slave_Outfit",
                      "Droid_Light_Plating", "Droid_Medium_Plating", "Droid_Heavy_Plating",
                      "Creature_Hide_Item"],
            "stats": "armor",
        },
        "accessoires": {
            "title": "Équipement — Accessoires (ceintures, masques, gants, brassards, implants, droïdes, consommables)",
            "cats": ["Belt", "Mask", "Gauntlets", "Forearm_Bands", "Implant_1", "Implant_2", "Implant_3",
                      "Implant_4", "Stealth_Unit", "Droid_Utility_Device", "Droid_Shield",
                      "Droid_Targeting_Computers", "Droid_Computer_Spike_Mount_x", "Droid_Repair_Equipment",
                      "Medical_Equipment", "Adrenaline", "Combat_Shots", "Squad_Recovery_kit", "Trap_Kit"],
            "stats": "misc",
        },
        "ameliorations": {
            "title": "Équipement — Améliorations d'établi (armes, armures, sabres) & Cristaux",
            "cats": ["Upgrade_Items", "Lightsaber_Crystals"],
            "stats": "misc",
        },
    }

    HEADER = (
        "> Généré automatiquement depuis les fichiers du jeu (installation telle que jouée : vanilla + mods installés)\n"
        "> par [`tools/extract_items.py`](file:///C:/Users/emman/Desktop/dev/Kotor%202%20Mods/tools/extract_items.py).\n"
        "> **Prérequis de niveau :** dans TSL, *aucun objet n'a de niveau minimum* — la disponibilité passe par :\n"
        "> le **palier de loot aléatoire** (indexé sur le niveau du PJ, colonne « Loot »), le **don de port d'armure**,\n"
        "> les **prérequis de caractéristique** (implants) et les restrictions d'alignement/classe.\n\n"
    )

    for fname, spec in CATS.items():
        lines = [f"# {spec['title']}", "", HEADER]
        for cat in spec["cats"]:
            rows = {rr: v for rr, v in items.items() if v["categorie"] == cat}
            if not rows:
                continue
            lines.append(f"## {cat.replace('_', ' ')} ({len(rows)} objets)")
            lines.append("")
            if spec["stats"] == "weapon":
                lines.append("| ResRef | Nom | Dégâts | Critique | Prérequis | Propriétés | Loot aléatoire (palier, niv. mini) | Lieux sûrs |")
                lines.append("| :-- | :-- | :--: | :--: | :-- | :-- | :-- | :-- |")
            elif spec["stats"] == "armor":
                lines.append("| ResRef | Nom | CA | Plaf. DEX | Prérequis (don) | Propriétés | Loot aléatoire (palier, niv. mini) | Lieux sûrs |")
                lines.append("| :-- | :-- | :--: | :--: | :-- | :-- | :-- | :-- |")
            else:
                lines.append("| ResRef | Nom | Prérequis | Propriétés | Loot aléatoire (palier, niv. mini) | Lieux sûrs |")
                lines.append("| :-- | :-- | :-- | :-- | :-- | :-- |")
            for rr in sorted(rows):
                v = rows[rr]
                nom = v["nom"] or f"*({rr})*"
                if spec["stats"] == "weapon":
                    dmg = f"{v['numdice']}d{v['dietoroll']}" if v["numdice"] else "—"
                    crit = f"{v['critthreat']}-20 ×{v['crithitmult']}" if v["critthreat"] else "—"
                    lines.append(f"| `{rr}` | {nom} | {dmg} | {crit} | {reqs_of(rr)} | {props_of(rr)} | {loot_of(rr)} | {locs_of(rr)} |")
                elif spec["stats"] == "armor":
                    lines.append(f"| `{rr}` | {nom} | {v['baseac']} | +{v['dexbonus']} | {reqs_of(rr)} | {props_of(rr)} | {loot_of(rr)} | {locs_of(rr)} |")
                else:
                    lines.append(f"| `{rr}` | {nom} | {reqs_of(rr)} | {props_of(rr)} | {loot_of(rr)} | {locs_of(rr)} |")
            lines.append("")
        (DATAS / f"equipement_{fname}.md").write_text("\n".join(lines), encoding="utf-8")
        print("écrit:", f"equipement_{fname}.md")

    # ---- loot_aleatoire.md
    L = ["# Loot Aléatoire — Système de Trésor de KotOR 2 (`k_inc_treas_k2.nss`)", "",
         "> Le moteur TSL ne possède **pas de `randomitem.2da`** (c'était KotOR 1) : tout le loot aléatoire est généré",
         "> par scripts (`PlaceTreasure` / `PlaceTreasureDisposable` de [`k_inc_treas_k2.nss`](",
         "file:///C:/Users/emman/Desktop/dev/Kotor%202%20Mods/_reference/scripts/k_inc_treas_k2.nss)).", "",
         "## 1. Mécanique générale", "",
         "1. **Niveau d'objet** : `niveau PJ + Random(8) − 5` (borné 1–30). Le niveau du PJ est la variable globale `G_PC_LEVEL`.",
         "2. **Rareté (objets d'équipement)** : jet `Random(95) + 000_RareItemChance` ; si `> 100` → objet **rare** (+5 niveaux d'objet).",
         "   Chaque échec augmente `000_RareItemChance` (système « pity » : une rare finit toujours par tomber).",
         "3. **Classe d'objet** (centaines) : 100 armes, 200 améliorations, 300 équipement, 400 armures, 500 droïdes, 900 consommables.",
         "   Sans classe imposée par le conteneur : `Random(4)+1` (l'équipement 300 est favorisé : 50 % des « améliorations » sont relancées en équipement).",
         "4. **Sous-classe** (dizaines) : tirage uniforme dans la classe (ex : 411–431 armures, 311 ceintures, 331 casques...).",
         "5. **Palier d'objet** (unités) : converti depuis le niveau d'objet selon une **courbe par famille** (tableau ci-dessous).",
         "6. **Restrictions spéciales** : pas d'armure avant le niveau 4 (Péragus), pas d'améliorations de sabre avant niv. d'objet 6 ET niv. PJ 10,",
         "   grenades « trop fortes » remplacées par une grenade inférieure, fusées uniquement si Mira est dans l'équipe,",
         "   et sur *Le Ravageur*/Malachor V (851/852NIH, 901–906MAL) : seulement medpacs/grenades/boucliers/composants/produits chimiques.", "",
         "## 2. Courbes palier ↔ niveau (inversées : niveau PJ minimum pour voir un palier)", "",
         "| Famille (préfixe) | Courbe (palier = f(niveau objet)) | Niveau PJ mini (normal) | Exemple |",
         "| :-- | :-- | :--: | :-- |"]
    curves = [
        ("Armes `w_blaste_` / `w_brifle_` / `w_melee_`", "palier = niveau (direct)", "palier + 4", "`w_blaste_09` dès niv. 13"),
        ("Améliorations `u_r_*` / `u_m_*` / `u_a_*`", "palier = niveau ÷ 2", "palier × 2 + 4", "`u_a_over_03` dès niv. 10"),
        ("Émetteurs/lentilles/cellules `u_l_emit/lens/cell`", "palier = (niveau − 6) ÷ 2", "palier × 2 + 10", "`u_l_lens_03` dès niv. 16"),
        ("Cristaux `u_l_crys_`", "palier = niveau − 5", "palier + 9", "`u_l_crys_04` dès niv. 13"),
        ("Cristaux de couleur `u_l_colo_`", "palier = Random((niveau−5)÷3+2) clampé 4–9", "niv. PJ 10+ (et niveau d'objet ≥ 10)", "—"),
        ("Ceintures / gants / casques", "palier = niveau ÷ 2", "palier × 2 + 4", "`a_belt_05` dès niv. 14"),
        ("Implants `e_imp1..4_`", "palier = niveau ÷ 3 (+ CON du PJ pour le rang d'implant)", "palier × 3 + 4", "`e_imp2_02` dès niv. 10"),
        ("Armures `a_light/medium/heavy/robe_`", "palier = niveau ÷ 2", "palier × 2 + 4", "`a_heavy_07` dès niv. 18"),
        ("Boucliers droïde `d_shield_`", "palier = niveau ÷ 3 (−4 si > 6)", "palier × 3 + 4", "—"),
        ("Objets rares", "niveau d'objet +5", "−5 par rapport au normal", "—"),
    ]
    for a, b, c, d in curves:
        L.append(f"| {a} | {b} | {c} | {d} |")
    L += ["", "## 3. Objets pouvant apparaître aléatoirement (par famille)", ""]
    fams: dict[tuple[str, str], list] = {}
    for rr, l in loot.items():
        fams.setdefault((l["cat"], l["sub"]), []).append(rr)
    for (cat, sub) in sorted(fams):
        rrs = sorted(fams[(cat, sub)], key=lambda x: loot[x]["tier"])
        L.append(f"### {cat} — {sub} ({len(rrs)})")
        L.append("")
        L.append("| Palier | ResRef | Nom | Niv. PJ mini (normal) | Niv. PJ mini (rare) |")
        L.append("| :--: | :-- | :-- | :--: | :--: |")
        for rr in rrs:
            l = loot[rr]
            L.append(f"| {l['tier']} | `{rr}` | {l['nom'] or '—'} | {l.get('plvl_normal') or '—'} | {l.get('plvl_rare') or '—'} |")
        L.append("")
    L += ["## 4. Consommables (bundles, `GetBundlePrefix`)", "",
          "| Code | Objet | Règle |",
          "| :--: | :-- | :-- |"]
    bundles = [
        ("911/961", "Crédits", "quantité = Random(10×niv) + Random(50) + 20 (ou variante réduite)"),
        ("921/922", "Composants / Produits chimiques", "quantité = Random(niv) + Random(niv) + 1"),
        ("931", "Bouclier de bras `a_shield_0X`", "palier = niv ÷ 4 + 1 (max 7)"),
        ("941/954", "Trousse de soins T1/T2/T3", "T1 < niv 9, T2 < niv 16, T3 ensuite"),
        ("942", "Kit de réparation droïde", "même courbe que les trousses"),
        ("951–953", "Stims FOR/DEX/CON", "version T1 < niv 12, T2 ensuite"),
        ("971–979", "Grenades", "grenades supérieures remplacées par des frag si niveau insuffisant"),
        ("981–983", "Pièces / pointes prog. / pointes sécurité", "quantité fixe"),
        ("991–995", "Fusées de Mira `w_rocket_0X`", "uniquement si Mira recrutée ; palier = niv ÷ 3 (max 5)"),
    ]
    for a, b, c in bundles:
        L.append(f"| {a} | {b} | {c} |")
    (DATAS / "loot_aleatoire.md").write_text("\n".join(L), encoding="utf-8")
    print("écrit: loot_aleatoire.md")

    # ---- loot_lieux_surs.md
    Ls = ["# Lieux Sûrs — Emplacements Fixes Garantis (conteneurs, créatures, marchands)", "",
          "> Extrait des templates `.mod` de chaque module : inventaires fixes des **conteneurs** (UTP),",
          "> **créatures** (UTC — `drop=oui` : tombe à la mort) et **marchands** (UTM).",
          "> Les emplacements aléatoires (majorité des conteneurs) ne figurent pas ici : voir [`loot_aleatoire.md`](loot_aleatoire.md).", ""]
    used_files = set()
    by_cat: dict[str, list] = {}
    for rr, ps in placements.items():
        it = items.get(rr)
        cat = it["categorie"] if it else "Inconnu"
        by_cat.setdefault(cat, []).append(rr)
    for cat in sorted(by_cat):
        rrs = sorted(by_cat[cat])
        Ls.append(f"## {cat.replace('_', ' ')} ({len(rrs)} objets localisés)")
        Ls.append("")
        Ls.append("| ResRef | Nom | Emplacements fixes |")
        Ls.append("| :-- | :-- | :-- |")
        for rr in rrs:
            nom = (items.get(rr) or {}).get("nom") or "—"
            Ls.append(f"| `{rr}` | {nom} | {locs_of(rr)} |")
        Ls.append("")
    (DATAS / "loot_lieux_surs.md").write_text("\n".join(Ls), encoding="utf-8")
    print("écrit: loot_lieux_surs.md")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--phase", type=int, required=True)
    args = ap.parse_args()
    ctx = Ctx()
    {1: phase1, 2: phase2, 3: phase3, 4: phase4, 5: phase5}[args.phase](ctx)


if __name__ == "__main__":
    main()
