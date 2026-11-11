
void BreakWhirlingBlade(object oUser, object oTarget)
{
	object oItem = GetFirstItemInInventory(oTarget);

	while (GetIsObjectValid(oItem))
	{
		if (GetTag(oItem) == "c_wb_pc")
		{
			if (GetIsPC(oUser))
			{
				DestroyObject(oItem);
			}
		}
		else if (GetTag(oItem) == "c_wb_at")
		{
			if (GetTag(oUser) == "Atton")
			{
				DestroyObject(oItem);
			}
		}
		else if (GetTag(oItem) == "c_wb_kr")
		{
			if (GetTag(oUser) == "Kreia")
			{
				DestroyObject(oItem);
			}
		}
		else if (GetTag(oItem) == "c_wb_bd")
		{
			if (GetTag(oUser) == "BaoDur")
			{
				DestroyObject(oItem);
			}
		}
		else if (GetTag(oItem) == "c_wb_dc")
		{
			if (GetTag(oUser) == "Disciple")
			{
				DestroyObject(oItem);
			}
		}
		else if (GetTag(oItem) == "c_wb_hm")
		{
			if (GetTag(oUser) == "Handmaiden")
			{
				DestroyObject(oItem);
			}
		}
		else if (GetTag(oItem) == "c_wb_mr")
		{
			if (GetTag(oUser) == "Mira")
			{
				DestroyObject(oItem);
			}
		}
		else if (GetTag(oItem) == "c_wb_vs")
		{
			if (GetTag(oUser) == "VisasMarr")
			{
				DestroyObject(oItem);
			}
		}
		
		oItem = GetNextItemInInventory(oTarget);
	}
}

void BreakHeartstopper(object oUser, object oTarget)
{
	object oItem = GetFirstItemInInventory(oTarget);

	while (GetIsObjectValid(oItem))
	{
		if (GetTag(oItem) == "c_hs_pc")
		{
			if (GetIsPC(oUser))
			{
				DestroyObject(oItem);
			}
		}
		else if (GetTag(oItem) == "c_hs_at")
		{
			if (GetTag(oUser) == "Atton")
			{
				DestroyObject(oItem);
			}
		}
		else if (GetTag(oItem) == "c_hs_kr")
		{
			if (GetTag(oUser) == "Kreia")
			{
				DestroyObject(oItem);
			}
		}
		else if (GetTag(oItem) == "c_hs_bd")
		{
			if (GetTag(oUser) == "BaoDur")
			{
				DestroyObject(oItem);
			}
		}
		else if (GetTag(oItem) == "c_hs_dc")
		{
			if (GetTag(oUser) == "Disciple")
			{
				DestroyObject(oItem);
			}
		}
		else if (GetTag(oItem) == "c_hs_hm")
		{
			if (GetTag(oUser) == "Handmaiden")
			{
				DestroyObject(oItem);
			}
		}
		else if (GetTag(oItem) == "c_hs_mr")
		{
			if (GetTag(oUser) == "Mira")
			{
				DestroyObject(oItem);
			}
		}
		else if (GetTag(oItem) == "c_hs_vs")
		{
			if (GetTag(oUser) == "VisasMarr")
			{
				DestroyObject(oItem);
			}
		}
		
		oItem = GetNextItemInInventory(oTarget);
	}
}

void BreakAllCombos(object oTarget)
{
	object oItem = GetFirstItemInInventory(oTarget);

	while (GetIsObjectValid(oItem))
	{
		if (GetBaseItemType(oItem) == 104)
			DestroyObject(oItem);
		
		oItem = GetNextItemInInventory(oTarget);
	}
}

