//:: k_sup_healing
/*
    Script for the 3 healing
    kits and the remove poison
    kit
*/
//:: Created By: Preston Watamaniuk
//:: Copyright (c) 2002 Bioware Corp.

#include "k_inc_debug"
#include "k_inc_constant"
#include "k_inc_force"

void main()
{
    int nItem = GetSpellId();
    int nSkill = GetSkillRank(SKILL_TREAT_INJURY);
    int nBonusSkill = 0;
    int nBonusStat = 0;
    effect eHeal;
    int bHeal = TRUE;
    int bDying = FALSE;

    if (GetMaxHitPoints(OBJECT_SELF) > (4*GetCurrentHitPoints(OBJECT_SELF)))
    {
       bDying = TRUE;
    }

    if (GetPartyMemberByIndex(0) != OBJECT_SELF)
    {
       if (GetHasFeat(FEAT_DESIGNATED_MEDIC,GetPartyMemberByIndex(0)))
       {
          if ((GetSkillRank(SKILL_TREAT_INJURY,GetPartyMemberByIndex(0)) + GetAbilityModifier(ABILITY_WISDOM,GetPartyMemberByIndex(0))) > (nBonusSkill+nBonusStat))
          {
             nBonusSkill = GetSkillRank(SKILL_TREAT_INJURY,GetPartyMemberByIndex(0));
             nBonusStat = GetAbilityModifier(ABILITY_WISDOM,GetPartyMemberByIndex(0));
          }
       }
    }

    if (GetPartyMemberByIndex(1) != OBJECT_SELF)
    {
       if (GetHasFeat(FEAT_DESIGNATED_MEDIC,GetPartyMemberByIndex(1)))
       {
          if ((GetSkillRank(SKILL_TREAT_INJURY,GetPartyMemberByIndex(1)) + GetAbilityModifier(ABILITY_WISDOM,GetPartyMemberByIndex(1))) > (nBonusSkill+nBonusStat))
          {
             nBonusSkill = GetSkillRank(SKILL_TREAT_INJURY,GetPartyMemberByIndex(1));
             nBonusStat = GetAbilityModifier(ABILITY_WISDOM,GetPartyMemberByIndex(1));
          }
       }
    }

    if (GetPartyMemberByIndex(2) != OBJECT_SELF)
    {
       if (GetHasFeat(FEAT_DESIGNATED_MEDIC,GetPartyMemberByIndex(2)))
       {
          if ((GetSkillRank(SKILL_TREAT_INJURY,GetPartyMemberByIndex(2)) + GetAbilityModifier(ABILITY_WISDOM,GetPartyMemberByIndex(2))) > (nBonusSkill+nBonusStat))
          {
             nBonusSkill = GetSkillRank(SKILL_TREAT_INJURY,GetPartyMemberByIndex(2));
             nBonusStat = GetAbilityModifier(ABILITY_WISDOM,GetPartyMemberByIndex(2));
          }
       }
    }

    if(nItem == 64)
    {
        nSkill = 10 + nSkill + nBonusSkill/2 + GetAbilityModifier(ABILITY_WISDOM) + nBonusStat/2;
    }
    else if(nItem == 65)
    {
        nSkill = 20 + (nSkill * 2) + nBonusSkill + GetAbilityModifier(ABILITY_WISDOM) + nBonusStat/2;
    }
    else if(nItem == 66)
    {
        nSkill = 30 + (nSkill * 3) + (nBonusSkill*3)/2 + GetAbilityModifier(ABILITY_WISDOM) + nBonusStat/2;
    }
    else if(nItem == 67)
    {
        Sp_RemoveSpecificEffect(EFFECT_TYPE_POISON, OBJECT_SELF);
        bHeal = FALSE;
    }
    else if(nItem == 84)
    {
        nSkill = GetSkillRank(SKILL_REPAIR) + GetAbilityModifier(ABILITY_INTELLIGENCE) + 15;
    }
    else if(nItem == 127)
    {
        nSkill = (GetSkillRank(SKILL_REPAIR) * 2 ) + GetAbilityModifier(ABILITY_INTELLIGENCE) + 25;
    }
    else if(nItem == 128)
    {
        nSkill = (GetSkillRank(SKILL_REPAIR) * 3 ) + GetAbilityModifier(ABILITY_INTELLIGENCE) + 35;
    }
    else if(nItem == 129)//Recovery Stim
    {
        bHeal = FALSE;
        int nHeal = 10;
        effect eVis =  EffectVisualEffect(VFX_IMP_CURE);
        int nCnt = 0;
        object oParty;

        oParty = GetPartyMemberByIndex(nCnt);
        while(nCnt < 3)
        {
            if(GetIsObjectValid(oParty))
            {
                if(GetIsDead(oParty))
                {
                    ApplyEffectToObject(DURATION_TYPE_INSTANT, EffectResurrection(), oParty);
                }
                ApplyEffectToObject(DURATION_TYPE_INSTANT, eVis, oParty);
                ApplyEffectToObject(DURATION_TYPE_INSTANT, EffectHeal(nHeal), oParty);
            }
            nCnt++;
            oParty = GetPartyMemberByIndex(nCnt);
        }
    }

    if(GetHasFeat(FEAT_SECOND_WIND,OBJECT_SELF))
    {
      if (bDying == TRUE)
      {
         nSkill = nSkill*2;  
      }
    }

    if(bHeal == TRUE)
    {
        eHeal = EffectHeal(nSkill);
        ApplyEffectToObject(DURATION_TYPE_INSTANT, eHeal, GetSpellTarget());
        if(GetTag(OBJECT_SELF) == "HK47")
        {
            ApplyEffectToObject(DURATION_TYPE_INSTANT, EffectVisualEffect(1048), OBJECT_SELF);
        }
    }
}
