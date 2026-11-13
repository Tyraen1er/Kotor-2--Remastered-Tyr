# -*- coding: utf-8 -*-
"""Génère « Kotor 2 - rééquilibrage - WIP Feats.csv » :

1. Tous les feats vanilla (feat.2da, 245 lignes) : prérequis décodés, effets, colonne Changement (mod).
2. Les feats custom de l'overhaul (decisions_finales.md + CSV WIP), marqués « absent du jeu vanilla ».

Usage : .venv\\Scripts\\python.exe tools\\build_feats_csv.py
"""
import csv
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "_reference", "2da", "feat.csv")
DST = os.path.join(ROOT, "Kotor 2 - rééquilibrage - WIP Feats.csv")

rows = list(csv.reader(open(SRC, encoding="utf-8-sig", newline="")))
HDR = rows[0]
IX = {c: HDR.index(c) for c in HDR}

labels = {r[0]: r[IX["label"]].strip() for r in rows[1:] if r and r[0]}

# ---------------------------------------------------------------- prérequis
def feat_name(idx):
    idx = str(idx).strip()
    if idx in ("", "0"):
        return ""
    return labels.get(idx, "?%s" % idx)

def prereq(row):
    p = []
    def g(col):
        v = row[IX[col]].strip() if col in IX and len(row) > IX[col] else ""
        return v
    if g("mincharlevel"): p.append("Niv. %s" % g("mincharlevel"))
    if g("minattackbonus"): p.append("BBA %s" % g("minattackbonus"))
    for col, ab in [("minstr", "FOR"), ("mindex", "DEX"), ("minint", "INT"), ("minwis", "SAG")]:
        if g(col): p.append("%s %s" % (ab, g(col)))
    for col in ("prereqfeat1", "prereqfeat2"):
        n = feat_name(g(col))
        if n: p.append(n)
    ors = [feat_name(g("orreqfeat%d" % i)) for i in range(5)]
    ors = [o for o in ors if o]
    if ors: p.append("OU : " + " / ".join(ors))
    if g("reqskill"): p.append("Compétence %s" % g("reqskill"))
    return " ; ".join(p)

# ------------------------------------------------- noms, catégories, effets
C_MELEE = "Actif — mêlée"
C_DIST = "Actif — distance"
C_STYLE = "Style & posture"
C_MAN = "Maniement d'arme"
C_DEF = "Défense & survie"
C_SKILL = "Compétence & utilitaire"
C_CLASS = "Classe (auto)"
C_COMP = "Compagnon / PNJ"
C_HID = "Caché / interne"
C_PREST = "Caché — pouvoir de prestige"

