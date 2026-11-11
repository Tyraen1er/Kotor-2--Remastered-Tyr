# Annexes des Décisions — Justifications, Recherche & Notes d'Implémentation

> Compagnon de [`decisions_finales.md`](decisions_finales.md) (le contrat de game design).
> Tout ce qui **explique ou prépare** les décisions sans en faire partie y est rassemblé :
> recherche sur les systèmes papier, diagnostics, mécanismes moteur vérifiés, options techniques validées.

---

## 1. Armures — Recherche et Justifications (décisions §8)

### A. Comparaison des systèmes papier (pourquoi « RD native + arbres par type »)

| Système | Légère | Intermédiaire | Lourde | Levier de différenciation |
| :--- | :--- | :--- | :--- | :--- |
| **D&D 3.5** | CA `+1` à `+4`, DEX pleine, vitesse pleine, malus `0` à `-2` | CA `+4/+5`, DEX max `+3`, vitesse `×3/4`, malus `-4/-6` | CA `+6` à `+8`, DEX max `+0/+1`, vitesse `×3/4` (course `×3`), malus `-6/-8` | La **CA** remonte au détriment de la DEX, de la vitesse et des compétences ; 3 dons de *Proficiency* séparés |
| **D&D 5e** | DEX entière, aucun désavantage | DEX max `+2` ; don *Medium Armor Master* (DEX `+3`, plus de désavantage de Discrétion) | Don ***Heavy Armor Master* = `RD 3` physique non-magique** | **Dons de spécialisation dédiés par type d'armure** |
| **SW d20 RCR** *(système source de KotOR)* | **RD 2–3**, DEX max `+4/+5`, malus `-1/-2` | **RD 4–5**, DEX max `+3`, malus `-3/-4` | **RD 7–9**, DEX max `+1`, malus `-6/-8` | **L'armure donne de la RD, pas de la Défense** (la Défense vient des niveaux de classe) ; les sabres ignorent la RD des armures |
| **SW Saga (SWSE)** | Remplace le niveau dans la Défense Réflexe | Talents *Armored Defense* | *Improved Armored Defense*, *Juggernaut* (annule le malus de vitesse), *Armor Mastery* (`+1` DEX max) | **Talents d'Armure** (arbre *Armor Specialist* du Soldat) |
| **KotOR 2 Vanilla** | CA `4-5`, DEX max `+5/+4` | CA `6-7`, DEX max `+3/+2` | CA `8-9`, DEX max `+1/+0` | **Aucune identité** : blocage uniforme des pouvoirs (`forbiditemmask 0x3F`) → armures Tier F pour les Jedi |

**Conclusion design :** KotOR 2 a hérité de la CA de D&D 3.0 *sans* les dons de spécialisation de D&D 5e *ni* la RD du JdR SW. L'overhaul restaure les deux leviers.

### B. Diagnostic de *Condition physique* (consensus communauté)

