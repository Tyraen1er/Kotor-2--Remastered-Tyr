
void ForceDamageOn(object oCaster)
{
	if (GetIsPC (oCaster))
		SetGlobalBoolean ("PC_Force_Damage", TRUE);
	else if (GetTag (oCaster) == "Atton")
		SetGlobalBoolean ("Atton_Force_Damage", TRUE);
	else if (GetTag (oCaster) == "Kreia")
		SetGlobalBoolean ("Kreia_Force_Damage", TRUE);
	else if (GetTag (oCaster) == "BaoDur")
		SetGlobalBoolean ("BaoDur_Force_Damage", TRUE);
	else if (GetTag (oCaster) == "Disciple")
		SetGlobalBoolean ("Disciple_Force_Damage", TRUE);
	else if (GetTag (oCaster) == "Handmaiden")
		SetGlobalBoolean ("Handmaiden_Force_Damage", TRUE);
	else if (GetTag (oCaster) == "Mira")
		SetGlobalBoolean ("Mira_Force_Damage", TRUE);
	else if (GetTag (oCaster) == "VisasMarr")
		SetGlobalBoolean ("Visas_Force_Damage", TRUE);
}

void ForceDamageOff(object oCaster)
{
	if (GetIsPC (oCaster))
		SetGlobalBoolean ("PC_Force_Damage", FALSE);
	else if (GetTag (oCaster) == "Atton")
		SetGlobalBoolean ("Atton_Force_Damage", FALSE);
	else if (GetTag (oCaster) == "Kreia")
		SetGlobalBoolean ("Kreia_Force_Damage", FALSE);
	else if (GetTag (oCaster) == "BaoDur")
		SetGlobalBoolean ("BaoDur_Force_Damage", FALSE);
	else if (GetTag (oCaster) == "Disciple")
		SetGlobalBoolean ("Disciple_Force_Damage", FALSE);
	else if (GetTag (oCaster) == "Handmaiden")
		SetGlobalBoolean ("Handmaiden_Force_Damage", FALSE);
	else if (GetTag (oCaster) == "Mira")
		SetGlobalBoolean ("Mira_Force_Damage", FALSE);
	else if (GetTag (oCaster) == "VisasMarr")
		SetGlobalBoolean ("Visas_Force_Damage", FALSE);
}

int FeatDarkRage()
{
	int nStr = 0;
	
	if(GetHasFeat(FEAT_DARK_RAGE, OBJECT_SELF))
	{
		if (GetAbilityModifier (ABILITY_STRENGTH) >= 0)
		{
			nStr = GetAbilityModifier (ABILITY_STRENGTH);
		}    

		int nAlign = GetGoodEvilValue(OBJECT_SELF);

		if (nAlign >= 70)
		{ 
			if (nStr >= 2)
			{
				nStr = nStr/2;
			}
		}
		else if (nAlign <= 30)
		{
			nStr = nStr*2;
		}
	}
	
	return nStr;
}

float FeatConstancy()
{
	float fConstancyMult = 1.0;
	
	if(GetHasFeat(FEAT_CONSTANCY, OBJECT_SELF))
	{
		int nAlign = GetGoodEvilValue(OBJECT_SELF);

		if (nAlign >= 70)
		{
			fConstancyMult = 2.0;
		}
		else if (nAlign <= 30)
		{
			fConstancyMult = 1.25;
		}
		else
		{
			fConstancyMult = 1.5;
		}
	}
	
	return fConstancyMult;	
}

void FeatRespite(object oTarget)
{
	if (GetHasFeat(FEAT_RESPITE, OBJECT_SELF))
	{
		int nHeal = (GetAbilityModifier(ABILITY_WISDOM) + GetAbilityModifier(ABILITY_CHARISMA) + 5 + GetHitDice(OBJECT_SELF));
			
		int nAlign = GetGoodEvilValue(OBJECT_SELF);
			
		if (nAlign >= 70)
		{
			nHeal = nHeal * 2;
		}
		else if (nAlign <= 30)
		{
			nHeal = nHeal / 2;
		}
		
		ApplyEffectToObject(DURATION_TYPE_INSTANT, EffectHeal(nHeal), oTarget);
	}
}

int FeatSadism(object oTarget)
{
	int bSadism = FALSE;
	int nMult = 0;
	
	if(GetHasFeat(FEAT_SADISM, OBJECT_SELF))
	{
		effect eSadismCheck = GetFirstEffect(oTarget);

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

			eSadismCheck = GetNextEffect(oTarget);
		}
		
		if (bSadism == TRUE)
		{                   
			if (GetGoodEvilValue(OBJECT_SELF) >= 70)
			{
				nMult = 4;
			}
			else if (GetGoodEvilValue(OBJECT_SELF) <= 30)
			{
				nMult = 1;
			}
			else
			{
				nMult = 2;
			}
		}
	}
	
	return nMult;
}