NOMS = {
 # --- Actifs mêlée
 "28": ("Attaque en puissance I", C_MELEE, "Mode actif : -3 Atq, +5 dégâts/coup (dégâts doublés à 2 armes ou arme double : +10)"),
 "17": ("Attaque en puissance II", C_MELEE, "-3 Atq, +7 dégâts (+14 à 2 armes/double)"),
 "83": ("Attaque en puissance III", C_MELEE, "-3 Atq, +10 dégâts (+20 à 2 armes/double)"),
 "11": ("Déluge de coups I", C_MELEE, "+1 attaque/round ; -4 Atq, -4 CA (le round)"),
 "91": ("Déluge de coups II", C_MELEE, "+1 attaque ; -2 Atq, -2 CA"),
 "53": ("Déluge de coups III (Maître)", C_MELEE, "+1 attaque ; -1 Atq, -1 CA"),
 "8":  ("Coup critique I", C_MELEE, "Plage de menace ×2, -5 CA ; étourdit 1 round si Vigueur échouée (DD = Niv. + Mod. FOR)"),
 "19": ("Coup critique II", C_MELEE, "Plage ×3 (reste -5 CA, stun)"),
 "81": ("Coup critique III", C_MELEE, "Plage ×4 (reste -5 CA, stun)"),
 # --- Actifs distance
 "29": ("Décharge d'énergie I", C_DIST, "Mode actif : -3 Atq, +5 dégâts/tir ; chance de renverser la cible"),
 "18": ("Décharge d'énergie II", C_DIST, "-3 Atq, +8 dégâts ; chance de renverser"),
 "82": ("Décharge d'énergie III", C_DIST, "-3 Atq, +12 dégâts ; chance de renverser"),
 "30": ("Tir rapide I", C_DIST, "+1 tir/round ; -4 Atq, -4 CA"),
 "92": ("Tir rapide II", C_DIST, "+1 tir ; -2 Atq, -2 CA"),
 "26": ("Tir rapide III", C_DIST, "+1 tir ; -1 Atq, -1 CA"),
 "31": ("Tir de sniper I", C_DIST, "Plage de menace ×2, -5 CA ; étourdit si Vigueur échouée (DD = Niv. + Mod. INT)"),
 "20": ("Tir de sniper II", C_DIST, "Plage ×3 (reste -5 CA, stun)"),
 "77": ("Tir de sniper III", C_DIST, "Plage ×4 (reste -5 CA, stun)"),
 # --- Styles
 "3":  ("Combat à deux armes I", C_STYLE, "Malus 2 armes : -4/-8 (arme équilibrée en main gauche : -2/-6)"),
 "9":  ("Combat à deux armes II", C_STYLE, "-2/-4 (0/-2 équilibrée)"),
 "85": ("Combat à deux armes III", C_STYLE, "0/-2 (0/0 équilibrée)"),
 "159": ("Combat à 2 armes supérieur I", C_STYLE, "+1 Atq & Dégâts main droite (classes martiales de prestige)"),
 "160": ("Combat à 2 armes supérieur II", C_STYLE, "+2 Atq & Dégâts main droite"),
 "161": ("Combat à 2 armes supérieur III", C_STYLE, "+3 Atq & Dégâts main droite"),
 "113": ("Duel I", C_STYLE, "1 arme à 1 main seulement : +1 Atq, +1 CA"),
 "114": ("Duel II", C_STYLE, "+2 Atq, +2 CA (1 arme 1M)"),
 "115": ("Duel III (Maître)", C_STYLE, "+3 Atq, +3 CA (1 arme 1M)"),
 "240": ("Tir de précision I", C_DIST, "+1 Atq & Dégâts (distance) ; +2 CA vs blasters ; réduit le malus de tir sur cible en mêlée"),
 "241": ("Tir de précision II", C_DIST, "+2 Atq & Dégâts ; +4 CA vs blasters ; réduit le malus en mêlée"),
 "242": ("Tir de précision III", C_DIST, "+3 Atq & Dégâts ; +6 CA vs blasters ; réduit le malus en mêlée"),
 "243": ("Tir de précision IV", C_DIST, "+4 Atq & Dégâts ; +8 CA vs blasters ; réduit le malus en mêlée"),
 "244": ("Tir de précision V", C_DIST, "+5 Atq & Dégâts ; +10 CA vs blasters ; réduit le malus en mêlée"),
 "139": ("Combat rapproché I", C_DIST, "Réduit de 2 la pénalité de -10 CA quand on tire au contact d'un ennemi de mêlée"),
 "140": ("Combat rapproché II", C_DIST, "Réduit de 4 la pénalité de -10 CA au tir au contact"),
 "190": ("Frappe simultanée I (Dual Strike)", C_STYLE, "Mode actif 2 armes : les deux armes frappent en une seule action ; malus de CA (détail exact à vérifier en jeu)"),
 "191": ("Frappe simultanée II", C_STYLE, "Malus de CA réduit"),
 "192": ("Frappe simultanée III", C_STYLE, "Malus de CA réduit"),
 "193": ("Arme de prédilection — Finesse : sabres", C_MAN, "Utilise le mod. de DEX au lieu de FOR aux jets d'attaque avec sabres si DEX > FOR"),
 "194": ("Arme de prédilection — Finesse : mêlée", C_MAN, "Utilise le mod. de DEX au lieu de FOR aux jets d'attaque en mêlée si DEX > FOR"),
 # --- Maniement
 "39": ("Port d'armes : pistolets blaster", C_MAN, "Équiper les pistolets sans le malus de non-maniement (-4 Atq)"),
 "40": ("Port d'armes : fusils blaster", C_MAN, "Équiper les fusils sans malus (-4 Atq)"),
 "43": ("Port d'armes : sabres laser", C_MAN, "Équiper les sabres sans malus (-4 Atq)"),
 "44": ("Port d'armes : armes de mêlée", C_MAN, "Équiper les armes de mêlée sans malus (-4 Atq)"),
 "208": ("Port d'armes : lanceur de poignet", C_MAN, "Mandalore — lanceur de poignet sans malus"),
 "32": ("Arme de prédilection : pistolets", C_MAN, "+1 Atq avec les pistolets blaster"),
 "33": ("Arme de prédilection : fusils", C_MAN, "+1 Atq avec les fusils"),
 "36": ("Arme de prédilection : sabres", C_MAN, "+1 Atq avec les sabres"),
 "37": ("Arme de prédilection : mêlée", C_MAN, "+1 Atq en mêlée"),
 "46": ("Spécialisation martiale : pistolets", C_MAN, "+2 dégâts avec les pistolets (Soldat/Gardien/prestige martiale)"),
 "47": ("Spécialisation martiale : fusils", C_MAN, "+2 dégâts avec les fusils"),
 "50": ("Spécialisation martiale : sabres", C_MAN, "+2 dégâts avec les sabres"),
 "51": ("Spécialisation martiale : mêlée", C_MAN, "+2 dégâts en mêlée"),
 "156": ("Arme de prédilection supérieure : sabres I", C_MAN, "+1 Atq sabres (prestige martiale)"),
 "157": ("Arme de prédilection supérieure : sabres II", C_MAN, "+2 Atq sabres"),
 "158": ("Arme de prédilection supérieure : sabres III", C_MAN, "+3 Atq sabres"),
 # --- Défense
 "5":  ("Port d'armure légère", C_DEF, "Porter les armures légères sans pénalité"),
 "6":  ("Port d'armure intermédiaire", C_DEF, "Porter les armures intermédiaires sans pénalité"),
 "4":  ("Port d'armure lourde", C_DEF, "Porter les armures lourdes sans pénalité"),
 "84": ("Robustesse I", C_DEF, "+1 PV par niveau de personnage"),
 "123": ("Robustesse II", C_DEF, "+1 PV/niv suppl. ET RD 2/- sur chaque attaque reçue"),
 "124": ("Robustesse III", C_DEF, "+1 PV/niv suppl. (total +3 PV/niv)"),
 "13": ("Condition physique I", C_DEF, "+1 à toutes les sauvegardes"),
 "21": ("Condition physique II", C_DEF, "+2 à toutes les sauvegardes"),
 "22": ("Condition physique III", C_DEF, "+3 à toutes les sauvegardes"),
 "55": ("Défense de Jedi I", C_DEF, "Dévier les tirs de blaster (jet opposé) ; renvoi si marge ≥ 10 (auto Jedi)"),
 "1":  ("Défense de Jedi II", C_DEF, "Bonus de renvoi +3 (auto Jedi)"),
 "24": ("Défense de Jedi III", C_DEF, "Bonus de renvoi +6 (auto Jedi)"),
 "125": ("Esquive (Evasion)", C_DEF, "Auto Éclaireur niv. 6 ; sauvegarde de Réflexes réussie contre une AoE → demi-dégâts"),
 "56": ("Esquive instinctive I", C_DEF, "Conserve le mod. de DEX à la CA même pris au dépourvu"),
 "57": ("Esquive instinctive II", C_DEF, "Bonus aux sauvegardes contre les mines"),
 "238": ("Immunité aux mines", C_DEF, "Ne déclenche pas les mines (auto, accordé par script/classe)"),
 # --- Compétences
 "7":  ("Prudence I", C_SKILL, "+1 Démolition et Premiers soins"),
 "117": ("Prudence II", C_SKILL, "+2 Démolition et Premiers soins"),
 "118": ("Prudence III", C_SKILL, "+3 Démolition et Premiers soins"),
 "10": ("Empathie I", C_SKILL, "+1 Persuasion, Vigilance et Premiers soins"),
 "121": ("Empathie II", C_SKILL, "+2 aux trois compétences"),
 "122": ("Empathie III", C_SKILL, "+3 aux trois compétences"),
 "12": ("Bricoleur I", C_SKILL, "+1 Sécurité, Informatique et Réparation"),
 "119": ("Bricoleur II", C_SKILL, "+2 aux trois compétences"),
 "120": ("Bricoleur III", C_SKILL, "+3 aux trois compétences"),
 "197": ("Course furtive", C_SKILL, "Se déplacer plus vite en mode furtif"),
 "175": ("Artisanat", C_SKILL, "Inutilisé dans K2 (l'établi est libre d'accès)"),
 "182": ("Interface de droïde", C_COMP, "Interne droïde"),
 # --- Classe (auto)
 "60": ("Attaque sournoise +1d6", C_CLASS, "+1d6 dégâts sur cible au dépourvu/flanquée/incapable de se défendre (auto Voyou/Assassin/Ombre)"),
 "88": ("Focalisation de la Force I", C_CLASS, "Réserve de Force accrue (auto Consulaire)"),
 "89": ("Focalisation de la Force II", C_CLASS, "Réserve accrue"),
 "90": ("Focalisation de la Force III", C_CLASS, "Réserve accrue"),
 "98": ("Immunité de la Force : Peur", C_CLASS, "Immunité à la Peur (auto Sentinelle)"),
 "99": ("Immunité de la Force : Étourdissement", C_CLASS, "Immunité à l'Étourdissement"),
 "100": ("Immunité de la Force : Paralysie", C_CLASS, "Immunité à la Paralysie"),
 "101": ("Saut de Force I", C_CLASS, "Bond d'attaque pour fermer la distance (auto Gardien)"),
 "102": ("Saut de Force II", C_CLASS, "Portée améliorée"),
 "103": ("Saut de Force III", C_CLASS, "Portée maximale"),
 "104": ("Chance du voyou I", C_CLASS, "+1 CA (auto Voyou)"),
 "105": ("Chance du voyou II", C_CLASS, "+2 CA"),
 "106": ("Chance du voyou III", C_CLASS, "+3 CA"),
 "107": ("Sens de la Force I", C_CLASS, "+2 CA (auto Jedi)"),
 "108": ("Sens de la Force II", C_CLASS, "+4 CA"),
 "109": ("Sens de la Force III", C_CLASS, "+6 CA"),
 "143": ("Régénération de Force", C_CLASS, "Régénère des PF avec le temps (interne)"),
 "196": ("Régénération de vitalité", C_CLASS, "Régénère des PV avec le temps (interne)"),
 "212": ("Spécialiste mains nues I", C_CLASS, "Dégâts à mains nues accrus (progression auto)"),
 "219": ("Spécialiste mains nues VIII", C_CLASS, "Dernier palier de dégâts à mains nues"),
 # --- Compagnons / PNJ
 "78": ("Amélioration de droïde I", C_COMP, "+1 emplacement de module utilitaire (droïdes)"),
 "79": ("Amélioration de droïde II", C_COMP, "+1 emplacement"),
 "80": ("Amélioration de droïde III", C_COMP, "+1 emplacement"),
 "110": ("Mise à niveau logique : combat", C_COMP, "T3-M4 — bonus de combat"),
 "111": ("Mise à niveau logique : tacticien", C_COMP, "T3-M4"),
 "112": ("Mise à niveau logique : droïde de guerre", C_COMP, "T3-M4"),
 "95": ("Robustesse wookiee I", C_COMP, "+PV (Hanharr)"),
 "224": ("Robustesse wookiee II", C_COMP, "+PV"),
 "225": ("Robustesse wookiee III", C_COMP, "+PV"),
 "231": ("Fureur wookiee I", C_COMP, "Rage de combat (Hanharr)"),
 "232": ("Fureur wookiee II", C_COMP, "Rage améliorée"),
 "233": ("Fureur wookiee III", C_COMP, "Rage maximale"),
 "209": ("Frappe echani I", C_COMP, "Bonus de combat (Servante)"),
 "210": ("Frappe echani II", C_COMP, "Bonus accru"),
 "211": ("Frappe echani III", C_COMP, "Bonus maximal"),
 "220": ("Brise-bouclier", C_COMP, "HK-47 — attaque vs boucliers (interne)"),
 "221": ("Frappe répulseur", C_COMP, "HK-47 — renversement sur impact (interne)"),
 "222": ("Frappe électrique", C_COMP, "HK-47 — dégâts ioniques sur impact (interne)"),
 "223": ("Frappe gravitonique", C_COMP, "HK-47 — étourdissement sur impact (interne)"),
 "228": ("Protocole d'assassin I", C_COMP, "HK-47 — protocole de chasse"),
 "229": ("Protocole d'assassin II", C_COMP, "HK-47"),
 "230": ("Protocole d'assassin III", C_COMP, "HK-47"),
 "234": ("Tour de droïde", C_COMP, "T3-M4 — piratage de droïde"),
 "235": ("Confusion de droïde", C_COMP, "T3-M4"),
 "200": ("Courage mandalorien", C_COMP, "Mandalore — immunité à la Peur (à vérifier)"),
 "206": ("Vétéran de guerre", C_COMP, "Interne compagnon"),
 "202": ("Mentor", C_COMP, "Interne (influence compagnons)"),
 "204": ("Esprit", C_COMP, "Interne (à documenter)"),
 "236": ("Esprit combattant", C_COMP, "Interne (à documenter)"),
 "237": ("Résolution héroïque", C_COMP, "Interne (à documenter)"),
 "198": ("Combat cinétique", C_COMP, "Kreia — combat au sabre télékinésique (PNJ)"),
 "201": ("Bouclier de camouflage personnel", C_COMP, "Interne — camouflage intégré"),
 "96":  ("Intégration blaster", C_COMP, "Interne HK-47"),
 "116": ("Sensible à la Force", C_HID, "Interne — marque de sensibilité à la Force"),
 "93":  ("Toutes maîtrises d'armes", C_HID, "Interne — toutes les proficiencies"),
 "168": ("Déflexion", C_HID, "Interne — déviation de tirs"),
 "203": ("Changement d'implant", C_HID, "Interne — gestion des implants"),
 "205": ("Chaîne de Force", C_HID, "Interne (Maître Jedi)"),
 "207": ("Animations mains nues avancées", C_HID, "Interne — animations"),
 "239": ("Garde rapprochée", C_HID, "Interne IA (Point Guard)"),
 "199": ("Survie", C_HID, "Interne (inutilisé — à documenter)"),
 "2":  ("Posture de garde améliorée", C_HID, "Caché (XXXX) — non utilisé"),
 "25": ("Posture de garde maître", C_HID, "Caché (XXXX) — non utilisé"),
 "54": ("Posture de garde", C_HID, "Caché (XXXX) — non utilisé"),
 "27": ("Perceptif", C_HID, "Caché (XXXX) — non utilisé"),
 "195": ("Mobilité", C_HID, "Caché (XXXX) — non utilisé"),
 "86": ("Focalisation Alternative", C_HID, "Caché (XXXX)"),
 "87": ("Focalisation Contrôle", C_HID, "Caché (XXXX)"),
 "149": ("Corruption du Côté Obscur", C_HID, "Interne — corruption"),
 "94":  ("Méditation de combat", C_PREST, "Caché — lié au pouvoir Méditation de combat (cf. Spé Pouvoirs.csv)"),
 "167": ("Illumination (LS)", C_PREST, "Caché — Maître Jedi, débloque Illumination de Force (cf. Spé Pouvoirs.csv)"),
}
# Chaînes générées
for i, idx in enumerate(range(61, 70), start=2):
    NOMS[str(idx)] = ("Attaque sournoise +%dd6" % i, C_CLASS, NOMS["60"][2].split(" (")[0] + " (auto Voyou/Assassin/Ombre)")
