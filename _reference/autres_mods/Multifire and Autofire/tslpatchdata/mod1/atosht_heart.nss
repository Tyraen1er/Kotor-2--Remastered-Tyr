//////////////////////////////////////////////////////////////////////////////////
/*	Multifire and Autofire

	This is the main heartbeat for Multifire and Autofire
	
	It is fired by k_ai_master on all henchmen
	
	It determines all of the bonuses and penalties when using
	certain weapons and feats, and adds them to a unified effect
	
	darthbdaman 2025-09-20														*/
//////////////////////////////////////////////////////////////////////////////////

int FEAT_AUTO_SHOT = #2DAMEMORY1#;
int FEAT_IMPROVED_AUTO_SHOT = #2DAMEMORY2#;
int FEAT_MASTER_AUTO_SHOT = #2DAMEMORY3#;
int FEAT_SUPER_WEAPON_FOCUS_BLASTER_1 = #2DAMEMORY4#;
int FEAT_SUPER_WEAPON_FOCUS_BLASTER_2 = #2DAMEMORY5#;
int FEAT_SUPER_WEAPON_FOCUS_BLASTER_3 = #2DAMEMORY6#;
int FEAT_SUPER_WEAPON_FOCUS_BLASTER_RIFLE_1 = #2DAMEMORY7#;
int FEAT_SUPER_WEAPON_FOCUS_BLASTER_RIFLE_2 = #2DAMEMORY8#;
int FEAT_SUPER_WEAPON_FOCUS_BLASTER_RIFLE_3 = #2DAMEMORY9#;
int FEAT_SUPER_WEAPON_FOCUS_MELEE_WEAPONS_1 = #2DAMEMORY10#;
int FEAT_SUPER_WEAPON_FOCUS_MELEE_WEAPONS_2 = #2DAMEMORY11#;
int FEAT_SUPER_WEAPON_FOCUS_MELEE_WEAPONS_3 = #2DAMEMORY12#;
int FEAT_SUPER_DUELING_1 = #2DAMEMORY13#;
int FEAT_SUPER_DUELING_2 = #2DAMEMORY14#;
int FEAT_SUPER_DUELING_3 = #2DAMEMORY15#;
int FEAT_SUPER_AUTO_SHOT_1 = #2DAMEMORY16#;
int FEAT_SUPER_AUTO_SHOT_2 = #2DAMEMORY17#;
int FEAT_SUPER_AUTO_SHOT_3 = #2DAMEMORY18#;

