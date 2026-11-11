# Ennemis & Boss Solo de Référence pour l'Équilibrage (KotOR 2)

Ce document recense les statistiques de référence des **adversaires et boss affrontés en duel (1v1 / Solo)** dans **Star Wars: Knights of the Old Republic II – The Sith Lords** (issues de *StrategyWiki* et des données communautaires), ainsi que le fonctionnement du système d'**Autobalance** qui ajuste dynamiquement leurs statistiques au niveau de l'Exilé.

---

## 1. Point Crucial : Le Système d'Autobalance (`autobalance.2da`)

Contrairement à KotOR 1 où les ennemis avaient des statistiques fixes, KotOR 2 applique un **scaling dynamique** dès que l'Exilé entre dans une zone. Chaque ennemi appartient à un palier (*Set 1* pour les ennemis faibles jusqu'à *Set 5* pour les Boss majeurs) qui multiplie ses statistiques selon le niveau actuel du joueur :

| Palier (*Set*) | Type d'ennemi | Mult. Vitalité (`vpmult`) | Mult. Attaque (`tohitmult`) | Mult. Défense (`armormult`) | Mult. Dégâts (`damagemult`) | Mult. Sauvegardes (`savemult`) | Mod. FP (`crmod`) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **`No_Auto_Balance`** | Ennemis fixes / Tutoriel | `0.00` | `0.00` | `0.00` | `0.000` | `0.00` | `0` |
| **`Set_1`** | Sbires faibles | `0.65` | `0.90` | `0.60` | `0.065` | `0.80` | `-3` |
| **`Set_2`** | Soldats standards | `0.65` | `0.90` | `0.70` | `0.090` | `0.90` | `-2` |
| **`Set_3`** | Soldats d'élite / Droïdes | `0.65` | `0.95` | `0.80` | `0.110` | `1.00` | `-1` |
| **`Set_4`** | Sous-boss / Lieutenants | `0.70` | `1.00` | `0.90` | `0.135` | `1.00` | `+1` |
| **`Set_5`** | **Boss majeurs (Sion, Traya, Atris...)** | **`0.80`** | **`1.10`** | **`1.00`** | **`0.175`** | **`1.05`** | **`+4`** |

> **Conséquence pour l'équilibrage du mod :** Un boss `Set_5` gagne **+1 point de Défense par niveau du joueur** (`armormult = 1.00`) et **+1,1 point d'Attaque par niveau** (`tohitmult = 1.10`). Si l'Exilé est niveau 28, un boss `Set_5` a une Défense dans la tranche **43 à 52** !

---

## 2. Tableau Récapitulatif des Duels & Boss Solo par Palier

