# Liste Complète des Pouvoirs de la Force (*Force Skills*) — JdR *Star Wars d20 (Revised Core Rulebook)*

Dans le jeu de rôle sur table ***Star Wars Roleplaying Game – Revised Core Rulebook (WotC, 2002)***, les pouvoirs de la Force ne sont pas des sorts à niveaux fixes comme dans D&D, mais des **Compétences de la Force (*Force Skills*)** réparties sous les trois disciplines fondamentales (**Control**, **Sense**, **Alter**).

Chaque utilisation coûte des **Points de Vitalité (VP)** (la santé/endurance du Jedi) et demande un **test de compétence (`1d20 + Rangs + Mod. Caractéristique`)** dont le résultat détermine la puissance de l'effet ou le DD du jet de sauvegarde de la cible.

> Pour la liste des pouvoirs de KotOR 2, voir [`datas_kotor/pouvoirs_kotor2.md`](file:///C:/Users/emman/Desktop/dev/Kotor%202%20Mods/datas_kotor/pouvoirs_kotor2.md). Pour l'analyse comparative JdR vs KotOR 2, voir [`datas_jdr_SW/dons_et_force_swd20.md`](file:///C:/Users/emman/Desktop/dev/Kotor%202%20Mods/datas_jdr_SW/dons_et_force_swd20.md).

---

## Sommaire
1. [Règles Générales des Pouvoirs dans *Star Wars d20* (Armures, Coût VP, Côté Obscur)](#1-règles-générales-des-pouvoirs-dans-star-wars-d20-armures-coût-vp-côté-obscur)
2. [Pouvoirs de Contrôle (*Control Skills* — Buffs & Guérison)](#2-pouvoirs-de-contrôle-control-skills--buffs--guérison)
3. [Pouvoirs de Sens (*Sense Skills* — Perception, Détection & Télépathie)](#3-pouvoirs-de-sens-sense-skills--perception-détection--télépathie)
4. [Pouvoirs d'Altération (*Alter Skills* — Télékinésie, Contrôle Mental & Attaque)](#4-pouvoirs-daltération-alter-skills--télékinésie-contrôle-mental--attaque)
5. [Pouvoirs du Côté Obscur (*Dark Side Skills*)](#5-pouvoirs-du-côté-obscur-dark-side-skills)

---

## 1. Règles Générales des Pouvoirs dans *Star Wars d20* (Armures, Coût VP, Côté Obscur)

1. **Coût en Vitalité (VP) :** Activer un pouvoir consomme directement les *Vitality Points* (PV) du personnage. S'il n'a plus de Vitalité, il peut puiser dans ses *Wound Points* (au risque de s'évanouir ou mourir).
2. **Impact des Armures sur les Pouvoirs (*Armor Check Penalty*) :**
   * Contrairement à KotOR qui interdit purement et simplement les pouvoirs sous armure, **dans *Star Wars d20*, aucune armure n'interdit d'utiliser la Force !**
   * Les pouvoirs marqués **"Malus d'Armure : Oui"** (uniquement ceux liés à uneCaractéristique physique FOR, DEX ou CON comme *Battlemind* ou *Enhance Ability*) subissent simplement le malus de compétence de l'armure (`-1` à `-8`) sur le jet de dé.
   * Les pouvoirs mentaux et télékinétiques (basés sur INT, SAG ou CHA : *Affect Mind, Move Object, Force Push, Force Grip, Force Lightning, Heal, Fear*) **ne subissent AUCUN malus d'armure** !

---

## 2. Pouvoirs de Contrôle (*Control Skills* — Buffs & Guérison)

Nécessitent le don **Control**. Ils régulent le corps et l'esprit du Jedi lui-même.

| Pouvoir (*Force Skill*) | Caract. Clé | Malus Armure | Coût VP | Action | Descriptif & Échelle d'Effet (*Star Wars d20 RCR*) | Équivalent KotOR 2 |
| :--- | :---: | :---: | :---: | :--- | :--- | :--- |
| **Battlemind**<br>*(Esprit de combat)* | **CON** | **Oui** | `2 + Bonus` *(3 à 7 VP)* | Mouvement | Concentre la Force au combat pendant **10 rounds (60 s)**.<br>Selon le résultat du test de *Battlemind* :<br>• **DD 15 :** `+1` aux jets d'attaque (coût 3 VP)<br>• **DD 20 :** `+2` à l'attaque (4 VP)<br>• **DD 25 :** `+3` à l'attaque (5 VP)<br>• **DD 30 :** `+4` à l'attaque (6 VP)<br>• **DD 35 :** `+5` à l'attaque (7 VP) | *Vaillance (Valor)* / *Aura de Force* |
| **Enhance Ability**<br>*(Amélioration de caractéristique)* | **CON** | **Oui** | **3 VP** | Complète | Augmente temporairement la **Force (FOR)** ou la **Dextérité (DEX)** pendant **10 rounds (60 s)** :<br>• **DD 15 :** `+2` FOR ou DEX<br>• **DD 25 :** `+4` FOR ou DEX<br>• **DD 35 :** `+6` FOR ou DEX<br>Permet aussi d'augmenter massivement les sauts (*Force Jump*). | *Aura / Bouclier / Armure de Force* & *Vaillance* |
| **Force Defense**<br>*(Défense de la Force)* | **CHA** | Non | **3 VP** | Mouvement | Crée un bouclier spirituel pendant **10 rounds** qui protège contre les pouvoirs de Force hostiles :<br>• **DD 15 :** `+2` aux jets de sauvegarde contre la Force<br>• **DD 20 :** `+4` aux jets de sauvegarde<br>• **DD 25 :** `+6` aux jets de sauvegarde<br>• **DD 30 :** `+8` aux jets de sauvegarde<br>Sert aussi au don *Dissipate Energy* pour absorber les tirs de blaster. | *Immunité à la Force* & *Barrière d'énergie* |
| **Force Stealth**<br>*(Camouflage de Force)* | **CHA** | Non | **2 VP / min** | Libre | Masque l'aura de Force du Jedi aux utilisateurs de *See Force*. Le résultat du test définit le DD que les autres Jedi doivent battre pour percevoir sa sensibilité à la Force ou son alignement. | *Camouflage de Force* |
| **Heal Self**<br>*(Guérison personnelle)* | **CHA** | Non | **2 VP** *(ou 0 sur les Wounds)* | Complète *(ou 1 heure)* | Permet au Jedi de se soigner lui-même :<br>• **Vitalité (1 action complète) :** Soigne `1d6` (DD 10), `2d6` (DD 15), `3d6` (DD 20) ou `4d6` (DD 25) points de Vitalité.<br>• **Blessures (1 heure) :** Soigne les *Wound Points* critiques et neutralise les poisons/maladies (DD du poison). | *Guérison (Heal)* & *Purge* |

---

## 3. Pouvoirs de Sens (*Sense Skills* — Perception, Détection & Télépathie)

Nécessitent le don **Sense**. Aucun d'entre eux ne subit de malus d'armure.

| Pouvoir (*Force Skill*) | Caract. Clé | Malus Armure | Coût VP | Action | Descriptif & Échelle d'Effet (*Star Wars d20 RCR*) | Équivalent KotOR 2 |
| :--- | :---: | :---: | :---: | :--- | :--- | :--- |
| **Enhance Senses**<br>*(Sens améliorés)* | **SAG** | Non | **3 VP** | Mouvement | Aiguise les sens pendant **10 rounds (60 s)**. Accorde un bonus aux tests de *Détection (Spot)*, *Écoute (Listen)* et *Fouille (Search)*, ainsi qu'à **l'Initiative** :<br>• **DD 10 :** `+2`<br>• **DD 15 :** `+4`<br>• **DD 20 :** `+6`<br>• **DD 25 :** `+8` | *Sens de la Force* / *Visée de Force* |
| **See Force**<br>*(Vision de la Force)* | **SAG** | Non | **3 VP** *(ou 1 VP)* | Complète | Permet de percevoir les auras de Force dans un rayon de 10 m à 100 m, de connaître l'alignement (Lumineux/Obscur) d'une cible, et de **voir les ennemis dans le noir total ou sous camouflage optique** sans malus pendant 10 rounds (1 VP). | *Vision de Force (Force Sight)* |
| **Farseeing**<br>*(Clairvoyance / Précognition)* | **SAG** | Non | **3 à 9 VP** | 1 minute | Permet d'avoir une vision d'un lieu ou d'une personne à travers la galaxie dans le présent (3 VP, DD 15), le passé (6 VP, DD 20) ou le futur (9 VP, DD 25). En combat, permet d'anticiper une embuscade (ne peut pas être surpris). | *Précognition* (Compétence passive de la Servante) |
| **Telepathy**<br>*(Télépathie)* | **SAG** | Non | **2 à 6 VP** | Attaque | Permet de lire les émotions superficielles ou d'envoyer un message mental à un allié ou un individu connu, de la même pièce (DD 10, 2 VP) jusqu'à un autre système stellaire (DD 25+, 6 VP). | *Compréhension des bêtes / Télépathie* (dialogues) |
| **Empathy**<br>*(Empathie)* | **SAG** | Non | **2 VP** | Libre | Ressent les émotions d'une cible à moins de 10 m et accorde un bonus de `+2` à `+8` (selon le test DD 10 à 25) aux tests de *Bluff, Diplomatie, Intimidation* et *Psychologie*. | *Persuasion de la Force* |

---

## 4. Pouvoirs d'Altération (*Alter Skills* — Télékinésie, Contrôle Mental & Attaque)

Nécessitent le don **Alter** (et parfois *Control* ou *Sense*).

| Pouvoir (*Force Skill*) | Caract. Clé | Malus Armure | Coût VP | Action | Descriptif & Échelle d'Effet (*Star Wars d20 RCR*) | Équivalent KotOR 2 |
| :--- | :---: | :---: | :---: | :--- | :--- | :--- |
| **Affect Mind**<br>*(Affecter l'esprit)* | **CHA** | Non | **2 ou 4 VP** | Attaque | Le fameux *"Jedi Mind Trick"* sur une cible vivante à moins de 10 m. Le résultat du test fixe le **DD du jet de Volonté** de la cible (`DD 10` à `DD 25`) :<br>• **Illusion auditive / Distraction (2 VP) :** Fait croire à un bruit ou détourne l'attention.<br>• **Suggestion (4 VP) :** Convainc la cible d'une affirmation raisonnable (*"Ce ne sont pas ces droïdes-là que vous cherchez"*). | *Affecter l'esprit / Dominer l'esprit* & *Confusion* |
| **Friendship**<br>*(Amitié)* | **CHA** | Non | **2 VP** | Complète | Calme l'agressivité d'une créature ou d'un PNJ non-engagé en combat et améliore son attitude (d'Hostile/Inamical vers Indifférent/Amical) selon le test opposant le jet de Volonté de la cible. | *Confusion / Apaisement animal* |
| **Illusion**<br>*(Illusion de Force)* | **CHA** | Non | **3 VP + 1/rd** | Complète | Crée une illusion visuelle et sonore ou projette un double illusoire du Jedi (DD de Volonté basé sur le test). Nécessite *Control + Sense + Alter*. | *Confusion de l'esprit* |
| **Force Push**<br>*(Poussée de Force)* | **INT** | Non | **1 à 5 VP** | Attaque | Projette violemment une cible à moins de 10 m. Le test fixe le **DD du jet de Force/Réflexes** de la cible (`DD 10` à `DD 25`).<br>En cas d'échec, la cible est repoussée de **2 m à 10 m**, tombe au sol (**Prone**) et subit **`1d6` à `3d6` dégâts** si elle percute un mur ou un obstacle ! | *Poussée de Force / Tourbillon / Vague de Force* |
| **Force Strike**<br>*(Frappe de Force)* | **INT** | Non | **2 VP** | Attaque | Onde de choc télékinétique projetée en cône ou sur une cible à 10 m.<br>Inflige **`3d4` dégâts de Vitalité** (ou `3d6` avec le don *Advanced Force Strike*). Le résultat du test fixe le **DD du jet de Réflexes** (`DD 10` à `DD 25`) pour réduire les dégâts de moitié. | *Vague de Force* (dégâts directs) |
| **Move Object**<br>*(Déplacement d'objet / Télékinésie)* | **INT** | Non | **1 à 20 VP** | Attaque | Soulever et projeter des objets ou des ennemis jusqu'à 10 m :<br>• **DD 10 (1 VP) :** Objet jusqu'à 5 kg (inflige `1d6` dégâts si lancé).<br>• **DD 15 (2 VP) :** Jusqu'à 50 kg (`2d6` dégâts).<br>• **DD 20 (4 VP) :** Jusqu'à 500 kg / un ennemi humain (`4d6` dégâts).<br>• **DD 25 (8 VP) :** Jusqu'à 5 tonnes / un chasseur spatial (`6d6` dégâts).<br>• **DD 30 (12 VP) :** Jusqu'à 10 tonnes (`8d6` dégâts). | *Tourbillon de Force* & *Lancer de sabre* |
| **Heal Another**<br>*(Soigner autrui)* | **SAG** | Non | **1 à 6 VP** | Complète | Nécessite *Control + Alter*. Permet de soigner un allié au toucher :<br>• **DD 10 (1 VP) :** Soigne `1d6` VP.<br>• **DD 15 (2 VP) :** Soigne `2d6` VP.<br>• **DD 20 (4 VP) :** Soigne `3d6` VP (ou `1d4` *Wound Points*).<br>• **DD 25 (6 VP) :** Soigne `4d6` VP (ou `2d4` *Wound Points*). | *Guérison (Heal)* (qui soigne tout le groupe dans KotOR) |
| **Plant Surge**<br>*(Croissance végétale)* | **INT** | Non | **1 VP** | Attaque | *(Supplément)* Fait surgir des plantes qui enchevêtrent les ennemis dans un rayon de 2 à 8 m (jet de Réflexes `DD 10` à `25` ou immobilisé, `-2` attaque et `-4` DEX). | *Stase / Champ de stase* |

---

## 5. Pouvoirs du Côté Obscur (*Dark Side Skills*)

Dans *Star Wars d20*, utiliser ces pouvoirs d'attaque pure ou de terreur fait automatiquement gagner un **Point du Côté Obscur (*Dark Side Point*)** (ou est réservé aux Sith/Jedi sombres). Aucun ne subit de malus d'armure.

| Pouvoir (*Force Skill*) | Caract. Clé | Malus Armure | Coût VP | Action | Descriptif & Échelle d'Effet (*Star Wars d20 RCR*) | Équivalent KotOR 2 |
| :--- | :---: | :---: | :---: | :--- | :--- | :--- |
| **Fear**<br>*(Peur)* | **SAG** | Non | **2 VP** | Attaque | Nécessite *Sense*. Inspire une terreur surnaturelle à une cible à moins de 10 m pendant `1d4` rounds. La cible subit un malus de **`-2` à `-10`** (selon le test : DD 10 = `-2`, DD 15 = `-4`, DD 20 = `-6`, DD 25 = `-8`, DD 30 = `-10`) à tous ses jets d'attaque, de sauvegarde et de compétence ! | *Peur / Horreur / Folie* |
| **Force Grip**<br>*(Étranglement de Force)* | **INT** | Non | **4 VP / rd** | Attaque *(Maintien)* | Nécessite *Control + Alter*. Étrangle une cible vivante à moins de 10 m.<br>Le résultat du test fixe le **DD du jet de Volonté** (`DD 10` à `DD 25`).<br>• **Si la cible échoue :** Elle subit **`3d6` dégâts** par round **ET est immobilisée/étouffée** (ne peut faire aucune action !).<br>• **Si la cible réussit :** Elle subit la moitié des dégâts (`3d6 / 2`) et peut agir normalement. | *Blessure / Étranglement / Mise à mort (Kill)* |
| **Force Lightning**<br>*(Éclairs de Force)* | **INT** | Non | **6 VP** | Attaque | Nécessite *Control + Alter*. Projette un arc d'éclairs du Côté Obscur sur une cible à moins de 10 m.<br>• Inflige **`3d8` dégâts d'énergie**.<br>• Le résultat du test fixe le **DD du jet de Réflexes** (`DD 10` à `DD 25`) de la cible : si elle échoue, elle subit la totalité des dégâts et est **étourdie (*Dazed*) pendant 1 round** ; si elle réussit, elle subit la moitié des dégâts. | *Choc / Éclair de Force / Tempête de Force* |
| **Drain Energy**<br>*(Drain d'énergie)* | **INT** | Non | **1 à 4 VP** | Complexe | Nécessite *Control + Sense + Alter*. Draine l'énergie électrique d'un blaster, d'un droïde ou d'un générateur (DD 10 à 20) pour recharger la Vitalité du lanceur ou désactiver l'arme/droïde. | *Désactivation / Destruction de droïde* & *Drain de Force* |
| **Drain Knowledge**<br>*(Drain de savoir)* | **INT** | Non | **4 VP** | Complète | *(Dark Side Sourcebook)* Arrache par la force un souvenir ou une compétence de l'esprit d'une cible (opposé à un jet de Volonté ou DD 20) et inflige `1d4` dégâts de Sagesse temporaires. | *Drain de Force* / *Écrasement de Force* |
| **Transfer Essence**<br>*(Transfert d'essence)* | **INT** | Non | Spécial | Rituel | *(Dark Side Sourcebook)* Permet à un Seigneur Sith mourant de transférer son esprit dans un clone ou de consumer des vies pour survivre (jet de Volonté DD 25+). | Capacité de Sion / Nihilus (*Champ de mort*) |
