
void main ()
{
	int nBeast;
	int nNormal;
	int nJedi;
	int nTotal;
	
	nBeast = GetGlobalNumber("Bounty_Beast") + GetGlobalNumber("Bounty_Beast_Overflow");
	nBeast = nBeast * 5;
	
	nNormal = GetGlobalNumber("Bounty_Normal") + GetGlobalNumber("Bounty_Normal_Overflow");
	nNormal = nNormal * 10;
	
	nJedi = GetGlobalNumber("Bounty_Jedi") + GetGlobalNumber("Bounty_Jedi_Overflow");
	nJedi = nJedi * 20;
	
	nTotal = nBeast + nNormal + nJedi;
	
	SetGlobalNumber("Bounty_Beast", 0);
	SetGlobalNumber("Bounty_Beast_Overflow", 0);
	SetGlobalNumber("Bounty_Normal", 0);
	SetGlobalNumber("Bounty_Normal_Overflow", 0);
	SetGlobalNumber("Bounty_Jedi", 0);
	SetGlobalNumber("Bounty_Jedi_Overflow", 0);
	
	GiveGoldToCreature(GetFirstPC(), nTotal);
	
}