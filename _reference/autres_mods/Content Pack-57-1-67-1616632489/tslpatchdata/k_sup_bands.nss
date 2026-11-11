//:: k_sup_bands
/*
    This is the generic script to run all
    forearm bands in the game

99  Energy Shield               Protects against energy weapons.  Damage Resistance 5.  Up to 50 damage.
100 Sith Energy Shield          Protects against energy weapons and sonic attacks. Damage Resistance 5. Up to 50 damage.
101 Arkanian Energy Shield      Protects against energy, sonic, cold and fire attacks. Damage Resistance 5. Up to 50 damage.
102 Echani shield               Protects against energy weapons.   Damage resistance 10.  Up to 50 damage.
103 Mandalorian melee           Damage Resistance 5.  Up to 50 damage.
104 Mandalorian power shield    Protects against energy weapons and physical damage.   Damage resistance 10.  Up to 50 damage.
105 Echani dueling shield       Protects against energy weapons.   Damage resistance 10.  Up to 100 damage.
106 Yusanis? Modified dueling shield    Protects against energy weapons.   Damage resistance 15.  Up to 100 damage.
107 Proto-type Verpine Energy shield    Protects against energy, sonic, cold and fire attacks. Damage Resistance 10. Up to 100 damage.
110 Droid 1 Energy
111 Droid 2 Energy
112 Droid 3 Energy
113 Droid 1 Hazard
114 Droid 2 Hazard
115 Droid 3 Hazard
132 Heat shield                 - Protects against energy weapons and heat damage. - RWT 12/08/03
*/
//:: Created By: Preston Watamaniuk
//:: Copyright (c) 2002 Bioware Corp.

#include "k_inc_debug"
#include "k_inc_constant"

void main()
{
    int nIndex = GetSpellId();

    int nShield;
    int nIcon;
    int nBoost;


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


    if(nIndex == 99) //SHIELD_ENERGY
    {
        nIcon = 45;    

        if (nBoost > 0)
        {
          nShield = BOOST_ENERGY + (nBoost-1);
        }           
        else
        {
           nShield = 6;
        }
    }
    else if(nIndex == 100) //SHIELD_ENERGY_SITH
    {
        nIcon = 46;

        if (nBoost > 0)
        {
          nShield = BOOST_ENERGY_SITH + (nBoost-1);
        }           
        else
        {
           nShield = 7;
        }
    }
    else if(nIndex == 101) //SHIELD_ENERGY_ARKANIAN
    {
        nIcon = 47;

        if (nBoost > 0)
        {
          nShield = BOOST_ENERGY_ARKANIAN + (nBoost-1);
        }           
        else
        {
           nShield = 8;
        }
    }
    else if(nIndex == 102) //SHIELD_ECHANI
    {
        nIcon = 48;

        if (nBoost > 0)
        {
          nShield = BOOST_ECHANI + (nBoost-1);
        }           
        else
        {
           nShield = 9;
        }
    }
    else if(nIndex == 103) //SHIELD_MANDALORIAN_MELEE
    {
        nIcon = 49;

        if (nBoost > 0)
        {
          nShield = BOOST_MANDALORIAN_MELEE + (nBoost-1);
        }           
        else
        {
           nShield = 10;
        }
    }
    else if(nIndex == 104) //SHIELD_MANDALORIAN_POWER
    {
        nIcon = 50;

        if (nBoost > 0)
        {
          nShield = BOOST_MANDALORIAN_POWER + (nBoost-1);
        }           
        else
        {
           nShield = 11;
        }
    }
    else if(nIndex == 105) //SHIELD_DUELING_ECHANI
    {
        nIcon = 51;

        if (nBoost > 0)
        {
          nShield = BOOST_DUELING_ECHANI + (nBoost-1);
        }           
        else
        {
           nShield = 12;
        }
    }
    else if(nIndex == 106) //SHIELD_DUELING_YUSANIS
    {
        nIcon = 52;
        if (nBoost > 0)
        {
          nShield = BOOST_DUELING_YUSANIS + (nBoost-1);
        }           
        else
        {
           nShield = 13;
        }
    }
    else if(nIndex == 107) //SHIELD_VERPINE_PROTOTYPE
    {
        nIcon = 53;

        if (nBoost > 0)
        {
          nShield = BOOST_VERPINE_PROTOTYPE + (nBoost-1);
        }           
        else
        {
           nShield = 14;
        }
    }
    else if(nIndex == 110) //SHIELD_DROID_ENERGY_1
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
    else if(nIndex == 111) //SHIELD_DROID_ENERGY_2
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
    else if(nIndex == 112) //SHIELD_DROID_ENERGY_3
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
    else if(nIndex == 113) //SHIELD_DROID_ENVIRO_1
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
    else if(nIndex == 114) //SHIELD_DROID_ENVIRO_2
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
    else if(nIndex == 115) //SHIELD_DROID_ENVIRO_3
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
    else if(nIndex == 132) //SHIELD_HEAT
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


    float fDuration = 200.0;
	
	if (GetHasFeat(FEAT_APPLIED_KNOWLEDGE,OBJECT_SELF))
	{
		int nRepairSkill = GetSkillRank( SKILL_REPAIR, OBJECT_SELF);
		int nRepairMod = GetAbilityModifier( ABILITY_INTELLIGENCE, OBJECT_SELF);
		if( nRepairSkill > 0 )
		{
			fDuration += 2.0 * (nRepairSkill + nRepairMod);
		}
	}

    effect eShield = EffectForceShield(nShield);
    eShield = SetEffectIcon(eShield, nIcon);
    ApplyEffectToObject(DURATION_TYPE_TEMPORARY, eShield, GetSpellTargetObject(), fDuration);
}
