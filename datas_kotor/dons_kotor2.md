# Référence Complète des Dons de KotOR 2 & Équivalents D&D 3.5

Ce document répertorie l'ensemble des dons (*feats*) de **Star Wars: Knights of the Old Republic II – The Sith Lords**, leurs effets exacts en jeu, leurs équivalents dans le système **D&D 3.5** (d20 System), le diagnostic d'équilibrage ainsi que les **retours et avis de la communauté** (forums r/kotor, DeadlyStream, guides de theorycraft) pour orienter le chantier de refonte.

---

## Sommaire
1. [Rappel du Moteur d20 & Différences Clés](#rappel-du-moteur-d20--différences-clés)
2. [Dons Actifs de Corps-à-Corps (Melee Active Feats)](#1-dons-actifs-de-corps-à-corps-melee-active-feats)
3. [Dons Actifs de Combat à Distance (Ranged Active Feats)](#2-dons-actifs-de-combat-à-distance-ranged-active-feats)
4. [Styles de Combat & Postures](#3-styles-de-combat--postures)
5. [Maniement & Spécialisation d'Armes](#4-maniement--spécialisation-darmes)
6. [Défense, Survie & Sauvegardes](#5-défense-survie--sauvegardes)
7. [Compétences & Utilitaires](#6-compétences--utilitaires)
8. [Aptitudes de Classe Automatiques](#7-aptitudes-de-classe-automatiques)
9. [Dons Uniques de Compagnons](#8-dons-uniques-de-compagnons)
10. [Axes Majeurs pour le Rééquilibrage](#9-axes-majeurs-pour-le-rééquilibrage)
11. [Tableau Supplémentaire (Lorem Ipsum)](#10-tableau-supplémentaire-lorem-ipsum)

---

## Rappel du Moteur d20 & Différences Clés

KotOR 2 repose sur le *Star Wars Roleplaying Game (Revised)* de Wizards of the Coast, lui-même dérivé direct de **D&D 3.0 / 3.5** :
* **Temps & Rounds :** Les combats sont divisés en rounds de 6 secondes.
* **Résolution :** Test au d20 + BBA (Bonus de Base à l'Attaque) + modificateur de caractéristique vs Défense (Classe d'Armure / CA).
* **Sauvegardes :** Vigueur (*Fortitude*), Réflexes (*Reflex*), Volonté (*Will*).
* **Modes d'attaque :** Plutôt que de déclarer des actions complexes comme dans D&D sur table, KotOR 2 utilise des dons actifs activables par round via l'interface d'action.

---

## 1. Dons Actifs de Corps-à-Corps (Melee Active Feats)

Ces dons modifient l'attaque de corps-à-corps (armes de mêlée et sabres laser) pour le round en cours.

| Don KotOR 2 (*Label 2DA*) | Rangs | Effet KotOR 2 | Équivalent D&D 3.5 | Diagnostic Équilibrage KotOR 2 | Avis & Retours Communauté (*Meta*) |
| :--- | :---: | :--- | :--- | :--- | :--- |
| **Attaque en puissance**<br>`POWER_ATTACK`<br>`IMPROVED_POWER_ATTACK`<br>`MASTER_POWER_ATTACK` | 3 | **Rang 1 :** -3 Attaque, +5 Dégâts<br>**Rang 2 :** -3 Attaque, +7 Dégâts<br>**Rang 3 :** -3 Attaque, +10 Dégâts<br>*(⚠️ Dans K2, les dégâts sont **doublés à 2 armes ou arme double** : soit +10 / +14 / **+20 dégâts** !)* | **Attaque en puissance** (*Power Attack*)<br>*(En 3.5, on choisit combien soustraire au BBA pour l'ajouter aux dégâts, x2 à 2 mains).* | **Surpuissant en fin de jeu.** Avec *Vitesse de Maître* (2 attaques supplémentaires) et deux sabres, Master Power Attack ajoute +80 à +100 dégâts bruts par round sans pénalité d'attaque additionnelle. | **Tier S (Le roi du DPS).** Considéré par la communauté comme le meilleur don offensif absolu en late game. Le scaling flat (+20 par coup à 2 armes) surpasse les attaques bonus de Flurry sur les cibles blindées. |
| **Déluge de coups**<br>`FLURRY`<br>`IMPROVED_FLURRY`<br>`WHIRLWIND_ATTACK` | 3 | **+1 attaque supplémentaire par round**.<br>**Rang 1 :** -4 Attaque, -4 Défense (pour le round)<br>**Rang 2 :** -2 Attaque, -2 Défense<br>**Rang 3 :** -1 Attaque, -1 Défense | **Déluge de coups** (*Flurry of Blows*, Moine) ou **Snap Kick** (*Tome of Battle*). | Dominant dans KotOR 1, mais dans KotOR 2 le malus de -1/-1 est tellement négligeable au rang 3 qu'il est spammé sans aucun compromis tactique. | **Tier S (Début de jeu) / Tier A (Fin).** Le choix par défaut de la majorité des joueurs. Jugé extrêmement fiable et simple à rentabiliser. La commu critique l'absence de réelle pénalité au rang 3 ("free extra attack"). |
| **Coup critique**<br>`CRITICAL_STRIKE`<br>`IMPROVED_CRITICAL_STRIKE`<br>`MASTER_CRITICAL_STRIKE` | 3 | Multiplie la plage de menace de critique de l'arme et applique -5 à la Défense.<br>**Rang 1 :** Plage x2, étourdissement 1 round si échec Vigueur (DD = Niv + Mod FOR)<br>**Rang 2 :** Plage x3<br>**Rang 3 :** Plage x4 | **Science du critique** (*Improved Critical*) + **Coup étourdissant** (*Stunning Fist*).<br>*(En 3.5, Improved Critical ne fait que doubler et ne se cumule pas).* | Permet d'atteindre des plages extrêmes (ex: sabre avec Keen + Shien = 11-20, soit **50 % de chances de critique** à chaque coup), tout en étourdissant en boucle les ennemis. | **Tier A (Fun / Build Crit) mais risqué.** Très populaire pour les builds thématiques à haut critique. En difficulté Difficile, la commu note que le malus persistant de -5 Défense rend très vulnérable face aux packs d'ennemis. |

---

## 2. Dons Actifs de Combat à Distance (Ranged Active Feats)

Ces dons s'activent pour les attaques à distance (pistolets blasters, fusils blasters et armes lourdes).

| Don KotOR 2 (*Label 2DA*) | Rangs | Effet KotOR 2 | Équivalent D&D 3.5 | Diagnostic Équilibrage KotOR 2 | Avis & Retours Communauté (*Meta*) |
| :--- | :---: | :--- | :--- | :--- | :--- |
| **Décharge d'énergie**<br>`POWER_BLAST`<br>`IMPROVED_POWER_BLAST`<br>`MASTER_POWER_BLAST` | 3 | **Rang 1 :** -3 Attaque, +5 Dégâts, chance de renverser<br>**Rang 2 :** -3 Attaque, +8 Dégâts<br>**Rang 3 :** -3 Attaque, +12 Dégâts | **Power Shot** (*règle optionnelle / Star Wars d20 / Dragon Magazine*). Pas d'équivalent direct dans le PHB 3.5. | Ne bénéficie pas du multiplicateur x2 à deux armes comme le corps-à-corps, ce qui le rend bien plus faible que *Rapid Shot*. | **Tier C/D (Le mal-aimé).** Considéré comme le pire des trois tirs. Sans attaque bonus et sans doublement des dégâts à deux armes, la commu ne l'utilise quasiment jamais, sauf pour le knockdown occasionnel. |
| **Tir rapide**<br>`RAPID_SHOT`<br>`IMPROVED_RAPID_SHOT`<br>`MULTI_SHOT` | 3 | **+1 tir supplémentaire par round**.<br>**Rang 1 :** -4 Attaque, -4 Défense<br>**Rang 2 :** -2 Attaque, -2 Défense<br>**Rang 3 :** -1 Attaque, -1 Défense | **Tir rapide** (*Rapid Shot*)<br>*(En 3.5 : donne 1 attaque de tir supplémentaire à -2 sur toutes les attaques).* | **Le meilleur don de tir du jeu.** Deux blasters + Vitesse de Maître + Tir rapide = 5 tirs par round à seulement -1 d'attaque. | **Tier S (Monstre des Gunslingers).** Le pilier absolu de tous les builds à distance. Deux blasters améliorés au max combinés à Rapid Shot transforment le personnage en tourelle qui fauche tout un groupe en 1 round. |
| **Précision de sniper**<br>`SNIPER_SHOT`<br>`IMPROVED_SNIPER_SHOT`<br>`MASTER_SNIPER_SHOT` | 3 | Multiplie la plage critique des tirs blaster et -5 Défense.<br>**Rang 1 :** Plage x2, étourdit sur échec Vigueur (DD = Niv + Mod INT)<br>**Rang 2 :** Plage x3<br>**Rang 3 :** Plage x4 | **Science du critique (à distance)** + **Ranged Pin / Stunning Attack**. | Intéressant sur les personnages à haute Intelligence (Scout / Droïde / Mira), mais sous-optimal face à la cadence brute de *Rapid Shot*. | **Tier B (Niche / Sneak Attack).** Prisé quasi exclusivement pour les builds Voyou / Assassin avec Attaque sournoise (l'étourdissement à distance active instantanément les dés de Sneak Attack). Trop pénalisant défensivement sinon. |

---

## 3. Styles de Combat & Postures

| Don KotOR 2 (*Label 2DA*) | Rangs | Effet KotOR 2 | Équivalent D&D 3.5 | Diagnostic Équilibrage KotOR 2 | Avis & Retours Communauté (*Meta*) |
| :--- | :---: | :--- | :--- | :--- | :--- |
| **Combat à deux armes**<br>`TWO_WEAPON_FIGHTING`<br>`TWO_WEAPON_ADVANCED`<br>`TWO_WEAPON_MASTERY` | 3 | Réduit les malus de base de 2 armes (-6 droite / -10 gauche) :<br>**Rang 1 :** -4 / -8 (-2 / -6 avec arme légère)<br>**Rang 2 :** -2 / -4 (0 / -2 avec arme légère)<br>**Rang 3 :** 0 / -2 (0 / 0 avec arme légère) | **Combat à deux armes** (*Two-Weapon Fighting*), **Science du combat à 2 armes** (*Improved TWF*), **Combat à 2 armes suprême** (*Greater TWF*). | **Incontournable.** Dans KotOR, l'attaque main gauche est accordée gratuitement dès qu'on équipe 2 armes ; monter ce don efface purement et simplement le malus. | **Tier S+ (Hégémonie totale).** Utilisé par ~90% des joueurs. La commu déplore l'absence totale de réelle concurrence : deux armes signifie deux sets d'upgrades/cristaux surpuissants et deux fois plus de chances de proc. |
| **Combat à 2 armes supérieur**<br>`SUPERIOR_TWO_WEAPON_1..3` | 3 | *(Réservé Maître d'Armes / Maraudeur)*<br>**Rang 1-3 :** +1/+2/+3 Attaque & Dégâts avec la main droite. | Aptitudes de classe de prestige (*Tempest* / *Dervish*). | Renforce encore l'hégémonie absolue du style ambidextre en fin de jeu. | **Tier S.** Adoré des min-maxers martiaux. Consolide le Maraudeur/Maître d'armes comme le hachoir à viande ultime du jeu. |
| **Duel / Combat à une arme**<br>`DUELING`<br>`IMPROVED_DUELING`<br>`MASTER_DUELING` | 3 | Quand le personnage combat avec **une seule arme à 1 main** :<br>**Rang 1 :** +1 Attaque, +1 Défense<br>**Rang 2 :** +2 Attaque, +2 Défense<br>**Rang 3 :** +3 Attaque, +3 Défense | Combinaison de **Esquive** (*Dodge*) et **Arme de prédilection** (*Weapon Focus*), ou styles de bretteur (*Swashbuckler*). | **Sous-évalué / Faible.** +3 Attaque et +3 Défense ne compensent jamais la perte d'une seconde arme complète (qui apporte une attaque en plus + un 2e set de cristaux/upgrades). | **Tier C (Piège à débutant / Niche Caster).** Regretté par la commu pour des raisons de roleplay (style iconique du sabre unique). Ne sert pratiquement qu'aux Consulaires purs qui ne frappent jamais et veulent juste +3 CA passif. |
| **Tir de précision**<br>`PRECISE_SHOT_I` à `_V` | 5 | Réduit le malus de tir sur cible en mêlée et confère :<br>**Rang 1 à 5 :** +1 à +5 à l'Attaque et aux Dégâts avec les blasters, et jusqu'à +10 en Défense contre les blasters. | **Tir à bout portant** (*Point Blank Shot*) + **Tir de précision** (*Precise Shot*). | Ajout d'Obsidian pour revaloriser les armes à distance. Très puissant pour les builds blaster/gunslinger. | **Tier S (Le sauveur des blasters).** Très apprécié par la commu. Considéré comme l'ajout clé d'Obsidian qui a enfin permis aux blasters de rivaliser avec les sabres laser dans KotOR 2. |
| **Combat rapproché**<br>`CLOSE_COMBAT`<br>`IMPROVED_CLOSE_COMBAT` | 2 | Réduit la pénalité de -10 en Défense subie lorsqu'on utilise un blaster au contact d'un ennemi de mêlée (+2/+2 au rang 1, +4/+4 au rang 2). | **Close-Quarters Fighting** (*Complete Warrior*) / *Point Blank Defense* (SW d20). | Corrige l'extrême vulnérabilité des tireurs engagés au corps-à-corps. | **Tier A (Obligatoire pour Gunner solo).** Indispensable dès qu'on joue un tireur sans tank pour attirer l'aggro, évitant de se faire découper en morceaux dès qu'un ennemi approche. |
| **Botte secrète / Finesse**<br>`FINESSE_MELEE_WEAPONS`<br>`FINESSE_LIGHTSABERS` | 1 | Permet d'utiliser le **modificateur de Dextérité** à la place de la Force sur les jets d'attaque si la DEX est supérieure. | **Attaque en finesse** (*Weapon Finesse*). | Séparé en deux dons distincts dans KotOR 2 (armes blanches vs sabres). *Note technique :* Ne remplace la DEX que pour le jet d'attaque, les dégâts continuent d'utiliser la Force. | **Tier A+ (Le pilier des builds DEX).** Très populaire pour les builds "intouchables" (DEX maxée pour Défense + Réflexes). *Note historique commu :* Dans le jeu vanilla non patché, Finesse Melee s'appliquait aussi par bug aux sabres laser ! |

---

## 4. Maniement & Spécialisation d'Armes

Ces dons s'appliquent séparément aux 5 catégories d'armes : *Pistolet blaster*, *Fusil blaster*, *Armes lourdes*, *Armes de mêlée*, *Sabre laser*.

| Don KotOR 2 (*Label 2DA*) | Rangs | Effet KotOR 2 | Équivalent D&D 3.5 | Diagnostic Équilibrage KotOR 2 | Avis & Retours Communauté (*Meta*) |
| :--- | :---: | :--- | :--- | :--- | :--- |
| **Maniement des armes**<br>`WEAPON_PROF_*` | 1 | Permet d'équiper la catégorie sans subir le malus de non-maniement (-4 à l'Attaque). | **Maniement d'une arme martiale** (*Martial Weapon Proficiency*) ou **Arme exotique** (*Exotic* pour le sabre). | Don de base donné automatiquement par la plupart des classes. | **Neutre (Passif de classe).** Pratiquement jamais acheté manuellement, les classes de départ fournissant déjà les compétences nécessaires. |
| **Arme de prédilection**<br>`WEAPON_FOCUS_*` | 1 | **+1 au jet d'attaque** avec la catégorie d'arme. | **Arme de prédilection** (*Weapon Focus*). | Standard, bonus modeste mais toujours utile pour fiabiliser les touches. | **Tier B.** Pris comme "filler" quand les dons essentiels sont déjà maxés ou pour débloquer la Spécialisation Martiale. |
| **Spécialisation martiale**<br>`WEAPON_SPEC_*` | 1 | **+2 aux dégâts** avec la catégorie d'arme. *(Réservé Soldat / Gardien / Maraudeur / Maître d'armes)* | **Spécialisation martiale** (*Weapon Specialization*, Guerrier Niv 4). | Bon bonus fixe en début/milieu de partie. | **Tier A (Combattants).** Très rentable sur les builds à attaques multiples (2 armes + Vitesse) où le +2 s'applique sur 4 ou 5 coups par round. |
| **Prédilection / Spéc. Supérieure**<br>`SUPERIOR_WEAPON_FOCUS_1..3`<br>`SUPERIOR_WEAPON_SPEC_1..3` | 3 | *(Réservé Classes de Prestige Martiales)*<br>Cumule jusqu'à +3 Attaque supplémentaire et +3 Dégâts. | **Science de l'arme de prédilection** (*Greater Weapon Focus*) et **Science de la spéc.** (*Greater Weapon Spec*). | Très bon bonus de spécialisation pure pour les combattants de mêlée. | **Tier A.** Un classique des builds de prestige pour maximiser le burst physique. |

---

## 5. Défense, Survie & Sauvegardes

| Don KotOR 2 (*Label 2DA*) | Rangs | Effet KotOR 2 | Équivalent D&D 3.5 | Diagnostic Équilibrage KotOR 2 | Avis & Retours Communauté (*Meta*) |
| :--- | :---: | :--- | :--- | :--- | :--- |
| **Port d'armure (Légère, Intermédiaire, Lourde)**<br>`ARMOUR_PROF_*` | 1 | Permet de porter les armures sans pénalité. | **Port des armures légères / intermédiaires / lourdes** (*Armor Proficiency*). | **Peu attractif pour les Jedi.** La quasi-totalité des pouvoirs de Force majeurs (Vitesse, Armure de Force, Éclairs) sont restreints par le port d'armure. | **Tier F pour les Jedi / B pour compagnons non-Jedi.** Consensus unanime : porter une armure sur un Jedi est une régression majeure. Ne sert qu'à Mandalore, HK-47 ou Mira/Bao-Dur avant leur entraînement. |
| **Robustesse**<br>`TOUGHNESS`<br>`IMPROVED_TOUGHNESS`<br>`MASTER_TOUGHNESS` | 3 | **Rang 1 :** +1 PV par niveau de perso.<br>**Rang 2 :** +1 PV/niv suppl. **ET Réduction des Dégâts de 2** (DR 2/-) sur chaque attaque reçue !<br>**Rang 3 :** +1 PV/niv suppl. (+3 PV/niv au total). | **Robustesse** (*Toughness* en 3.5 ne donne que +3 PV fixes !) / **Science de la robustesse** (*Improved Toughness*, +1 PV/DV) + **Réduction des dégâts** (*Damage Reduction*). | **Le Rang 2 est l'un des meilleurs dons du jeu.** La réduction de dégâts fixe de 2 s'applique à chaque tir ou coup reçu, rendant le personnage quasi-invulnérable aux attaques rapides de début de jeu. | **Rang 2 = Tier S (Early Game) / Rang 3 = Tier C.** La commu recommande quasi-systématiquement de monter jusqu'à *Improved Toughness* dès le début (sur Taris/Peragus/Telos, le DR 2/- annule la moitié des dégâts des blasters et bêtes). Le rang 3 n'est en revanche presque jamais pris. |
| **Condition physique**<br>`CONDITIONING`<br>`IMPROVED_CONDITIONING`<br>`MASTER_CONDITIONING` | 3 | **Rang 1 :** +1 à TOUTES les sauvegardes (Vigueur, Réflexes, Volonté).<br>**Rang 2 :** +2 à toutes les sauvegardes.<br>**Rang 3 :** +3 à toutes les sauvegardes. | D&D 3.5 sépare cela en 3 dons distincts : **Vigueur surhumaine** (*Great Fortitude*, +2 Vig), **Réflexes surhumains** (*Lightning Reflexes*, +2 Réf), **Volonté de fer** (*Iron Will*, +2 Vol). | Don défensif solide et universel, bien plus rentable que son équivalent 3.5. | **Tier B+ (Très bon filler défensif).** Recommandé en difficulté Difficile, surtout pour les classes à faible Volonté (Gardien / Soldat) pour éviter d'être paralysé ou terrifié par les Sith dans les zones de fin de jeu. |
| **Défense de Jedi**<br>`JEDI_DEFENSE`<br>`ADVANCED_JEDI_DEFENSE`<br>`MASTER_JEDI_DEFENSE` | 3 | Permet de dévier les tirs de blaster (jet opposé BBA + 1d20 vs jet de tir ennemi). Si le jet dépasse de 10+, le tir est renvoyé à l'attaquant.<br>Les rangs 2 et 3 augmentent le bonus de renvoi (+3 / +6). | **Dévier les flèches** (*Deflect Arrows*) et **Interception de projectiles** (*Snatch Arrows*). | Signature thématique du Jedi. Le rang 1 est accordé d'office aux Jedi ; les rangs 2 et 3 sont des options confortables. | **Rang 1 = Gratuit / Rangs 2 & 3 = Tier D.** La commu s'accorde sur le fait que le rang de base suffit amplement. Avec le scaling naturel du BBA et de la Force, les Jedi dévient déjà 95% des tirs sans dépenser de dons supplémentaires. |

---

## 6. Compétences & Utilitaires

| Don KotOR 2 (*Label 2DA*) | Rangs | Effet KotOR 2 | Équivalent D&D 3.5 | Diagnostic Équilibrage KotOR 2 | Avis & Retours Communauté (*Meta*) |
| :--- | :---: | :--- | :--- | :--- | :--- |
| **Prudence**<br>`CAUTIOUS` | 3 | +1 / +2 / +3 en **Démolition** et **Premiers soins**. | **Doigts de fée** (*Nimble Fingers*) / **Investigateur** (*Investigator*). | **Très faible / Inutile.** Les points de compétences s'obtiennent facilement avec des implants ou des compagnons spécialisés. | **Tier F ("Trash Tier").** Consensus absolu : ne jamais sélectionner ce don. Dépenser un slot de don pour +1 à +3 dans des skills mineurs est une pure perte. |
| **Empathie**<br>`EMPATHY` | 3 | +1 / +2 / +3 en **Persuasion**, **Vigilance**, **Premiers soins**. | **Négociateur** (*Negotiator*) / **Vigilance** (*Alertness*). | Peu rentable, sauf si vous voulez maxer Persuasion sans investir de points de classe. | **Tier D.** Parfois pris par des débutants voulant réussir tous les dialogues de persuasion, mais jugé inutile dès qu'on sait répartir ses points de compétences. |
| **Bricoleur ("Implants crâniens")**<br>`GEAR_HEAD` | 3 | +1 / +2 / +3 en **Sécurité**, **Informatique**, **Réparation**. | Dons de compétences de voleur (*Nimble Fingers*). | Même constat : gaspiller un slot de don pour +1 à +3 dans des skills secondaires est rarement justifiable face à un don de combat. | **Tier F.** Totalement redondant avec les droïdes (T3-M4) ou Bao-Dur qui ont déjà des dizaines de points dans ces compétences. |
| **Compétences de classe**<br>`CLASS_SKILL_*` | 1 | Transforme une compétence trans-classe en **compétence de classe** (coût de 1 point au lieu de 2 au level up). | **Apprentissage spontané** (*Able Learner*, *Races of Destiny*) ou *Open Minded*. | Utile sur l'Exilé pour débloquer Réparation ou Sécurité afin de maximiser le craft d'objets sur l'établi. | **Tier A (Très ciblé pour l'artisanat).** *Class Skill: Repair* est vivement conseillé sur l'Exilé (s'il n'est pas Sentinelle) pour atteindre les 20/21 nécessaires à la réparation complète de T3 et au rendement de désassemblage 100%. |

---

## 7. Aptitudes de Classe Automatiques

Ces dons sont accordés automatiquement au fur et à mesure de la montée en niveau :

| Don KotOR 2 (*Label 2DA*) | Rangs | Effet KotOR 2 | Équivalent D&D 3.5 | Avis & Retours Communauté (*Meta*) |
| :--- | :---: | :--- | :--- | :--- |
| **Attaque sournoise**<br>`SNEAK_ATTACK_1D6` à `_10D6` | 10 | +1d6 à +10d6 de dégâts quand la cible est prise au dépourvu, flanquée ou incapable de se défendre (Voyou / Assassin Sith / Jedi Ombre). | **Attaque sournoise** (*Sneak Attack*, aptitude de Roublard). | **Tier S (Synergies dévastatrices).** Adoré en combinaison avec les pouvoirs de contrôle de zone (*Insanité*, *Stase de zone*) : chaque cible immobilisée subit la totalité des dés de sournoise sur chaque coup. |
| **Esquive instinctive**<br>`UNCANNY_DODGE_1`<br>`UNCANNY_DODGE_2` | 2 | **Rang 1 :** Conserve le bonus de Dextérité à la Défense même surpris.<br>**Rang 2 :** Bonus aux sauvegardes contre les mines. | **Esquive instinctive** (*Uncanny Dodge* / *Improved Uncanny Dodge*, Roublard / Barbare). | **Tier B.** Excellent passif de confort qui évite les mauvaises surprises contre les embuscades de droïdes ou de mercenaires furtifs. |
| **Spécialiste mains nues**<br>`UNARMED_SPECIALIST_I..VIII` | 8 | Augmente progressivement les dégâts à mains nues (1d6, 1d8, 1d10, 1d12, 1d20, 2d10...). | **Dégâts à mains nues du Moine** (*Monk Unarmed Strike progression*). | **Tier B (Fun / Thématique).** Permet des builds "Moine Jedi" ou sans armes viables (notamment avec la Servante ou Bao-Dur), même si les sabres laser optimisés restent supérieurs. |
| **Immunité de la Force**<br>`FORCE_IMMUNITY_*` | 3 | Immunité totale contre la Peur, la Paralysie et l'Étourdissement (Jedi Sentinelle). | **Aura de bravoure** (Paladin), **Corps de diamant** et **Âme de diamant** (Moine). | **Tier A+ (Le pilier de la Sentinelle).** Très prisé en mode Difficile car cela immunise le joueur contre les sorts incapacitants les plus dangereux du jeu sans avoir besoin d'équipement dédié. |
| **Sens de la Force**<br>`FORCE_SENSE_I..II` | 2 | Bonus passif à la Défense (+2 à +4) accordé à tous les Jedi. | Équivalent d'un bonus d'armure naturelle ou d'intuition. | **Tier A (Passif indispensable).** Bonus gratuit de Défense qui contribue à rendre les Jedi très difficiles à toucher sans armure. |
| **Formes de sabre & de Force**<br>`FORM_*` | 11 | Formes martiales sélectionnables conférant des bonus/malus spécialisés (Shii-Cho, Makashi, Soresu, Ataru, Shien, Juyo, Niman, et formes de la Force). | **Postures martiales** (*Stances* du *Tome of Battle: Book of Nine Swords*). | **Tier S (Le cœur de KotOR 2).** La communauté adore ce système. *Juyo* (attaque supplémentaire) et *Shien* (critiques destructeurs) sont les formes dominantes en DPS physique. |

---

## 8. Dons Uniques de Compagnons

| Compagnon / Don (*Label*) | Effet KotOR 2 | Équivalent D&D 3.5 | Avis & Retours Communauté (*Meta*) |
| :--- | :--- | :--- | :--- |
| **Servante :** *Précognition de combat*<br>`BATTLE_PRECOGNITION` | Ajoute le **modificateur de Sagesse à la Défense** quand le personnage ne porte aucune armure. Transmissible au joueur via dialogue. | **Bonus de CA du Moine** (*Monk AC Bonus*, Sagesse à la CA sans armure). | **Tier S+ (L'un des plus gros buffs du jeu).** Rend l'Exilé masculin ridiculement résistant. La Sagesse est comptée deux fois avec l'Armure de Force et les robes Jedi, atteignant des scores de CA inatteignables autrement. |
| **Servante :** *Frappe Echani I-III*<br>`ECHANI_STRIKE_I..III` | Ajoute des dés de dégâts supplémentaires aux attaques à mains nues (+1d4, +1d6...). | Dons de style d'arts martiaux de D&D 3.5 (*Superior Unarmed Strike*). | **Tier B.** Don signature agréable qui rend la Servante très amusante à jouer en artiste martial avant ou après sa conversion Jedi. |
| **Hanharr :** *Rage de Wookie I-III*<br>`WOOKIEE_RAGE_I..III` | Bonus massif de FOR/CON et PV temporaires, malus de Défense. | **Rage de berserker** (*Barbarian Rage*). | **Tier S.** Transforme Hanharr en monstre de mêlée absolu. Cumulé avec ses stats de départ, c'est l'un des compagnons avec le DPS brut le plus élevé du jeu. |
| **Hanharr :** *Robustesse de Wookie*<br>`WOOKIEE_TOUGHNESS_I..III` | Bonus de PV et Réduction de Dégâts massive (DR 4/- voire 6/-). | **Réduction des dégâts** (*Damage Reduction*) de classe du Barbare. | **Tier S.** Compense entièrement l'impossibilité pour Hanharr de porter une armure. Rend Hanharr capable d'encaisser sans sourciller les plus gros boss. |
| **Atton :** *Esprit / Reconstitution*<br>`SPIRIT` | Si Atton tombe à 0 PV, il se relève automatiquement à 1 PV tant qu'un compagnon est encore vivant. | **Dur à cuire** (*Diehard*) ou capacité de *Revenant*. | **Tier S ("Atton l'immortel").** Célèbre auprès de la commu pour rendre Atton virtuellement impossible à tuer tant que le joueur reste en vie à distance. |
| **Kreia :** *Mentor*<br>`MENTOR` | Confère un bonus de **+10 % d'XP à tout le groupe** tant que Kreia est dans l'équipe active. | Don de commandement / Leadership. | **Tier S (Must-have leveling).** Les joueurs gardent souvent Kreia dans le groupe rien que pour accélérer la montée en niveau et atteindre plus vite les classes de prestige. |
| **Kreia :** *Lien de Force*<br>`FORCE_CHAIN` | Tout pouvoir de Force de soutien personnel lancé par l'Exilé affecte aussi Kreia (et inversement). | Don de lien magique (*Share Spells* avec familier). | **Tier A+.** Double la rentabilité de tous les buffs personnels (*Vitesse*, *Armure*, *Valor*), économisant des points de Force précieux. |
| **Bao-Dur :** *Destruction de bouclier*<br>`SHIELD_BREAKER` | Ses attaques à mains nues pulvérisent instantanément les boucliers d'énergie ennemis. | Attaque de brèche magique / *Sunder Shield*. | **Tier A (Utilitaire unique).** Très apprécié contre les droïdes et boss protégés par des boucliers Mandaloriens tenaces. |
| **HK-47 :** *Protocoles d'assassin I-III*<br>`ASSASSIN_PROTOCOL_I..III` | Bonus substantiel aux coups critiques et chances d'assommer avec les armes à distance. | Capacités de classe d'Assassin / *Assassin's Stance*. | **Tier A.** Permet à HK-47 de redevenir un sniper létal une fois ses protocoles déverrouillés via ses dialogues. |

---

## 9. Axes Majeurs pour le Rééquilibrage

1. **Le fossé Duel vs Deux Armes :**
   * *Problème :* Le don Duel n'offre que +3 Attaque et +3 Défense au maximum. En face, Deux Armes confère une attaque complète additionnelle par round sans aucune pénalité au rang 3, tout en permettant d'équiper un second ensemble de cristaux/upgrades d'armes (qui ajoutent des dizaines de points de dégâts dans KotOR 2).
   * *Pistes :* Augmenter le bonus du don Duel (ex: ajouter un multiplicateur de dégâts ou basé sur la DEX, ou augmenter la plage de critique de l'arme unique).

2. **La suprématie d'Attaque en Puissance :**
   * *Problème :* Dans KotOR 2, Obsidian a doublé le bonus de dégâts de *Power Attack* pour les armes tenues à deux mains ou les armes doubles (+20 dégâts par coup au rang 3). Avec *Vitesse de Maître* (2 attaques supplémentaires) et deux sabres, cela ajoute jusqu'à +100 de dégâts purs par round pour un malus d'attaque dérisoire de -3.
   * *Pistes :* Réduire le bonus à deux mains (ex: x1.5 au lieu de x2) ou augmenter la pénalité d'attaque au rang 3 (-5 au lieu de -3, plus proche de D&D 3.5).

3. **La faiblesse des dons de compétences (*Cautious*, *Empathy*, *Gear Head*) :**
   * *Problème :* Accorder seulement +1 à +3 dans 2 compétences est négligeable dans KotOR 2 où les établis et les implants permettent d'atteindre des scores de compétences de 20 à 40+. Ces dons ne sont presque jamais choisis.
   * *Pistes :* Ajouter des effets passifs utilitaires (ex: *Gear Head* donne +10 % de dégâts contre les droïdes, *Cautious* confère une immunité ou réduction de dégâts face aux mines).

4. **L'obsolescence des armures pour les Jedi :**
   * *Problème :* Les armures lourdes et intermédiaires bloquent les pouvoirs de soutien vitaux (Vitesse de la Force, Armure de Force), tandis que les robes Jedi permettent de cumuler sans restriction la Dextérité et la Sagesse (via le don *Précognition de combat*).
   * *Pistes :* Autoriser certains pouvoirs de Force sous armure ou créer des dons spécialisés permettant de réduire les restrictions de Force liées au port d'armure.