void ProcWhirlingBlade(object oUser)
{
	effect ePush = EffectForcePushed();
	effect eStun = EffectStunned();
	effect eDamage = EffectDamage(GetHitDice(oUser), DAMAGE_TYPE_SLASHING);
	int nDC = 5 + GetHitDice(oUser) + GetAbilityModifier(ABILITY_DEXTERITY, oUser);

	ApplyEffectAtLocation(DURATION_TYPE_INSTANT, EffectVisualEffect(VFX_FNF_FORCE_WAVE), GetLocation(oUser));	
	 
	object oTarget = GetFirstObjectInShape(SHAPE_SPHERE, 15.0, GetLocation(OBJECT_SELF), FALSE, OBJECT_TYPE_CREATURE );
	 
	while(GetIsObjectValid(oTarget))
	{
		if (GetIsEnemy(oTarget, oUser))
		{
			if(!ResistForce(oUser, oTarget))
			{
				ApplyEffectToObject(DURATION_TYPE_INSTANT, EffectVisualEffect(VFX_IMP_FORCE_PUSH), oTarget);			
				ApplyEffectToObject(DURATION_TYPE_TEMPORARY, ePush, oTarget, 0.2);
				
				if(!ReflexSave(oTarget, nDC))
				{
					DelayCommand(0.4, ApplyEffectToObject(DURATION_TYPE_INSTANT, eDamage, oTarget));				
					DelayCommand(1.0, ApplyEffectToObject(DURATION_TYPE_TEMPORARY, eStun, oTarget, 6.0));
				}
				else
				{
					ApplyEffectToObject(DURATION_TYPE_INSTANT, EffectForceResisted(oUser), oTarget);  
					
					if (!GetHasFeat(FEAT_EVASION, oTarget))
					{
						eDamage = EffectDamage(GetHitDice(oUser)/2, DAMAGE_TYPE_SLASHING);
						ApplyEffectToObject(DURATION_TYPE_INSTANT, eDamage, oTarget);
					}
				}
			}
		}
		
		oTarget = GetNextObjectInShape(SHAPE_SPHERE, 15.0, GetLocation(OBJECT_SELF), FALSE, OBJECT_TYPE_CREATURE );
	}	 
}

void ProcThunderousBlade(object oUser)
{
	effect ePush = EffectForcePushed();
	effect eStun = EffectStunned();
	effect eDamage = EffectDamage((GetHitDice(oUser)*3)/2, DAMAGE_TYPE_ELECTRICAL);
	int nDC = 10 + GetHitDice(oUser) + GetAbilityModifier(ABILITY_DEXTERITY, oUser);
	effect eBeam = EffectBeam(2066, oUser, BODY_NODE_HAND);

	ApplyEffectAtLocation(DURATION_TYPE_INSTANT, EffectVisualEffect(VFX_FNF_FORCE_WAVE), GetLocation(oUser));	
	 
	object oTarget = GetFirstObjectInShape(SHAPE_SPHERE, 15.0, GetLocation(OBJECT_SELF), FALSE, OBJECT_TYPE_CREATURE );
	 
	while(GetIsObjectValid(oTarget))
	{
		if (GetIsEnemy(oTarget, oUser))
		{
			if(!ResistForce(oUser, oTarget))
			{
				ApplyEffectToObject(DURATION_TYPE_INSTANT, EffectVisualEffect(VFX_IMP_FORCE_PUSH), oTarget);
				ApplyEffectToObject(DURATION_TYPE_TEMPORARY, eBeam, oTarget, 1.0);
				ApplyEffectToObject(DURATION_TYPE_TEMPORARY, ePush, oTarget, 0.2);
				
				if(!ReflexSave(oTarget, 15))
				{
					DelayCommand(0.4, ApplyEffectToObject(DURATION_TYPE_INSTANT, eDamage, oTarget));				
					DelayCommand(1.0, ApplyEffectToObject(DURATION_TYPE_TEMPORARY, eStun, oTarget, 6.0));
				}
				else
				{
					ApplyEffectToObject(DURATION_TYPE_INSTANT, EffectForceResisted(oUser), oTarget);  
					
					if (!GetHasFeat(FEAT_EVASION, oTarget))
					{
						eDamage = EffectDamage((GetHitDice(oUser)*3)/4, DAMAGE_TYPE_ELECTRICAL);
						ApplyEffectToObject(DURATION_TYPE_INSTANT, eDamage, oTarget);
					}
				}
			}
		}
		
		oTarget = GetNextObjectInShape(SHAPE_SPHERE, 15.0, GetLocation(OBJECT_SELF), FALSE, OBJECT_TYPE_CREATURE );
	}	 
}

void ProcHeartstopper(object oTarget)
{
	if (GetCurrentHitPoints(oTarget) < GetMaxHitPoints(oTarget)/3)
	{
		ApplyEffectToObject(DURATION_TYPE_INSTANT, EffectDeath(), oTarget);
	}
}

