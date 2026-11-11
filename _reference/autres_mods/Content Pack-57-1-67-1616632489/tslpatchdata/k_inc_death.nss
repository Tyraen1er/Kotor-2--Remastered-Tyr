
void FeatKillerInstinct()
{
	object oKiller = GetLastKiller();
	
	if (GetHasFeat(FEAT_MASTER_KILLER_INSTINCT, oKiller)) //Master Killer Instinct
	{
		ApplyEffectToObject(DURATION_TYPE_TEMPORARY, EffectAttackIncrease(3, ATTACK_BONUS_MISC), oKiller, 30.0);
	}
    else if (GetHasFeat(FEAT_IMPROVED_KILLER_INSTINCT, oKiller)) //Improved Killer Instinct
	{
		ApplyEffectToObject(DURATION_TYPE_TEMPORARY, EffectAttackIncrease(2, ATTACK_BONUS_MISC), oKiller, 30.0);
	}
	else if (GetHasFeat(FEAT_KILLER_INSTINCT, oKiller)) //Killer Instinct
	{
		ApplyEffectToObject(DURATION_TYPE_TEMPORARY, EffectAttackIncrease(1, ATTACK_BONUS_MISC), oKiller, 30.0);
	}
}

void FeatSweetRelease()
{
	object oKiller = GetLastKiller();

	int bSadism = FALSE;
	int nHeal = 0;
	int nAlign = 0;		
	
	if (GetHasFeat(FEAT_SWEET_RELEASE,(oKiller)))
    {
		bSadism = FALSE;
		effect eSadismCheck = GetFirstEffect(OBJECT_SELF);

		while (GetIsEffectValid(eSadismCheck))
		{
			if (GetEffectType(eSadismCheck) == EFFECT_TYPE_STUNNED)
			{
				bSadism = TRUE;
			}
			else if (GetEffectType(eSadismCheck) == EFFECT_TYPE_TURNED)
			{
				bSadism = TRUE;
			}
			else if (GetEffectType(eSadismCheck) == EFFECT_TYPE_PARALYZE)
			{
				bSadism = TRUE;
			}
			else if (GetEffectType(eSadismCheck) == EFFECT_TYPE_FRIGHTENED)
			{
				bSadism = TRUE;
			}

			eSadismCheck = GetNextEffect(OBJECT_SELF);
		}

		if (bSadism == TRUE)
		{
			nHeal = 10 + GetHitDice(oKiller);

			nAlign = GetGoodEvilValue(oKiller);

			if (nAlign >= 70)
			{
				nHeal = nHeal/2;
			}
			else if (nAlign <= 30)
			{
				nHeal = nHeal*2;
			}

			ApplyEffectToObject(DURATION_TYPE_INSTANT, EffectHeal(nHeal), oKiller);
		}
	}
}

void FeatPayday()
{
	object oKiller = GetLastKiller();
	object oPC = GetFirstPC();
	
	int nPayday = 0;
	int nBountyType = 0;

	int iMundaneLevel = GetLevelByClass(0,OBJECT_SELF) + GetLevelByClass(1,OBJECT_SELF) + GetLevelByClass(2,OBJECT_SELF) + GetLevelByClass(6,OBJECT_SELF) + GetLevelByClass(7,OBJECT_SELF) + GetLevelByClass(8,OBJECT_SELF) + GetLevelByClass(9,OBJECT_SELF) + GetLevelByClass(10,OBJECT_SELF);
	int iForceLevel = GetLevelByClass(3,OBJECT_SELF) + GetLevelByClass(4,OBJECT_SELF) + GetLevelByClass(5,OBJECT_SELF) + GetLevelByClass(11,OBJECT_SELF) + GetLevelByClass(12,OBJECT_SELF) + GetLevelByClass(13,OBJECT_SELF) + GetLevelByClass(14,OBJECT_SELF) + GetLevelByClass(15,OBJECT_SELF) + GetLevelByClass(16,OBJECT_SELF);
	int iTotalLevel = iMundaneLevel + iForceLevel;
	
	
	if (GetRacialType (OBJECT_SELF) == RACIAL_TYPE_DROID)
	{
		nBountyType = 0;
	}
	else if (iForceLevel > 0)
	{
		nBountyType = 4;
	}
	else if (GetSubRace(OBJECT_SELF) == SUBRACE_NONE)
	{
		nBountyType = 2;
	}
	else
	{
		nBountyType = 1;
	}
  

	if (IsObjectPartyMember(oKiller))
	{	
		if (GetHasFeat (FEAT_PAYDAY, GetPartyMemberByIndex(0))) //Payday
		{
			nPayday = 1;
		}
		else if (GetHasFeat (FEAT_PAYDAY, GetPartyMemberByIndex(1)))
		{
			nPayday = 1;
		}
		else if (GetHasFeat (FEAT_PAYDAY, GetPartyMemberByIndex(2)))
		{
			nPayday = 1;
		}
		
		if (nPayday == 1)
		{
			if (nBountyType == 1)
			{
				if (GetGlobalNumber("Bounty_Beast") + iTotalLevel > 127)
				{
					if (GetGlobalNumber("Bounty_Beast_Overflow") + iTotalLevel > 127)
					{
						SetGlobalNumber("Bounty_Beast_Overflow", 127);
					}
					else
					{
						IncrementGlobalNumber("Bounty_Beast_Overflow", iTotalLevel);
					}
				}
				else
				{
					IncrementGlobalNumber("Bounty_Beast", iTotalLevel);
				}				
			}		
			else if (nBountyType == 2)
			{
				if (GetGlobalNumber("Bounty_Normal") + iTotalLevel > 127)
				{
					if (GetGlobalNumber("Bounty_Normal_Overflow") + iTotalLevel > 127)
					{
						SetGlobalNumber("Bounty_Normal_Overflow", 127);
					}
					else
					{
						IncrementGlobalNumber("Bounty_Normal_Overflow", iTotalLevel);
					}
				}
				else
				{
					IncrementGlobalNumber("Bounty_Normal", iTotalLevel);
				}				
			}
			else if (nBountyType == 4)
			{
				if (GetGlobalNumber("Bounty_Jedi") + iTotalLevel > 127)
				{
					if (GetGlobalNumber("Bounty_Jedi_Overflow") + iTotalLevel > 127)
					{
						SetGlobalNumber("Bounty_Jedi_Overflow", 127);
					}
					else
					{
						IncrementGlobalNumber("Bounty_Jedi_Overflow", iTotalLevel);
					}
				}
				else
				{
					IncrementGlobalNumber("Bounty_Jedi", iTotalLevel);
				}				
			}
		}
		
	}	
}

void DeathFeats()
{
	FeatKillerInstinct();
	FeatSweetRelease();
	FeatPayday();
}