for i, idx in enumerate(range(213, 219), start=2):
    NOMS[str(idx)] = ("Spécialiste mains nues %s" % ["II", "III", "IV", "V", "VI", "VII"][i - 2], C_CLASS, "Dégâts à mains nues accrus (progression auto)")
for i, idx in enumerate(range(126, 136), start=1):
    NOMS[str(idx)] = ("Visée %d" % i, C_HID, "Interne PNJ — bonus de précision (IA)")
for idx, (nom, cat, eff) in {
    "34": ("Arme de prédilection : grenades", C_HID, "Caché (XXXX) — utilisé par les PNJ lanceurs de grenades"),
    "35": ("Arme de prédilection : armes lourdes", C_HID, "Caché (XXXX) — PNJ"),
    "38": ("Arme de prédilection : armes simples", C_HID, "Caché (XXXX) — PNJ"),
    "41": ("Port d'armes : grenades", C_HID, "Caché (XXXX) — PNJ"),
    "42": ("Port d'armes : armes lourdes", C_HID, "Caché (XXXX) — PNJ"),
    "45": ("Port d'armes : armes simples", C_HID, "Caché (XXXX) — PNJ"),
    "48": ("Spécialisation : grenades", C_HID, "Caché (XXXX) — PNJ"),
    "49": ("Spécialisation : armes lourdes", C_HID, "Caché (XXXX) — PNJ"),
    "52": ("Spécialisation : armes simples", C_HID, "Caché (XXXX) — PNJ"),
}.items():
    NOMS[idx] = (nom, cat, eff)
