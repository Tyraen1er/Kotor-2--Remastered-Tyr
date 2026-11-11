# KotOR 2 Modding Workspace — Guide & Pièges Techniques (Pour Agents IA & Développeurs)

Ce dépôt contient l'environnement de développement CLI/Python pour créer des mods **Star Wars: Knights of the Old Republic II (TSL)**.
Ce document répertorie l'architecture de l'espace de travail ainsi que les **découvertes critiques et correctifs appliqués à `pykotor`** afin qu'aucun agent ne reproduise les bugs rencontrés lors de la mise en place.

---

## 1. Environnement & Chemins Clés

* **Installation du jeu (Steam) :** `C:\Program Files (x86)\Steam\steamapps\common\Knights of the Old Republic II`
  * Contient déjà un dossier `Override/` peuplé (TSLRCM / mods graphiques). **Toujours vérifier si un fichier `.2da` ou `.ncs` existe déjà dans `Override/` avant d'extraire la version vanilla de `chitin.key`.**
  * Utiliser `Installation.resource(resname, restype)` de `pykotor` (qui respecte l'ordre de priorité `Override` > `Modules` > `chitin.key`).
* **Environnement Python local :** `.venv\Scripts\python.exe` (Python 3.14 + `pykotor 2.3.12` patché).
* **Outil CLI maison :** [`tools/k2mod.py`](tools/k2mod.py)
  * Compiler un script `.nss` en `.ncs` :
    ```powershell
    .\.venv\Scripts\python.exe tools\k2mod.py compile chemin\vers\script.nss -o chemin\vers\script.ncs
    ```
  * Extraire une ressource du jeu (en respectant la priorité `Override`) :
    ```powershell
    .\.venv\Scripts\python.exe tools\k2mod.py extract <resname> <ext> -o <output_path>
    ```
* **Ressources de référence extraites (`_reference/`) :**
  * `_reference/scripts/` : Contient les 638 scripts `.nss` du jeu (`nwscript.nss`, `k_inc_force.nss`, `k_ai_master.nss`, `k_sp1_generic.nss`, etc.).
  * `_reference/2da/` : Contient les fichiers `.2da` et `.csv` de référence (`feat.2da`, `spells.2da`, `baseitems.2da`, `iprp_damagecost.2da`, `iprp_onhit.2da`).

---

## 2. Bugs Critiques de `pykotor` (v2.3.12) Identifiés et Corrigés dans `.venv`

> **⚠️ ATTENTION :** Si l'environnement virtuel `.venv` est recréé ou si `pykotor` est réinstallé via `pip`, **ces 4 bugs réapparaîtront** et casseront silencieusement les fichiers `.2da` ou les scripts `.ncs` en jeu. Vérifiez toujours qu'ils sont bien patchés dans `.venv\Lib\site-packages\pykotor\`.

### Bug #1 : Ordre des arguments inversé dans les appels moteur (`ACTION`) du compilateur NCS
* **Fichier :** `.venv\Lib\site-packages\pykotor\resource\formats\ncs\compiler\classes.py` (`EngineCallExpression.compile`, ~ligne 1341)
* **Symptôme en jeu :** Les scripts compilés cassent complètement le jeu (impossible d'interagir avec le loot au sol, IA figée, fonctions comme `GetHasFeat(245, oTarget)` ou `ExecuteScript("k_ai_master", OBJECT_SELF, 2001)` qui reçoivent leurs paramètres à l'envers).
* **Cause :** Dans le bytecode NWScript de l'Odyssey Engine, les arguments d'une instruction `ACTION` doivent être empilés **de droite à gauche** (du dernier paramètre au premier : `range(len(self._args) - 1, -1, -1)`). `pykotor` les empilait de gauche à droite (`range(len(self._args))`).
* **Correctif appliqué :** Boucle remplacée par `for i in range(len(self._args) - 1, -1, -1):`.

### Bug #2 : Prologue `JSR` manquant à l'octet 0 quand un script contient des variables globales
* **Fichier :** `.venv\Lib\site-packages\pykotor\resource\formats\ncs\compiler\classes.py` (`CodeRoot.compile`, ~ligne 393)
* **Symptôme en jeu :** Tout script ayant des variables globales (ou incluant `k_inc_switch.nss`, `k_inc_generic.nss`, `k_inc_force.nss`, comme `k_ai_master.ncs` ou `k_sp1_generic.ncs`) est silencieusement ignoré ou rejeté par la VM de KotOR 2.
* **Cause :** La VM de KotOR exige que l'instruction `0` d'un fichier `.ncs` soit **toujours** un `JSR` suivi à l'instruction `1` d'un `RETN`. Lorsqu'il y a des variables globales, l'instruction `0` doit faire `JSR` vers la routine d'initialisation des globales (instruction `2`), qui se termine par :
  ```text
  SAVEBP
  JSR -> main
  RESTOREBP
  MOVSP [-taille_globales]
  RETN
  ```
  Par défaut, `pykotor` plaçait directement `RSADDI` à l'instruction `0` sans `JSR` initial et oubliait `RESTOREBP` / `MOVSP`.
* **Correctif appliqué :** `CodeRoot.compile` génère désormais le prologue/épilogue complet exact attendu par l'Odyssey Engine.

### Bug #3 : Erreur de syntaxe sur les boucles `for ( ; condition; inc )` d'Obsidian
* **Fichier :** `.venv\Lib\site-packages\pykotor\resource\formats\ncs\compiler\parser.py` (`p_for_loop`, ~ligne 310)
* **Symptôme :** Échec de compilation (`Syntax error at line 1626, token=';'`) lorsqu'on compile un script qui inclut `k_inc_force.nss`.
* **Cause :** Les développeurs d'Obsidian ont écrit `int index = 0; for ( ; index < 3; ++index )` dans `k_inc_force.nss`. La grammaire Yacc/PLY de `pykotor` n'acceptait pas d'expression d'initialisation vide dans `for (...)`.
* **Correctif appliqué :** Ajout de la règle `| FOR_CONTROL '(' ';' expression ';' expression ')' '{' code_block '}'` dans `parser.py`.

### Bug #4 : Cellules vides lors de la lecture des fichiers binaires `.2da` (`V2.b`)
* **Fichier :** `.venv\Lib\site-packages\pykotor\resource\formats\twoda\io_twoda.py` (`TwoDABinaryReader.load`, ~ligne 165)
* **Symptôme :** `read_2da()` ou `pykotorcli 2da2csv` renvoie un tableau avec le bon nombre de lignes et de colonnes, mais **toutes les cellules sont vides (`""`)**.
* **Cause :** Le lecteur Kaitai (`_load_twoda_from_kaitai`) échoue silencieusement à lire les chaînes de caractères des offsets sans lever d'exception, empêchant le fallback vers `_load_twoda_legacy`.
* **Correctif appliqué :** `TwoDABinaryReader.load` utilise désormais directement `_load_twoda_legacy(BinaryReader.from_bytes(data, 0))`, qui lit parfaitement 100 % des `.2da` de KotOR 2.

### Bug #5 : Paramètre manquant `nOpponentPazaakDeck` dans la signature de `PlayPazaak`
* **Fichier :** `.venv\Lib\site-packages\pykotor\common\scriptdefs.py` (~lignes 6321 et 12669)
* **Symptôme :** `CompileError: Type mismatch for parameter 'oOpponent' in call to 'PlayPazaak'` lors de la compilation de tout script appelant `PlayPazaak(...)`.
* **Cause :** La liste `ScriptParam` de `PlayPazaak` omettait le premier paramètre `int nOpponentPazaakDeck`, décalant tous les arguments suivants.
* **Correctif appliqué :** Ajout de `ScriptParam(DataType.INT, "nOpponentPazaakDeck", None)` en tête de liste des paramètres pour K1 et K2.

---

## 3. Règles et Pièges Spécifiques au Moteur de KotOR 2 (Odyssey Engine)

### A. Création de Dons (`feat.2da`) et Effets Passifs
1. **`feat.2da` ne gère que l'interface et la sélection :**
   * Ajouter une ligne dans `feat.2da` (et ses StrRefs de nom/description dans `dialog.tlk`) permet d'afficher le don, ses prérequis et sa disponibilité au passage de niveau (`*_list = 1`, `*_granted = -1`, `pips = 1`).
   * **Important pour la fiche de personnage :** Dans KotOR 2, la liste des dons acquis d'un personnage est filtrée par `masterfeat` et `pips`, mais aussi par les colonnes de classe (`scd_list`, `sol_list`, etc.). Copiez toujours les colonnes de base d'un don fonctionnel (ex: ligne `194` `FINESSE_MELEE_WEAPONS`) avant de modifier les champs souhaités.
2. **Où coder l'effet d'un nouveau don passif ?**
   * Les dons vanilla ont leurs effets codés en dur dans `swkotor2.exe`.
   * Pour un nouveau don (ex: ID `245`), il faut vérifier `GetHasFeat(245, oTarget)` dans un script exécuté régulièrement.
   * **Point d'entrée universel :** Le joueur (`pc.utc`), les compagnons (`p_*.utc`) et les PNJ ont tous un script `ScriptHeartbeat` (`k_hen_heartbt01` ou `k_def_heartbt01`) qui appelle `ExecuteScript("k_ai_master", OBJECT_SELF, ...)`.
   * Placer une vérification au début de `void main()` dans `k_ai_master.nss` sur `OBJECT_SELF` et `GetFirstPC()` garantit que le bonus passif est appliqué automatiquement toutes les 6 secondes (et à chaque round de combat).
3. **Éviter le cumul infini des bonus passifs :**
   * Avant d'appliquer un effet `DURATION_TYPE_PERMANENT` + `ExtraordinaryEffect(eLink)` dans `k_ai_master`, **toujours parcourir `GetFirstEffect(oTarget)` / `GetNextEffect(oTarget)`** pour vérifier si l'effet (`EFFECT_TYPE_*` avec `SUBTYPE_EXTRAORDINARY` et `DURATION_TYPE_PERMANENT`) n'est pas déjà présent sur la créature.

### B. Fonctionnement de `EffectDamageIncrease` vs `DAMAGE_BONUS_*`
* **Piège classique :** Dans `nwscript.nss`, le commentaire au-dessus de `EffectDamageIncrease(int nBonus, ...)` mentionne `DAMAGE_BONUS_*` (qui sont les constantes de la table `iprp_damagecost.2da` où `1..5` = `+1..+5`, `6` = `1d4`, `10` = `2d6`).
* **Réalité dans KotOR 2 :**
  * Pour `EffectDamageIncrease(nBonus, DAMAGE_TYPE_*)` (comme utilisé par Obsidian dans `k_inc_force.nss` pour *Inspire Followers*), passer un entier direct comme `10` donne directement **+10 de dégâts fixes** sur la feuille de personnage !
  * De plus, deux effets `EffectDamageIncrease` du même type de dégâts ne se cumulent pas entre eux s'ils sont appliqués séparément (seul le plus élevé est retenu sur la feuille de personnage). Pour donner `+10`, il faut donc passer directement `EffectDamageIncrease(10, DAMAGE_TYPE_UNIVERSAL)`.

### C. Scripts `.nss` vs `.ncs` et Fichiers `#include`
* Le jeu n'exécute **que** les fichiers compilés `.ncs` présents dans `Override/` (ou dans les modules `.mod`/`.rim`).
* Les fichiers `k_inc_*.nss` (comme `k_inc_force.nss` ou `k_inc_combat.nss`) sont des bibliothèques (`#include`) sans fonction `main()`. Si vous modifiez `k_inc_force.nss` (par exemple pour rééquilibrer le pouvoir de Vitesse), vous devez compiler **`k_sp1_generic.nss` ➔ `k_sp1_generic.ncs`** et placer `k_sp1_generic.ncs` dans `Override/`.
