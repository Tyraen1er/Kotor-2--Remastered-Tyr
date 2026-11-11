# Liste Complète des Dons (*Feats*) — JdR *Star Wars d20 (Revised Core Rulebook)*

Ce document de référence répertorie l'ensemble des **Dons Généraux, Martiaux et Compétences** ainsi que les **Dons de la Force (*Force Feats*)** du livre de règles officiel ***Star Wars Roleplaying Game – Revised Core Rulebook (WotC, 2002)*** avec leurs prérequis, leurs effets exacts et leur statut dans *KotOR 2*.

> Pour l'analyse comparative et les idées d'équilibrage entre ce système et KotOR 2, voir [`datas_jdr_SW/dons_et_force_swd20.md`](file:///C:/Users/emman/Desktop/dev/Kotor%202%20Mods/datas_jdr_SW/dons_et_force_swd20.md).

---

## Sommaire
1. [Dons de Combat au Corps-à-Corps & Arts Martiaux](#1-dons-de-combat-au-corps-à-corps--arts-martiaux)
2. [Dons de Combat à Distance (Blasters & Armes Lourdes)](#2-dons-de-combat-à-distance-blasters--armes-lourdes)
3. [Dons Défensifs, Armures & Survie](#3-dons-défensifs-armures--survie)
4. [Dons de Compétences, Mouvement & Général](#4-dons-de-compétences-mouvement--général)
5. [Dons de la Force (*Force Feats*)](#5-dons-de-la-force-force-feats)

---

## 1. Dons de Combat au Corps-à-Corps & Arts Martiaux

| Don (*Feat* VO / VF) | Prérequis | Descriptif Officiel (*Star Wars d20 RCR*) | Présent dans KotOR 2 ? |
| :--- | :--- | :--- | :---: |
| **Ambidexterity**<br>*(Ambidextrie)* | DEX 15 | Réduit de 4 le malus de la main secondaire lors du combat à deux armes (le malus passe de `-6 / -10` à `-6 / -6`, ou `-4 / -4` avec une arme légère). | Fusionné dans *Combat à deux armes* |
| **Two-Weapon Fighting**<br>*(Combat à deux armes)* | — | Réduit de 2 le malus de la main principale et de 6 celui de la main secondaire. Combiné avec *Ambidexterity* et une arme secondaire légère, le malus tombe à **`-2 / -2`**. | Oui (*Combat à deux armes I/II/III*) |
| **Improved Two-Weapon Fighting**<br>*(Science du combat à deux armes)* | DEX 17, *Two-Weapon Fighting*, *Ambidexterity*, BBA +9 | Accorde une **deuxième attaque avec l'arme secondaire** (avec un malus de `-5` supplémentaire). | Non (KotOR plafonne à 1 attaque main gauche) |
| **Power Attack**<br>*(Attaque en puissance)* | FOR 13 | Avant d'attaquer, le personnage peut soustraire un nombre jusqu'à son BBA à ses jets d'attaque de mêlée et ajouter ce même nombre à ses jets de dégâts pendant tout le round. | Oui (*Attaque en puissance I/II/III*) |
| **Cleave**<br>*(Enchaînement)* | FOR 13, *Power Attack* | Si le personnage inflige assez de dégâts en mêlée pour faire tomber un ennemi (0 PV/WP), il obtient immédiatement **une attaque de mêlée supplémentaire gratuite** contre un autre adversaire à portée. (1 fois par round). | **Non** |
| **Great Cleave**<br>*(Grand enchaînement)* | FOR 13, *Power Attack*, *Cleave*, BBA +4 | Comme *Cleave*, mais **sans limite** sur le nombre d'attaques gratuites d'enchaînement par round tant que chaque coup achève une cible. | **Non** |
| **Sunder**<br>*(Destruction d'arme)* | FOR 13, *Power Attack* | Permet d'attaquer l'arme ou le bouclier tenu par un adversaire sans provoquer d'attaque d'opportunité et en infligeant des dégâts doublés à l'objet. | **Non** |
| **Combat Expertise**<br>*(Expertise du combat)* | INT 13 | Lors d'une action d'attaque en mêlée, le personnage peut subir un malus volontaire allant jusqu'à `-5` à ses jets d'attaque pour ajouter le même montant (jusqu'à **`+5`**) en **bonus d'esquive à sa Défense**. | **Non** |
| **Improved Disarm**<br>*(Science du désarmement)* | INT 13, *Combat Expertise* | Le personnage ne provoque pas d'attaque d'opportunité lorsqu'il tente de désarmer un ennemi, et l'ennemi ne peut pas le désarmer en retour s'il échoue. | **Non** |
| **Improved Trip**<br>*(Science du croc-en-jambe)* | INT 13, *Combat Expertise* | Ne provoque pas d'attaque d'opportunité lors d'un croc-en-jambe. Si l'ennemi tombe au sol (*Prone*), le personnage gagne immédiatement **une attaque gratuite** contre lui. | **Non** |
| **Whirlwind Attack**<br>*(Attaque circulaire)* | INT 13, DEX 13, *Combat Expertise*, *Dodge*, *Mobility*, *Spring Attack*, BBA +4 | Au prix d'une action complète, le personnage abandonne ses attaques supplémentaires normales pour porter **une attaque de mêlée au bonus maximal contre CHAQUE adversaire adjacent** dans un rayon de 2 mètres. | **Non** *(Déluge ne cible qu'un ennemi)* |
| **Weapon Finesse**<br>*(Finesse des armes)* | Arme maîtrisée, BBA +1 | Avec une arme légère, une vibrolame ou un sabre laser, le personnage utilise son **modificateur de Dextérité** au lieu de son modificateur de Force pour ses jets d'attaque au corps-à-corps. | Oui (*Finesse : Armes de mêlée / Sabres*) |
| **Weapon Focus**<br>*(Arme de prédilection)* | Arme maîtrisée, BBA +1 | Accorde un bonus de **`+1` aux jets d'attaque** avec le groupe d'armes choisi. | Oui (*Arme de prédilection*) |
| **Improved Critical**<br>*(Science du critique)* | Arme maîtrisée, BBA +8 | **Double la plage de menace critique** de l'arme choisie (ex: `20` devient `19-20`, `19-20` devient `17-20`). | Remplacé par *Déluge de coups Critique* |
| **Martial Arts**<br>*(Arts martiaux)* | BBA +1 | Les attaques à mains nues sont considérées comme armées (pas d'attaque d'opportunité), infligent **`1d4`** dégâts (au lieu de `1d3`) et accordent **`+1` de bonus d'esquive à la Défense** en mêlée. | Remplacé par *Spécialiste du combat à mains nues* |
| **Defensive Martial Arts**<br>*(Arts martiaux défensifs)* | *Martial Arts* | Le bonus d'esquive à la Défense contre les attaques de mêlée passe à **`+2`** (ou `+4` contre les attaques d'opportunité). | **Non** |
| **Improved Martial Arts**<br>*(Science des arts martiaux)* | *Martial Arts*, *Defensive Martial Arts*, BBA +6 | La plage de menace critique des attaques à mains nues passe de `20` à **`19-20`**. | **Non** |
| **Combat Reflexes**<br>*(Réflexes de combat)* | — | Permet de faire un nombre d'attaques d'opportunité par round égal à `1 + modificateur de DEX`, et d'en faire même en étant pris au dépourvu. | **Non** |
| **Blind-Fight**<br>*(Combat en aveugle)* | — | En mêlée, permet de relancer le jet de pourcentage d'échec dû au camouflage/invisibilité de la cible. Les attaquants invisibles n'ont pas de bonus au toucher contre le personnage. | **Non** |

---

## 2. Dons de Combat à Distance (Blasters & Armes Lourdes)

| Don (*Feat* VO / VF) | Prérequis | Descriptif Officiel (*Star Wars d20 RCR*) | Présent dans KotOR 2 ? |
| :--- | :--- | :--- | :---: |
| **Point Blank Shot**<br>*(Tir à bout portant)* | — | Accorde **`+1` aux jets d'attaque et `+1` aux dégâts** avec les armes à distance sur les cibles situées à moins de 10 mètres. | Oui (*Tir à bout portant*) |
| **Precise Shot**<br>*(Tir de précision)* | *Point Blank Shot* | Permet de tirer sur un ennemi engagé au corps-à-corps avec un allié sans subir le malus standard de `-4` et réduit la capacité de déviation des Jedi. | Oui (*Tir de précision I/II/III*) |
| **Far Shot**<br>*(Tir lointain)* | *Point Blank Shot* | Augmente le facteur de portée des armes à distance de +50% (+100% pour les armes de jet). | **Non** |
| **Rapid Shot**<br>*(Tir rapide)* | DEX 13, *Point Blank Shot* | Permet d'effectuer **une attaque à distance supplémentaire par round** au bonus maximal, mais toutes les attaques du round subissent un malus de `-2`. | Oui (*Tir rapide I/II/III*) |
| **Multishot**<br>*(Tir multiple)* | DEX 17, *Point Blank Shot*, *Rapid Shot*, BBA +6 | Réduit de 2 les malus liés à l'utilisation du mode **Multifire** (passe de `-4` à `-2`) et du mode **Autofire** (passe de `-6` à `-4`) sur les **Fusils Blasters et Armes à répétition**. | **Non** *(Crucial pour les Fusils)* |
| **Power Blast**<br>*(Décharge d'énergie)* | *Point Blank Shot* | Avant de tirer, le personnage peut soustraire jusqu'à `-5` (limité par son BBA) à ses jets d'attaque à distance pour ajouter **`+1` à `+5` aux dégâts** de ses tirs. | Oui (*Décharge d'énergie I/II/III*) |
| **Sharp-Shooting**<br>*(Tir ajusté)* | *Point Blank Shot*, *Precise Shot*, BBA +3 | Accorde un bonus de **`+2` aux jets d'attaque à distance** contre toute cible bénéficiant d'un couvert (réduit l'efficacité du couvert ennemi). | **Non** |
| **Shot on the Run**<br>*(Tir en mouvement)* | DEX 13, *Point Blank Shot*, *Dodge*, *Mobility*, BBA +4 | Permet de se déplacer à la fois avant et après une attaque à distance, dans la limite de sa vitesse totale de déplacement. | **Non** |

---

## 3. Dons Défensifs, Armures & Survie

| Don (*Feat* VO / VF) | Prérequis | Descriptif Officiel (*Star Wars d20 RCR*) | Présent dans KotOR 2 ? |
| :--- | :--- | :--- | :---: |
| **Armor Proficiency (Light / Medium / Heavy / Powered)**<br>*(Port d'armure)* | Légère ➔ Intermédiaire ➔ Lourde ➔ Assistée | Permet de porter la catégorie d'armure correspondante (qui accorde une **Réduction de Dégâts de DR 2 à DR 9**) sans appliquer le malus d'armure aux jets d'attaque. | Oui (*Port d'armure légère / intermédiaire / lourde*) |
| **Dodge**<br>*(Esquive)* | DEX 13 | Pendant son tour, le personnage désigne un adversaire et gagne **`+1` de bonus d'esquive à la Défense** contre les attaques de cet adversaire. | **Non** |
| **Mobility**<br>*(Souplesse du serpent)* | DEX 13, *Dodge* | Accorde un bonus d'esquive de **`+4` à la Défense** contre les attaques d'opportunité provoquées par le déplacement. | **Non** |
| **Spring Attack**<br>*(Attaque éclair)* | DEX 13, *Dodge*, *Mobility*, BBA +4 | En mêlée, permet de se déplacer avant et après l'attaque sans provoquer d'attaque d'opportunité de la part de la cible. | **Non** |
| **Toughness**<br>*(Robustesse)* | — | Le personnage gagne **+3 points de Vitalité** (cumulable plusieurs fois). | Oui (*Robustesse I/II/III*) |
| **Stamina**<br>*(Vigueur / Récupération)* | CON 13 | Le personnage récupère ses points de Vitalité et de Blessures **deux fois plus vite** lors du repos. | Oui (*Régénération*) |
| **Endurance**<br>*(Endurance)* | *Stamina* | Bonus de `+4` aux jets de Vigueur et de Constitution liés à la fatigue, l'asphyxie, la faim ou les environnements extrêmes. | **Non** |
| **Great Fortitude**<br>*(Vigueur surhumaine)* | — | Accorde un bonus permanent de **`+2` aux jets de sauvegarde de Vigueur**. | Oui (*Conditionnement I/II/III*) |
| **Iron Will**<br>*(Volonté de fer)* | — | Accorde un bonus permanent de **`+2` aux jets de sauvegarde de Volonté**. | Oui (*Conditionnement I/II/III*) |
| **Lightning Reflexes**<br>*(Réflexes surhumains)* | — | Accorde un bonus permanent de **`+2` aux jets de sauvegarde de Réflexes**. | Oui (*Conditionnement I/II/III*) |

---

## 4. Dons de Compétences, Mouvement & Général

| Don (*Feat* VO / VF) | Prérequis | Descriptif Officiel (*Star Wars d20 RCR*) | Présent dans KotOR 2 ? |
| :--- | :--- | :--- | :---: |
| **Heroic Surge**<br>*(Sursaut héroïque)* | — | Une à plusieurs fois par jour (selon le niveau : 1/jour niv. 1-4, 2/jour niv. 5-8, etc.), le personnage peut effectuer **une action d'attaque ou de mouvement supplémentaire** pendant son tour ! | **Non** *(Super idée de don actif martial !)* |
| **Frightful Presence**<br>*(Présence terrifiante)* | CHA 15, BBA +5 | Lorsque le personnage attaque ou dégaine, les ennemis de niveau inférieur dans un rayon de 10 m doivent réussir un jet de Volonté (`DD 10 + 1/2 Niv + Mod. CHA`) ou subir `-2` aux jets d'attaque, de sauvegarde et de compétence pendant 10 rounds. | **Non** |
| **Quick Draw**<br>*(Dégainage rapide)* | BBA +1 | Permet de dégainer ou changer d'arme par une action gratuite au lieu d'une action de mouvement. | **Non** |
| **Improved Initiative**<br>*(Science de l'initiative)* | — | Accorde un bonus de **`+4` aux jets d'initiative**. | **Non** |
| **Weapon Group Proficiency**<br>*(Maniement d'armes)* | — | Supprime le malus de `-4` à l'attaque pour une famille d'armes (*Simple, Primitive, Blaster Pistols, Blaster Rifles, Heavy Weapons, Vibroweapons, Slugthrowers*). | Oui (*Maniement des armes*) |
| **Exotic Weapon Proficiency**<br>*(Arme exotique)* | BBA +1 | Permet de manier une arme exotique spécifique (*Sabre laser, Sabre double, Arbalète Wookie, Amphistaff*). | Oui (*Maniement du sabre laser*) |
| **Skill Emphasis**<br>*(Talent)* | — | Accorde un bonus de **`+3` à une compétence** choisie. | Oui (*Talent : Compétence*) |
| **Dons de Compétences Doubles** | — | **Acrobatic, Alertness, Athletic, Cautious, Gearhead, Low Profile, Mimic, Persuasive, Spacer, Stealthy, Street Smart, Surgery, Track, Trick, Trustworthy, Zero-G Training** : Accordent `+2` à deux compétences liées. | Oui (*Prudence, Empathie, Équipement*) |

---

## 5. Dons de la Force (*Force Feats*)

Dans *Star Wars d20*, les **Dons de la Force** nécessitent le don initial **Force-Sensitive**. Beaucoup des capacités qui sont des dons passifs ou des pouvoirs dans KotOR 2 sont en réalité des **Dons de la Force** dans le JdR papier :

| Don de la Force (*Force Feat*) | Prérequis | Descriptif Officiel (*Star Wars d20 RCR*) | Équivalent dans KotOR 2 |
| :--- | :--- | :--- | :--- |
| **Force-Sensitive**<br>*(Sensible à la Force)* | — | Permet d'apprendre les compétences de Force, de dépenser des Points de Force comme un Jedi et d'accéder aux Dons de Force. | Don *Sensibilité à la Force* |
| **Control / Sense / Alter**<br>*(Contrôle / Sens / Altération)* | *Force-Sensitive* | Les 3 piliers fondamentaux. Chacun débloque sa liste de compétences de Force (*Control* = buffs personnels/soin ; *Sense* = détection/télépathie ; *Alter* = télékinésie/éclairs/esprit). | Remplacé par les niveaux de Jedi |
| **Lightsaber Defense**<br>*(Défense au sabre laser)* | *Force-Sensitive*, *Exotic Weapon (Lightsaber)* | Tant que le personnage manie un sabre laser allumé, il gagne un **bonus d'esquive de `+2` à la Défense**. | Don *Duel I* / *Sens de la Force* |
| **Knight Defense**<br>*(Défense de Chevalier)* | Niv. Force 7+, *Control*, *Lightsaber Defense* | Le bonus d'esquive à la Défense avec un sabre laser passe à **`+4`** (cumulé avec *Lightsaber Defense*). | Don *Duel II* / *Sens du Chevalier* |
| **Master Defense**<br>*(Défense de Maître)* | Niv. Force 13+, *Control*, *Knight Defense* | Le bonus d'esquive à la Défense avec un sabre laser passe à **`+6`**. | Don *Duel III* / *Sens du Maître* |
| **Deflect (Defense / Attack / Extend)**<br>*(Déviation des tirs)* | *Force-Sensitive*, Sabre laser | • **Deflect (Defense) :** Bonus d'esquive de `+1` à `+4` contre les attaques à distance.<br>• **Deflect (Attack) :** Permet de renvoyer un tir de blaster vers un ennemi (`-4` à l'attaque).<br>• **Extend Defense :** Permet de dévier les tirs visant des alliés adjacents. | Dons *Déviation de blaster* / *Redirection* |
| **Burst of Speed**<br>*(Pointe de vitesse)* | *Force-Sensitive*, *Control* | Coûte 2 VP. Multiplie la vitesse de déplacement par **×2** pendant 1 round (action gratuite). | Pouvoir *Pointe de vitesse* |
| **Force Speed / Knight Speed / Master Speed**<br>*(Vitesse de la Force / Chevalier / Maître)* | *Control*, *Burst of Speed*, Niv. Force 3 / 7 / 13 | Permet de multiplier sa vitesse par ×3, ×4 ou ×5, ou d'obtenir un **bonus d'esquive à la Défense (`+2 / +4 / +6`) et une action supplémentaire**. | Pouvoirs *Vitesse du Chevalier / Maître* |
| **Dissipate Energy**<br>*(Dissiper l'énergie)* | *Control*, *Force Defense* (5 rangs) | Permet d'absorber à mains nues les dégâts d'énergie (blasters, feu, éclairs de Force) via un test de *Force Defense* (`DD 10 + dégâts subis`). Si le test réussit de 10+, les dégâts absorbés **soignent la Vitalité** du Jedi ! | Pouvoir *Barrière d'énergie* / *Absorption* |
| **Force Mastery**<br>*(Maîtrise de la Force)* | Niv. Force 7+, *Control*, *Sense*, *Alter* | Permet de faire "Prendre 10" (*Take 10*) aux tests de compétences de Force même en plein combat et réduit le temps d'activation des pouvoirs. | Forme *Maîtrise de la Force* |
| **High Force Mastery**<br>*(Haute maîtrise de la Force)* | Niv. Force 13+, *Force Mastery* | Réduit de **2 points de Vitalité** le coût de tous les pouvoirs de Force utilisés (minimum 1 VP) et permet d'activer les pouvoirs de maintien en action gratuite. | Don de classe *Affinité avec la Force* |
| **Mettle**<br>*(Trempe / Résolution)* | *Control*, *Force Defense* (5 rangs) | Si le Jedi réussit un jet de sauvegarde de **Vigueur ou de Volonté** contre une attaque qui inflige normalement un demi-effet en cas de réussite, il ne subit **aucun effet** ! | **Non** *(Idée de don défensif Jedi/Gardien)* |
| **Force Mind / Knight Mind / Master Mind**<br>*(Esprit de Force / Méditation de combat)* | *Sense*, *Enhance Ability* | Permet de partager ses bonus de Force avec ses alliés proches (*Force Mind*), à l'échelle d'une bataille (*Knight Mind*) ou d'un système stellaire (*Master Mind*) : accorde `+1` à `+4` d'attaque et de moral aux alliés. | Pouvoir *Méditation de combat* |
| **Rage**<br>*(Rage du Côté Obscur)* | *Control*, Côté Obscur | Coûte 2 VP (et donne 1 Point du Côté Obscur). Accorde **`+4 FOR`, `+4 CON`, `+2 Volonté`** et **`-2 Défense`** pendant `5 + Mod. CON` rounds. | Pouvoir *Fureur (Fury)* |
| **Malevolent**<br>*(Malveillance)* | *Alter*, 4+ Points du Côté Obscur | Ajoute un bonus de **`+2` à tous les tests de pouvoirs du Côté Obscur** (*Fear, Force Grip, Force Lightning*). | Forme *Puissance de la Force* |
| **Summon Storm**<br>*(Invoquer la tempête)* | Niv. Force 13+, *Control*, *Alter*, *Force Lightning* | Permet d'invoquer un orage dévastateur de Force qui frappe une large zone d'éclairs à chaque round. | Pouvoir *Tempête de Force* |
| **Force Flight**<br>*(Vol de Force)* | *Control*, *Alter*, *Move Object* | Permet au Jedi de léviter et de voler par télékinésie personnelle. | **Non** |
| **Link**<br>*(Lien de Force)* | *Sense*, *Telepathy* | Crée un lien télépathique permanent avec un maître ou un apprenti (comme le lien Exilée–Kreia dans KotOR 2 !). | Chaîne de Force (*Force Chain*) |
