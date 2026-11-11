
void FeatLastStand()
{
	if (GetHasFeat(FEAT_LAST_STAND, OBJECT_SELF))
	{
		if (GetPartyMemberByIndex(1) != OBJECT_INVALID && GetPartyMemberByIndex(2) != OBJECT_INVALID)
		{			
			object oFirstGuy;
			object oSecondGuy;
			
			if (GetPartyMemberByIndex(0) == OBJECT_SELF)
			{
				oFirstGuy = GetPartyMemberByIndex(1);
				oSecondGuy = GetPartyMemberByIndex(2);
			}
			else if (GetPartyMemberByIndex(1) == OBJECT_SELF)
			{
				oFirstGuy = GetPartyMemberByIndex(0);
				oSecondGuy = GetPartyMemberByIndex(2);
			}
			else if (GetPartyMemberByIndex(2) == OBJECT_SELF)
			{
				oFirstGuy = GetPartyMemberByIndex(0);
				oSecondGuy = GetPartyMemberByIndex(1);
			}
			
			if (GetCurrentHitPoints(oFirstGuy) < 1 && GetCurrentHitPoints(oSecondGuy) < 1)			
			{
				effect eRegen = EffectHeal(GetMaxHitPoints(OBJECT_SELF)/20);
				
				ApplyEffectToObject(DURATION_TYPE_INSTANT, eRegen, OBJECT_SELF);
			}
			
		}
	}
}

void FeatAutoShield()
{
	int bGoTime = 0;

	if (GetHasFeat(FEAT_AUTO_SHIELD_PROTOCOL,OBJECT_SELF))
	{
		if (GetTag(OBJECT_SELF) == "T3M4")
		{
			if (GetGlobalBoolean("T3_Health_Recharged") == FALSE)
			{
				if (GetCurrentHitPoints(OBJECT_SELF) == GetMaxHitPoints(OBJECT_SELF))
				{
					SetGlobalBoolean("T3_Health_Recharged", TRUE);
				}				
			}
			else
			{
				bGoTime = 1;
			}
		}
		else if (GetTag(OBJECT_SELF) == "G0T0")
		{
			if (GetGlobalBoolean("Goto_Health_Recharged") == FALSE)
			{
				if (GetCurrentHitPoints(OBJECT_SELF) == GetMaxHitPoints(OBJECT_SELF))
				{
					SetGlobalBoolean("Goto_Health_Recharged", TRUE);
				}				
			}
			else
			{
				bGoTime = 1;
			}
		}		
		
		if (bGoTime == 1)
		{
			if ((GetCurrentHitPoints(OBJECT_SELF)*2) < GetMaxHitPoints(OBJECT_SELF))
			{
				if (GetTag(OBJECT_SELF) == "T3M4")
				{
					SetGlobalBoolean("T3_Health_Recharged", FALSE);
				}
				else if (GetTag(OBJECT_SELF) == "G0T0")
				{
					SetGlobalBoolean("Goto_Health_Recharged", FALSE);
				}
				
				object oShield = GetItemInSlot(INVENTORY_SLOT_BELT, OBJECT_SELF);
				string sTag = GetTag(oShield);
				int nShield;
				int nIcon;
				int nBoost;
				float fDuration = 200.0;		  
				int nRepairSkill = GetSkillRank( SKILL_REPAIR, OBJECT_SELF );
			
				if (GetHasFeat(FEAT_APPLIED_KNOWLEDGE,OBJECT_SELF))
				{
					int nRepairSkill = GetSkillRank( SKILL_REPAIR, OBJECT_SELF);
					int nRepairMod = GetAbilityModifier( ABILITY_INTELLIGENCE, OBJECT_SELF);
					if( nRepairSkill > 0 )
					{
						fDuration += 2.0 * (nRepairSkill + nRepairMod);
					}
				}
			
				if (GetHasFeat(FEAT_MASTER_SHIELD_BOOST,OBJECT_SELF))
				{
					nBoost = 3;
				}
				else if (GetHasFeat(FEAT_IMPROVED_SHIELD_BOOST,OBJECT_SELF))
				{
					nBoost = 2;
				}
				else if (GetHasFeat(FEAT_SHIELD_BOOST,OBJECT_SELF))
				{
					nBoost = 1;
				}
				else
				{
					nBoost = 0;
				}			
				
				if(sTag == "d_shield_01") //SHIELD_DROID_ENERGY_1
				{
					nIcon = 54;
					if (nBoost > 0)
					{
					nShield = BOOST_DROID_ENERGY_1 + (nBoost-1);
					}           
					else
					{
					nShield = 0;
					}
				}
				else if(sTag == "d_shield_02") //SHIELD_DROID_ENERGY_2
				{
					nIcon = 93;

					if (nBoost > 0)
					{
					nShield = BOOST_DROID_ENERGY_2 + (nBoost-1);
					}           
					else
					{
					nShield = 1;
					}
				}
				else if(sTag == "d_shield_05") //SHIELD_DROID_ENERGY_3
				{
					nIcon = 94;

					if (nBoost > 0)
					{
						nShield = BOOST_DROID_ENERGY_3 + (nBoost-1);
					}           
					else
					{
						nShield = 2;
					}
				}
				else if(sTag == "d_shield_03" || sTag == "G_I_DRDSHLD005") //SHIELD_DROID_ENVIRO_1
				{
					nIcon = 95;

					if (nBoost > 0)
					{
						nShield = BOOST_DROID_ENVIRO_1 + (nBoost-1);
					}           
					else
					{
						nShield = 3;
					}
				}
				else if(sTag == "d_shield_04") //SHIELD_DROID_ENVIRO_2
				{
					nIcon = 96;

					if (nBoost > 0)
					{
						nShield = BOOST_DROID_ENVIRO_2 + (nBoost-1);
					}           
					else
					{
						nShield = 4;
					}
				}
				else if(sTag == "d_shield_06") //SHIELD_DROID_ENVIRO_3
				{
					nIcon = 97;

					if (nBoost > 0)
					{
						nShield = BOOST_DROID_ENVIRO_3 + (nBoost-1);
					}           
					else
					{
						nShield = 5;
					}
				}	
				else if(sTag == "100_Fore01" || sTag == "g_i_drdshld004") //SHIELD_HEAT
				{
					nIcon = 91;

					if (nBoost > 0)
					{
						nShield = BOOST_HEAT + (nBoost-1);
					}           
					else
					{
						nShield = 19;
					}
				}			
			
				effect eShield = EffectForceShield(nShield);
				eShield = SetEffectIcon(eShield, nIcon);
				ApplyEffectToObject(DURATION_TYPE_TEMPORARY, eShield, OBJECT_SELF, fDuration);
				
			}
		}		
	}
}

void OnHeartbeatFeats()
{
	FeatLastStand();
	FeatAutoShield();
}
