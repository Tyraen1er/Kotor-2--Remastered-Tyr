# Système de Combat, Armures & Armes — JdR Papier *Star Wars d20 (Revised)*

Ce document synthétise les règles officielles du jeu de rôle sur table ***Star Wars Roleplaying Game – Revised Core Rulebook* (Wizards of the Coast, 2002)** dont est directement tiré KotOR, en mettant en évidence **les mécaniques originales supprimées ou simplifiées par BioWare/Obsidian** et comment elles peuvent servir de modèles pour rééquilibrer KotOR 2.

> **Catalogues complets de référence (descriptifs intégraux du JdR) :**
> * **Tous les Dons du JdR (Généraux, Martiaux & Force Feats) :** [`_reference/jdr/dons_swd20.md`](file:///C:/Users/emman/Desktop/dev/Kotor%202%20Mods/_reference/jdr/dons_swd20.md)
> * **Tous les Pouvoirs de la Force du JdR (Control, Sense, Alter, Dark Side) :** [`_reference/jdr/pouvoirs_swd20.md`](file:///C:/Users/emman/Desktop/dev/Kotor%202%20Mods/_reference/jdr/pouvoirs_swd20.md)
> * **Analyse comparative Dons & Force (JdR vs KotOR 2) :** [`datas_jdr_SW/dons_et_force_swd20.md`](file:///C:/Users/emman/Desktop/dev/Kotor%202%20Mods/datas_jdr_SW/dons_et_force_swd20.md)

---

## Sommaire
1. [Santé, Défense et Armures : Le Système VP/WP et la Réduction de Dégâts](#1-santé-défense-et-armures--le-système-vpwp-et-la-réduction-de-dégâts)
2. [Tableau des Armures du JdR *Star Wars d20*](#2-tableau-des-armures-du-jdr-star-wars-d20)
3. [Pourquoi les Fusils Blasters dominent les Pistolets dans le JdR Papier (*Multifire* & *Autofire*)](#3-pourquoi-les-fusils-blasters-dominent-les-pistolets-dans-le-jdr-papier-multifire--autofire)
4. [Tableau des Armes à Distance & Mêlée du JdR *Star Wars d20*](#4-tableau-des-armes-à-distance--mêlée-du-jdr-star-wars-d20)

---

## 1. Santé, Défense et Armures : Le Système VP/WP et la Réduction de Dégâts

Dans le JdR papier *Star Wars d20*, l'équilibrage entre un personnage sans armure (Jedi, Voyou) et un personnage en armure (Soldat, Mandalorien) repose sur **3 règles majeures** :

1. **Deux jauges de vie : *Vitality Points (VP)* et *Wound Points (WP)* :**
   * **Vitality Points (VP) :** Augmentent à chaque niveau (comme les PV de KotOR). Ils représentent l'endurance, la chance et la capacité à transformer un coup mortel en simple éraflure.
   * **Wound Points (WP) :** Égaux au **score de Constitution** du personnage (ex: 14 WP).
   * **Fonctionnement des Coups Critiques :** En *Star Wars d20 Revised*, un coup critique **ne multiplie plus les dégâts par 2** ; à la place, **les dégâts du coup critique ignorent la jauge de Vitalité et s'appliquent directement aux *Wound Points*** (avec un jet de Vigueur DD 15 sous peine d'être étourdi/inconscient).
2. **La Défense monte automatiquement avec le niveau de classe :**
   * Comme dans Star Wars les héros se battent rarement en armure complète, toutes les classes gagnent un **Bonus de Classe à la Défense** qui augmente avec le niveau (équivalent aux dons *Sens de la Force / Sens du Chevalier* de KotOR, mais pour **toutes** les classes).
3. **Les Armures donnent de la Réduction de Dégâts (DR), pas de la Défense !**
   * Dans la version révisée (2002), porter une armure **ne remplace pas le bonus de Défense de classe**, mais accorde une **Réduction de Dégâts (DR)** fixe contre toutes les attaques (sauf les sabres laser qui ignorent la DR des armures non-Cortosis).
   * *Pourquoi KotOR a cassé les armures :* BioWare a supprimé la DR des armures pour revenir à la CA de D&D 3.0 (avec plafond de Dextérité strict). Résultat : dans KotOR, une armure lourde donne à peine plus de CA qu'une robe Jedi avec haute DEX, tout en bloquant les pouvoirs de Force.

---

## 2. Tableau des Armures du JdR *Star Wars d20*

| Catégorie | Modèle d'armure (*Star Wars d20 RCR*) | Réduction de Dégâts (*DR*) | Bonus DEX Max | Malus d'Armure (Compétences) | Vitesse (base 10m) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **Légère** | Combinaison matelassée (*Padded Flight Suit*) | **DR 2** | +4 | -1 | 10 m |
| **Légère** | Combinaison de combat (*Combat Jumpsuit*) | **DR 3** | +4 | -2 | 10 m |
| **Légère** | Gilet et casque anti-blaster (*Blast Helmet & Vest*) | **DR 3** | +5 | -1 | 10 m |
| **Intermédiaire** | Armure de bataille légère (*Padded Battle Armor*) | **DR 4** | +3 | -3 | 8 m |
| **Intermédiaire** | Armure de Stormtrooper (*Stormtrooper Armor*) | **DR 4** | +3 | -4 | 8 m |
| **Intermédiaire** | Combinaison assistée Corellienne (*Corellian Powersuit*) | **DR 5** *(+2 FOR)* | +3 | -4 | 8 m |
| **Lourde** | Armure de bataille lourde (*Heavy Battle Armor*) | **DR 7** | +1 | -6 | 6 m |
| **Lourde** | Armure Mandalorienne / Matrice (*Matrix Armor*) | **DR 9** | +1 | -8 | 6 m |

> **Idée directe pour ton Mod KotOR 2 :**
> Redonner aux armures intermédiaires et lourdes (ou aux dons *Port d'armure intermédiaire / lourde*) leur **Réduction de Dégâts (DR 3 à DR 8)** issue du JdR papier permettrait immédiatement de créer un vrai archétype de **Tank Cuirassé**, très différent du Jedi esquiveur en robe !

---

## 3. Pourquoi les Fusils Blasters dominent les Pistolets dans le JdR Papier (*Multifire* & *Autofire*)

Tu avais remarqué que dans KotOR, un fusil blaster est strictement inférieur à deux pistolets blasters.
Dans le JdR papier *Star Wars d20*, **c'est exactement l'inverse** grâce à **3 règles que BioWare n'a pas implémentées** :

1. **Le mode *Multifire* (Rafale courte — Exclusif aux Carabines et Fusils) :**
   * Les pistolets blasters sont limités au tir coup par coup (*Single Shot*).
   * Les **Carabines et Fusils blasters** possèdent un sélecteur de tir **Multifire** : en subissant `-2` au jet d'attaque, le tireur effectue **+1 tir supplémentaire** dans le round, **sans avoir besoin d'aucun don** !
   * Mieux : *Multifire* **se cumule avec le don *Tir rapide (Rapid Shot)*** ! Un soldat avec un seul Fusil Blaster et *Rapid Shot* tire donc **3 fois dès le niveau 1** (à `-4` d'attaque), là où un pistolet unique ne tire que 2 fois.
2. **Le mode *Autofire* (Tir de barrage / Zone — Carabines, Fusils & Blasters à répétition) :**
   * L'arme arrose une **zone de 2 m × 2 m** (consomme 10 munitions).
   * Le tireur fait un jet d'attaque à `-4` contre une **Défense fixe de 10**. S'il réussit, **tous les ennemis présents dans la zone** subissent les dégâts complets de l'arme (jet de Réflexes **DD 15** pour réduire de moitié).
3. **Un vrai écart de dés de dégâts ET de portée de tir étourdissant (*Stun*) :**
   * Pistolet blaster = `3d6` (moy. **10,5**) | Pistolet lourd = `3d8` (moy. **13,5**).
   * Fusil blaster = `3d8` Critique `19-20` (moy. **13,5** + *Multifire/Autofire*) | Arbalète Wookie = `3d10` (moy. **16,5**) | Blaster lourd à répétition = **`5d8` (moy. 22,5 !)**.

---

## 4. Tableau des Armes à Distance & Mêlée du JdR *Star Wars d20*

### A. Armes à Distance (*Ranged Weapons*)

| Arme (*Star Wars d20 RCR*) | Dégâts Papier | Moyenne | Critique | Portée Incr. | Modes de Tir | Particularité JdR Papier |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Blaster de poche** (*Hold-out blaster*) | `3d4` | 7,5 | `20` | 8 m | Coup par coup | Facile à dissimuler (+4 Discrétion) |
| **Pistolet blaster** (*Blaster pistol*) | `3d6` | 10,5 | `20` | 10 m | Coup par coup | Mode Stun (Vigueur DD 15) |
| **Pistolet blaster lourd** (*Heavy blaster*) | `3d8` | 13,5 | `20` | 8 m | Coup par coup | Consomme double énergie |
| **Carabine blaster** (*Blaster carbine*) | `3d8` | 13,5 | `19-20` | 12 m | Coup, **Multifire**, **Autofire** | Arme polyvalente d'assaut |
| **Fusil blaster** (*Blaster rifle*) | `3d8` | 13,5 | `19-20` | 30 m | Coup, **Multifire**, **Autofire** | Mode Stun amélioré (Vigueur **DD 18**) |
| **Arbalète Wookie** (*Bowcaster*) | `3d10` | 16,5 | `19-20` | 12 m | Coup par coup | Requiert FOR 14 minimum |
| **Blaster léger à répétition** (*Light repeating*) | `4d8` | 18,0 | `20` | 25 m | **Multifire**, **Autofire** | Pas de tir coup par coup |
| **Blaster lourd à répétition** (*Heavy repeating*) | `5d8` | 22,5 | `20` | 30 m | **Autofire** | Dégâts massifs de suppression |

### B. Armes de Mêlée & Sabres Laser (*Melee & Lightsabers*)

| Arme (*Star Wars d20 RCR*) | Dégâts Papier | Critique | Prise en main | Particularité JdR Papier |
| :--- | :---: | :---: | :---: | :--- |
| **Matraque étourdissante** (*Stun baton*) | `1d6` + Stun | `20` | 1 main | Étourdit sur jet de Vigueur **DD 15** |
| **Vibrodague** (*Vibrodagger*) | `2d4` | `19-20` | Légère | Arme légère idéale en main secondaire |
| **Vibrolame** (*Vibroblade*) | `2d6` | `19-20` | 1 main | Peut être tenue à 2 mains (`1.5× FOR`) |
| **Vibro-hache** (*Vibro-ax*) | `2d10` | `20` | **2 mains** | Ajoute **`1.5× Mod. FOR`** aux dégâts |
| **Pique de Force** (*Force pike*) | `2d8` | `20` | **2 mains** | Arme d'allonge, `1.5× FOR` |
| **Sabre laser** (*Lightsaber*) | **`2d8` à `6d8`** *(selon niv.)* | `19-20` | 1 ou 2 mains | **Dégâts évolutifs avec le niveau du Jedi** (`+1d8` tous les 4-5 niveaux) et **ignore la DR** ! Peut être tenu à **2 mains pour `1.5× FOR`** ! |
| **Sabre laser double** (*Double lightsaber*) | `2d8 / 2d8` *(évolutif)* | `19-20` | Double | 2 attaques, mais ne permet pas le `1.5× FOR` d'un sabre unique tenu à deux mains |

> **Observation capitale sur le Sabre Laser dans le JdR Papier :**
> Dans *Star Wars d20*, un Jedi qui n'utilise **qu'un seul sabre laser** le tient naturellement **à deux mains** (comme Luke, Obi-Wan ou Vader dans les films), ce qui lui donne **`1.5× son modificateur de Force`** aux dégâts, tandis qu'un sabre double (style Maul) donne une attaque supplémentaire mais à `1.0× / 0.5× FOR` !
> Dans KotOR 2, Obsidian a fait **l'erreur inverse** : le sabre simple est bloqué à `1.0× FOR` et le sabre double reçoit `1.5× FOR` ! Ton idée de donner `+25% / +50% / +100% FOR` au don *Duel* rétablit en fait la vraie logique du JdR papier.