for idx, skill in {"58": "Informatique", "70": "Démolition", "71": "Discrétion", "72": "Vigilance",
                   "73": "Persuasion", "74": "Réparation", "75": "Sécurité", "76": "Premiers soins"}.items():
    NOMS[idx] = ("Expertise : %s" % skill, C_HID, "Caché (XXXX) — focus de compétence")
for idx, (r, lvl) in {"136": ("I", 4), "137": ("II", 8), "138": ("III", 12), "226": ("IV", 16), "227": ("V", 20)}.items():
    NOMS[idx] = ("Tir de précision %s (PNJ)" % r, C_HID, "Caché (XXX) — version PNJ du Tir de précision")
for idx, r in {"144": "I", "145": "II", "146": "III", "147": "IV", "148": "V"}.items():
    NOMS[idx] = ("Écraser l'opposition %s" % r, C_PREST, "Caché — Seigneur Sith (débuff zone Atq/Volonté, cf. Spé Pouvoirs.csv)")
for idx, r in {"162": "I", "163": "II", "164": "III", "165": "IV", "166": "V"}.items():
    NOMS[idx] = ("Inspirer les fidèles %s" % r, C_PREST, "Caché — Maître d'armes (buff de groupe, cf. Spé Pouvoirs.csv)")
for idx, r in {"97": "I", "141": "II", "142": "III"}.items():
    NOMS[idx] = ("Camouflage de Force %s" % r, C_PREST, "Caché — Assassin Sith / Protecteur (discrétion sans générateur, cf. Spé Pouvoirs.csv)")
for idx, r in {"150": "I", "151": "II", "152": "III"}.items():
    NOMS[idx] = ("Ignorer la douleur %s" % r, C_HID, "Interne PNJ — réduit les dégâts subis")
for idx, r in {"153": "I", "154": "II", "155": "III"}.items():
    NOMS[idx] = ("Dégâts de combat accrus %s" % r, C_HID, "Interne PNJ — bonus de dégâts")
for idx, r in {"169": "I", "170": "II", "171": "III"}.items():
    NOMS[idx] = ("Force intérieure %s" % r, C_HID, "Interne (à documenter)")
for idx, r in {"172": "I", "173": "II", "174": "III"}.items():
    NOMS[idx] = ("Dégâts de mêlée accrus %s" % r, C_HID, "Interne PNJ — bonus de dégâts en mêlée")
for idx, r in {"14": "1", "15": "2", "16": "3"}.items():
    NOMS[idx] = ("Niveau d'implant %s (caché)" % r, C_HID, "Permet d'équiper les implants de niveau %s" % r)
