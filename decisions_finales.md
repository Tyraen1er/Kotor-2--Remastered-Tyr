# Décisions Finales d'Équilibrage — Synthèse (*KotOR 2 Overhaul*)

Ce document est le **contrat de game design** : chaque décision actée y figure sous forme condensée.
Les justifications, la recherche (JdR papier, D&D, consensus communauté) et les notes d'implémentation sont dans **[`decisions_annexes.md`](decisions_annexes.md)**.

| Domaine | Décision (résumé) | Détail |
| :--- | :--- | :---: |
| Progression des classes | Symétrie inverse Combattants ↔ Mages (dons ↔ pouvoirs) | §1 |
| Pouvoirs de la Force | Aucun ajout ; nerf du haut du panier, buff des alternatives, restauration via Métamagie | §2 |
| Établi & Boss | Plafonds d'amélioration `+2/+5/+10`, RD des boss `3/7/12`, combats de 5–10 rounds | §3 |
| Armes à distance | Triangle Pistolet / Fusil / Gatling, 3 rangs de dons par famille | §4 |
| Armes de mêlée | 5 archétypes (Double lame, Ambidextrie, Duel, Hache 2M, Bâton/Mains nues) | §5 |
| Architecture de dons | 9 dons par style (3×3) ; budgets : Gardien 21 / Sentinelle 16 / Consulaire 13 | §6 |
| Dons transversaux | 7 dons de Métamagie + *Esquive Totale* (anti-AoE) | §7 |
| Armures | RD native (Interm. 2 / Lourde 4), 3 arbres de dons par type, dégradé de pouvoirs, *Condition physique* révisé | §8 |
| Contrat mathématique | DPR nets et durées de boss cibles par phase de jeu | §9 |

---

## Partie 1 : Décisions Actées

### 1. Progression des Classes (`spellgain.2da` & `featgain.2da`)

Symétrie inverse stricte entre Combattants et Mages :

| Famille de Classes | Gain de Pouvoirs | Total Pouvoirs (Niv. 30) | Gain de Dons | Total Dons (Niv. 30) | Identité |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Gardien / Maître d'Armes / Maraudeur Sith** | `1/3` niveaux | ~12 | `2/3` niveaux + 1 don Niv. 1 | **21** | Maître Martial : style (3) + spé (3) + active (3) + défenses (6) + 6 dons bonus |
| **Sentinelle / Veilleur / Assassin Sith** | `1/2` niveaux | ~16 | `1/2` niveaux + 1 don Niv. 1 | **16** | Hybride Tactique : style (3) + spé (3) + active (3) + défenses (6) + 1 don bonus |
| **Consulaire / Maître Jedi / Seigneur Sith** | `1/1` niveau | ~31 | `1/2,5` niveaux + 1 don Niv. 1 | **13** | Archimage : métamagie (7) + robustesse (3) + 3 dons bonus |

### 2. Philosophie des Pouvoirs de la Force