void main() {

//Strip the Permanent Extraordinary Concealment Effect from this character (along with all linked effects)
	effect eEffect = GetFirstEffect(OBJECT_SELF);
	while(GetIsEffectValid(eEffect))
	{
		if((GetEffectType(eEffect)) == EFFECT_TYPE_CONCEALMENT){
			if (GetEffectSubType(eEffect) == SUBTYPE_EXTRAORDINARY){
				if ((GetEffectDurationType(eEffect) == DURATION_TYPE_PERMANENT)){
					RemoveEffect(OBJECT_SELF, eEffect);
				}
			}
		}
		eEffect = GetNextEffect(OBJECT_SELF);
	}

//Determine current weapon type
	object oItem = GetItemInSlot(INVENTORY_SLOT_RIGHTWEAPON, OBJECT_SELF);
	object oItem2 = GetItemInSlot(INVENTORY_SLOT_LEFTWEAPON, OBJECT_SELF);
	int iItemType = GetBaseItemType(oItem);
	int iItemType2 = GetBaseItemType(oItem2);

	int iWeapon;
	
	if ((iItemType == BASE_ITEM_REPEATING_BLASTER) || (iItemType == BASE_ITEM_HEAVY_REPEATING_BLASTER)) {
		iWeapon = 8;
	}
	else if ((iItemType == BASE_ITEM_ION_RIFLE) || (iItemType == BASE_ITEM_BOWCASTER) || (iItemType == BASE_ITEM_BLASTER_CARBINE) || (iItemType == BASE_ITEM_DISRUPTER_RIFLE) || (iItemType == BASE_ITEM_SONIC_RIFLE) || (iItemType == BASE_ITEM_BLASTER_RIFLE)) {
		iWeapon = 7;
	}
	else if ((iItemType == BASE_ITEM_BLASTER_PISTOL) || (iItemType == BASE_ITEM_HEAVY_BLASTER) || (iItemType == BASE_ITEM_HOLD_OUT_BLASTER) || (iItemType == BASE_ITEM_ION_BLASTER) || (iItemType == BASE_ITEM_DISRUPTER_PISTOL)  || (iItemType == BASE_ITEM_SONIC_PISTOL)) {
		iWeapon = 6;
	}
	else if ((iItemType == BASE_ITEM_QUARTER_STAFF) || (iItemType == BASE_ITEM_DOUBLE_BLADED_SWORD) || (iItemType == BASE_ITEM_VIBRO_DOUBLE_BLADE) || (iItemType == BASE_ITEM_GHAFFI_STICK) || (iItemType == BASE_ITEM_WOOKIE_WARBLADE) || (iItemType == BASE_ITEM_FORCE_PIKE)) {
		iWeapon = 5;
	}
	else if ((iItemType == BASE_ITEM_LONG_SWORD) || (iItemType == BASE_ITEM_VIBRO_SWORD) || (iItemType == BASE_ITEM_SHORT_SWORD) || (iItemType == BASE_ITEM_VIBRO_BLADE) || (iItemType == BASE_ITEM_GAMMOREAN_BATTLEAXE)) {
		iWeapon = 4;
	}
	else if (iItemType == BASE_ITEM_DOUBLE_BLADED_LIGHTSABER) {
		iWeapon = 3;
	}
	else if ((iItemType == BASE_ITEM_LIGHTSABER) || (iItemType == BASE_ITEM_SHORT_LIGHTSABER)) {
		iWeapon = 2;
	}
	else if ((iItemType == BASE_ITEM_INVALID) && (iItemType2 == BASE_ITEM_INVALID)) {
		iWeapon = 1;
	}

	int iAttacks = 0;
	int iAttackBonus = 0;
//	int iDamageBonus = 0;
	int iDamage1d4Bonus = 0;
	int iDefenseBonus = 0;
	
//If rifle or repeater
	if (iWeapon >= 7){
		if ((GetHasSpellEffect(FORCE_POWER_SPEED_MASTERY)) || (GetHasSpellEffect(FORCE_POWER_MASTER_FURY)) || (GetHasSpellEffect(FORCE_POWER_WOOKIEE_RAGE_III)) || ((GetHasSpellEffect(FORCE_POWER_FORCE_ENLIGHTENMENT)) && (GetSpellAcquired(FORCE_POWER_SPEED_MASTERY, OBJECT_SELF)))){
			iAttacks += 2;
		}
		else if ((GetHasSpellEffect(FORCE_POWER_KNIGHT_SPEED)) || (GetHasSpellEffect(FORCE_POWER_IMPROVED_FURY)) || (GetHasSpellEffect(FORCE_POWER_WOOKIEE_RAGE_II)) || ((GetHasSpellEffect(FORCE_POWER_FORCE_ENLIGHTENMENT)) && (GetSpellAcquired(FORCE_POWER_KNIGHT_SPEED, OBJECT_SELF)))){
			iAttacks += 1;
		}

		if (GetHasFeat(FEAT_SUPER_AUTO_SHOT_3, OBJECT_SELF)){
			iAttackBonus += 8;
		}
		else if (GetHasFeat(FEAT_SUPER_AUTO_SHOT_2, OBJECT_SELF)){
			iAttackBonus += 6;
		}
		else if (GetHasFeat(FEAT_SUPER_AUTO_SHOT_1, OBJECT_SELF)){
			iAttackBonus += 5;
		}
		else if (GetHasFeat(FEAT_MASTER_AUTO_SHOT, OBJECT_SELF)){
			iAttackBonus += 4;
		}
		else if (GetHasFeat(FEAT_IMPROVED_AUTO_SHOT, OBJECT_SELF)){
			iAttackBonus += 3;
		}
		else if (GetHasFeat(FEAT_AUTO_SHOT, OBJECT_SELF)){
			iAttackBonus += 2;
		}

		if (GetHasFeat(FEAT_SUPER_WEAPON_FOCUS_BLASTER_RIFLE_3, OBJECT_SELF)){
			iAttackBonus += 3;
		}
		else if (GetHasFeat(FEAT_SUPER_WEAPON_FOCUS_BLASTER_RIFLE_2, OBJECT_SELF)){
			iAttackBonus += 2;
		}
		else if (GetHasFeat(FEAT_SUPER_WEAPON_FOCUS_BLASTER_RIFLE_1, OBJECT_SELF)){
			iAttackBonus += 1;
		}

//If repeater
		if (iWeapon == 8){
			if (iAttacks >= 2){}
			else if (iAttacks >= 1){
				iAttacks += 1;
				iAttackBonus -= 4;
			}
			else {
				iAttacks += 2;
				iAttackBonus -= 6;
			}
		}
//If rifle //Removed with Option 2
/*		else if (iWeapon == 7)
		{
			if (iAttacks >= 2) {}
			else {
				iAttacks += 1;
				iAttackBonus -= 4;
			}
		}*/
	}
//If blaster Pistol
	else if (iWeapon == 6){
		if (GetHasFeat(FEAT_SUPER_WEAPON_FOCUS_BLASTER_3, OBJECT_SELF)){
			iAttackBonus += 3;
		}
		else if (GetHasFeat(FEAT_SUPER_WEAPON_FOCUS_BLASTER_2, OBJECT_SELF)){
			iAttackBonus += 2;
		}
		else if (GetHasFeat(FEAT_SUPER_WEAPON_FOCUS_BLASTER_1, OBJECT_SELF)){
			iAttackBonus += 1;
		}
	}
//If melee weapons
	else if (iWeapon >= 4){
		if (GetHasFeat(FEAT_SUPER_WEAPON_FOCUS_MELEE_WEAPONS_3, OBJECT_SELF)){
			iAttackBonus += 3;
		}
		else if (GetHasFeat(FEAT_SUPER_WEAPON_FOCUS_MELEE_WEAPONS_2, OBJECT_SELF)){
			iAttackBonus += 2;
		}
		else if (GetHasFeat(FEAT_SUPER_WEAPON_FOCUS_MELEE_WEAPONS_1, OBJECT_SELF)){
			iAttackBonus += 1;
		}
	}
//If lightsaber, subtract difference between str and dex, if we have finesse melee, but not lightsaber
	else if (iWeapon >= 2){
		if (!(GetHasFeat(FEAT_FINESSE_LIGHTSABERS, OBJECT_SELF)) && (GetHasFeat(FEAT_FINESSE_MELEE_WEAPONS, OBJECT_SELF))){
			int iSTR = GetAbilityModifier(ABILITY_STRENGTH, OBJECT_SELF);
			int iDEX = GetAbilityModifier(ABILITY_DEXTERITY, OBJECT_SELF);

			if (iDEX > iSTR){
				iDEX -= iSTR;
				iAttackBonus -= iDEX;
			}
		}
	}
//If unarmed, add difference between str and dex, if we have either finesse
	else if (iWeapon >= 1){
		if ((GetHasFeat(FEAT_FINESSE_LIGHTSABERS, OBJECT_SELF)) || (GetHasFeat(FEAT_FINESSE_MELEE_WEAPONS, OBJECT_SELF))){
			int iSTR = GetAbilityModifier(ABILITY_STRENGTH, OBJECT_SELF);
			int iDEX = GetAbilityModifier(ABILITY_DEXTERITY, OBJECT_SELF);

			if (iDEX > iSTR){
				iDEX -= iSTR;
				iAttackBonus += iDEX;
			}
		}
	}
//If one handed or unarmed, add superior dueling
	if (iItemType2 == BASE_ITEM_INVALID) {
		if ((iWeapon == 6) || (iWeapon == 4) || (iWeapon == 2) || (iWeapon == 1)){
			if (GetHasFeat(FEAT_SUPER_DUELING_3, OBJECT_SELF)){
				iAttackBonus += 3;
				iDamage1d4Bonus += 3;
				iDefenseBonus += 3;
			}
			else if (GetHasFeat(FEAT_SUPER_DUELING_2, OBJECT_SELF)){
				iAttackBonus += 2;
				iDamage1d4Bonus += 2;
				iDefenseBonus += 2;
			}
			else if (GetHasFeat(FEAT_SUPER_DUELING_1, OBJECT_SELF)){
				iAttackBonus += 1;
				iDamage1d4Bonus += 1;
				iDefenseBonus += 1;
			}
		}
	}

//Init the effect with an unused miss chance effect. This lets us identify the attacks affect later, which would normally be impossible
	eEffect = EffectMissChance(1);
	if (iAttacks >= 1){
//Cap attacks to 2 for EffectModifyAttacks. It does not work properly with values over 2
		if (iAttacks >= 2){
			iAttacks = 2;
		}
//Force speed will interfere with the attack effect, so we just always apply 2 if it is active
		else if ((GetHasSpellEffect(FORCE_POWER_SPEED_MASTERY)) || (GetHasSpellEffect(FORCE_POWER_KNIGHT_SPEED)) || (GetHasSpellEffect(FORCE_POWER_MASTER_FURY)) || (GetHasSpellEffect(FORCE_POWER_IMPROVED_FURY)) || (GetHasSpellEffect(FORCE_POWER_WOOKIEE_RAGE_III)) || (GetHasSpellEffect(FORCE_POWER_WOOKIEE_RAGE_II)) || ((GetHasSpellEffect(FORCE_POWER_FORCE_ENLIGHTENMENT)) && ((GetSpellAcquired(FORCE_POWER_SPEED_MASTERY, OBJECT_SELF)) || (GetSpellAcquired(FORCE_POWER_KNIGHT_SPEED, OBJECT_SELF))))) {
			iAttacks = 2;
		}
		eEffect = EffectLinkEffects(eEffect, EffectModifyAttacks(iAttacks));
	}
//Invert the attack bonus if it is negative
	if (iAttackBonus >= 1){
		eEffect = EffectLinkEffects(eEffect, EffectAttackIncrease(iAttackBonus));
	}
	else if (iAttackBonus <= -1){
		iAttackBonus = iAttackBonus * -1;
		eEffect = EffectLinkEffects(eEffect, EffectAttackDecrease(iAttackBonus));
	}
//Invert the damage bonus if it is negative
/*	if (iDamageBonus >= 1){
		//Damage Bonus isn't actually a number, its a lookup on the damagecost table
		while (iDamageBonus >= 1) {
			eEffect = EffectLinkEffects(eEffect, EffectDamageIncrease(DAMAGE_BONUS_1));
			iDamageBonus -= 1;
		}
	}
	else if (iDamageBonus <= -1){
		iDamageBonus = iDamageBonus * -1;
		//Damage Bonus isn't actually a number, its a lookup on the damagecost table
		while (iDamageBonus >= 1) {
			eEffect = EffectLinkEffects(eEffect, EffectDamageIncrease(DAMAGE_BONUS_1));
			iDamageBonus -= 1;
		}
	}*/
//Invert the damage bonus if it is negative
	if (iDamage1d4Bonus >= 1){
		//Damage Bonus isn't actually a number, its a lookup on the damagecost table
		while (iDamage1d4Bonus >= 1) {
			eEffect = EffectLinkEffects(eEffect, EffectDamageIncrease(DAMAGE_BONUS_1d4));
			iDamage1d4Bonus -= 1;
		}
	}
	else if (iDamage1d4Bonus <= -1){
		iDamage1d4Bonus = iDamage1d4Bonus * -1;
		//Damage Bonus isn't actually a number, its a lookup on the damagecost table
		while (iDamage1d4Bonus >= 1) {
			eEffect = EffectLinkEffects(eEffect, EffectDamageIncrease(DAMAGE_BONUS_1d4));
			iDamage1d4Bonus -= 1;
		}
	}
//Invert the defense bonus if it is negative. Applied as a shield enhancement bonus, so it should stack with anything else in the game
	if (iDefenseBonus >= 1){
		eEffect = EffectLinkEffects(eEffect, EffectACIncrease(iDefenseBonus, 3));
	}
	else if (iDefenseBonus <= -1){
		iDefenseBonus = iDefenseBonus * -1;
		eEffect = EffectLinkEffects(eEffect, EffectACDecrease(iDefenseBonus, 3));
	}
//The effect has to be applied on a delay, otherwise the EffectModifyAttacks will not function properly (at least in K1), if another EffectModifyAttacks was removed in the same script, which it always will be due to how this is written
	if(GetIsEffectValid(eEffect)){
		eEffect = ExtraordinaryEffect(eEffect);
		DelayCommand(0.0, ApplyEffectToObject(DURATION_TYPE_PERMANENT, eEffect, OBJECT_SELF));
	}

//Loop the script again. On henchmen it will be run 6 times per heartbeat call, which should even out to being every second
	int iReruns = GetRunScriptVar();
	if (iReruns >= 1){
		iReruns -= 1;
		DelayCommand(1.0, ExecuteScript("atosht_heart", OBJECT_SELF, iReruns));
	}
}