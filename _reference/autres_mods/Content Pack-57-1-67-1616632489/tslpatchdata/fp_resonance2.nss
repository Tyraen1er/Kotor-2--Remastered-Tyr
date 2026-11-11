#include "k_inc_debug"
#include "k_inc_constant"
#include "k_inc_force"

void main ()

{
	int nMaxBonus = 4;
	effect eEffect;
	float fDuration = 60.0 * FeatConstancy();

	int nStrength = 0;
	int nBestStrength = 0;
	int nStrengthBonus = 0;
	
	int nMyStrength = GetAbilityScore(OBJECT_SELF, ABILITY_STRENGTH);
	
	nStrength = GetAbilityScore(GetPartyMemberByIndex(0), ABILITY_STRENGTH);
	
	if (nStrength > nMyStrength)
	nBestStrength = nStrength;
	
	nStrength = GetAbilityScore(GetPartyMemberByIndex(1), ABILITY_STRENGTH);
	
	if (nStrength > nMyStrength)
	nBestStrength = nStrength;
	
	nStrength = GetAbilityScore(GetPartyMemberByIndex(2), ABILITY_STRENGTH);
	
	if (nStrength > nMyStrength)
	nBestStrength = nStrength;
	
	if (nBestStrength > nMyStrength)
	{
		nStrengthBonus = nBestStrength - nMyStrength;
		
		if (nStrengthBonus > nMaxBonus)
		nStrengthBonus = nMaxBonus;
	}
	
	int nDexterity = 0;
	int nBestDexterity = 0;
	int nDexterityBonus = 0;
	
	int nMyDexterity = GetAbilityScore(OBJECT_SELF, ABILITY_DEXTERITY);
	
	nDexterity = GetAbilityScore(GetPartyMemberByIndex(0), ABILITY_DEXTERITY);
	
	if (nDexterity > nMyDexterity)
	nBestDexterity = nDexterity;
	
	nDexterity = GetAbilityScore(GetPartyMemberByIndex(1), ABILITY_DEXTERITY);
	
	if (nDexterity > nMyDexterity)
	nBestDexterity = nDexterity;
	
	nDexterity = GetAbilityScore(GetPartyMemberByIndex(2), ABILITY_DEXTERITY);
	
	if (nDexterity > nMyDexterity)
	nBestDexterity = nDexterity;
	
	if (nBestDexterity > nMyDexterity)
	{
		nDexterityBonus = nBestDexterity - nMyDexterity;
		
		if (nDexterityBonus > nMaxBonus)
		nDexterityBonus = nMaxBonus;
	}
	
	int nConstitution = 0;
	int nBestConstitution = 0;
	int nConstitutionBonus = 0;
	
	int nMyConstitution = GetAbilityScore(OBJECT_SELF, ABILITY_CONSTITUTION);
	
	nConstitution = GetAbilityScore(GetPartyMemberByIndex(0), ABILITY_CONSTITUTION);
	
	if (nConstitution > nMyConstitution)
	nBestConstitution = nConstitution;
	
	nConstitution = GetAbilityScore(GetPartyMemberByIndex(1), ABILITY_CONSTITUTION);
	
	if (nConstitution > nMyConstitution)
	nBestConstitution = nConstitution;
	
	nConstitution = GetAbilityScore(GetPartyMemberByIndex(2), ABILITY_CONSTITUTION);
	
	if (nConstitution > nMyConstitution)
	nBestConstitution = nConstitution;
	
	if (nBestConstitution > nMyConstitution)
	{
		nConstitutionBonus = nBestConstitution - nMyConstitution;
		
		if (nConstitutionBonus > nMaxBonus)
		nConstitutionBonus = nMaxBonus;
	}

	int nIntelligence = 0;
	int nBestIntelligence = 0;
	int nIntelligenceBonus = 0;
	
	int nMyIntelligence = GetAbilityScore(OBJECT_SELF, ABILITY_INTELLIGENCE);
	
	nIntelligence = GetAbilityScore(GetPartyMemberByIndex(0), ABILITY_INTELLIGENCE);
	
	if (nIntelligence > nMyIntelligence)
	nBestIntelligence = nIntelligence;
	
	nIntelligence = GetAbilityScore(GetPartyMemberByIndex(1), ABILITY_INTELLIGENCE);
	
	if (nIntelligence > nMyIntelligence)
	nBestIntelligence = nIntelligence;
	
	nIntelligence = GetAbilityScore(GetPartyMemberByIndex(2), ABILITY_INTELLIGENCE);
	
	if (nIntelligence > nMyIntelligence)
	nBestIntelligence = nIntelligence;
	
	if (nBestIntelligence > nMyIntelligence)
	{
		nIntelligenceBonus = nBestIntelligence - nMyIntelligence;
		
		if (nIntelligenceBonus > nMaxBonus)
		nIntelligenceBonus = nMaxBonus;
	}
	
	int nWisdom = 0;
	int nBestWisdom = 0;
	int nWisdomBonus = 0;
	
	int nMyWisdom = GetAbilityScore(OBJECT_SELF, ABILITY_WISDOM);
	
	nWisdom = GetAbilityScore(GetPartyMemberByIndex(0), ABILITY_WISDOM);
	
	if (nWisdom > nMyWisdom)
	nBestWisdom = nWisdom;
	
	nWisdom = GetAbilityScore(GetPartyMemberByIndex(1), ABILITY_WISDOM);
	
	if (nWisdom > nMyWisdom)
	nBestWisdom = nWisdom;
	
	nWisdom = GetAbilityScore(GetPartyMemberByIndex(2), ABILITY_WISDOM);
	
	if (nWisdom > nMyWisdom)
	nBestWisdom = nWisdom;
	
	if (nBestWisdom > nMyWisdom)
	{
		nWisdomBonus = nBestWisdom - nMyWisdom;
		
		if (nWisdomBonus > nMaxBonus)
		nWisdomBonus = nMaxBonus;
	}
	
	int nCharisma = 0;
	int nBestCharisma = 0;
	int nCharismaBonus = 0;
	
	int nMyCharisma = GetAbilityScore(OBJECT_SELF, ABILITY_CHARISMA);
	
	nCharisma = GetAbilityScore(GetPartyMemberByIndex(0), ABILITY_CHARISMA);
	
	if (nCharisma > nMyCharisma)
	nBestCharisma = nCharisma;
	
	nCharisma = GetAbilityScore(GetPartyMemberByIndex(1), ABILITY_CHARISMA);
	
	if (nCharisma > nMyCharisma)
	nBestCharisma = nCharisma;
	
	nCharisma = GetAbilityScore(GetPartyMemberByIndex(2), ABILITY_CHARISMA);
	
	if (nCharisma > nMyCharisma)
	nBestCharisma = nCharisma;
	
	if (nBestCharisma > nMyCharisma)
	{
		nCharismaBonus = nBestCharisma - nMyCharisma;
		
		if (nCharismaBonus > nMaxBonus)
		nCharismaBonus = nMaxBonus;
	}
	
	
	eEffect = EffectAbilityIncrease(ABILITY_STRENGTH, nStrengthBonus);
	eEffect = EffectLinkEffects(eEffect, EffectAbilityIncrease(ABILITY_DEXTERITY, nDexterityBonus));
	eEffect = EffectLinkEffects(eEffect, EffectAbilityIncrease(ABILITY_CONSTITUTION, nConstitutionBonus));
	eEffect = EffectLinkEffects(eEffect, EffectAbilityIncrease(ABILITY_INTELLIGENCE, nIntelligenceBonus));
	eEffect = EffectLinkEffects(eEffect, EffectAbilityIncrease(ABILITY_WISDOM, nWisdomBonus));
	eEffect = EffectLinkEffects(eEffect, EffectAbilityIncrease(ABILITY_CHARISMA, nCharismaBonus));
	
	eEffect = SetEffectIcon(eEffect, #2DAMEMORY46#);
	
	ApplyEffectToObject(DURATION_TYPE_TEMPORARY, eEffect, OBJECT_SELF, fDuration);
	ApplyEffectToObject(DURATION_TYPE_INSTANT, EffectVisualEffect(VFX_IMP_MIND_FORCE), OBJECT_SELF);
	
	FeatRespite(OBJECT_SELF);

}