1. **Aucun nouveau pouvoir** : rééquilibrage à 100 % dans [`k_inc_force.nss`](file:///C:/Users/emman/Desktop/dev/Kotor%202%20Mods/_reference/scripts/k_inc_force.nss) et [`spells.csv`](file:///C:/Users/emman/Desktop/dev/Kotor%202%20Mods/_reference/2da/spells.csv).
2. **Hiérarchie :** *Éclair/Tempête* (zone) et *Blessure/Étranglement/Mise à mort* (monocible) restent les meilleurs DPS de Force — **nerfés à la base**, restaurables via **Métamagie**. Les alternatives sont boostées sans jamais dépasser ce plafond.
3. **Alignement :** *Champ de Stase* reste un pouvoir du Côté Lumineux.

### 3. Établi & Boss (Rythme des Combats)

**A. Plafond des améliorations d'armes** (pièces `u_r_*`, `u_m_*`, `u_l_*` retravaillées) :
- Early (Niv. 1–10, Mk I) : max **`+2` dégâts moyens/coup** *(vanilla `+3,5`)* • Mid (Niv. 11–18, Mk II) : max **`+5`** *(vanilla `+11`)* • Late (Niv. 19+, Mk III) : max **`+10`** *(vanilla `+25` à `+30`)*

**B. Boss** :
- **Règle d'or :** aucun boss tué en moins de 4 rounds ; cible **5–10 rounds** (10–15 pour Sion/Traya).
- **RD passive** des Sous-Boss/Boss (`Set_4`/`Set_5`) : `RD 3` (Early) / `RD 7` (Mid) / `RD 12` (Late).
- **`damagemult` des boss réduit** (`autobalance.2da`) pour que le joueur tienne aussi 5–10 rounds.

### 4. Identités — Armes à Distance (Triangle Pistolet / Fusil / Gatling)

| Archétype | Rôle | Cadence (sans / avec *Vitesse*) | Dons dédiés (I → II → III) |
| :--- | :--- | :---: | :--- |
| **Pistolets Blasters** | Mobilité, esquive, multi-effets | 3 / 5 tirs | **Maîtrise du Pistolet :** `+1/+2/+3 Atq`, `+1/+2/+4 Dégâts`, `+1` puis `+2 CA` |
| **Fusil Blaster (2M)** | Sniper Perce-Armure | 1–2 / 3–4 tirs | **Maîtrise du Fusil :** `+1/+2/+3 Atq`, ignore RD `3/7/12`, `+50/100/150% Mod. DEX`, Crit `×3` au rang III |
| **Gatling (Arme Lourde)** | Saturation offensive pure | 4 / 6 tirs | **Maîtrise de la Gatling :** `+1` puis `+2 attaques/round`, recul `-4/-2/-1`, `+3` puis `+6 Dégâts` |

### 5. Identités — Armes de Mêlée

| Archétype | Rôle | Mécaniques actées |
| :--- | :--- | :--- |
| **Lame Double** | Offensif pur | Gros dés (`2d12`/`2d10`), `1.5× FOR`, bonus de dégâts dédié. Contrepartie : `0 CA`, crit `20-20`, pas de *Finesse*, sensible à la RD |
| **Ambidextrie (2 armes)** | Parade & polyvalence | Malus réduits **+ CA** : Rang I `-4/-8 Atq, +1 CA` → Rang III `0/-2 Atq, +3 CA` (`0/0` avec arme légère en main gauche). 6 slots / 4 cristaux, crit `19-20`, *Finesse* OK |
| **Arme Simple (1M) — Duel** |  |  |
| **Arme Lourde (2M)** |  |  |
| **Mains Nues** | Moine contrôleur / Arts Mutaki | Bonus de CA, scaling SAG + (FOR ou DEX), critique étendu (`17-20`) et **Force Whirlwind sur critique** (`DD = 10 + Niveau + SAG`) |

### 6. Architecture de Dons & Budgets par Classe

**Règle : chaque style = 9 dons** (3 rangs de Posture + 3 de Maîtrise d'arme + 3 de Maîtrise Supérieure), CaC comme distance. Le bonus CA de l'Ambidextrie est intégré dans *Combat à deux armes* (pas d'arbre payant en plus).

| Style | Arbre 1 : Posture | Arbre 2 : Maîtrise | Arbre 3 : Supérieure (Prestige) |
| :--- | :--- | :--- | :--- |
| **1M / 1 Pistolet** | *Science du Duel* (`+1/+2/+3 Atq & CA`, ignore RD) | *Spécialisation 1M/Pistolet* (`+50/+100% Mod.`) | *Duel Supérieur* (`+150% Mod.`, crit, ignore RD 12) |
| **Ambidextrie (2 armes/pistolets)** | *Combat à 2 armes* (malus → `0/-2` + `+1/+2/+3 CA`) | *Spécialisation Mêlée/Pistolet* | *Cà2A Supérieur* |
| **Lame Double** | *Combat à 2 armes* (malus → `0/-2` + **`+1/+2/+3 Dégâts`**, `0 CA`) | *Spécialisation Lame Double* (`1.5× FOR`) | *Cà2A Supérieur* (assaut lourd) |
| **Arme Lourde (2M)** | *Focus Arme Lourde* (précision, Brise-Armure) | *Spécialisation Hache* (`2.0× FOR`) | *Maîtrise Hache Supérieure* (crit `19-20 ×3`) |
| **Mains Nues / Pique de Force / Baton** | *Arts Martiaux* (`+1/+2/+3 CA`, précision) | *Arts Mutaki I/II/III* (Whirlwind sur crit) | *Arts Martiaux Supérieurs* |
| **Fusil Blaster** | *Focus Fusil* (`+Atq`, ignore RD) | *Spécialisation Fusil* (`Mod. DEX`) | *Sniper Supérieur* (crit `×3`) |
| **Gatling** | *Focus Gatling* (cadence) | *Spécialisation Gatling* (recul, dégâts) | *Saturation Supérieure* |

**Détail Arbre Mains Nues — Arts Mutaki (I → II → III) :**
- **Arts Mutaki I :** Attaque et dégâts = jet + `(DEX ou FOR) + SAG`. `+1 CA`. Plage de critique `19-20`.
- **Arts Mutaki II :** Attaque et dégâts = jet + `(DEX ou FOR) + SAG`. `+2 CA` à mains nues. Plage de critique `18-20`. *Force Whirlwind* (DD Vigueur : `10 + Niveau + SAG`) pendant **1 tour** en cas de critique.
- **Arts Mutaki III :** Attaque et dégâts = jet + `(DEX ou FOR) + SAG`. `+3 CA`. Plage de critique `17-20`. *Force Whirlwind* (DD Vigueur : `10 + Niveau + SAG`) pendant **2 tours** en cas de critique.

**Budgets Fin de Jeu (Niv. 30) — Répartition Précise :**
- **Gardien / Maître d'Armes / Maraudeur (21 dons) — Maître Martial Accomplie :**
  - **15 dons socle :** 3 (Style de combat) + 3 (Spécialisation d'arme) + 3 (Attaque active) + 6 (Défense : *Robustesse* 3 + *Condition physique* 3 ou *Armure* 3).
  - **+ 6 dons bonus :** personnalisation totale (ex. *Esquive Totale*, *Finesse*, second style/arme, spécialisation d'armure additionnelle, implants).
- **Sentinelle / Veilleur / Assassin (16 dons) — Hybride Tactique Équilibré :**
  - **15 dons socle :** 3 (Style) + 3 (Spécialisation d'arme) + 3 (Attaque active) + 6 (Défense : *Robustesse* 3 + *Condition physique* ou *Seconde Peau* 3).
  - **+ 1 don bonus :** choix utilitaire (*Esquive Totale*, *Finesse*).
- **Consulaire / Maître Jedi / Seigneur Sith (13 dons) — Archimage Spécialisé :**
  - **10 dons socle :** 7 (Métamagie complète : *Amplifié* 3 + *Pénétrant* 3 + *Prolongé* 1) + 3 (*Robustesse* pour combler son dé de vie d6).
  - **+ 3 dons bonus :** flexibilité (*Condition physique* pour sauvegardes, posture *Duel 1M* pour +3 CA, ou *Arts Mutaki* pour combat au contact).

### 7. Dons Transversaux : Métamagie & Esquive Totale

**A. Métamagie (7 dons, calibrés sur le budget du Consulaire) :**

| Don | Rangs | Effet |
| :--- | :---: | :--- |
| **Pouvoir Amplifié** | 3 | Dégâts des pouvoirs offensifs `+15/+30/+50 %` (coût `+2/+4/+6 PF`) |
| **Pouvoir Pénétrant** | 3 | `+2/+4/+6` au DD de sauvegarde des pouvoirs offensifs et de contrôle |
| **Pouvoir Prolongé** | 1 | Durée de tous les buffs de Force `×2` |

**B. Esquive Totale** (`FEAT_EVASION`, ligne 125) — contre-mesure anti-AoE :
- **Effet :** réussite du jet de sauvegarde face à une AoE (*Tempête*, *Éclair*, *Vague*, *Champ de Mort*, *Cri*, grenades...) → **0 dégât** ; échec → **dégâts ÷ 2**.
- **Accès joueur :** sélectionnable **uniquement à partir d'une classe de prestige** (Niv. 15+) ; conservé en don automatique de l'Éclaireur niv. 6 (Mira).
- **Ennemis :** octroyé automatiquement à **tous les Jedi/Sith de niveau 20+** (via `k_inc_force.nss`).

### 8. Armures : RD Native, 3 Arbres de Dons, Dégradé de Pouvoirs, *Condition physique* révisé

Décisions actées (08/11/2026) — justifications et recherche dans [`decisions_annexes.md`](decisions_annexes.md#1-armures--recherche-et-justifications) :

**A. RD native des armures (passif, sans don)** — CA et plafonds DEX vanilla inchangés :

| Type | CA base | Plafond DEX | **RD Physique & Énergie native** |
| :--- | :---: | :---: | :---: |
| Légère | 4–5 | +4/+5 | **0** |
| Intermédiaire | 6–7 | +2/+3 | **RD 2** |
| Lourde | 8–9 | +0/+1 | **RD 4** |

**B. Trois arbres de dons (3 dons chacun, actifs uniquement avec le type d'armure associé) :**

| Arbre | Prérequis | Rang I | Rang II | Rang III | Identité |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Seconde Peau** (légère) | Port d'armure légère | `+1 CA` | `+2 CA`, `+1 Réflexes` | `+3 CA`, `+2 Réflexes` | Le Fugitif Blindé (Mira, Atton) |
| **Blindage de Combat** (intermédiaire) | Port d'armure interm. | `RD 2`, `+1 Vigueur` | `RD 4`, `+2 Vigueur` | `RD 6`, `+3 Vigueur` | Le Soldat Professionnel (Bao-Dur) |
| **Juggernaut** (lourde) | Port d'armure lourde | `RD 3` | `RD 5`, Immun. Renversement | `RD 7`, Immun. Renversement + Étourdissement | La Forteresse (Mandalore, HK-47, Jedi cuirassé) |

RD cumulée max fin de jeu (Juggernaut complet) : lourde `RD 4` + *Juggernaut III* `RD 7` + *Robustesse II* `RD 2` = **RD 13**.

**C. Dégradé des pouvoirs autorisés sous armure** (`spells.2da`, `forbiditemmask`) :

| Équipement | Pouvoirs accessibles |
| :--- | :--- |
| Robe Jedi / sans armure | Tous (inchangé) |
| Armure légère | Vanilla **+ *Vaillance I* et *Résistance à la Force*** |
| Armure intermédiaire | Vanilla **+ *Résistance à la Force*** |
| Armure lourde | Vanilla strict — le prix du blindage |

**D. *Condition physique* révisé** (lignes 13/21/22 de `feat.2da`) :

| Rang | Vanilla | Révisé |
| :--- | :--- | :--- |
| I / II | `+1` / `+2` toutes sauvegardes | inchangé |
| III (Maître) | `+3` toutes sauvegardes | `+3` **+ `+2` supplémentaires contre les pouvoirs de Force** |

### 9. Contrat Mathématique (DPR nets & durées de boss cibles)

Avec établi plafonné (`+2/+5/+10`) et RD des boss (`3/7/12`) :

| Phase (Boss étalon) | Gatling / Lame Double | 2 Pistolets / 2 Armes | Fusil / Duel 1M |
| :--- | :--- | :--- | :--- |
| **EARLY** — Niv. 8 (120 PV, CA 20, RD 3) | 16,5 DPR — 7,2 rounds | 11,7 DPR — 6–10 rounds | 19,5 DPR — 6,1 rounds |
| **MID** — Niv. 16 (280 PV, CA 29, RD 7) | 39,0 DPR — 7,2 rounds | 25,2 DPR — 6–11 rounds | 58,6 DPR — 4,8 rounds |
| **LATE** — Niv. 26 (650 PV, CA 44, RD 12) | 57,6 DPR — 11,2 rounds | 45,5 DPR — 7–14 rounds | 122–128 DPR — 5,1 rounds |

*Ambidextrie : l'Attaque Sournoise sur cible contrôlée double le DPR net. Détail complet (attaques/round, dégâts bruts, précision, DPR sbires) : [`decisions_annexes.md`](decisions_annexes.md#3-contrat-mathématique-détaillé).*

---

## Partie 2 : TODOs & Chantiers Ouverts

1. **[TODO Équipement & Loot] :** Revoir les statistiques des équipements et leur distribution dans les tables de loot et chez les marchands (notamment pour soutenir la viabilité des armes Primitives, Contondantes et Vibrantes sur toute la progression Niv. 1 à 30).
2. **[TODO Craft & Établi] :** Revoir les équipements craftables à l'établi (`itemcreate.2da` / `.uti`) pour garantir que chaque famille d'arme dispose de recettes viables et cohérentes avec les plafonds d'amélioration fixés.
3. **[TODO Améliorations par Famille d'Armes] :** Revoir les types d'améliorations accessibles par catégorie d'arme à l'établi (ex. Lame + Garde uniquement pour les armes Primitives sans cellule énergétique ; Lame + Garde + Cellule pour les Vibrantes ; cristaux pour les Lasers).
4. **[TODO Amélioration de la Furtivité] :** Une attaque en étant furtif est forcément un critique ?
