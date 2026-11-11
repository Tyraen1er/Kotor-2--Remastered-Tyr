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

void main ()
{
	ForceDamageOn(OBJECT_SELF);

	object oWeapon = GetItemInSlot(INVENTORY_SLOT_RIGHTWEAPON, GetSpellTargetObject());

	if (GetOverloadMod(oWeapon) > 0)
	{
		DestroyObject(oWeapon);
	}
	else
	{
        oWeapon = GetItemInSlot(INVENTORY_SLOT_LEFTWEAPON, GetSpellTargetObject());
		
		if (GetOverloadMod(oWeapon) > 0)
		{
			DestroyObject(oWeapon);		
		}
	}
	
	ForceDamageOff(OBJECT_SELF);
}