int GetCountWhirlingBlade(object oUser, object oTarget)
{
	int nCount = 0;
	
	object oItem = GetFirstItemInInventory(oTarget);

	while (GetIsObjectValid(oItem))
	{
		if (GetTag(oItem) == "c_wb_pc")
		{
			if (GetIsPC(oUser))
			{
				nCount += GetNumStackedItems(oItem);
			}
		}
		else if (GetTag(oItem) == "c_wb_at")
		{
			if (GetTag(oUser) == "Atton")
			{
				nCount += GetNumStackedItems(oItem);
			}
		}
		else if (GetTag(oItem) == "c_wb_kr")
		{
			if (GetTag(oUser) == "Kreia")
			{
				nCount += GetNumStackedItems(oItem);
			}
		}
		else if (GetTag(oItem) == "c_wb_bd")
		{
			if (GetTag(oUser) == "BaoDur")
			{
				nCount += GetNumStackedItems(oItem);
			}
		}
		else if (GetTag(oItem) == "c_wb_dc")
		{
			if (GetTag(oUser) == "Disciple")
			{
				nCount += GetNumStackedItems(oItem);
			}
		}
		else if (GetTag(oItem) == "c_wb_hm")
		{
			if (GetTag(oUser) == "Handmaiden")
			{
				nCount += GetNumStackedItems(oItem);
			}
		}
		else if (GetTag(oItem) == "c_wb_mr")
		{
			if (GetTag(oUser) == "Mira")
			{
				nCount += GetNumStackedItems(oItem);
			}
		}
		else if (GetTag(oItem) == "c_wb_vs")
		{
			if (GetTag(oUser) == "VisasMarr")
			{
				nCount += GetNumStackedItems(oItem);
			}
		}
		
		oItem = GetNextItemInInventory(oTarget);
	}

	return nCount;
}

int GetCountHeartstopper(object oUser, object oTarget)
{
	int nCount = 0;
	
	object oItem = GetFirstItemInInventory(oTarget);

	while (GetIsObjectValid(oItem))
	{
		if (GetTag(oItem) == "c_hs_pc")
		{
			if (GetIsPC(oUser))
			{
				nCount += GetNumStackedItems(oItem);
			}
		}
		else if (GetTag(oItem) == "c_hs_at")
		{
			if (GetTag(oUser) == "Atton")
			{
				nCount += GetNumStackedItems(oItem);
			}
		}
		else if (GetTag(oItem) == "c_hs_kr")
		{
			if (GetTag(oUser) == "Kreia")
			{
				nCount += GetNumStackedItems(oItem);
			}
		}
		else if (GetTag(oItem) == "c_hs_bd")
		{
			if (GetTag(oUser) == "BaoDur")
			{
				nCount += GetNumStackedItems(oItem);
			}
		}
		else if (GetTag(oItem) == "c_hs_dc")
		{
			if (GetTag(oUser) == "Disciple")
			{
				nCount += GetNumStackedItems(oItem);
			}
		}
		else if (GetTag(oItem) == "c_hs_hm")
		{
			if (GetTag(oUser) == "Handmaiden")
			{
				nCount += GetNumStackedItems(oItem);
			}
		}
		else if (GetTag(oItem) == "c_hs_mr")
		{
			if (GetTag(oUser) == "Mira")
			{
				nCount += GetNumStackedItems(oItem);
			}
		}
		else if (GetTag(oItem) == "c_hs_vs")
		{
			if (GetTag(oUser) == "VisasMarr")
			{
				nCount += GetNumStackedItems(oItem);
			}
		}
		
		oItem = GetNextItemInInventory(oTarget);
	}
	
	return nCount;
}

void FeatAntiShield()
{
	object oAttacker = GetLastDamager();
	string oTag = GetTag(oAttacker);
	int bDisruptor = 0;
	
	if (GetBaseItemType(GetLastWeaponUsed(oAttacker)) == BASE_ITEM_DISRUPTER_PISTOL)
	{
		bDisruptor = 1;
	}
	else if (GetBaseItemType(GetLastWeaponUsed(oAttacker)) == BASE_ITEM_DISRUPTER_RIFLE)
	{
		bDisruptor = 1;
	}	
	
	if (oTag == "HK47" && GetHasFeat(FEAT_ANTI_SHIELD_PROTOCOL, oAttacker))
	{
		if (bDisruptor == 1 && GetGlobalBoolean("HK_Force_Damage") == FALSE)
		{
			 effect eEffect = GetFirstEffect(OBJECT_SELF);

			while (GetIsEffectValid(eEffect))
			{
				if (GetEffectType(eEffect) == EFFECT_TYPE_INVALIDEFFECT)
				RemoveEffect(OBJECT_SELF, eEffect);
				eEffect = GetNextEffect(OBJECT_SELF);
			}
		}
	}
}

