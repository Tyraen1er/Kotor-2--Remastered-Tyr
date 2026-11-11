# État des Lieux Défensif des Ennemis — Immunités, Résistances, Dons défensifs

> Extrait de **tous les templates de créatures hostiles** (`FactionID = 1`) des fichiers du jeu
> (chitin.key + modules, installation telle que jouée) par [`tools/extract_enemies.py`](file:///C:/Users/emman/Desktop/dev/Kotor%202%20Mods/tools/extract_enemies.py).
> Compagnon de [`ennemis_reference_kotor2.md`](ennemis_reference_kotor2.md) (autobalance, PV/CA des boss).
> **Limites :** les bonus appliqués par scripts (`OnSpawn`, dialogues) ne sont pas comptés ; stats des templates *avant* scaling autobalance.

## 1. Vue d'ensemble

- **313** templates hostiles : **229** organiques + **84** droïdes (27 %).
- **115/313 (37 %)** n'ont **aucune** défense identifiée (ni don, ni immunité, ni résistance).
- Chez les **organiques** seulement : **114/229 (50 %)** sans rien ;
  **115** ont au moins un élément défensif (souvent un simple don de port d'armure).
- **Armures réellement portées : 15 pièces** sur l'ensemble des 313 templates — la quasi-totalité combat à CA naturelle.

## 2. Dons défensifs recensés (fréquence)

| Don défensif | Ennemis | % des hostiles |
| :-- | :--: | :--: |
| Port d'armure intermédiaire | 102 | 33 % |
| Port d'armure lourde | 102 | 33 % |
| Port d'armure légère | 102 | 33 % |
| Déviation de tirs (Jedi) | 28 | 9 % |
| PV/RD (Robustesse) | 14 | 4 % |
| Esquive instinctive I | 11 | 4 % |
| Déviation de tirs (avancée) | 6 | 2 % |
| Esquive instinctive II | 3 | 1 % |
| Déviation de tirs (maîtrise) | 3 | 1 % |

> Les « Port d'armure L/I/L » (102 templates, soldats) sont des dons de **classe**, mais seuls ~15 portent réellement une armure.

## 3. Immunités & résistances d'équipement

| Immunité (objet) | Ennemis | Portés par |
| :-- | :--: | :-- |
| Poison | 88 | `g_i_crhide008` ×61, `g_i_crhide015` ×15, `a_helmet_02` ×6 |
| MindSpells | 82 | `g_i_crhide008` ×61, `g_i_crhide015` ×15, `g_i_crhide001` ×4 |
| Paralysis | 82 | `g_i_crhide008` ×61, `g_i_crhide015` ×15, `g_i_crhide001` ×4 |
| Critical_Hits | 1 | `a_light_08` ×1 |

**Résistances aux dégâts d'équipement : 7 ennemis sur 313 (2 %)** — essentiellement des peaux de droïde (`Résist 15/-` physique).

## 4. Droïdes : la seule « adaptation forcée » du jeu

Les droïdes cumulent **trois couches d'immunités** :
1. **Raciales moteur** (vérifications `GetRacialType != RACIAL_TYPE_DROID` dans `k_inc_force.nss`) : esprit (*Peur, Folie, Stase, Dominance*), poison, drain de vie/Force, ligne *Blessure/Étranglement* ;
2. **Peaux de droïde** (`g_i_crhide008` ×61, etc.) : *Immunité Esprit + Paralysie + Poison* — redondant avec le moteur ;
3. Certaines peaux d'assaut ajoutent `Résist 15/-` contondant/perforant/tranchant.

→ Face aux droïdes, le joueur **doit** changer de plan (pouvoirs Biologiques inutiles, *Destruction de droïde* devient requis).
**84 templates** concernés (27 % des hostiles) — mais la réponse est *binaire* : droïde ou pas.

## 5. Boss & duels notables — profils défensifs détaillés

*(Y compris les UTC non hostiles au sens strict — compagnons/duels scriptés hostiles — identifiés par nom.)*

**909sion** (`909sion`) — Organique, CR 22, niv. 5, CA naturelle 0
- Dons défensifs : Déviation de tirs (Jedi), Déviation de tirs (avancée), Déviation de tirs (maîtrise), Dévier sans sabre
- Immunités (dons + objets) : Déviation de tirs (Jedi), Déviation de tirs (avancée), Déviation de tirs (maîtrise), Dévier sans sabre
- Résistances objets : —
- Équipement : Lightsaber (g_w_drkjdisbr001)

**DarthNihilus** (`n_darthnihilu001`) — Organique, CR 20, niv. 1, CA naturelle 0
- Dons défensifs : Déviation de tirs (Jedi), Déviation de tirs (avancée)
- Immunités (dons + objets) : Déviation de tirs (Jedi), Déviation de tirs (avancée)
- Résistances objets : —
- Équipement : Jedi_Master_Robe (a_robe_18), Lightsaber (g_w_lghtsbr02)

**DarthSion** (`n_darthsion`) — Organique, CR 20, niv. 20, CA naturelle 0
- Dons défensifs : Déviation de tirs (Jedi), Déviation de tirs (avancée), Déviation de tirs (maîtrise)
- Immunités (dons + objets) : Déviation de tirs (Jedi), Déviation de tirs (avancée), Déviation de tirs (maîtrise)
- Résistances objets : —
- Équipement : Lightsaber (g_w_drkjdisbr001)

**Atris** (`n_darthtraya001`) — Organique, CR 20, niv. 1, CA naturelle 0
- Dons défensifs : Déviation de tirs (Jedi), Déviation de tirs (avancée), Dévier sans sabre, Immunité mentale (Peur)
- Immunités (dons + objets) : Déviation de tirs (Jedi), Déviation de tirs (avancée), Dévier sans sabre, Immunité mentale (Peur)
- Résistances objets : —
- Équipement : —

**KreiaEvil** (`p_kreia_evil`) — Organique, CR 20, niv. 20, CA naturelle 0
- Dons défensifs : — AUCUN —
- Immunités (dons + objets) : — AUCUNE —
- Résistances objets : —
- Équipement : Basic_Clothing (g_a_clothes01)

**KraytDragon** (`c_kraytdragon`) — Organique, CR 20, niv. 20, CA naturelle 23
- Dons défensifs : — AUCUN —
- Immunités (dons + objets) : — AUCUNE —
- Résistances objets : —
- Équipement : Creature_Item_Slash (g_w_crslash006), Creature_Item_Slash (g_w_crslash006)

**Rancor** (`c_rancor`) — Organique, CR 20, niv. 20, CA naturelle 17
- Dons défensifs : — AUCUN —
- Immunités (dons + objets) : — AUCUNE —
- Résistances objets : —
- Équipement : Creature_Item_Slash (g_w_crslash006), Creature_Item_Slash (g_w_crslash006)

**StormBeastG** (`c_stormbeast003`) — Organique, CR 20, niv. 1, CA naturelle 0
- Dons défensifs : Esquive instinctive I, Esquive instinctive II
- Immunités (dons + objets) : Esquive instinctive I, Esquive instinctive II
- Résistances objets : —
- Équipement : Creature_Item_Slash (g_w_crslash006), Creature_Item_Slash (g_w_crslash006)

**StormBeastGBoss** (`c_stormbeast004`) — Organique, CR 20, niv. 1, CA naturelle 0
- Dons défensifs : Esquive instinctive I, Esquive instinctive II
- Immunités (dons + objets) : Esquive instinctive I, Esquive instinctive II
- Résistances objets : —
- Équipement : Creature_Item_Slash (g_w_crslash006), Creature_Item_Slash (g_w_crslash006)

**g_kraytdragon01** (`g_kraytdragon01`) — Organique, CR 20, niv. 20, CA naturelle 23
- Dons défensifs : — AUCUN —
- Immunités (dons + objets) : — AUCUNE —
- Résistances objets : —
- Équipement : Creature_Item_Slash (g_w_crslash006), Creature_Item_Slash (g_w_crslash006)

**g_rancor01** (`g_rancor002`) — Organique, CR 20, niv. 20, CA naturelle 17
- Dons défensifs : — AUCUN —
- Immunités (dons + objets) : — AUCUNE —
- Résistances objets : —
- Équipement : Creature_Item_Slash (g_w_crslash006), Creature_Item_Slash (g_w_crslash006)

**DarthMalak** (`n_darthmalak`) — Organique, CR 20, niv. 20, CA naturelle 0
- Dons défensifs : Déviation de tirs (Jedi), Déviation de tirs (avancée)
- Immunités (dons + objets) : Déviation de tirs (Jedi), Déviation de tirs (avancée)
- Résistances objets : —
- Équipement : Lightsaber (g_w_lghtsbr02)

**DarthRevan** (`n_darthrevan`) — Organique, CR 20, niv. 20, CA naturelle 0
- Dons défensifs : Déviation de tirs (Jedi), Déviation de tirs (avancée), Déviation de tirs (maîtrise)
- Immunités (dons + objets) : Déviation de tirs (Jedi), Déviation de tirs (avancée), Déviation de tirs (maîtrise)
- Résistances objets : —
- Équipement : Lightsaber (g_w_drkjdisbr001)

**n_darthrevan002** (`n_darthrevan002`) — Organique, CR 20, niv. 20, CA naturelle 0
- Dons défensifs : Déviation de tirs (Jedi), Déviation de tirs (avancée), Déviation de tirs (maîtrise)
- Immunités (dons + objets) : Déviation de tirs (Jedi), Déviation de tirs (avancée), Déviation de tirs (maîtrise)
- Résistances objets : —
- Équipement : —

**DarthTraya** (`n_darthtraya`) — Organique, CR 20, niv. 20, CA naturelle 0
- Dons défensifs : Déviation de tirs (Jedi), Déviation de tirs (avancée)
- Immunités (dons + objets) : Déviation de tirs (Jedi), Déviation de tirs (avancée)
- Résistances objets : —
- Équipement : Lightsaber (g_w_lghtsbr02)

**G_DARKJEDI04** (`g_darkjedi04`) — Organique, CR 16, niv. 16, CA naturelle 0
- Dons défensifs : Déviation de tirs (Jedi), Déviation de tirs (avancée)
- Immunités (dons + objets) : Déviation de tirs (Jedi), Déviation de tirs (avancée)
- Résistances objets : —
- Équipement : Lightsaber (g_w_lghtsbr02)

**StormBeast** (`c_stormbeast002`) — Organique, CR 15, niv. 1, CA naturelle 0
- Dons défensifs : Esquive instinctive I
- Immunités (dons + objets) : Esquive instinctive I
- Résistances objets : —
- Équipement : Creature_Item_Slash (g_w_crslash013), Creature_Item_Slash (g_w_crslash013)

## 6. Verdict — pourquoi le combat ne s'adapte jamais

1. **50 % des ennemis organiques n'ont aucun profil défensif** (pas d'immunité, pas de résistance, pas de don défensif utile).
2. Les seules immunités de masse sont **raciales et binaires** : droïde ou organique. Aucun spectre intermédiaire.
3. Les résistances d'équipement sont anecdotiques (peaux de droïde mises à part) et les immunités d'objets organiques se comptent **en unités** (quelques casques `a_helmet_02`).
4. Les boss majeurs (Traya, Nihilus, Jedi obscurs) ne portent **aucun objet défensif** : leur résistance vient uniquement de l'autobalance (PV/CA/sauvegardes) — jamais d'une mécanique à contourner.
5. **Conséquence gameplay** : la réponse optimale est *toujours la même* — même pouvoir, même type de dégâts, du Péragus à Malachor. Rien n'incite à :
   - diversifier les types de dégâts (aucune résistance sélective),
   - préparer un anti-soin (aucun boss ne se soigne),
   - contourner une immunité (sauf droïdes),
   - gérer une phase de bouclier (aucun boss n'active de bouclier énergétique scripté).

## 7. Ce que ça implique pour l'overhaul (pistes, non décisions)

- Donner des **profils défensifs thématiques par faction** (Sith = immunités mentales partielles + Résistance à la Force ; Mandaloriens = armures réelles + boucliers ; bêtes = RD physique ; assassins = Esquive).
- Utiliser les **leviers déjà existants** : peaux de créature (immunités/RD), `EffectForceResistance`, boucliers énergétiques scriptés, RD physique (nos boss `3/7/12` actés).
- Étendre la logique droïde à d'autres « familles » sans la copier binairement : résistances *partielles* (50 %) plutôt qu'immunités totales.
- Notre *Esquive Totale* accordée aux Jedi/Sith 20+ (décision §7) est déjà un premier pas : les AoE perdent de la valeur contre les élites.