for idx, skill in {"183": "Vigilance", "184": "Informatique", "185": "Démolition", "186": "Réparation",
                   "187": "Sécurité", "188": "Discrétion", "189": "Premiers soins"}.items():
    NOMS[idx] = ("Compétence de classe : %s" % skill, C_SKILL, "Transforme la compétence en compétence de classe (coût 1 pt au level up)")
for idx, r in {"176": "I", "177": "II", "178": "III"}.items():
    NOMS[idx] = ("Artisanat supérieur : armes %s" % r, C_SKILL, "Inutilisé dans K2 (établi libre)")
for idx, r in {"179": "I", "180": "II", "181": "III"}.items():
    NOMS[idx] = ("Artisanat supérieur : armures %s" % r, C_SKILL, "Inutilisé dans K2 (établi libre)")

# ------------------------------------------------- changements (mod) actés/WIP
CHG = {
 "3":  "Style de combat.csv (WIP) : Rang I devient -6/-6 Atq & +1 CA",
 "9":  "Style de combat.csv (WIP) : Rang II devient -4/-4 Atq & +2 CA",
 "85": "Style de combat.csv (WIP) : Rang III devient -2/-2 Atq & +3 CA (identité parade/CA de l'Ambidextrie)",
 "113": "Refonte prévue « Science du Duel » (§6 : +Atq & CA, ignore RD / Style CSV : +crit, 150 % FOR) — à harmoniser ; mains nues = arme 1M pour ce style (cf. Style de combat.csv)",
 "114": "Refonte prévue « Science du Duel » — à harmoniser",
 "115": "Refonte prévue « Duel Supérieur » (§6 : +150 % Mod., crit, ignore RD 12) — à harmoniser",
 "125": "§7.B ACTÉ « Esquive Totale » : save réussie vs AoE = 0 dégât (échec = moitié) ; sélection uniquement via classe de prestige Niv. 15+ ; auto Jedi/Sith ennemis 20+ ; reste auto Éclaireur niv. 6 (Mira)",
 "22": "§8.D ACTÉ : rang III passe à +3 toutes saves + 2 supplémentaires vs pouvoirs de Force",
 "5":  "§8 ACTÉ : RD native ajoutée par type d'armure (légère 0 / interm. 2 / lourde 4) — le don lui-même est inchangé",
 "6":  "§8 ACTÉ : RD native 2 (don inchangé)",
 "4":  "§8 ACTÉ : RD native 4 (don inchangé)",
 "156": "Annexes §5.B : ouvrir l'accès des dons Supérieurs aux classes hybrides (comble les dons vides de la Sentinelle/Veilleur, diagnostic §6.B)",
 "157": "Idem : élargir l'accès",
 "158": "Idem : élargir l'accès",
 "159": "Idem : élargir l'accès",
 "160": "Idem : élargir l'accès",
 "161": "Idem : élargir l'accès",
 "32": "Doublon potentiel avec les Spé d'arme custom par famille (Contondante/Primitive/Vibrante/Laser) — arbitrage à faire",
 "33": "Doublon potentiel avec l'arbre Fusil custom — arbitrage à faire",
 "36": "Doublon potentiel avec la Spé Arme Laser custom — arbitrage à faire",
 "37": "Doublon potentiel avec les Spé d'arme custom — arbitrage à faire",
 "46": "Doublon potentiel avec les Spé d'arme custom (rang I +2 Atq & Dégâts) — arbitrage à faire",
 "47": "Doublon potentiel avec l'arbre Fusil custom — arbitrage à faire",
 "50": "Doublon potentiel avec la Spé Arme Laser custom — arbitrage à faire",
 "51": "Doublon potentiel avec les Spé d'arme custom — arbitrage à faire",
 "190": "Non couvert par l'overhaul — à arbitrer (redondant avec l'Ambidextrie refondue ?)",
 "212": "Socle conservé ; l'identité mains nues passe par la posture Duel (1M) + Spé Arme Contondante + Matukai L3 — l'arbre dédié (Arts Martiaux / Arts Mutaki) est SUPPRIMÉ",
 "193": "À RETIRER du jeu — les remaps d'attaque passent par les Spé carac (Echanis DEX mêlée / Gand INT distance / Matukai SAG)",
 "194": "À RETIRER du jeu — remplacé par les remaps d'attaque des Spé carac (Echanis DEX mêlée / Matukai SAG)",
 "209": "TODO : remplacer le don de la Servante (Brianna) — éviter le cumul avec l'arbre joueur « Techniques Echanis »",
 "210": "TODO : remplacer le don de la Servante — éviter le cumul avec l'arbre joueur « Techniques Echanis »",
 "211": "TODO : remplacer le don de la Servante — éviter le cumul avec l'arbre joueur « Techniques Echanis »",
 "94":  "Référencé dans Spé Pouvoirs.csv (chantier Pouvoirs — sélection de pouvoir)",
 "144": "Référencé dans Spé Pouvoirs.csv (Prestige Seigneur Sith)",
 "145": "Référencé dans Spé Pouvoirs.csv (Prestige Seigneur Sith)",
 "146": "Référencé dans Spé Pouvoirs.csv (Prestige Seigneur Sith)",
 "147": "Référencé dans Spé Pouvoirs.csv (Prestige Seigneur Sith)",
 "148": "Référencé dans Spé Pouvoirs.csv (Prestige Seigneur Sith)",
 "162": "Référencé dans Spé Pouvoirs.csv (Prestige Maître d'armes, rangs I-VI)",
 "163": "Référencé dans Spé Pouvoirs.csv (Prestige Maître d'armes)",
 "164": "Référencé dans Spé Pouvoirs.csv (Prestige Maître d'armes)",
 "165": "Référencé dans Spé Pouvoirs.csv (Prestige Maître d'armes)",
 "166": "Référencé dans Spé Pouvoirs.csv (Prestige Maître d'armes)",
 "167": "Référencé dans Spé Pouvoirs.csv (Illumination — Quête / Lumineux max)",
 "97":  "Référencé dans Spé Pouvoirs.csv (Force Camouflage — Prestige Assassin/Protecteur)",
 "141": "Référencé dans Spé Pouvoirs.csv",
 "142": "Référencé dans Spé Pouvoirs.csv",
 "24":  "§4 axiome distance/mêlée (proposition) : déflexion conservée = identité de l'élite Jedi face à la distance",
 "1":   "Idem §4",
 "55":  "Idem §4",
}