void FeatWhirlingBlade()
{
	object oAttacker = GetLastDamager();
	string oTag = GetTag(oAttacker);
	int bSword = 0;
	
	if (GetBaseItemType(GetLastWeaponUsed(oAttacker)) == BASE_ITEM_LONG_SWORD)
	{
		bSword = 1;
	}
	else if (GetBaseItemType(GetLastWeaponUsed(oAttacker)) == BASE_ITEM_SHORT_SWORD)
	{
		bSword = 1;
	}
	else if (GetBaseItemType(GetLastWeaponUsed(oAttacker)) == BASE_ITEM_DOUBLE_BLADED_SWORD)
	{
		bSword = 1;
	}
	else if (GetBaseItemType(GetLastWeaponUsed(oAttacker)) == BASE_ITEM_WOOKIE_WARBLADE)
	{
		bSword = 1;
	}
	if (GetHasFeat(FEAT_WHIRLING_BLADE_COMBO, oAttacker))
	{
		if (GetIsPC(oAttacker))
		{
			if (GetGlobalBoolean("PC_Force_Damage") == TRUE)
			{
				BreakWhirlingBlade(oAttacker, OBJECT_SELF);
			}
			else if (bSword == 0)
			{
				BreakWhirlingBlade(oAttacker, OBJECT_SELF);
			}
			else if (GetCountWhirlingBlade(oAttacker, OBJECT_SELF) >= 3)
			{
				BreakWhirlingBlade(oAttacker, OBJECT_SELF);
				
				if (GetHasFeat(FEAT_THUNDEROUS_BLADE_COMBO, oAttacker))
				{
					ProcThunderousBlade(oAttacker);
				}
				else
				{
					ProcWhirlingBlade(oAttacker);
				}		
			}
			else
			{
				CreateItemOnObject("c_wb_pc",OBJECT_SELF);
			}
		}
		else if (GetTag(oAttacker) == "Atton")
		{
			if (GetGlobalBoolean("Atton_Force_Damage") == TRUE)
			{
				BreakWhirlingBlade(oAttacker, OBJECT_SELF);
			}
			else if (bSword == 0)
			{
				BreakWhirlingBlade(oAttacker, OBJECT_SELF);
			}
			else if (GetCountWhirlingBlade(oAttacker, OBJECT_SELF) >= 3)
			{
				BreakWhirlingBlade(oAttacker, OBJECT_SELF);
				
				if (GetHasFeat(FEAT_THUNDEROUS_BLADE_COMBO, oAttacker))
				{
					ProcThunderousBlade(oAttacker);
				}
				else
				{
					ProcWhirlingBlade(oAttacker);
				}	
			}
			else
			{
				CreateItemOnObject("c_wb_at",OBJECT_SELF);
			}
		}
		else if (GetTag(oAttacker) == "Kreia")
		{
			if (GetGlobalBoolean("Kreia_Force_Damage") == TRUE)
			{
				BreakWhirlingBlade(oAttacker, OBJECT_SELF);
			}
			else if (bSword == 0)
			{
				BreakWhirlingBlade(oAttacker, OBJECT_SELF);
			}
			else if (GetCountWhirlingBlade(oAttacker, OBJECT_SELF) >= 3)
			{
				BreakWhirlingBlade(oAttacker, OBJECT_SELF);
				
				if (GetHasFeat(FEAT_THUNDEROUS_BLADE_COMBO, oAttacker))
				{
					ProcThunderousBlade(oAttacker);
				}
				else
				{
					ProcWhirlingBlade(oAttacker);
				}	
			}
			else
			{
				CreateItemOnObject("c_wb_kr",OBJECT_SELF);
			}
		}
		else if (GetTag(oAttacker) == "BaoDur")
		{
			if (GetGlobalBoolean("BaoDur_Force_Damage") == TRUE)
			{
				BreakWhirlingBlade(oAttacker, OBJECT_SELF);
			}
			else if (bSword == 0)
			{
				BreakWhirlingBlade(oAttacker, OBJECT_SELF);
			}
			else if (GetCountWhirlingBlade(oAttacker, OBJECT_SELF) >= 3)
			{
				BreakWhirlingBlade(oAttacker, OBJECT_SELF);
				
				if (GetHasFeat(FEAT_THUNDEROUS_BLADE_COMBO, oAttacker))
				{
					ProcThunderousBlade(oAttacker);
				}
				else
				{
					ProcWhirlingBlade(oAttacker);
				}	
			}
			else
			{
				CreateItemOnObject("c_wb_bd",OBJECT_SELF);
			}
		}
		else if (GetTag(oAttacker) == "Disciple")
		{
			if (GetGlobalBoolean("Disciple_Force_Damage") == TRUE)
			{
				BreakWhirlingBlade(oAttacker, OBJECT_SELF);
			}
			else if (bSword == 0)
			{
				BreakWhirlingBlade(oAttacker, OBJECT_SELF);
			}
			else if (GetCountWhirlingBlade(oAttacker, OBJECT_SELF) >= 3)
			{
				BreakWhirlingBlade(oAttacker, OBJECT_SELF);
				
				if (GetHasFeat(FEAT_THUNDEROUS_BLADE_COMBO, oAttacker))
				{
					ProcThunderousBlade(oAttacker);
				}
				else
				{
					ProcWhirlingBlade(oAttacker);
				}	
			}
			else
			{
				CreateItemOnObject("c_wb_ds",OBJECT_SELF);
			}
		}
		else if (GetTag(oAttacker) == "Handmaiden")
		{
			if (GetGlobalBoolean("Handmaiden_Force_Damage") == TRUE)
			{
				BreakWhirlingBlade(oAttacker, OBJECT_SELF);
			}
			else if (bSword == 0)
			{
				BreakWhirlingBlade(oAttacker, OBJECT_SELF);
			}
			else if (GetCountWhirlingBlade(oAttacker, OBJECT_SELF) >= 3)
			{
				BreakWhirlingBlade(oAttacker, OBJECT_SELF);
				
				if (GetHasFeat(FEAT_THUNDEROUS_BLADE_COMBO, oAttacker))
				{
					ProcThunderousBlade(oAttacker);
				}
				else
				{
					ProcWhirlingBlade(oAttacker);
				}	
			}
			else
			{
				CreateItemOnObject("c_wb_hm",OBJECT_SELF);
			}
		}
		else if (GetTag(oAttacker) == "Mira")
		{
			if (GetGlobalBoolean("Mira_Force_Damage") == TRUE)
			{
				BreakWhirlingBlade(oAttacker, OBJECT_SELF);
			}
			else if (bSword == 0)
			{
				BreakWhirlingBlade(oAttacker, OBJECT_SELF);
			}
			else if (GetCountWhirlingBlade(oAttacker, OBJECT_SELF) >= 3)
			{
				BreakWhirlingBlade(oAttacker, OBJECT_SELF);
				
				if (GetHasFeat(FEAT_THUNDEROUS_BLADE_COMBO, oAttacker))
				{
					ProcThunderousBlade(oAttacker);
				}
				else
				{
					ProcWhirlingBlade(oAttacker);
				}	
			}
			else
			{
				CreateItemOnObject("c_wb_mr",OBJECT_SELF);
			}
		}
		else if (GetTag(oAttacker) == "VisasMarr")
		{
			if (GetGlobalBoolean("Visas_Force_Damage") == TRUE)
			{
				BreakWhirlingBlade(oAttacker, OBJECT_SELF);
			}
			else if (bSword == 0)
			{
				BreakWhirlingBlade(oAttacker, OBJECT_SELF);
			}
			else if (GetCountWhirlingBlade(oAttacker, OBJECT_SELF) >= 3)
			{
				BreakWhirlingBlade(oAttacker, OBJECT_SELF);
				
				if (GetHasFeat(FEAT_THUNDEROUS_BLADE_COMBO, oAttacker))
				{
					ProcThunderousBlade(oAttacker);
				}
				else
				{
					ProcWhirlingBlade(oAttacker);
				}	
			}
			else
			{
				CreateItemOnObject("c_wb_vs",OBJECT_SELF);
			}
		}
	}
}

