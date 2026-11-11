# Loot Aléatoire — Système de Trésor de KotOR 2 (`k_inc_treas_k2.nss`)

> Le moteur TSL ne possède **pas de `randomitem.2da`** (c'était KotOR 1) : tout le loot aléatoire est généré
> par scripts (`PlaceTreasure` / `PlaceTreasureDisposable` de [`k_inc_treas_k2.nss`](
file:///C:/Users/emman/Desktop/dev/Kotor%202%20Mods/_reference/scripts/k_inc_treas_k2.nss)).

## 1. Mécanique générale

1. **Niveau d'objet** : `niveau PJ + Random(8) − 5` (borné 1–30). Le niveau du PJ est la variable globale `G_PC_LEVEL`.
2. **Rareté (objets d'équipement)** : jet `Random(95) + 000_RareItemChance` ; si `> 100` → objet **rare** (+5 niveaux d'objet).
   Chaque échec augmente `000_RareItemChance` (système « pity » : une rare finit toujours par tomber).
3. **Classe d'objet** (centaines) : 100 armes, 200 améliorations, 300 équipement, 400 armures, 500 droïdes, 900 consommables.
   Sans classe imposée par le conteneur : `Random(4)+1` (l'équipement 300 est favorisé : 50 % des « améliorations » sont relancées en équipement).
4. **Sous-classe** (dizaines) : tirage uniforme dans la classe (ex : 411–431 armures, 311 ceintures, 331 casques...).
5. **Palier d'objet** (unités) : converti depuis le niveau d'objet selon une **courbe par famille** (tableau ci-dessous).
6. **Restrictions spéciales** : pas d'armure avant le niveau 4 (Péragus), pas d'améliorations de sabre avant niv. d'objet 6 ET niv. PJ 10,
   grenades « trop fortes » remplacées par une grenade inférieure, fusées uniquement si Mira est dans l'équipe,
   et sur *Le Ravageur*/Malachor V (851/852NIH, 901–906MAL) : seulement medpacs/grenades/boucliers/composants/produits chimiques.

## 2. Courbes palier ↔ niveau (inversées : niveau PJ minimum pour voir un palier)

| Famille (préfixe) | Courbe (palier = f(niveau objet)) | Niveau PJ mini (normal) | Exemple |
| :-- | :-- | :--: | :-- |
| Armes `w_blaste_` / `w_brifle_` / `w_melee_` | palier = niveau (direct) | palier + 4 | `w_blaste_09` dès niv. 13 |
| Améliorations `u_r_*` / `u_m_*` / `u_a_*` | palier = niveau ÷ 2 | palier × 2 + 4 | `u_a_over_03` dès niv. 10 |
| Émetteurs/lentilles/cellules `u_l_emit/lens/cell` | palier = (niveau − 6) ÷ 2 | palier × 2 + 10 | `u_l_lens_03` dès niv. 16 |
| Cristaux `u_l_crys_` | palier = niveau − 5 | palier + 9 | `u_l_crys_04` dès niv. 13 |
| Cristaux de couleur `u_l_colo_` | palier = Random((niveau−5)÷3+2) clampé 4–9 | niv. PJ 10+ (et niveau d'objet ≥ 10) | — |
| Ceintures / gants / casques | palier = niveau ÷ 2 | palier × 2 + 4 | `a_belt_05` dès niv. 14 |
| Implants `e_imp1..4_` | palier = niveau ÷ 3 (+ CON du PJ pour le rang d'implant) | palier × 3 + 4 | `e_imp2_02` dès niv. 10 |
| Armures `a_light/medium/heavy/robe_` | palier = niveau ÷ 2 | palier × 2 + 4 | `a_heavy_07` dès niv. 18 |
| Boucliers droïde `d_shield_` | palier = niveau ÷ 3 (−4 si > 6) | palier × 3 + 4 | — |
| Objets rares | niveau d'objet +5 | −5 par rapport au normal | — |

## 3. Objets pouvant apparaître aléatoirement (par famille)

### Accessoire — Casque/Masque (30)

| Palier | ResRef | Nom | Niv. PJ mini (normal) | Niv. PJ mini (rare) |
| :--: | :-- | :-- | :--: | :--: |
| 1 | `a_helmet_01` | Serre-tête neural | 6 | 1 |
| 2 | `a_helmet_02` | Masque respirateur | 8 | 3 |
| 3 | `a_helmet_03` | Serre-tête de Rakata | 10 | 5 |
| 4 | `a_helmet_04` | Augmentateur de discrétion | 12 | 7 |
| 5 | `a_helmet_05` | Visière de perception bothan | 14 | 9 |
| 6 | `a_helmet_06` | Bloquants soniques | 16 | 11 |
| 7 | `a_helmet_07` | Serre-tête d'interface | 18 | 13 |
| 8 | `a_helmet_08` | Visière de visée | 20 | 15 |
| 9 | `a_helmet_09` | Visière de protection | 22 | 17 |
| 10 | `a_helmet_10` | Capteur de pilote spatial | 24 | 19 |
| 11 | `a_helmet_11` | Visière royale | 26 | 21 |
| 12 | `a_helmet_12` | Serre-tête de méditation | 28 | 23 |
| 13 | `a_helmet_13` | Visière sensorielle bothan | 30 | 25 |
| 14 | `a_helmet_14` | Aveuglants arkaniens | 30 | 27 |
| 15 | `a_helmet_15` | Capteur de combat | 30 | 29 |
| 16 | `a_helmet_16` | Analyseur de visée multispectral | 30 | 30 |
| 17 | `a_helmet_17` | Casque de conscience | 30 | 30 |
| 18 | `a_helmet_18` | Respirateur | 30 | 30 |
| 19 | `a_helmet_19` | Masque de chasse de Das'skar | 30 | 30 |
| 20 | `a_helmet_20` | Masque de la Force | 30 | 30 |
| 21 | `a_helmet_21` | Masque Sith | 30 | 30 |
| 22 | `a_helmet_22` | Masque stabilisant | 30 | 30 |
| 23 | `a_helmet_23` | Serre-tête de méditation Mutaki | 30 | 30 |
| 24 | `a_helmet_24` | Evaluateur de cible | 30 | 30 |
| 25 | `a_helmet_25` | Serre-tête de Saresh | 30 | 30 |
| 26 | `a_helmet_26` | Serre-tête de Bindo | 30 | 30 |
| 27 | `a_helmet_27` | Visière de protection améliorée | 30 | 30 |
| 28 | `a_helmet_28` | Bouclier de Force | 30 | 30 |
| 29 | `a_helmet_29` | Visière d'absorption | 30 | 30 |
| 30 | `a_helmet_30` | Visière de Force | 30 | 30 |

### Accessoire — Ceinture (30)

| Palier | ResRef | Nom | Niv. PJ mini (normal) | Niv. PJ mini (rare) |
| :--: | :-- | :-- | :--: | :--: |
| 1 | `a_belt_01` | Amplificateur d'adrénaline | 6 | 1 |
| 2 | `a_belt_02` | Cardio-régulateur | 8 | 3 |
| 3 | `a_belt_03` | Générateur de champ de camouflage | 10 | 5 |
| 4 | `a_belt_04` | Ceinture multifonction de la Czerka | 12 | 7 |
| 5 | `a_belt_05` | Ampli. d'adrénaline amélioré | 14 | 9 |
| 6 | `a_belt_06` | Ceinture d'atténuation Aratech | 16 | 11 |
| 7 | `a_belt_07` | Augmentateur de force | 18 | 13 |
| 8 | `a_belt_08` | Cardio-régulateur Systech | 20 | 15 |
| 9 | `a_belt_09` | Hyper-amplificateur d'adrénaline | 22 | 17 |
| 10 | `a_belt_10` | Diffuseur d'ombres de l'Echange | 24 | 19 |
| 11 | `a_belt_11` | Inhibiteur d'inertie | 26 | 21 |
| 12 | `a_belt_12` | Bouclier de capacitance | 28 | 23 |
| 13 | `a_belt_13` | Générateur de bouclier thermique | 30 | 25 |
| 14 | `a_belt_14` | Générateur de camouflage ériadu | 30 | 27 |
| 15 | `a_belt_15` | Augmentateur de force CNS | 30 | 29 |
| 16 | `a_belt_16` | Ceinture multifonction de l'Echange | 30 | 30 |
| 17 | `a_belt_17` | Ceinture d'immunité | 30 | 30 |
| 18 | `a_belt_18` | Stimulateur d'adrénaline | 30 | 30 |
| 19 | `a_belt_19` | Ceinture d'amplification nerveuse | 30 | 30 |
| 20 | `a_belt_20` | Ceinture Jal Shey | 30 | 30 |
| 21 | `a_belt_21` | Générateur de boucliers multiples | 30 | 30 |
| 22 | `a_belt_22` | Caméléon defel | 30 | 30 |
| 23 | `a_belt_23` | Ceinture d'éclaireur frozian | 30 | 30 |
| 24 | `a_belt_24` | Ceinture de spécialiste en technologie | 30 | 30 |
| 25 | `a_belt_25` | Cardio-régulateur Aratech | 30 | 30 |
| 26 | `a_belt_26` | Augmentateur de force GNS | 30 | 30 |
| 27 | `a_belt_27` | Ceinture de Qel-Droma | 30 | 30 |
| 28 | `a_belt_28` | Ceinture d'immortalité | 30 | 30 |
| 29 | `a_belt_29` | Ceinture d'échos Aratech | 30 | 30 |
| 30 | `a_belt_30` | Ceinture de mentor Jal Shey | 30 | 30 |

### Accessoire — Gants (29)

| Palier | ResRef | Nom | Niv. PJ mini (normal) | Niv. PJ mini (rare) |
| :--: | :-- | :-- | :--: | :--: |
| 1 | `a_gloves_01` | Gants isolants | 6 | 1 |
| 2 | `a_gloves_02` | Gants de l'Echange | 8 | 3 |
| 4 | `a_gloves_04` | Gants de survie de Taris | 12 | 7 |
| 5 | `a_gloves_05` | Gants de précision | 14 | 9 |
| 6 | `a_gloves_06` | Gantelets gamorréens | 16 | 11 |
| 7 | `a_gloves_07` | Gants de travail de l'Echange | 18 | 13 |
| 8 | `a_gloves_08` | Gantelets de défense de la Czerka | 20 | 15 |
| 9 | `a_gloves_09` | Gants détonateurs | 22 | 17 |
| 10 | `a_gloves_10` | Gants de précision sans arme | 24 | 19 |
| 11 | `a_gloves_11` | Gants d'infiltrateur | 26 | 21 |
| 12 | `a_gloves_12` | Gants de perception de Jal Shey | 28 | 23 |
| 13 | `a_gloves_13` | Gants de guerre gamorréens | 30 | 25 |
| 14 | `a_gloves_14` | Ampli. force physique ériadu | 30 | 27 |
| 15 | `a_gloves_15` | Gantelets de Karakan | 30 | 29 |
| 16 | `a_gloves_16` | Gants de précision bothans | 30 | 30 |
| 17 | `a_gloves_17` | Gantelets de puissance Sith | 30 | 30 |
| 18 | `a_gloves_18` | Gantelets de puissance gamorréens | 30 | 30 |
| 19 | `a_gloves_19` | Gants de combat nagai | 30 | 30 |
| 20 | `a_gloves_20` | Gants de voyou kubaz | 30 | 30 |
| 21 | `a_gloves_21` | Gants d'automatisme | 30 | 30 |
| 22 | `a_gloves_22` | Gants de méditation de Jal Shey | 30 | 30 |
| 23 | `a_gloves_23` | Gants de précision Echani | 30 | 30 |
| 24 | `a_gloves_24` | Gants de Zeison Sha | 30 | 30 |
| 25 | `a_gloves_25` | Gantelets de dominateur | 30 | 30 |
| 26 | `a_gloves_26` | Gants de soldat nikto | 30 | 30 |
| 27 | `a_gloves_27` | Gants d'Ossluk | 30 | 30 |
| 28 | `a_gloves_28` | Gants de désintégration | 30 | 30 |
| 29 | `a_gloves_29` | Gants d'automatisme améliorés | 30 | 30 |
| 30 | `a_gloves_30` | Gants de foudre | 30 | 30 |

### Amélioration — Cellule d'énergie (mêlée) (15)

| Palier | ResRef | Nom | Niv. PJ mini (normal) | Niv. PJ mini (rare) |
| :--: | :-- | :-- | :--: | :--: |
| 1 | `u_m_cell_01` | Cellule à ions | 6 | 1 |
| 2 | `u_m_cell_02` | Cellule à vibrations | 8 | 3 |
| 3 | `u_m_cell_03` | Cellule d'énergie alcaline | 10 | 5 |
| 4 | `u_m_cell_04` | Cellule à décharge sonique | 12 | 7 |
| 5 | `u_m_cell_05` | Cellule à ions T2 | 14 | 9 |
| 6 | `u_m_cell_06` | Cellule à vibrations T2 | 16 | 11 |
| 7 | `u_m_cell_07` | Cellule d'énergie alcaline T2 | 18 | 13 |
| 8 | `u_m_cell_08` | Cellule à décharge sonique T2 | 20 | 15 |
| 9 | `u_m_cell_09` | Cellule à ions T3 | 22 | 17 |
| 10 | `u_m_cell_10` | Cellule à vibrations T3 | 24 | 19 |
| 11 | `u_m_cell_11` | Cellule d'énergie alcaline T3 | 26 | 21 |
| 12 | `u_m_cell_12` | Cellule à décharge sonique T3 | 28 | 23 |
| 13 | `u_m_cell_13` | Cellule à ions T4 | 30 | 25 |
| 14 | `u_m_cell_14` | Cellule à vibrations T4 | 30 | 27 |
| 15 | `u_m_cell_15` | Cellule d'énergie alcaline T4 | 30 | 29 |

### Amélioration — Cellule d'énergie (sabre) (13)

| Palier | ResRef | Nom | Niv. PJ mini (normal) | Niv. PJ mini (rare) |
| :--: | :-- | :-- | :--: | :--: |
| 1 | `u_l_cell_01` | Cellule d'énergie à décharge | 12 | 7 |
| 2 | `u_l_cell_02` | Cellule d'énergie au diatum | 14 | 9 |
| 3 | `u_l_cell_03` | Cellule d'énergie à ions | 16 | 11 |
| 4 | `u_l_cell_04` | Cellule à décharge de Telgorn T1 | 18 | 13 |
| 5 | `u_l_cell_05` | Cellule d'énergie à décharge améliorée | 20 | 15 |
| 6 | `u_l_cell_06` | Cellule d'énergie au diatum améliorée | 22 | 17 |
| 7 | `u_l_cell_07` | Cellule d'énergie à ions améliorée | 24 | 19 |
| 8 | `u_l_cell_08` | Cellule à décharge de Telgorn T2 | 26 | 21 |
| 9 | `u_l_cell_09` | Cellule d'énergie à grande décharge | 28 | 23 |
| 10 | `u_l_cell_10` | Cellule d'énergie supérieure au diatium | 30 | 25 |
| 11 | `u_l_cell_11` | Cellule d'énergie à ions supérieure | 30 | 27 |
| 12 | `u_l_cell_12` | Cellule à décharge de Telgorn T3 | 30 | 29 |
| 13 | `u_l_cell_13` | Cellule d'énergie au diatum ultime | 30 | 30 |

### Amélioration — Chambre de tir (15)

| Palier | ResRef | Nom | Niv. PJ mini (normal) | Niv. PJ mini (rare) |
| :--: | :-- | :-- | :--: | :--: |
| 1 | `u_r_firi_01` | Chambre d'élargissement T1 | 6 | 1 |
| 2 | `u_r_firi_02` | Chambre d'amplification T1 | 8 | 3 |
| 3 | `u_r_firi_03` | Chambre de précision T1 | 10 | 5 |
| 4 | `u_r_firi_04` | Séparateur de rayon T1 | 12 | 7 |
| 5 | `u_r_firi_05` | Chambre mand. T1 | 14 | 9 |
| 6 | `u_r_firi_06` | Chambre d'élargissement T2 | 16 | 11 |
| 7 | `u_r_firi_07` | Chambre d'amplification T2 | 18 | 13 |
| 8 | `u_r_firi_08` | Chambre de précision T2 | 20 | 15 |
| 9 | `u_r_firi_09` | Séparateur de rayon T2 | 22 | 17 |
| 10 | `u_r_firi_10` | Chambre mand. T2 | 24 | 19 |
| 11 | `u_r_firi_11` | Chambre d'élargissement T3 | 26 | 21 |
| 12 | `u_r_firi_12` | Chambre d'amplification T3 | 28 | 23 |
| 13 | `u_r_firi_13` | Chambre de précision T3 | 30 | 25 |
| 14 | `u_r_firi_14` | Séparateur de rayon T3 | 30 | 27 |
| 15 | `u_r_firi_15` | Chambre mand. T3 | 30 | 29 |

### Amélioration — Cristal (sabre) (25)

| Palier | ResRef | Nom | Niv. PJ mini (normal) | Niv. PJ mini (rare) |
| :--: | :-- | :-- | :--: | :--: |
| 1 | `u_l_crys_01` | Cristal, adegan | 10 | 5 |
| 2 | `u_l_crys_02` | Cristal, rubat | 11 | 6 |
| 3 | `u_l_crys_03` | Cristal, Ruusan | 12 | 7 |
| 4 | `u_l_crys_04` | Cristal, nextor | 13 | 8 |
| 5 | `u_l_crys_05` | Cristal, dragite | 14 | 9 |
| 6 | `u_l_crys_06` | Cristal, fikrann | 15 | 10 |
| 7 | `u_l_crys_07` | Cristal, phond | 16 | 11 |
| 8 | `u_l_crys_08` | Cristal, bondar | 17 | 12 |
| 9 | `u_l_crys_09` | Cristal, velmorite | 18 | 13 |
| 10 | `u_l_crys_10` | Cristal, sigil | 19 | 14 |
| 11 | `u_l_crys_11` | Cristal, jenruax | 20 | 15 |
| 12 | `u_l_crys_12` | Cristal, kasha | 21 | 16 |
| 13 | `u_l_crys_13` | Cristal, opila | 22 | 17 |
| 14 | `u_l_crys_14` | Cristal, éralam | 23 | 18 |
| 15 | `u_l_crys_15` | Cristal, stygium | 24 | 19 |
| 16 | `u_l_crys_16` | Cristal, damind | 25 | 20 |
| 17 | `u_l_crys_17` | Cristal, sapith | 26 | 21 |
| 18 | `u_l_crys_18` | Cristal, pontite | 27 | 22 |
| 19 | `u_l_crys_19` | Cristal, upari | 28 | 23 |
| 20 | `u_l_crys_20` | Ultima-perle | 29 | 24 |
| 21 | `u_l_crys_21` | Cristal, solari | 30 | 25 |
| 22 | `u_l_crys_22` | Gemme lordienne | 30 | 26 |
| 23 | `u_l_crys_23` | Lingot de minerai de Barab | 30 | 27 |
| 24 | `u_l_crys_24` | Saphir d'Ankarès | 30 | 28 |
| 25 | `u_l_crys_25` | Cristal, kaiburr | 30 | 29 |

### Amélioration — Cristal de couleur (10)

| Palier | ResRef | Nom | Niv. PJ mini (normal) | Niv. PJ mini (rare) |
| :--: | :-- | :-- | :--: | :--: |
| 1 | `u_l_colo_01` | Cristal, bleu | 10 | 5 |
| 2 | `u_l_colo_02` | Cristal, vert | 10 | 5 |
| 3 | `u_l_colo_03` | Cristal, jaune | 10 | 5 |
| 4 | `u_l_colo_04` | Cristal, rouge | 10 | 5 |
| 5 | `u_l_colo_05` | Cristal, violet | 10 | 5 |
| 6 | `u_l_colo_06` | Cristal, bleu cyan | 10 | 5 |
| 7 | `u_l_colo_07` | Cristal, argenté | 10 | 5 |
| 8 | `u_l_colo_08` | Cristal, orange | 10 | 5 |
| 9 | `u_l_colo_09` | Cristal, viridien | 10 | 5 |
| 10 | `u_l_colo_10` | Cristal, bronze | 10 | 5 |

### Amélioration — Lame (mêlée) (15)

| Palier | ResRef | Nom | Niv. PJ mini (normal) | Niv. PJ mini (rare) |
| :--: | :-- | :-- | :--: | :--: |
| 1 | `u_m_edge_01` | Tranchant dévaronien modéré | 6 | 1 |
| 2 | `u_m_edge_02` | Cellule à décharge sonique T3 (mêlée) | 8 | 3 |
| 3 | `u_m_edge_03` | Tranchant en mullinine de base | 10 | 5 |
| 4 | `u_m_edge_04` | Tranchant en neutronium de base | 12 | 7 |
| 5 | `u_m_edge_05` | Tranchant dévaronien modéré | 14 | 9 |
| 6 | `u_m_edge_06` | Tranchant en ionite amélioré | 16 | 11 |
| 7 | `u_m_edge_07` | Tranchant en mullinine amélioré | 18 | 13 |
| 8 | `u_m_edge_08` | Tranchant en neutronium amélioré | 20 | 15 |
| 9 | `u_m_edge_09` | Tranchant dévaronien important | 22 | 17 |
| 10 | `u_m_edge_10` | Tranchant en ionite supérieur | 24 | 19 |
| 11 | `u_m_edge_11` | Tranchant supérieur en mullinine | 26 | 21 |
| 12 | `u_m_edge_12` | Tranchant supérieur en neutronium | 28 | 23 |
| 13 | `u_m_edge_13` | Tranchant mortel dévaronien | 30 | 25 |
| 14 | `u_m_edge_14` | Tranchant en quadranium | 30 | 27 |
| 15 | `u_m_edge_15` | Tranchant en ostrine | 30 | 29 |

### Amélioration — Lentille (sabre) (13)

| Palier | ResRef | Nom | Niv. PJ mini (normal) | Niv. PJ mini (rare) |
| :--: | :-- | :-- | :--: | :--: |
| 1 | `u_l_lens_01` | Lentille de kunda synthétisé | 12 | 7 |
| 2 | `u_l_lens_02` | Lentille de dragite | 14 | 9 |
| 3 | `u_l_lens_03` | Lentille de byrhotse | 16 | 11 |
| 4 | `u_l_lens_04` | Lentille de gemme à rayon | 18 | 13 |
| 5 | `u_l_lens_05` | Lentille vibratoire | 20 | 15 |
| 6 | `u_l_lens_06` | Lentille de kunda pur | 22 | 17 |
| 7 | `u_l_lens_07` | Lentille d'adegan | 24 | 19 |
| 8 | `u_l_lens_08` | Lentille de byrhotse pur | 26 | 21 |
| 9 | `u_l_lens_09` | Lentille de gemme à rayon améliorée | 28 | 23 |
| 10 | `u_l_lens_10` | Lentille vibratoire améliorée | 30 | 25 |
| 11 | `u_l_lens_11` | Lentille de duel d'Ossus | 30 | 27 |
| 12 | `u_l_lens_12` | Lentille de pontite | 30 | 29 |
| 13 | `u_l_lens_13` | Lentille de byrhotse améliorée | 30 | 30 |

### Amélioration — Lunette de visée (15)

| Palier | ResRef | Nom | Niv. PJ mini (normal) | Niv. PJ mini (rare) |
| :--: | :-- | :-- | :--: | :--: |
| 1 | `u_r_targ_01` | Lunette de sniper T1 | 6 | 1 |
| 2 | `u_r_targ_02` | Lunette de précision T1 | 8 | 3 |
| 3 | `u_r_targ_03` | Lunette de visée T1 | 10 | 5 |
| 4 | `u_r_targ_04` | Lunette de mutilation T1 | 12 | 7 |
| 5 | `u_r_targ_05` | Lunette de sniper T2 | 14 | 9 |
| 6 | `u_r_targ_06` | Lunette de précision T2 | 16 | 11 |
| 7 | `u_r_targ_07` | Lunette de visée T2 | 18 | 13 |
| 8 | `u_r_targ_08` | Lunette de mutilation T2 | 20 | 15 |
| 9 | `u_r_targ_09` | Lunette de sniper T3 | 22 | 17 |
| 10 | `u_r_targ_10` | Lunette de précision T3 | 24 | 19 |
| 11 | `u_r_targ_11` | Lunette de visée T3 | 26 | 21 |
| 12 | `u_r_targ_12` | Lunette de mutilation T3 | 28 | 23 |
| 13 | `u_r_targ_13` | Lunette de sniper T4 | 30 | 25 |
| 14 | `u_r_targ_14` | Lunette de précision T4 | 30 | 27 |
| 15 | `u_r_targ_15` | Lunette de visée T4 | 30 | 29 |

### Amélioration — Overlay (armure) (30)

| Palier | ResRef | Nom | Niv. PJ mini (normal) | Niv. PJ mini (rare) |
| :--: | :-- | :-- | :--: | :--: |
| 1 | `u_a_over_01` | Protection contre la chaleur T1 | 6 | 1 |
| 2 | `u_a_over_02` | Revêtement 'Armure' T1 | 8 | 3 |
| 3 | `u_a_over_03` | Sur-couche atténuatrice T1 | 10 | 5 |
| 4 | `u_a_over_04` | Revêtement ablatif T1 | 12 | 7 |
| 5 | `u_a_over_05` | Protection contre l'énergie T1 | 14 | 9 |
| 6 | `u_a_over_06` | Protection antibalistique T1 | 16 | 11 |
| 7 | `u_a_over_07` | Plaques liées T1 | 18 | 13 |
| 8 | `u_a_over_08` | Plaques lourdes liées T1 | 20 | 15 |
| 9 | `u_a_over_09` | Protection contre la chaleur T2 | 22 | 17 |
| 10 | `u_a_over_10` | Revêtement 'Armure' T2 | 24 | 19 |
| 11 | `u_a_over_11` | Sur-couche atténuatrice T2 | 26 | 21 |
| 12 | `u_a_over_12` | Revêtement ablatif T2 | 28 | 23 |
| 13 | `u_a_over_13` | Protection contre l'énergie T2 | 30 | 25 |
| 14 | `u_a_over_14` | Protection antibalistique T2 | 30 | 27 |
| 15 | `u_a_over_15` | Plaques liées T2 | 30 | 29 |
| 16 | `u_a_over_16` | Plaques lourdes liées T2 | 30 | 30 |
| 17 | `u_a_over_17` | Protection contre la chaleur T3 | 30 | 30 |
| 18 | `u_a_over_18` | Revêtement 'Armure' T3 | 30 | 30 |
| 19 | `u_a_over_19` | Sur-couche atténuatrice T3 | 30 | 30 |
| 20 | `u_a_over_20` | Revêtement ablatif T3 | 30 | 30 |
| 21 | `u_a_over_21` | Protection contre l'énergie T3 | 30 | 30 |
| 22 | `u_a_over_22` | Protection antibalistique T3 | 30 | 30 |
| 23 | `u_a_over_23` | Plaques liées T3 | 30 | 30 |
| 24 | `u_a_over_24` | Plaques lourdes liées T3 | 30 | 30 |
| 25 | `u_a_over_25` | Protection contre la chaleur T4 | 30 | 30 |
| 26 | `u_a_over_26` | Revêtement 'Armure' T4 | 30 | 30 |
| 27 | `u_a_over_27` | Sur-couche atténuatrice T4 | 30 | 30 |
| 28 | `u_a_over_28` | Revêtement ablatif T4 | 30 | 30 |
| 29 | `u_a_over_29` | Protection contre l'énergie T4 | 30 | 30 |
| 30 | `u_a_over_30` | Plaques liées T4 | 30 | 30 |

### Amélioration — Pack d'énergie (distance) (15)

| Palier | ResRef | Nom | Niv. PJ mini (normal) | Niv. PJ mini (rare) |
| :--: | :-- | :-- | :--: | :--: |
| 1 | `u_r_powe_01` | Chargeur d'ions T1 | 6 | 1 |
| 2 | `u_r_powe_02` | Générateur d'impulsions T1 | 8 | 3 |
| 3 | `u_r_powe_03` | Cellule d'énergie de base au rylith | 10 | 5 |
| 4 | `u_r_powe_04` | Chargeur d'ions T2 | 12 | 7 |
| 5 | `u_r_powe_05` | Générateur d'impulsions T2 | 14 | 9 |
| 6 | `u_r_powe_06` | Cellule d'énergie au rylith classique | 16 | 11 |
| 7 | `u_r_powe_07` | Chargeur d'ions T3 | 18 | 13 |
| 8 | `u_r_powe_08` | Générateur d'impulsions T3 | 20 | 15 |
| 9 | `u_r_powe_09` | Cellule d'énergie alcaline au rylith | 22 | 17 |
| 10 | `u_r_powe_10` | Chargeur d'ions T4 | 24 | 19 |
| 11 | `u_r_powe_11` | Générateur d'impulsions T4 | 26 | 21 |
| 12 | `u_r_powe_12` | Cellule d'énergie supérieure au rylith | 28 | 23 |
| 13 | `u_r_powe_13` | Chargeur d'ions T5 | 30 | 25 |
| 14 | `u_r_powe_14` | Générateur d'impulsions T5 | 30 | 27 |
| 15 | `u_r_powe_15` | Cellule d'énergie pure au rylith | 30 | 29 |

### Amélioration — Poignée (mêlée) (15)

| Palier | ResRef | Nom | Niv. PJ mini (normal) | Niv. PJ mini (rare) |
| :--: | :-- | :-- | :--: | :--: |
| 1 | `u_m_grip_01` | Poignée en agrinium | 6 | 1 |
| 2 | `u_m_grip_02` | Poignée galbée | 8 | 3 |
| 3 | `u_m_grip_03` | Poignée zabrak | 10 | 5 |
| 4 | `u_m_grip_04` | Poignée à garde | 12 | 7 |
| 5 | `u_m_grip_05` | Poignée nagai | 14 | 9 |
| 6 | `u_m_grip_06` | Poignée en agrinium améliorée | 16 | 11 |
| 7 | `u_m_grip_07` | Poignée galbée améliorée | 18 | 13 |
| 8 | `u_m_grip_08` | Poignée zabrak améliorée | 20 | 15 |
| 9 | `u_m_grip_09` | Poignée à garde améliorée | 22 | 17 |
| 10 | `u_m_grip_10` | Poignée nagai améliorée | 24 | 19 |
| 11 | `u_m_grip_11` | Poignée supérieure en agrinium | 26 | 21 |
| 12 | `u_m_grip_12` | Poignée galbée supérieure | 28 | 23 |
| 13 | `u_m_grip_13` | Poignée zabrak supérieure | 30 | 25 |
| 14 | `u_m_grip_14` | Poignée à garde supérieure | 30 | 27 |
| 15 | `u_m_grip_15` | Poignée nagai supérieure | 30 | 29 |

### Amélioration — Underlay (armure) (30)

| Palier | ResRef | Nom | Niv. PJ mini (normal) | Niv. PJ mini (rare) |
| :--: | :-- | :-- | :--: | :--: |
| 1 | `u_a_unde_01` | Sous-couche anti-environnement T1 | 6 | 1 |
| 2 | `u_a_unde_02` | Sous-couche bio-restaurative T1 | 8 | 3 |
| 3 | `u_a_unde_03` | Sous-couche fortificatrice T1 | 10 | 5 |
| 4 | `u_a_unde_04` | Sous-couche renforçante T1 | 12 | 7 |
| 5 | `u_a_unde_05` | Sous-couche flexible T1 | 14 | 9 |
| 6 | `u_a_unde_06` | Sous-couche en duracier T1 | 16 | 11 |
| 7 | `u_a_unde_07` | Sous-couche anti-environnement T2 | 18 | 13 |
| 8 | `u_a_unde_08` | Sous-couche bio-restaurative T2 | 20 | 15 |
| 9 | `u_a_unde_09` | Sous-couche fortificatrice T2 | 22 | 17 |
| 10 | `u_a_unde_10` | Sous-couche renforçante T2 | 24 | 19 |
| 11 | `u_a_unde_11` | Sous-couche flexible T2 | 26 | 21 |
| 12 | `u_a_unde_12` | Sous-couche en duracier T2 | 28 | 23 |
| 13 | `u_a_unde_13` | Sous-couche anti-environnement T3 | 30 | 25 |
| 14 | `u_a_unde_14` | Sous-couche bio-restaurative T3 | 30 | 27 |
| 15 | `u_a_unde_15` | Sous-couche fortificatrice T3 | 30 | 29 |
| 16 | `u_a_unde_16` | Sous-couche renforçante T3 | 30 | 30 |
| 17 | `u_a_unde_17` | Sous-couche flexible T3 | 30 | 30 |
| 18 | `u_a_unde_18` | Sous-couche en duracier T3 | 30 | 30 |
| 19 | `u_a_unde_19` | Sous-couche anti-environnement T4 | 30 | 30 |
| 20 | `u_a_unde_20` | Sous-couche bio-restaurative T4 | 30 | 30 |
| 21 | `u_a_unde_21` | Sous-couche fortificatrice T4 | 30 | 30 |
| 22 | `u_a_unde_22` | Sous-couche renforçante T4 | 30 | 30 |
| 23 | `u_a_unde_23` | Sous-couche flexible T4 | 30 | 30 |
| 24 | `u_a_unde_24` | Sous-couche en duracier T4 | 30 | 30 |
| 25 | `u_a_unde_25` | Sous-couche anti-environnement T5 | 30 | 30 |
| 26 | `u_a_unde_26` | Sous-couche bio-restaurative T5 | 30 | 30 |
| 27 | `u_a_unde_27` | Sous-couche fortificatrice T5 | 30 | 30 |
| 28 | `u_a_unde_28` | Sous-couche renforçante T5 | 30 | 30 |
| 29 | `u_a_unde_29` | Sous-couche flexible T5 | 30 | 30 |
| 30 | `u_a_unde_30` | Sous-couche en duracier T5 | 30 | 30 |

### Amélioration — Émetteur (sabre) (13)

| Palier | ResRef | Nom | Niv. PJ mini (normal) | Niv. PJ mini (rare) |
| :--: | :-- | :-- | :--: | :--: |
| 1 | `u_l_emit_01` | Émetteur de parade | 12 | 7 |
| 2 | `u_l_emit_02` | Émetteur de désordre nerveux | 14 | 9 |
| 3 | `u_l_emit_03` | Émetteur au phobium brut | 16 | 11 |
| 4 | `u_l_emit_04` | Émetteur de parade | 18 | 13 |
| 5 | `u_l_emit_05` | Émetteur de parade amélioré | 20 | 15 |
| 6 | `u_l_emit_06` | Émetteur de désordre nerveux amélioré | 22 | 17 |
| 7 | `u_l_emit_07` | Émetteur au phobium synthétisé | 24 | 19 |
| 8 | `u_l_emit_08` | Émetteur de parade amélioré | 26 | 21 |
| 9 | `u_l_emit_09` | Émetteur de parade haut de gamme | 28 | 23 |
| 10 | `u_l_emit_10` | Émetteur de désordre nerveux hightech | 30 | 25 |
| 11 | `u_l_emit_11` | Émetteur à alliage au phobium | 30 | 27 |
| 12 | `u_l_emit_12` | Émetteur de parade haut de gamme | 30 | 29 |
| 13 | `u_l_emit_13` | Émetteur au phobium raffiné | 30 | 30 |

### Arme de mêlée — Mêlée (30)

| Palier | ResRef | Nom | Niv. PJ mini (normal) | Niv. PJ mini (rare) |
| :--: | :-- | :-- | :--: | :--: |
| 1 | `w_melee_01` | Epée courte | 5 | 1 |
| 2 | `w_melee_02` | Epée longue | 6 | 1 |
| 3 | `w_melee_03` | Matraque à énergie | 7 | 2 |
| 4 | `w_melee_04` | Bâton | 8 | 3 |
| 5 | `w_melee_05` | Vibro-lame | 9 | 4 |
| 6 | `w_melee_06` | Vibro-épée | 10 | 5 |
| 7 | `w_melee_07` | Double-lame | 11 | 6 |
| 8 | `w_melee_08` | Négociateur de l'Echange | 12 | 7 |
| 9 | `w_melee_09` | Hache de guerre gamorréenne | 13 | 8 |
| 10 | `w_melee_10` | Vibro-lame zabrak | 14 | 9 |
| 11 | `w_melee_11` | Epée rodienne | 15 | 10 |
| 12 | `w_melee_12` | Epée de guerre Sith | 16 | 11 |
| 13 | `w_melee_13` | Epée trandoshan | 17 | 12 |
| 14 | `w_melee_14` | Pique de Force | 18 | 13 |
| 15 | `w_melee_15` | Vibro-double-lame | 19 | 14 |
| 16 | `w_melee_16` | Tranchoir gamorréen | 20 | 15 |
| 17 | `w_melee_17` | Epée de mort rodienne | 21 | 16 |
| 18 | `w_melee_18` | Silencieux gand | 22 | 17 |
| 19 | `w_melee_19` | Epée de Ryyk | 23 | 18 |
| 20 | `w_melee_20` | Double-lame trandoshan | 24 | 19 |
| 21 | `w_melee_21` | Vibro-épée Echani | 25 | 20 |
| 22 | `w_melee_22` | Epée à saccades Sith | 26 | 21 |
| 23 | `w_melee_23` | Bâton électrique gand | 27 | 22 |
| 24 | `w_melee_24` | Shyarn | 28 | 23 |
| 25 | `w_melee_25` | Arg'garok | 29 | 24 |
| 26 | `w_melee_26` | Bâton électrique géonosien | 30 | 25 |
| 27 | `w_melee_27` | Epée de Tehk'la | 30 | 26 |
| 28 | `w_melee_28` | Zhaboka | 30 | 27 |
| 29 | `w_melee_29` | Émetteur de décharges gand | 30 | 28 |
| 30 | `w_melee_30` | Epée de guerre de Freyyr | 30 | 29 |

### Arme à distance — Fusil blaster (30)

| Palier | ResRef | Nom | Niv. PJ mini (normal) | Niv. PJ mini (rare) |
| :--: | :-- | :-- | :--: | :--: |
| 1 | `w_brifle_01` | Fusil blaster automatique | 5 | 1 |
| 2 | `w_brifle_02` | Fusil automatique à ions | 6 | 1 |
| 3 | `w_brifle_03` | Fusil automatique sonique | 7 | 2 |
| 4 | `w_brifle_04` | Fusil blaster | 8 | 3 |
| 5 | `w_brifle_05` | Arbalète laser | 9 | 4 |
| 6 | `w_brifle_06` | Blaster auto. à répétition | 10 | 5 |
| 7 | `w_brifle_07` | Fusil à ions | 11 | 6 |
| 8 | `w_brifle_08` | Fusil automatique désintégrateur | 12 | 7 |
| 9 | `w_brifle_09` | Fusil sonique | 13 | 8 |
| 10 | `w_brifle_10` | Fusil blaster à répétition | 14 | 9 |
| 11 | `w_brifle_11` | Arbalète laser de guerre | 15 | 10 |
| 12 | `w_brifle_12` | Fusil blaster arkanien | 16 | 11 |
| 13 | `w_brifle_13` | Fusil désintégrateur | 17 | 12 |
| 14 | `w_brifle_14` | Etourdisseur argazdan | 18 | 13 |
| 15 | `w_brifle_15` | Désintégrateur de droïdes bothan | 19 | 14 |
| 16 | `w_brifle_16` | Blaster de combat | 20 | 15 |
| 17 | `w_brifle_17` | Fusil lourd à répétition | 21 | 16 |
| 18 | `w_brifle_18` | Projecteur de plasma | 22 | 17 |
| 19 | `w_brifle_19` | Fusil d'assaut mand. | 23 | 18 |
| 20 | `w_brifle_20` | Désintégrateur de droïdes verpine | 24 | 19 |
| 21 | `w_brifle_21` | Arbalète laser de cérémonie | 25 | 20 |
| 22 | `w_brifle_22` | Fusil à répétition lourd | 26 | 21 |
| 23 | `w_brifle_23` | Charric | 27 | 22 |
| 24 | `w_brifle_24` | Fusil blaster automatique zabrak | 28 | 23 |
| 25 | `w_brifle_25` | Fusil d'esclavagiste | 29 | 24 |
| 26 | `w_brifle_26` | Fusil à répétition d'Ondéron | 30 | 25 |
| 27 | `w_brifle_27` | Désintégrateur sonique | 30 | 26 |
| 28 | `w_brifle_28` | Fusil à répétition lourd mand. | 30 | 27 |
| 29 | `w_brifle_29` | Désintégrateur de droïdes verpine | 30 | 28 |
| 30 | `w_brifle_30` | Fusil au zersium | 30 | 29 |

### Arme à distance — Pistolet blaster (30)

| Palier | ResRef | Nom | Niv. PJ mini (normal) | Niv. PJ mini (rare) |
| :--: | :-- | :-- | :--: | :--: |
| 1 | `w_blaste_01` | Pistolet blaster | 5 | 1 |
| 2 | `w_blaste_02` | Blaster à ions | 6 | 1 |
| 3 | `w_blaste_03` | Pistolet de survie | 7 | 2 |
| 4 | `w_blaste_04` | Pistolet sonique | 8 | 3 |
| 5 | `w_blaste_05` | Pistolet désintégrateur | 9 | 4 |
| 6 | `w_blaste_06` | Blaster lourd | 10 | 5 |
| 7 | `w_blaste_07` | Pistolet d'éclaireur | 11 | 6 |
| 8 | `w_blaste_08` | Blaster auditif Systech | 12 | 7 |
| 9 | `w_blaste_09` | Blaster de la République | 13 | 8 |
| 10 | `w_blaste_10` | Oxydroïde Aratech | 14 | 9 |
| 11 | `w_blaste_11` | Pistolet lourd arkanien | 15 | 10 |
| 12 | `w_blaste_12` | Blaster mand. | 16 | 11 |
| 13 | `w_blaste_13` | Blaster parasitant Systech | 17 | 12 |
| 14 | `w_blaste_14` | Blaster sonique arkanien | 18 | 13 |
| 15 | `w_blaste_15` | Désintégrateur Sith | 19 | 14 |
| 16 | `w_blaste_16` | Blaster lourd mand. | 20 | 15 |
| 17 | `w_blaste_17` | Blaster sonique lourd | 21 | 16 |
| 18 | `w_blaste_18` | Blaster de vigile | 22 | 17 |
| 19 | `w_blaste_19` | Pistolet blaster zabrak | 23 | 18 |
| 20 | `w_blaste_20` | Déchiqueteur mand. | 24 | 19 |
| 21 | `w_blaste_21` | Émetteur d'ions Aratech | 25 | 20 |
| 22 | `w_blaste_22` | Blaster d'Onasi | 26 | 21 |
| 23 | `w_blaste_23` | Blaster sonique dashade | 27 | 22 |
| 24 | `w_blaste_24` | Blaster lourd zabrak | 28 | 23 |
| 25 | `w_blaste_25` | Blaster électrique Systech | 29 | 24 |
| 26 | `w_blaste_26` | Blaster à micro-impulsions | 30 | 25 |
| 27 | `w_blaste_27` | Blaster de protecteur d'élite | 30 | 26 |
| 28 | `w_blaste_28` | Désintégrateur mand. | 30 | 27 |
| 29 | `w_blaste_29` | Désintégrateur sonique dashade | 30 | 28 |
| 30 | `w_blaste_30` | Blaster de Freedon Nadd | 30 | 29 |

### Armure — Intermédiaire (15)

| Palier | ResRef | Nom | Niv. PJ mini (normal) | Niv. PJ mini (rare) |
| :--: | :-- | :-- | :--: | :--: |
| 1 | `a_medium_01` | Combinaison militaire | 6 | 1 |
| 2 | `a_medium_02` | Armure de combat légère | 8 | 3 |
| 3 | `a_medium_03` | Armure de combat Echani | 10 | 5 |
| 4 | `a_medium_04` | Armure de guerre de Cinnagar | 12 | 7 |
| 5 | `a_medium_05` | Combinaison de combat Sith | 14 | 9 |
| 6 | `a_medium_06` | Armure de combat légère en bronzium | 16 | 11 |
| 7 | `a_medium_07` | Maille en fibre verpine | 18 | 13 |
| 8 | `a_medium_08` | Armure lourde krath | 20 | 15 |
| 9 | `a_medium_09` | Armure de combat légère à servomoteurs | 22 | 17 |
| 10 | `a_medium_10` | Armure de guerre sacrée de Krath | 24 | 19 |
| 11 | `a_medium_11` | Armure de guerre légère d'Exar Kun | 26 | 21 |
| 12 | `a_medium_12` | Armure de guerre lourde de Cinnagar | 28 | 23 |
| 13 | `a_medium_13` | Ultramaille de fibre verpine | 30 | 25 |
| 14 | `a_medium_14` | Armure de mailles électriques | 30 | 27 |
| 15 | `a_medium_15` | Armure de combat de Jamoh Hogra | 30 | 29 |

### Armure — Lourde (15)

| Palier | ResRef | Nom | Niv. PJ mini (normal) | Niv. PJ mini (rare) |
| :--: | :-- | :-- | :--: | :--: |
| 1 | `a_heavy_01` | Armure de combat | 6 | 1 |
| 2 | `a_heavy_02` | Armure de combat lourde | 8 | 3 |
| 3 | `a_heavy_03` | Armure lourde Echani | 10 | 5 |
| 4 | `a_heavy_04` | Armure lourde en duracier | 12 | 7 |
| 5 | `a_heavy_05` | Armure de combat à servomoteurs | 14 | 9 |
| 6 | `a_heavy_06` | Armure lourde flexible | 16 | 11 |
| 7 | `a_heavy_07` | Armure de combat mand. | 18 | 13 |
| 8 | `a_heavy_08` | Armure lourde mand. | 20 | 15 |
| 9 | `a_heavy_09` | Maille verpine en alliage zal | 22 | 17 |
| 10 | `a_heavy_10` | Armure d'assaut mand. | 24 | 19 |
| 11 | `a_heavy_11` | Combinaison de puissance de Corellia | 26 | 21 |
| 12 | `a_heavy_12` | M'uhk'gfa | 28 | 23 |
| 13 | `a_heavy_13` | Armure-exosquelette Iotran | 30 | 25 |
| 14 | `a_heavy_14` | Armure de Félénar | 30 | 27 |
| 15 | `a_heavy_15` | Armure matrice | 30 | 29 |

### Armure — Légère (15)

| Palier | ResRef | Nom | Niv. PJ mini (normal) | Niv. PJ mini (rare) |
| :--: | :-- | :-- | :--: | :--: |
| 1 | `a_light_01` | Combinaison de combat légère | 6 | 1 |
| 2 | `a_light_02` | Combinaison de combat | 8 | 3 |
| 3 | `a_light_03` | Combinaison de combat lourde | 10 | 5 |
| 4 | `a_light_04` | Combinaison de combat mand. | 12 | 7 |
| 5 | `a_light_05` | Combinaison de combat zabrak | 14 | 9 |
| 6 | `a_light_06` | Combinaison de alliage Bonadan | 16 | 11 |
| 7 | `a_light_07` | Armure légère Echani | 18 | 13 |
| 8 | `a_light_08` | Armure de cérémonie massassi | 20 | 15 |
| 9 | `a_light_09` | Combinaison lourde mand. | 22 | 17 |
| 10 | `a_light_10` | Armure de combat zabrak | 24 | 19 |
| 11 | `a_light_11` | Combinaison anti-environnement ubèse | 26 | 21 |
| 12 | `a_light_12` | Combinaison-bouclier Echani | 28 | 23 |
| 13 | `a_light_13` | Armure de fibre renforcée | 30 | 25 |
| 14 | `a_light_14` | Armure de guerre zabrak | 30 | 27 |
| 15 | `a_light_15` | Combinaison de mailles d'Ulic Qel Droma | 30 | 29 |

### Armure — Robe Jedi (30)

| Palier | ResRef | Nom | Niv. PJ mini (normal) | Niv. PJ mini (rare) |
| :--: | :-- | :-- | :--: | :--: |
| 1 | `a_robe_01` | Vêtements | 6 | 1 |
| 2 | `a_robe_02` | Bure de padawan | 8 | 3 |
| 3 | `a_robe_03` | Bure de padawan Obscur | 10 | 5 |
| 4 | `a_robe_04` | Bure de novice Baran Do | 12 | 7 |
| 5 | `a_robe_05` | Bure d'apprenti Mutaki | 14 | 9 |
| 6 | `a_robe_06` | Armure d'initié Zeison Sha | 16 | 11 |
| 7 | `a_robe_07` | Armure de néophyte Jal Shey | 18 | 13 |
| 8 | `a_robe_08` | Bure de Jedi | 20 | 15 |
| 9 | `a_robe_09` | Bure de Jedi Obscur | 22 | 17 |
| 10 | `a_robe_10` | Bure de Norris | 24 | 19 |
| 11 | `a_robe_11` | Armure de conseiller Jal Shey | 26 | 21 |
| 12 | `a_robe_12` | Bure de Jedi gris | 28 | 23 |
| 13 | `a_robe_13` | Bure de chevalier Jedi | 30 | 25 |
| 14 | `a_robe_14` | Bure de chevalier Jedi Obscur | 30 | 27 |
| 15 | `a_robe_15` | Bure d'adepte Mutaki | 30 | 29 |
| 16 | `a_robe_16` | Armure de guerrier Zeison Sha | 30 | 30 |
| 17 | `a_robe_17` | Bure de maître Jedi | 30 | 30 |
| 18 | `a_robe_18` | Bure de maître Jedi Obscur | 30 | 30 |
| 19 | `a_robe_19` | Bure de sage Baran Do | 30 | 30 |
| 20 | `a_robe_20` | Armure de mentor Jal Shey | 30 | 30 |
| 21 | `a_robe_21` | Bure de gardien d'Ossus | 30 | 30 |
| 22 | `a_robe_22` | Foulard de Natth | 30 | 30 |
| 23 | `a_robe_23` | Bure d'Arca Jeth | 30 | 30 |
| 24 | `a_robe_24` | Bure d'Aleema Keto | 30 | 30 |
| 25 | `a_robe_25` | Bure de Sylvar | 30 | 30 |
| 26 | `a_robe_26` | Armure de Dark Malak | 30 | 30 |
| 27 | `a_robe_27` | Bure de Jolee | 30 | 30 |
| 28 | `a_robe_28` | Bure de Thon | 30 | 30 |
| 29 | `a_robe_29` | Bure de Crado | 30 | 30 |
| 30 | `a_robe_30` | Bure de Nomi | 30 | 30 |

### Droïde — Arme spéciale (15)

| Palier | ResRef | Nom | Niv. PJ mini (normal) | Niv. PJ mini (rare) |
| :--: | :-- | :-- | :--: | :--: |
| 1 | `d_device_01` | Pacificateur neural pour droïde | 6 | 1 |
| 2 | `d_device_02` | Répulseur pour droïde | 8 | 3 |
| 3 | `d_device_03` | Lance-flammes pour droïde | 10 | 5 |
| 4 | `d_device_04` | Émetteur de toxines pour droïde | 12 | 7 |
| 5 | `d_device_05` | Brouilleur neural pour droïde | 14 | 9 |
| 6 | `d_device_06` | Projecteur à ions | 16 | 11 |
| 7 | `d_device_07` | Canon à fusion pour droïde | 18 | 13 |
| 8 | `d_device_08` | Projecteur de carbonite pour droïde | 20 | 15 |
| 9 | `d_device_09` | Lance-plasma pour droïde | 22 | 17 |
| 10 | `d_device_10` | Pulvérisateur biotoxique d'assaut | 24 | 19 |
| 11 | `d_device_11` | Émetteur de carbonite pour droïde | 26 | 21 |
| 12 | `d_device_12` | Blaster à ions T1 | 28 | 23 |
| 13 | `d_device_13` | Blaster à ions T2 | 30 | 25 |
| 14 | `d_device_14` | Blaster à ions T3 | 30 | 27 |
| 15 | `d_device_15` | Émetteur multi-spectral pour droïde | 30 | 29 |

### Droïde — Blindage (15)

| Palier | ResRef | Nom | Niv. PJ mini (normal) | Niv. PJ mini (rare) |
| :--: | :-- | :-- | :--: | :--: |
| 1 | `d_armor_01` | Armure anti-impact T1 | 6 | 1 |
| 2 | `d_armor_02` | Revêtement modulaire T1 | 8 | 3 |
| 3 | `d_armor_03` | Armure anti-impact T2 | 10 | 5 |
| 4 | `d_armor_04` | Revêtement en desh pour droïde | 12 | 7 |
| 5 | `d_armor_05` | Armure anti-impact T3 | 14 | 9 |
| 6 | `d_armor_06` | Revêtement modulaire T2 | 16 | 11 |
| 7 | `d_armor_07` | Revêtement modulaire T3 | 18 | 13 |
| 8 | `d_armor_08` | Armure pour droïde en agrinium | 20 | 15 |
| 9 | `d_armor_09` | Placage en duracier T1 | 22 | 17 |
| 10 | `d_armor_10` | Armure pour droïde en quadranium | 24 | 19 |
| 11 | `d_armor_11` | Placage en duracier T2 | 26 | 21 |
| 12 | `d_armor_12` | Revêtement pour droïde en diatium | 28 | 23 |
| 13 | `d_armor_13` | Armure énergétique T1 | 30 | 25 |
| 14 | `d_armor_14` | Armure énergétique T2 | 30 | 27 |
| 15 | `d_armor_15` | Armure énergétique T3 | 30 | 29 |

### Droïde — Bouclier (6)

| Palier | ResRef | Nom | Niv. PJ mini (normal) | Niv. PJ mini (rare) |
| :--: | :-- | :-- | :--: | :--: |
| 1 | `d_shield_01` | Déflecteur T1 | 7 | 2 |
| 2 | `d_shield_02` | Déflecteur T2 | 10 | 5 |
| 3 | `d_shield_03` | Barrière de défense pour droïde | 13 | 8 |
| 4 | `d_shield_04` | Récupérateur d'énergie pour droïde | 16 | 11 |
| 5 | `d_shield_05` | Déflecteur T3 | 19 | 14 |
| 6 | `d_shield_06` | Quadrillage d'unification | 22 | 17 |

### Droïde — Interface (15)

| Palier | ResRef | Nom | Niv. PJ mini (normal) | Niv. PJ mini (rare) |
| :--: | :-- | :-- | :--: | :--: |
| 1 | `d_interface_01` | Interface optimisée pour droïde | 6 | 1 |
| 2 | `d_interface_02` | Sous-programme de stabilisation | 8 | 3 |
| 3 | `d_interface_03` | Interface machine pour droïde | 10 | 5 |
| 4 | `d_interface_04` | Contournement de verrouillage | 12 | 7 |
| 5 | `d_interface_05` | Guides paraboliques pour droïde | 14 | 9 |
| 6 | `d_interface_06` | Amplificateur de motivateur | 16 | 11 |
| 7 | `d_interface_07` | Amélioration de durabilité | 18 | 13 |
| 8 | `d_interface_08` | Amélioration d'agilité pour droïde | 20 | 15 |
| 9 | `d_interface_09` | Amélioration de sagesse pour droïde | 22 | 17 |
| 10 | `d_interface_10` | Interface d'échange pour droïde | 24 | 19 |
| 11 | `d_interface_11` | Interface à distance pour droïde | 26 | 21 |
| 12 | `d_interface_12` | Bibliothèque anatomique | 28 | 23 |
| 13 | `d_interface_13` | Amélioration pour droïde ferrailleur | 30 | 25 |
| 14 | `d_interface_14` | Dénicheur de source pour droïde | 30 | 27 |
| 15 | `d_interface_15` | Amélioration des systèmes pour droïde | 30 | 29 |

### Implant — Niveau 1 (10)

| Palier | ResRef | Nom | Niv. PJ mini (normal) | Niv. PJ mini (rare) |
| :--: | :-- | :-- | :--: | :--: |
| 1 | `e_imp1_01` | Pack de réflexes | 7 | 2 |
| 2 | `e_imp1_02` | Pack de phéromones | 10 | 5 |
| 3 | `e_imp1_03` | Pack cardio-vasculaire | 13 | 8 |
| 4 | `e_imp1_04` | Pack de force | 16 | 11 |
| 5 | `e_imp1_05` | Pack réaction | 19 | 14 |
| 6 | `e_imp1_06` | Pack de condition physique | 22 | 17 |
| 7 | `e_imp1_07` | Pack de compétences | 25 | 20 |
| 8 | `e_imp1_08` | Pack de santé | 28 | 23 |
| 9 | `e_imp1_09` | Pack d'augmentation phys. | 30 | 26 |
| 10 | `e_imp1_10` | Pack d'augmentation mentale | 30 | 29 |

### Implant — Niveau 2 (10)

| Palier | ResRef | Nom | Niv. PJ mini (normal) | Niv. PJ mini (rare) |
| :--: | :-- | :-- | :--: | :--: |
| 1 | `e_imp2_01` | Implant de combat rétinien | 7 | 2 |
| 2 | `e_imp2_02` | Implant lornan | 10 | 5 |
| 3 | `e_imp2_03` | Implant biotech. | 13 | 8 |
| 4 | `e_imp2_04` | Implant de puissance | 16 | 11 |
| 5 | `e_imp2_05` | Implant de promptitude | 19 | 14 |
| 6 | `e_imp2_06` | Implant de perspicacité | 22 | 17 |
| 7 | `e_imp2_07` | Implant de compétences | 25 | 20 |
| 8 | `e_imp2_08` | Implant de durabilité | 28 | 23 |
| 9 | `e_imp2_09` | Implant d'augmentation phys. | 30 | 26 |
| 10 | `e_imp2_10` | Implant d'augmentation mentale | 30 | 29 |

### Implant — Niveau 3 (10)

| Palier | ResRef | Nom | Niv. PJ mini (normal) | Niv. PJ mini (rare) |
| :--: | :-- | :-- | :--: | :--: |
| 1 | `e_imp3_01` | Système de bio-antidote | 7 | 2 |
| 2 | `e_imp3_02` | Système de régulation nerveuse | 10 | 5 |
| 3 | `e_imp3_03` | Système de réaction | 13 | 8 |
| 4 | `e_imp3_04` | Système de combat amélioré | 16 | 11 |
| 5 | `e_imp3_05` | Système de force de Bavakar | 19 | 14 |
| 6 | `e_imp3_06` | Système de puissance cardiaque | 22 | 17 |
| 7 | `e_imp3_07` | Système de compétences | 25 | 20 |
| 8 | `e_imp3_08` | Système d'atténuation de sensations | 28 | 23 |
| 9 | `e_imp3_09` | Système d'augmentation phys. | 30 | 26 |
| 10 | `e_imp3_10` | Système d'augmentation mentale | 30 | 29 |

### Implant — Niveau 4 (10)

| Palier | ResRef | Nom | Niv. PJ mini (normal) | Niv. PJ mini (rare) |
| :--: | :-- | :-- | :--: | :--: |
| 1 | `e_imp4_01` | Pack-D de force | 7 | 2 |
| 2 | `e_imp4_02` | Pack-D d'immunité | 10 | 5 |
| 3 | `e_imp4_03` | Pack-D de perception | 13 | 8 |
| 4 | `e_imp4_04` | Pack-D d'augmentation | 16 | 11 |
| 5 | `e_imp4_05` | Pack-D d'immortalité | 19 | 14 |
| 6 | `e_imp4_06` | Pack-D de rapidité | 22 | 17 |
| 7 | `e_imp4_07` | Pack-D de compétences | 25 | 20 |
| 8 | `e_imp4_08` | Pack-D universel | 28 | 23 |
| 9 | `e_imp4_09` | Pack-D d'augmentation phys. | 30 | 26 |
| 10 | `e_imp4_10` | Pack-D d'augmentation mentale | 30 | 29 |

## 4. Consommables (bundles, `GetBundlePrefix`)

| Code | Objet | Règle |
| :--: | :-- | :-- |
| 911/961 | Crédits | quantité = Random(10×niv) + Random(50) + 20 (ou variante réduite) |
| 921/922 | Composants / Produits chimiques | quantité = Random(niv) + Random(niv) + 1 |
| 931 | Bouclier de bras `a_shield_0X` | palier = niv ÷ 4 + 1 (max 7) |
| 941/954 | Trousse de soins T1/T2/T3 | T1 < niv 9, T2 < niv 16, T3 ensuite |
| 942 | Kit de réparation droïde | même courbe que les trousses |
| 951–953 | Stims FOR/DEX/CON | version T1 < niv 12, T2 ensuite |
| 971–979 | Grenades | grenades supérieures remplacées par des frag si niveau insuffisant |
| 981–983 | Pièces / pointes prog. / pointes sécurité | quantité fixe |
| 991–995 | Fusées de Mira `w_rocket_0X` | uniquement si Mira recrutée ; palier = niv ÷ 3 (max 5) |