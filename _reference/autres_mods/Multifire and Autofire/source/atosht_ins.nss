//////////////////////////////////////////////////////////////////////////////////
/*	Multifire and Autofire

	This file can be used as a conditional in other mods
	
	If ATOSHT is installed, the the conditional will return true
	otherwise it will not exist, and will return false
	
	It can also be used as an ExecuteScript, followed by
	GetGlobalBoolean("ATOSHT_INS")
	to check if ATOSHT is installed
	If it is not installed the execute will fail, and the
	global will return false.
	
	darthbdaman 2025-04-19														*/
//////////////////////////////////////////////////////////////////////////////////

int StartingConditional()
{
	SetGlobalBoolean("ATOSHT_INS", TRUE);
    return TRUE;
}