Consensus Reddit/GameFAQs : *filler feat* typique — les vétérans préfèrent *Robustesse* (PV bruts utiles contre tout, y compris l'irrésistible) et couvrent les sauvegardes par équipement/immunités ; *Condition physique* n'est pris qu'en fin de build par les classes riches en dons.
**Mais sa valeur remonte dans notre overhaul :** DD des pouvoirs de boss renforcés (niveau effectif `0,75 × L`) et *Esquive Totale* qui rend chaque point de Réflexes directement rentable (0 dégât au lieu de la moitié). D'où le rang III révisé (§8.D) sans dupliquer *Robustesse* ni l'arbre lourde.

### C. Notes d'implémentation (§8)

- **RD native & arbres** : hook fin de round de [`k_ai_master.nss`](file:///C:/Users/emman/Desktop/dev/Kotor%202%20Mods/mods/00-test-feat/k_ai_master.nss) lisant `GetBaseItemType()` de l'armure équipée (lignes `baseitems.2da` 38–43), avec parcours anti-cumul d'effets (voir README §3.A).
- **Effets NWScript validés disponibles** : `EffectDamageReduction`, `EffectACIncrease`, `EffectSavingThrowIncrease`, `EffectImmunity` (`IMMUNITY_TYPE_KNOCKDOWN = 28`, `IMMUNITY_TYPE_STUN = 12`), `EffectSavingThrowIncrease(..., SAVING_THROW_TYPE_FORCE_POWER)` pour *Condition physique* III.
- **`forbiditemmask` (`spells.2da`) — mapping CONFIRMÉ (09/11/2026)** :
  `0x01` = Armor_Class_4 (ligne 38, légère) · `0x02` = AC5 (39) · `0x04` = AC6 (40, intermédiaire) · `0x08` = AC7 (41) · `0x10` = AC8 (42, lourde) · `0x20` = AC9 (43).
  Un pouvoir est bloqué si `(masque ET bits de l'armure portée) ≠ 0`. D'où : `0x3C` = interdit intermédiaire+lourde (léger + robe OK), `0x30` = interdit lourde seulement, etc.
- **Exceptions du masque (trouvées dans les données)** : les lignes spéciales **98** (*Combinaison ubese*) et **102** (*Zeison Sha*), ainsi que robes (35–37) et vêtements, échappent à **tous** les masques → ces armures resteront compatibles Force. **Décision associée à prendre** : les assumer comme armures « Force-friendly » rares (recommandé, lore-friendly) ou re-pointer leurs `.uti` vers les lignes standard.
- **Bonus découvert** : la colonne `requireitemmask` (inverse) fonctionne aussi — permet des pouvoirs **exclusifs aux armures** (ex. « Assaut blindé » réservé aux lourdes), piste de compensation pour le Juggernaut sans toucher à *Vitesse*.
- **`feat.2da`** : *Condition physique* = lignes 13/21/22 ; *Esquive* = ligne 125 (existe déjà en base). Dons automatiques possibles via colonnes `sol_granted`/`tec_granted` (option à valider pour Mandalore/HK-47 → *Juggernaut*).

### D. Budget détaillé par build (§6 et §8)

- **Gardien Juggernaut (cuirassé, 21 dons) :** 15 dons socle (3 style + 3 spé + 3 active + 3 *Robustesse* + 3 *Juggernaut*) + 6 dons bonus (implants, *Condition physique*, second style, etc.).
- **Gardien en robe (21 dons) :** 15 dons socle (3 style + 3 spé + 3 active + 3 *Robustesse* + 3 *Condition physique* révisé) + 6 dons bonus (*Esquive Totale*, *Finesse*, implants, second style).
- **Sentinelle (16 dons) :** 15 dons socle (3 style + 3 spé + 3 active + 3 *Robustesse* + 3 *Condition physique* ou *Seconde Peau*) + 1 don bonus (*Esquive Totale* ou *Finesse*).
- **Consulaire (13 dons) :** 10 dons socle (7 Métamagie + 3 *Robustesse*) + 3 dons bonus (*Condition physique*, posture *Duel 1M* pour +3 CA, ou *Arts Mutaki*).

---

## 2. Options techniques validées (à activer lors des chantiers en suspens)

- **Coût de PF dynamique à l'impact** (chantier Pouvoirs §2-1) : toolkit complet confirmé — `GetCurrentForcePoints`, `EffectDamageForcePoints`/`EffectHealForcePoints`, `GetSpellBaseForcePointCost`. Permet « payer au réel » (facturation selon dégâts infligés), *Tempête* à 1 PF/cible touchée, remboursements du *Drain*. Précédent vanilla : remboursement commenté de la forme Consulaire (lignes ~5950 de `k_inc_force.nss`). Contraintes : l'UI n'affiche que le coût 2DA (documenter dans `dialog.tlk`) ; garder un coût de base non nul pour l'IA.
- **`requireitemmask`** : pouvoirs exclusifs à un type d'armure (voir §1.C).

---

## 3. Contrat mathématique détaillé (décisions §9)

Détail des hypothèses du tableau de synthèse (attaques/round, dégâts bruts et nets après RD, précision, DPR sur sbires) :

| Phase & Boss | Archétype | Atq/round | Dégâts bruts/coup | Nets après RD | Précision vs boss | **DPR net boss** | DPR sbires (RD 0) | **Durée (rounds)** |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **EARLY (Niv. 8)**<br>120 PV, CA 20, RD 3 | Gatling / Lame Double<br>2 Pistolets / 2 Armes (+1 CA)<br>Fusil / 1M Duel (ignore RD 3) | 3<br>3<br>2 | 13<br>9,5<br>13 | 10<br>6,5<br>13 *(perce)* | 55 %<br>60 %<br>75 % | **16,5**<br>11,7<br>**19,5** | 25,0<br>19,0<br>21,0 | 7,2<br>6–10<br>6,1 |
| **MID (Niv. 16)**<br>280 PV, CA 29, RD 7 | Gatling / Lame Double<br>2 Pistolets / 2 Armes (+2 CA)<br>Fusil / 1M Duel (ignore RD 7) | 5 (Gat) / 4<br>4<br>3 | 20<br>16<br>23 | 13<br>9<br>23 *(perce)* | 60 %<br>70 %<br>85 % | **39,0**<br>25,2<br>**58,6** | 75,0<br>54,0<br>62,0 | 7,2<br>6–11<br>4,8 |
| **LATE (Niv. 26)**<br>650 PV, CA 44, RD 12 | Gatling (6 tirs) / Lame Double<br>2 Pistolets / 2 Armes (+3/+5 CA)<br>Fusil / 1M Duel (ignore RD 12) | 6 (Gat) / 5<br>5<br>3–4 | 28<br>25<br>40–48 | 16<br>13<br>40–48 *(perce)* | 60 %<br>70 %<br>85 % | **57,6**<br>45,5<br>**122–128** | 134,4<br>100,0<br>122–128 | 11,2<br>7–14<br>5,1 |

*Ambidextrie : l'Attaque Sournoise sur cible contrôlée double le DPR net. Hypothèses : établi plafonné `+2/+5/+10`, RD boss `3/7/12`, *Vitesse* encore comptée dans les simulations Late (à revisiter après le chantier « Vitesse », Partie 2-2).*

---

## 4. Références de données

- **Équipement, loot aléatoire, lieux sûrs** : [`datas_kotor/`](file:///C:/Users/emman/Desktop/dev/Kotor%202%20Mods/datas_kotor) (`equipement_*.md`, `loot_aleatoire.md`, `loot_lieux_surs.md`) — extrait par [`tools/extract_items.py`](file:///C:/Users/emman/Desktop/dev/Kotor%202%20Mods/tools/extract_items.py).
- **Dons, pouvoirs, ennemis, modèles mathématiques** : [`datas_kotor/dons_kotor2.md`](file:///C:/Users/emman/Desktop/dev/Kotor%202%20Mods/datas_kotor/dons_kotor2.md), [`pouvoirs_kotor2.md`](file:///C:/Users/emman/Desktop/dev/Kotor%202%20Mods/datas_kotor/pouvoirs_kotor2.md), [`ennemis_reference_kotor2.md`](file:///C:/Users/emman/Desktop/dev/Kotor%202%20Mods/datas_kotor/ennemis_reference_kotor2.md), [`modeles_mathematiques_equilibrage.md`](file:///C:/Users/emman/Desktop/dev/Kotor%202%20Mods/datas_kotor/modeles_mathematiques_equilibrage.md).
- **JdR Star Wars d20** : [`datas_jdr_SW/`](file:///C:/Users/emman/Desktop/dev/Kotor%202%20Mods/datas_jdr_SW) (dons, pouvoirs, armures/armes, comparatif).
- **Idées brutes** : [`idée mods.md`](file:///C:/Users/emman/Desktop/dev/Kotor%202%20Mods/id%C3%A9e%20mods.md).

---

## 5. Architecture Moteur — Ce qui est moddable vs hardcodé (Odyssey Engine)

Le moteur *Odyssey* (`swkotor2.exe`) sépare la logique en trois couches : l'exécutable C++ (fermé), les tables de données `.2da` (ouvertes) et les scripts NWScript `.nss`/`.ncs` (ouverts).

### ❌ A. Ce qui est codé en dur dans `swkotor2.exe` (Impossible à modifier directement)
1. **L'effet interne des dons passifs vanilla :**
   * On ne peut pas modifier ni *supprimer* le `+1 / +2 / +3` Attaque/Défense de **Duel**, le `-6/-10 ➔ -2/-2` de **Combat à deux armes**, le `+2` dégâts de **Spécialisation d'arme**, ou le `+1/+2/+3` PV/niv de **Robustesse**.
   * *Contournement :* On peut **ajouter** des effets supplémentaires par-dessus (ou compenser par un malus) via [`k_ai_master.nss`](file:///C:/Users/emman/Desktop/dev/Kotor%202%20Mods/mods/00-test-feat/k_ai_master.nss), ou remplacer le don dans l'arbre par un nouveau don custom.
2. **Les formules internes des 6 attaques actives (Déluge, Attaque en puissance, Critique, Tir rapide, Décharge, Sniper) :**
   * Le bonus `+3 / +7 / +12` dégâts d'*Attaque en puissance* / *Décharge d'énergie*, l'attaque supplémentaire de *Déluge* / *Tir rapide* et le multiplicateur de *Science du critique* sont codés dans l'exécutable.
3. **Le calcul du multiplicateur de Force natif par configuration :**
   * Contrairement à KotOR 1, KotOR 2 applique déjà nativement `1.5× FOR` à une arme simple tenue à une main (main gauche vide) ainsi qu'à la frappe principale des armes à double lame (`0.5× FOR` en secondaire). L'ambidextrie (2 armes séparées) applique `1.0× FOR` (droite) et `0.5× FOR` (gauche).
   * Tout bonus additionnel (ex: passer la Hache Lourde 2M à `2.0× FOR` ou le Duel à `2.0×/2.5×`) est injecté via script dans `k_ai_master.nss`.
4. **Le ciblage des attaques multiples dans un même round :**
   * Si la 1re attaque du round tue la cible, les attaques restantes du round sont perdues (sauf *Enchaînement / Cleave* scripté manuellement sur l'événement `OnDamage`).

---

### ✅ B. Ce qu'on PEUT modder directement dans les tables `.2da` (Sans script)
1. **Tous les prérequis des Dons ([`_reference/2da/feat.csv`](file:///C:/Users/emman/Desktop/dev/Kotor%202%20Mods/_reference/2da/feat.csv)) :**
   * Colonnes `minstr`, `mindex`, `minint`, `minwis`, `mincha`, `minlevel`, `prereqfeat1`, `prereqfeat2`.
2. **L'accès aux Dons par classe (`_list` et `_granted` dans `feat.2da`) et le rythme de gain (`featgain.2da`) :**
   * Permet de donner accès aux dons *Supérieurs* aux autres classes, ou d'offrir certains dons gratuitement à des paliers précis.
3. **Toutes les statistiques de base des Armes et Armures ([`_reference/2da/baseitems.csv`](file:///C:/Users/emman/Desktop/dev/Kotor%202%20Mods/_reference/2da/baseitems.csv)) :**
   * Dés de dégâts (`numdice`, `dietoroll`), plage critique (`critthreat`), multiplicateur critique (`crithitmult`), Défense de base des armures (`ac_enchant`) et plafond de Dextérité (`dexbonus`).
4. **Les coûts en PF et restrictions d'armure des Pouvoirs ([`_reference/2da/spells.csv`](file:///C:/Users/emman/Desktop/dev/Kotor%202%20Mods/_reference/2da/spells.csv)) :**
   * Colonne `forbiditemmask` : permet d'autoriser certains pouvoirs même sous armure.
5. **Le scaling des ennemis (`autobalance.2da`) et les recettes d'artisanat (`itemcreate.2da` + fichiers `.uti`).**

---

### ⚡ C. Ce qu'on PEUT modder et créer par Script (`.nss` ➔ `.ncs`)
1. **Tous les Pouvoirs de la Force ([`_reference/scripts/k_inc_force.nss`](file:///C:/Users/emman/Desktop/dev/Kotor%202%20Mods/_reference/scripts/k_inc_force.nss)) :**
   * Contrôle total à 100 % sur les formules de dégâts, les plafonds de dés (ex: plafonner *Tempête de Force*), le nombre d'attaques bonus (*Rapidité*, *Fureur*), les durées (`Sp_CalcDuration`) et les DD de sauvegarde.
2. **Effets Passifs Dynamiques via le Hook `1003` (Fin de Round) de [`k_ai_master.nss`](file:///C:/Users/emman/Desktop/dev/Kotor%202%20Mods/mods/00-test-feat/k_ai_master.nss) :**
   * Permet de lire les dons du personnage (`GetHasFeat`), ses caractéristiques (`GetAbilityModifier`), son arme équipée (`GetBaseItemType`) et son armure, puis d'appliquer des bonus/malus de dégâts, d'attaque, de Défense, de Réduction de Dégâts ou d'**attaques supplémentaires par round (`EffectModifyAttacks`)**.
3. **Effets *On-Hit* via le Hook `1006` (`OnDamage`) de [`k_ai_master.nss`](file:///C:/Users/emman/Desktop/dev/Kotor%202%20Mods/mods/00-test-feat/k_ai_master.nss) :**
   * Se déclenche à chaque fois qu'une créature subit des dégâts : étourdissement à mains nues, brise-armure, drain, procs de Force sur critique.

---

## 6. Diagnostic des Archétypes Vanilla (Niv. 28–30) — Budgets et Déséquilibres

Analyse comparative de ce que le jeu vanilla offre face aux besoins réels d'un build :

### A. Synthèse des budgets vanilla (Niveau 28–30)

| Archétype / Classe | Nb Arbres Utiles Voulus | Arbres Maxables Disponibles | Total Dons Reçus | Budget Dons Vanilla | Total Pouvoirs Reçus | Budget Pouvoirs Vanilla |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Gunslinger 2 Blasters** *(Voyou 15 / Pistolero)* | 5 | 5 | **17 à 18** | **Équilibré** | 0 *(ou 15 si Jedi)* | 0 *(ou 5 arbres)* |
| **Maraudeur Sith (2 Sabres)** *(Gardien 15 / Maraudeur 15)* | 6 | 6 | **17 à 18** | **Équilibré** (18 dons utiles) | **29 à 31** | **+16 pouvoirs en trop** |
| **Jedi / Sith Mage** *(Consulaire 15 / Maître ou Seigneur 15)* | 2 à 3 | 4 | **12 à 13** | **+4 à +6 dons inutiles** | **38 à 40** | **+18 à +24 pouvoirs en trop** |
| **Sentinelle / Veilleur** *(Sentinelle 15 / Veilleur 15)* | 3 à 4 | 5 | **15 à 16** | **+6 dons sans option martiale** | **29 à 31** | **+14 pouvoirs en trop** |

### B. Constats clés :
1. **Le Consulaire (Mage)** finit avec près de 40 pouvoirs (il prend tous les sorts du jeu) et n'a aucun don martial ou métamagique pour dépenser ses dons.
2. **Le Gardien / Maraudeur** a un budget de dons qui tombe juste en combat à 2 armes (18 dons), mais croule sous ~30 pouvoirs qui effacent son identité martiale.
3. **La Sentinelle / Veilleur** est bloquée à ~10 dons utiles car elle n'a pas accès aux dons de spécialisation du Maître d'Armes (`SUPER_WEAPON_FOCUS`), laissant 6 dons vides en fin de partie.

---

## 7. Recherche & Conception : Arts Mutaki (Mains Nues Jedi)

L'ordre des **Mutaki** (*Matukai* dans le lore étendu Star Wars / JdR d20) est une tradition d'adeptes de la Force qui canalisent l'énergie spirituelle directement à travers leur corps et les arts martiaux physiques (associé en jeu aux bures d'apprenti et d'adepte Mutaki `a_robe_05`/`a_robe_15` et au serre-tête `a_helmet_23`).

### Spécification Actée pour KotOR 2 : « Arts Mutaki » (I → II → III)
*Prérequis : Classe Jedi/Sith, Combat à mains nues (aucune arme équipée).*

- **Arts Mutaki I :** 
  - Attaque et dégâts = jet + `(DEX ou FOR) + SAG`.
  - `+1 CA` à mains nues.
  - Plage de critique portée à **`19–20`**.
- **Arts Mutaki II :** 
  - Attaque et dégâts = jet + `(DEX ou FOR) + SAG`.
  - `+2 CA` à mains nues.
  - Plage de critique portée à **`18–20`**.
  - **Force Whirlwind :** En cas de coup critique, applique l'effet de contrôle **Tourbillon de Force** pendant **1 tour** (DD Vigueur : `10 + Niveau + SAG`, prenant en compte l'échelle de sauvegarde via autobalance).
- **Arts Mutaki III :** 
  - Attaque et dégâts = jet + `(DEX ou FOR) + SAG`.
  - `+3 CA` à mains nues.
  - Plage de critique portée à **`17–20`**.
  - **Force Whirlwind :** En cas de coup critique, applique l'effet de contrôle **Tourbillon de Force** pendant **2 tours** (DD Vigueur : `10 + Niveau + SAG`).
