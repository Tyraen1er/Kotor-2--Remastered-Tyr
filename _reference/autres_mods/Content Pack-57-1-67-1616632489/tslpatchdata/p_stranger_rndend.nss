
#include "k_inc_summon"
#include "k_inc_switch"
#include "k_inc_constant"

void main()
{
	CheckForUnsummon();
    ExecuteScript("k_ai_master", OBJECT_SELF, KOTOR_DEFAULT_EVENT_ON_COMBAT_ROUND_END);
}