#include "k_inc_debug"
#include "k_inc_constant"
#include "k_inc_force"

int GetOverloadMod(object oWeapon)
{
	int nModifier = 0;
	int nBaseItem = GetBaseItemType(oWeapon);
	
	switch(nBaseItem)
	{
		case BASE_ITEM_BLASTER_PISTOL:
		case BASE_ITEM_HEAVY_BLASTER:
		case BASE_ITEM_HOLD_OUT_BLASTER:
		case BASE_ITEM_ION_BLASTER:
		case BASE_ITEM_DISRUPTER_PISTOL:
		case BASE_ITEM_SONIC_PISTOL:
			nModifier = 1;
			break;
		
		case BASE_ITEM_BLASTER_RIFLE:
		case BASE_ITEM_ION_RIFLE:
		case BASE_ITEM_BOWCASTER:
		case BASE_ITEM_BLASTER_CARBINE:
		case BASE_ITEM_DISRUPTER_RIFLE:
		case BASE_ITEM_SONIC_RIFLE:
			nModifier = 2;
			break;
			
		case BASE_ITEM_REPEATING_BLASTER:
		case BASE_ITEM_HEAVY_REPEATING_BLASTER:
			nModifier = 3;
			break;

		case BASE_ITEM_STUN_BATON:
			nModifier = 1;
			break;
			
		case BASE_ITEM_VIBRO_SWORD:
		case BASE_ITEM_VIBRO_BLADE:
			nModifier = 2;
			break;
		
		case BASE_ITEM_VIBRO_DOUBLE_BLADE:
			nModifier = 3;
			break;
	}
	
	return nModifier;
}

int GetOverloadDamage(object oWeapon)
{
	int nDamage = 10 + (GetOverloadMod(oWeapon)*10);
	
	nDamage += FeatDarkRage();
	
	return nDamage;
}

void OverloadWeapon(object oWeapon)
{
	DestroyObject(oWeapon);
	int nDamage = GetOverloadDamage(oWeapon);
		
	ApplyEffectAtLocation(DURATION_TYPE_INSTANT, EffectVisualEffect(3010),GetSpellTargetLocation());          

	object oTarget = GetFirstObjectInShape(SHAPE_SPHERE, 4.0, GetSpellTargetLocation());
	while(GetIsObjectValid(oTarget))
	{
		if(!GetIsNeutral(oTarget))
		{
			SignalEvent(oTarget, EventSpellCastAt(OBJECT_SELF, GetSpellId(), SWFP_HARMFUL));
			DelayCommand(0.1, ApplyEffectToObject(DURATION_TYPE_INSTANT, EffectDamage(nDamage, DAMAGE_TYPE_BLASTER), oTarget));
		}
			
		oTarget = GetNextObjectInShape(SHAPE_SPHERE, 4.0, GetSpellTargetLocation());
	}
}

void main ()
{
	ForceDamageOn(OBJECT_SELF);

	object oWeapon = GetItemInSlot(INVENTORY_SLOT_RIGHTWEAPON, GetSpellTargetObject());

	if (GetOverloadMod(oWeapon) > 0)
	{
		OverloadWeapon(oWeapon);		
	}
	else
	{
        oWeapon = GetItemInSlot(INVENTORY_SLOT_LEFTWEAPON, GetSpellTargetObject());
		
		if (GetOverloadMod(oWeapon) > 0)
		{
			OverloadWeapon(oWeapon);		
		}
	}
	
	ForceDamageOff(OBJECT_SELF);
}