# ================================================================ FEATS CUSTOM
CUSTOM = []  # (section, nom, label suggéré, préreq, effet, note)
S1 = "STYLES DE COMBAT — Style de combat.csv"
CUSTOM += [
 (S1, "Maniement d'Arme Lourde I", "MOD_HEAVY_WEAPON_1", "Arme 2M équipée", "+1 Atq ; dégâts mêlée 250 % FOR ; dégâts distance 200 % DEX (base moddée : 200 % FOR / 150 % DEX)", "S'applique aux armes 2M (hache, vibro-épée, fusils 2M)"),
 (S1, "Maniement d'Arme Lourde II", "MOD_HEAVY_WEAPON_2", "Maniement d'Arme Lourde I", "+2 Atq ; dégâts mêlée 275 % FOR ; dégâts distance 225 % DEX", ""),
 (S1, "Maniement d'Arme Lourde III", "MOD_HEAVY_WEAPON_3", "Maniement d'Arme Lourde II", "+3 Atq ; dégâts mêlée 300 % FOR ; dégâts distance 250 % DEX", "Arbitrage : seuils finaux à valider vs contrat DPR §9"),
 (S1, "Maniement d'Arme Double / Repeating I", "MOD_DOUBLE_WEAPON_1", "Arme double ou blaster à répétition équipé", "Dégâts +1/+1 (chaque bout) ; malus de CA réduit à -3 (base moddée -5 CA au lieu de -6/-10 Atq)", "Remplace les malus vanilla -6/-10 des armes doubles"),
 (S1, "Maniement d'Arme Double / Repeating II", "MOD_DOUBLE_WEAPON_2", "Rang I", "Dégâts +2/+2 ; malus de CA -2", ""),
 (S1, "Maniement d'Arme Double / Repeating III", "MOD_DOUBLE_WEAPON_3", "Rang II", "Dégâts +3/+3 ; malus de CA -1", "Rang III de l'arbre Lame Double §6 (« Cà2A Supérieur » assaut lourd)"),
]
S2 = "SPÉCIALISATIONS D'ARME PAR FAMILLE — Spécialisation d'arme.csv"
NOTE_PROC = "Règle commune : proc = plage de menace de l'arme / 20 par coup (évolue avec la posture Duel) ; DD = 10 + Niv. attaquant + mod. de la carac. directrice de l'arme"
CUSTOM += [
 (S2, "Spécialisation Arme Contondante I", "MOD_SPEC_BLUNT_1", "Port d'armes mêlée + arme contondante équipée", "+2 Atq et +2 Dégâts (armes contondantes : matraque, bâton, pique de Force)", ""),
 (S2, "Spécialisation Arme Contondante II", "MOD_SPEC_BLUNT_2", "Rang I + arme contondante équipée", "Étourdit 1 tour (Vigueur annule). " + NOTE_PROC, "Stun droïde pour les cibles mécaniques"),
 (S2, "Spécialisation Arme Contondante III", "MOD_SPEC_BLUNT_3", "Rang II", "Stun 2 tours ; cibles immunisées : -2 Atq 1 tour à la place", "Retenu 13/11 (remplace « durée+1 / crit+1 »)"),
 (S2, "Spécialisation Arme Primitive I", "MOD_SPEC_PRIM_1", "Port d'armes mêlée + arme primitive équipée", "+2 Atq et +2 Dégâts (épées, hache, lames doubles primitives)", ""),
 (S2, "Spécialisation Arme Primitive II", "MOD_SPEC_PRIM_2", "Rang I + arme primitive équipée", "Bris d'armure : -4 CA, 1 tour (Vigueur annule). " + NOTE_PROC, ""),
 (S2, "Spécialisation Arme Primitive III", "MOD_SPEC_PRIM_3", "Rang II", "Bris d'armure aggravé : -6 CA, 1 tour", "Retenu 13/11 (variante RD -3 écartée : aucun EffectDamageReductionDecrease en NWScript)"),
 (S2, "Spécialisation Arme Vibrante I", "MOD_SPEC_VIBRO_1", "Port d'armes mêlée + arme vibrante équipée", "+2 Atq et +2 Dégâts (vibrolames, vibro-épées, vibrolames doubles)", ""),
 (S2, "Spécialisation Arme Vibrante II", "MOD_SPEC_VIBRO_2", "Rang I + arme vibrante équipée", "Mutilation : -4 Atq et -4 Dégâts, 1 tour (Vigueur annule). " + NOTE_PROC, ""),
 (S2, "Spécialisation Arme Vibrante III", "MOD_SPEC_VIBRO_3", "Rang II", "Mutilation empilable : -2 supplémentaires par proc, plafond -8, durée rafraîchie 1 tour", "Retenu 13/11 (variante simple possible : -6 fixe)"),
 (S2, "Spécialisation Arme Laser I", "MOD_SPEC_LASER_1", "Port d'armes sabres + sabre équipé", "+2 Atq et +2 Dégâts (sabres laser)", ""),
 (S2, "Spécialisation Arme Laser II", "MOD_SPEC_LASER_2", "Rang I + sabre équipé", "Bris de volonté : -4 aux sauvegardes, 1 tour (Volonté annule). " + NOTE_PROC, ""),
 (S2, "Spécialisation Arme Laser III", "MOD_SPEC_LASER_3", "Rang II", "Bris de volonté aggravé : -6 sauvegardes et draine 1d6 PF par proc", "Retenu 13/11 — identité anti-caster (EffectDamageForcePoints validé)"),
]
S3 = "DISTANCE — Triangle Pistolet/Fusil/Gatling (§4 & §6)"
CUSTOM += [
 (S3, "Spécialisation Pistolet I", "MOD_PISTOL_SPEC_1", "Port d'armes : pistolets + pistolet équipé", "+1 Atq, +1 Dégât, +1 CA (« Maîtrise du Pistolet » §4)", "Mobilité / multi-effets ; posture fournie par Science du Duel (1M)"),
 (S3, "Spécialisation Pistolet II", "MOD_PISTOL_SPEC_2", "Rang I", "+2 Atq, +2 Dégâts, +2 CA", ""),
 (S3, "Spécialisation Pistolet III", "MOD_PISTOL_SPEC_3", "Rang II", "+3 Atq, +4 Dégâts, +2 CA", "Duel Supérieur §6 pour le 1 pistolet"),
 (S3, "Focus Fusil I", "MOD_RIFLE_FOCUS_1", "Port d'armes : fusils + fusil 2M équipé", "+1 Atq ; ignore RD 3", "Sniper perce-armure"),
 (S3, "Focus Fusil II", "MOD_RIFLE_FOCUS_2", "Rang I", "+2 Atq ; ignore RD 7", ""),
 (S3, "Focus Fusil III", "MOD_RIFLE_FOCUS_3", "Rang II", "+3 Atq ; ignore RD 12", ""),
 (S3, "Spécialisation Fusil I", "MOD_RIFLE_SPEC_1", "Focus Fusil I", "+50 % Mod. DEX aux dégâts", ""),
 (S3, "Spécialisation Fusil II", "MOD_RIFLE_SPEC_2", "Rang I", "+100 % Mod. DEX aux dégâts", ""),
 (S3, "Spécialisation Fusil III", "MOD_RIFLE_SPEC_3", "Rang II", "+150 % Mod. DEX aux dégâts", ""),
 (S3, "Sniper Supérieur", "MOD_SNIPER_MASTER", "Spécialisation Fusil III", "Multiplicateur de critique ×3", "Détail des rangs intermédiaires à définir"),
 (S3, "Focus Gatling I", "MOD_GATLING_FOCUS_1", "Port d'armes : fusils + blaster à répétition", "+1 attaque/round", "Saturation offensive"),
 (S3, "Focus Gatling II", "MOD_GATLING_FOCUS_2", "Rang I", "+2 attaques/round", ""),
 (S3, "Focus Gatling III", "MOD_GATLING_FOCUS_3", "Rang II", "+2 attaques/round (à définir)", "Détail rang III à définir"),
 (S3, "Spécialisation Gatling I", "MOD_GATLING_SPEC_1", "Focus Gatling I", "Recul -4 ; +3 Dégâts", ""),
 (S3, "Spécialisation Gatling II", "MOD_GATLING_SPEC_2", "Rang I", "Recul -2 ; +6 Dégâts", ""),
 (S3, "Spécialisation Gatling III", "MOD_GATLING_SPEC_3", "Rang II", "Recul -1 ; dégâts à définir", "« Saturation Supérieure » §6 — effets finaux à définir"),
]
# Section MAINS NUES supprimée (13/11) : l'identité mains nues passe par la posture Duel (1M),
# la Spécialisation Arme Contondante et le rang III de Maîtrise Matukai (cf. Style de combat.csv / spé carac.csv).
S5 = "ARMURES — 3 arbres (§8.B, acté)"
CUSTOM += [
 (S5, "Seconde Peau I (légère)", "MOD_ARMOR_LIGHT_1", "Port d'armure légère + armure légère équipée", "+1 CA", "Identité : le Fugitif Blindé (Mira, Atton)"),
 (S5, "Seconde Peau II", "MOD_ARMOR_LIGHT_2", "Rang I + armure légère", "+2 CA, +1 Réflexes", ""),
 (S5, "Seconde Peau III", "MOD_ARMOR_LIGHT_3", "Rang II + armure légère", "+3 CA, +2 Réflexes", "Endgame : CA la plus haute, aucun plafond DEX"),
 (S5, "Blindage de Combat I (intermédiaire)", "MOD_ARMOR_MED_1", "Port d'armure interm. + armure interm. équipée", "RD 2, +1 Vigueur", "Identité : le Soldat Professionnel (Bao-Dur)"),
 (S5, "Blindage de Combat II", "MOD_ARMOR_MED_2", "Rang I + armure interm.", "RD 4, +2 Vigueur", ""),
 (S5, "Blindage de Combat III", "MOD_ARMOR_MED_3", "Rang II + armure interm.", "RD 6, +3 Vigueur", "Endgame : CA moyenne, plafond DEX +4"),
 (S5, "Juggernaut I (lourde)", "MOD_ARMOR_HEAVY_1", "Port d'armure lourde + armure lourde équipée", "RD 3", "Identité : la Forteresse (Mandalore, HK-47, Jedi cuirassé)"),
 (S5, "Juggernaut II", "MOD_ARMOR_HEAVY_2", "Rang I + armure lourde", "RD 5, Immunité Renversement", ""),
 (S5, "Juggernaut III", "MOD_ARMOR_HEAVY_3", "Rang II + armure lourde", "RD 7, Immunité Renversement + Étourdissement", "RD cumulée max : lourde 4 + Jugg III 7 + Robustesse II 2 = RD 13"),
]
S6 = "MÉTAMAGIE (§7.A, acté — budget Consulaire)"
CUSTOM += [
 (S6, "Pouvoir Amplifié I", "MOD_META_EMPOWER_1", "Classe Jedi/Sith", "Dégâts des pouvoirs offensifs +15 % ; coût +2 PF", ""),
 (S6, "Pouvoir Amplifié II", "MOD_META_EMPOWER_2", "Rang I", "+30 % ; coût +4 PF", ""),
 (S6, "Pouvoir Amplifié III", "MOD_META_EMPOWER_3", "Rang II", "+50 % ; coût +6 PF", ""),
 (S6, "Pouvoir Pénétrant I", "MOD_META_PENETRATE_1", "Classe Jedi/Sith", "+2 au DD des pouvoirs offensifs et de contrôle", ""),
 (S6, "Pouvoir Pénétrant II", "MOD_META_PENETRATE_2", "Rang I", "+4 au DD", ""),
 (S6, "Pouvoir Pénétrant III", "MOD_META_PENETRATE_3", "Rang II", "+6 au DD", ""),
 (S6, "Pouvoir Prolongé", "MOD_META_EXTEND", "Classe Jedi/Sith", "Durée de tous les buffs de Force ×2", "1 seul rang"),
]
S7 = "SPÉCIALISATIONS CARACTÉRISTIQUE — spé carac.csv (ordre canonique FOR, DEX, CON, INT, SAG, CHA ; une par caractéristique, arbres exclusifs entre eux)"
CUSTOM += [
 (S7, "Raffinement Gamoréen I", "MOD_GAMORREAN_1", "À définir", "+1 FOR ; + ½ mod. FOR en rangs sur toutes les compétences ; interdit les 5 autres arbres de carac", ""),
 (S7, "Raffinement Gamoréen II", "MOD_GAMORREAN_2", "Rang I", "+2 FOR ; tient toutes les armes à 1M (mêlée ET distance) ; postures autorisées : Duel et Ambidextrie uniquement", "Test moteur T1 requis (arme double en main gauche) ; les repeating ne sont pas des armes doubles côté moteur"),
 (S7, "Raffinement Gamoréen III", "MOD_GAMORREAN_3", "Rang II", "+3 FOR ; immunité au mental", ""),
 (S7, "Techniques Echanis I", "MOD_ECHANI_1", "À définir", "+1 DEX ; attaque mêlée : FOR/DEX (si DEX > FOR) ; interdit les 5 autres arbres", "Validé"),
 (S7, "Techniques Echanis II", "MOD_ECHANI_2", "Rang I", "+2 DEX ; dégâts mêlée : FOR/DEX (si DEX > FOR)", "Validé"),
 (S7, "Techniques Echanis III", "MOD_ECHANI_3", "Rang II", "+3 DEX ; supprime le plafond de DEX des armures", "Perce le pilier §8.A (assumé) — la duelliste cuirassée (Brianna)"),
 (S7, "Voie du dragon Kraith I", "MOD_KRAITH_CON_1", "À définir", "+1 CON ; RD + mod. CON ; interdit les 5 autres arbres", ""),
 (S7, "Voie du dragon Kraith II", "MOD_KRAITH_CON_2", "Rang I", "+2 CON ; toutes les 6 s : convertit 5 % des PV max en 5 % des PF max si PF < 50 % (jamais sous 75 % PV)", "Rituel complet = 25 % PV ↔ 25 % PF ; combo assumé avec le pouvoir Corps de Force"),
 (S7, "Voie du dragon Kraith III", "MOD_KRAITH_CON_3", "Rang II", "+3 CON ; toutes les sauvegardes + mod. CON", ""),
 (S7, "Chasseur de prime Gand I", "MOD_GAND_1", "À définir", "+1 INT ; attaque distance : DEX/INT (si INT > DEX) ; interdit les 5 autres arbres", "Validé"),
 (S7, "Chasseur de prime Gand II", "MOD_GAND_2", "Rang I", "+2 INT ; dégâts distance : DEX/INT (si INT > DEX)", "Validé"),
 (S7, "Chasseur de prime Gand III", "MOD_GAND_3", "Rang II", "+3 INT ; dégâts des grenades ×2", "Implémentation via le chantier Pouvoirs (scripts des sorts d'objet)"),
 (S7, "Maîtrise Matukai I", "MOD_MATUKAI_SAG_1", "À définir", "+1 SAG ; ajoute le mod. de SAG à l'attaque (s'ajoute à la carac directrice) ; interdit les 5 autres arbres", "Exclusivité : colonne exclusion de feat.2da (à tester) + garde-fou script"),
 (S7, "Maîtrise Matukai II", "MOD_MATUKAI_SAG_2", "Rang I", "+2 SAG ; la SAG remplace la DEX pour la CA", "Cumulable avec Précognition guerrière (types de bonus distincts)"),
 (S7, "Maîtrise Matukai III", "MOD_MATUKAI_SAG_3", "Rang II", "+3 SAG ; sur critique à mains nues : Vague de Force gratuite — renversement 1 tour, aucun dégât (DD Réflexes 10 + Niv + SAG ; proc = plage/20/coup ; max 1/round ; pas de re-proc au sol ; stun uniquement via Spé Contondante L2 — même jet de proc ; rien si immunisé)", "Mains nues = arme 1M : cf. Duel dans Style de combat.csv"),
 (S7, "Héritage de Nomi I", "MOD_NOMI_1", "À définir", "+1 CHA ; les compagnons gagnent 100 % de l'XP ; interdit les 5 autres arbres", ""),
 (S7, "Héritage de Nomi II", "MOD_NOMI_2", "Rang I", "+2 CHA ; groupe : jets de sauvegarde + mod. CHA", ""),
 (S7, "Héritage de Nomi III", "MOD_NOMI_3", "Rang II", "+3 CHA ; CA + mod. CHA", "Cumulable avec Précognition guerrière (types de bonus distincts)"),
]

# ---------------------------------------------------------------- écriture
out = [["ID 2DA", "Label 2DA", "Nom (FR)", "Source", "Catégorie", "Prérequis (vanilla)", "Effet (vanilla / description)", "Changement (mod)"]]
for r in rows[1:]:
    idx = r[0]
    if labels.get(idx, "") == "":
        continue
    nom, cat, eff = NOMS.get(idx, (labels[idx], C_HID, "À documenter"))
    out.append([idx, labels[idx], nom, "Vanilla", cat, prereq(r), eff, CHG.get(idx, "")])

cur = None
for section, nom, label, pre, eff, note in CUSTOM:
    if section != cur:
        out.append(["", "", "══ %s ══" % section, "CUSTOM — absent du jeu vanilla", "", "", "", ""])
        cur = section
    out.append(["nouveau (246+)", label, nom, "CUSTOM — absent du jeu vanilla", section.split(" — ")[0], pre, eff, note])

with open(DST, "w", encoding="utf-8-sig", newline="") as f:
    csv.writer(f).writerows(out)
print("OK :", DST, "-", len(out) - 1, "lignes")
