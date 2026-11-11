
void SummonStranger()
{
	object oNearest;
	object oEnemy;
	float fDistance = 0.0;
	object oTarget;
	object oSummon;	 
	location lTarget;
	
	int nLevel = GetLevelByPosition(1)+GetLevelByPosition(2)+GetLevelByPosition(3);
	effect eBonusStats = EffectTemporaryHitpoints(nLevel*12);
	eBonusStats = EffectLinkEffects(eBonusStats, EffectAttackIncrease(nLevel));
	eBonusStats = EffectLinkEffects(eBonusStats, EffectACIncrease(nLevel));
		 
	oNearest = GetNearestCreature(CREATURE_TYPE_PERCEPTION, PERCEPTION_SEEN, OBJECT_SELF, 1, CREATURE_TYPE_REPUTATION, REPUTATION_TYPE_ENEMY);
		
	if (GetIsObjectValid(oNearest))
	{					
		oEnemy = GetFirstObjectInShape(SHAPE_SPHERE, 20.0, GetLocation(OBJECT_SELF), FALSE, OBJECT_TYPE_CREATURE );
		while(GetIsObjectValid(oEnemy))
		{		 
			if (GetReputation(oEnemy, OBJECT_SELF) < 11)
			{
				if (GetDistanceToObject(oEnemy) > fDistance)
				{						
					fDistance = GetDistanceToObject(oEnemy);
					oTarget = oEnemy;
				}
			}
			oEnemy = GetNextObjectInShape(SHAPE_SPHERE, 20.0, GetLocation(OBJECT_SELF), FALSE, OBJECT_TYPE_CREATURE );
		}
		
		if (oTarget != OBJECT_INVALID)
		{
			lTarget = GetLocation(oTarget);

			ApplyEffectAtLocation(DURATION_TYPE_INSTANT, EffectVisualEffect(3001), lTarget);
			oSummon = CreateObject(OBJECT_TYPE_CREATURE,"p_stranger",lTarget,FALSE);
			ApplyEffectToObject(DURATION_TYPE_PERMANENT, eBonusStats, oSummon);
			SetGoodEvilValue(oSummon, GetGoodEvilValue(OBJECT_SELF));
		}
	}
}

void CheckForUnsummon()
{
    int nHostiles = 0;
	object oCreature;
	 
	if (GetTag(OBJECT_SELF) == "Stranger")
	{
		 oCreature = GetFirstObjectInShape(SHAPE_SPHERE, 20.0, GetLocation(OBJECT_SELF), FALSE, OBJECT_TYPE_CREATURE );
         while(GetIsObjectValid(oCreature))
		 {		 
			if (GetReputation(oCreature, OBJECT_SELF) < 11)
			{
				nHostiles += 1;
			}
			oCreature = GetNextObjectInShape(SHAPE_SPHERE, 20.0, GetLocation(OBJECT_SELF), FALSE, OBJECT_TYPE_CREATURE );
		 }
		 
		 if (nHostiles == 0)
		 {			
			ApplyEffectAtLocation(DURATION_TYPE_INSTANT, EffectVisualEffect(3001), GetLocation(OBJECT_SELF));
			DestroyObject(OBJECT_SELF, 0.0, TRUE, 0.0, 0);
		 }
	}
}

void CheckForStranger()
{
	int nSummoned = 0;
	int nTimeToGo = 0;
	object oCreature;

	if (GetHasFeat(FEAT_MYSTERIOUS_BENEFACTOR))
	{
		oCreature = GetFirstObjectInShape(SHAPE_SPHERE, 30.0, GetLocation(OBJECT_SELF), FALSE, OBJECT_TYPE_CREATURE );
        while(GetIsObjectValid(oCreature))
		{		 
			if (GetTag(oCreature) == "Stranger")
			{				
				nSummoned = 1;
			}
			oCreature = GetNextObjectInShape(SHAPE_SPHERE, 30.0, GetLocation(OBJECT_SELF), FALSE, OBJECT_TYPE_CREATURE );
		}
		
		if (nSummoned == 0) //No extant summons
		{
			oCreature = GetNearestCreature(CREATURE_TYPE_PERCEPTION, PERCEPTION_SEEN, OBJECT_SELF, 1, CREATURE_TYPE_REPUTATION, REPUTATION_TYPE_ENEMY);
		
			if (GetIsObjectValid(oCreature)) //Enemy in sight
			{
				if (GetCurrentHitPoints(OBJECT_SELF) < GetMaxHitPoints(OBJECT_SELF)/3 && GetCurrentHitPoints(OBJECT_SELF) > 0)
				{
					nTimeToGo = 1;
				}
				else if (Random(20) == 19)
				{
					nTimeToGo = 1;
				}
				else
				{
					nTimeToGo = 0;
				}
				
				if (nTimeToGo == 1)
				{
					SummonStranger();
				}
			}
		}
	}
}