| Phase du jeu | Adversaire Solo (Lieu & Restrictions) | Vitalité (PV) | Défense (CA) | Sauvegardes (Vig / Réf / Vol) | Caractéristiques (FOR / DEX / CON / INT / SAG / CHA) | Particularités & Rôle d'Étalon |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **Début (Niv. 6–8)** | **Servante / Brianna**<br>*(Académie de Telos — Duel 1v1 sans armes ni armure)* | **78** | **16** | ~6 / 7 / 4 *(Soldat 6)* | **FOR** 14 (+2) \| **DEX** 16 (+3)<br>**CON** 14 (+2) \| **INT** 10 (0)<br>**SAG** 10 (0) \| **CHA** 14 (+2) | **Étalon Early Game & Mains nues.** Test pur de précision et de combat à mains nues / au bâton sans équipement. |
| **Début / Milieu (Niv. 8–12)** | **Visas Marr**<br>*(Ebon Hawk — Duel 1v1 à l'embuscade)* | ~90–120 *(selon niv.)* | ~22–24 | Profil Sentinelle | **FOR** 12 (+1) \| **DEX** 18 (+4)<br>**CON** 12 (+1) \| **INT** 10 (0)<br>**SAG** 12 (+1) \| **CHA** 15 (+2) | **Étalon Duelliste Agile.** Très haute Dextérité (+4 de base), se bat en finesse mais possède peu de PV (CON 12). |
| **Milieu (Niv. 12–16)** | **Kelborn (4e duel) & Bralor**<br>*(Cercle de Bataille de Dxun — 1v1 mêlée, **sans pouvoirs de Force**)* | **138** *(Kelborn)* | **25** *(Kelborn)* | Moyennes-Hautes *(Mandaloriens)* | Profil Soldat lourd (haute FOR/CON) | **Étalon Martial Pur (Sans Force).** Idéal pour tester la valeur des dons de mêlée et d'armure sans l'aide de *Vitesse de la Force*. |
| **Milieu / Fin (Niv. 18–22)** | **Atris**<br>*(Académie de Telos — Duel 1v1 au sabre)* | **252**<br>*(PF : 513)* | **43** | **34 / 33 / 34** | **FOR** 16 (+3) \| **DEX** 16 (+3)<br>**CON** 16 (+3) \| **INT** 16 (+3)<br>**SAG** 16 (+3) \| **CHA** 16 (+3) | **Premier mur de Défense (CA 43).** Montre pourquoi un build sans bonus d'attaque suffisant rate énormément en fin de jeu. |
| **Fin (Niv. 21–24)** | **Darth Nihilus**<br>*(Pont du Ravager — Référence Boss Niv. 21)* | **183 – 204** *(base)* | **35 – 38** | **32 / 31 / 29** à **33 / 34 / 32** | **FOR** 12–18 \| **CON** 12–26 \| **SAG** 10–40 | **Étalon Boss Hybride.** Défense autour de 36–38, sauvegardes autour de 32. |
| **Fin (Niv. 24–28)** | **Grande Bête d'Orage (*Greater Storm Beast*)**<br>*(Surface de Malachor V — 100% Solo)* | **204 – 225** | ~28–32 | Haute Vigueur | Très haute FOR & CON | **Étalon Sac à PV Physique.** Sert à tester le DPS brut et la survie au corps-à-corps sans boucliers énergétiques. |
| **Fin (Niv. 26–30)** | **Darth Sion**<br>*(Académie de Trayus — Duel 1v1 Solo)* | **~250–350 × 4 phases** *(Régénération)* | **45 – 55+** *(selon niv.)* | Très haute Vigueur | **FOR** 18+ \| **CON** ~36 (+13) | **Étalon Tank d'Endurance.** Oblige à vider sa barre de vie 3 à 4 fois (ou à réduire sa CON/SAG/Volonté par Persuasion). |
| **Boss Final (Niv. 26–30+)** | **Darth Traya (Kreia)**<br>*(Noyau de Trayus — Duel 1v1 Solo + 3 Sabres flottants)* | **1 180**<br>*(PF : 1 221)* | **51** | **Volonté : 58+** | **FOR** 28 (+9) \| **DEX** 26 (+8)<br>**CON** 50 (+20) \| **INT** 26 (+8)<br>**SAG** 64 (+27) \| **CHA** 18 (+4) | **Plafond Absolu du Jeu.** Avec **51 de Défense**, **1 180 PV** et **58+ en Volonté**, elle immunise de fait contre les sorts à DD normal et exige un jet d'attaque de **+40 à +45** pour être touchée régulièrement. |

---

## 3. Les 3 Seuils Mathématiques à Retenir pour Équilibrer tes Dons

Grâce à ces statistiques, on obtient les **3 cibles chiffrées exactes** que tes nouveaux builds doivent pouvoir franchir en solo :

1. **Seuil Début de Jeu (Niv. 6–8 — Cercle d'entraînement de Telos / Brianna) :**
   * **Cible :** Défense **16 à 20** | PV **80 à 100**.
   * **Ce qu'il faut :** Un jet d'attaque autour de **+10 à +14** (pour toucher 70 % du temps) et environ **20 à 25 dégâts/round** pour gagner en 4 rounds.
2. **Seuil Milieu de Jeu (Niv. 14–16 — Cercle Mandalorien de Dxun / Kelborn & Bralor, sans Force) :**
   * **Cible :** Défense **25 à 28** | PV **140 à 180**.
   * **Ce qu'il faut :** C'est ici que les builds purement martiaux (sans *Vitesse de la Force*) sont testés ! Il faut un jet d'attaque de **+18 à +22** et **45 à 60 dégâts/round** tout en encaissant les coups.
3. **Seuil Fin de Jeu / Boss Solo (Niv. 24–30 — Atris, Sion, Darth Traya) :**
   * **Cible :** Défense **43 (Atris) à 51 (Traya)** | Sauvegardes **34 à 58** | PV **250 à 1 180**.
   * **Enseignement majeur :**
     * Contrairement aux soldats de base de Malachor (qui ont ~30–35 de Défense), **Atris (43 CA), Sion (45–55 CA) et Traya (51 CA) ont une Défense énorme !**
     * Cela signifie qu'en duel de boss, **un bonus au jet d'attaque (+Attaque) reste en réalité TRÈS utile même au niveau 28** : contre **51 de Défense** (Traya), un personnage qui a `+36` d'attaque ne la touche que sur un `15+` au dé (**30 % de chances de toucher** !), alors qu'un Duelliste à `+42` d'attaque la touche deux fois plus souvent (**60 %**) !
     * De même, tout don qui donne un **effet d'étourdissement ou de contrôle (comme ton don Mains Nues)** ne passera **jamais** sur Atris/Traya si son DD est fixe : son DD doit obligatoirement scaler avec le **Niveau complet du personnage + modificateur de caractéristique** pour espérer atteindre un DD de 35 à 45 en fin de jeu.