void FeatHeartstopper()
{
	object oAttacker = GetLastDamager();
	string oTag = GetTag(oAttacker);
	int bPunch = 0;
	
	if (GetItemInSlot(INVENTORY_SLOT_RIGHTWEAPON, oAttacker) == OBJECT_INVALID)
	{
		bPunch = 1;
	}
	
	if (GetHasFeat(FEAT_HEARTSTOPPER_COMBO, oAttacker))
	{
		if (GetIsPC(oAttacker))
		{
			if (GetGlobalBoolean("PC_Force_Damage") == TRUE)
			{
				BreakHeartstopper(oAttacker, OBJECT_SELF);
			}
			else if (bPunch == 0)
			{
				BreakHeartstopper(oAttacker, OBJECT_SELF);
			}
			else
			{
				CreateItemOnObject("c_hs_pc",OBJECT_SELF);
			}
		}
		else if (GetTag(oAttacker) == "Atton")
		{
			if (GetGlobalBoolean("Atton_Force_Damage") == TRUE)
			{
				BreakHeartstopper(oAttacker, OBJECT_SELF);
			}
			else if (bPunch == 0)
			{
				BreakHeartstopper(oAttacker, OBJECT_SELF);
			}
			else
			{
				CreateItemOnObject("c_hs_at",OBJECT_SELF);
			}
		}
		else if (GetTag(oAttacker) == "Kreia")
		{		
			if (GetGlobalBoolean("Kreia_Force_Damage") == TRUE)
			{
				BreakHeartstopper(oAttacker, OBJECT_SELF);
			}
			else if (bPunch == 0)
			{
				BreakHeartstopper(oAttacker, OBJECT_SELF);
			}
			else
			{
				CreateItemOnObject("c_hs_kr",OBJECT_SELF);
			}
		}
		else if (GetTag(oAttacker) == "BaoDur")
		{
			if (GetGlobalBoolean("BaoDur_Force_Damage") == TRUE)
			{
				BreakHeartstopper(oAttacker, OBJECT_SELF);
			}
			else if (bPunch == 0)
			{
				BreakHeartstopper(oAttacker, OBJECT_SELF);
			}
			else
			{
				CreateItemOnObject("c_hs_bd",OBJECT_SELF);
			}
		}
		else if (GetTag(oAttacker) == "Disciple")
		{
			if (GetGlobalBoolean("Disciple_Force_Damage") == TRUE)
			{
				BreakHeartstopper(oAttacker, OBJECT_SELF);
			}
			else if (bPunch == 0)
			{
				BreakHeartstopper(oAttacker, OBJECT_SELF);
			}
			else
			{
				CreateItemOnObject("c_hs_dc",OBJECT_SELF);
			}
		}
		else if (GetTag(oAttacker) == "Handmaiden")
		{
			if (GetGlobalBoolean("Handmaiden_Force_Damage") == TRUE)
			{
				BreakHeartstopper(oAttacker, OBJECT_SELF);
			}
			else if (bPunch == 0)
			{
				BreakHeartstopper(oAttacker, OBJECT_SELF);
			}
			else
			{
				CreateItemOnObject("c_hs_hm",OBJECT_SELF);
			}
		}
		else if (GetTag(oAttacker) == "Mira")
		{
			if (GetGlobalBoolean("Mira_Force_Damage") == TRUE)
			{
				BreakHeartstopper(oAttacker, OBJECT_SELF);
			}
			else if (bPunch == 0)
			{
				BreakHeartstopper(oAttacker, OBJECT_SELF);
			}
			else
			{
				CreateItemOnObject("c_hs_mr",OBJECT_SELF);
			}
		}
		else if (GetTag(oAttacker) == "VisasMarr")
		{
			if (GetGlobalBoolean("Visas_Force_Damage") == TRUE)
			{
				BreakHeartstopper(oAttacker, OBJECT_SELF);
			}
			else if (bPunch == 0)
			{
				BreakHeartstopper(oAttacker, OBJECT_SELF);
			}
			else
			{
				CreateItemOnObject("c_hs_vs",OBJECT_SELF);
			}
		}
	}
}

void CheckHeartstopper(object oUser, object oTarget)
{	
	if (GetCountHeartstopper(oUser, oTarget) >= 3)
	{	
		BreakHeartstopper(oUser, oTarget);
		ProcHeartstopper(oTarget);
	}
}

void OnDamageFeats()
{
	FeatAntiShield();
	FeatWhirlingBlade();
	FeatHeartstopper();
}

