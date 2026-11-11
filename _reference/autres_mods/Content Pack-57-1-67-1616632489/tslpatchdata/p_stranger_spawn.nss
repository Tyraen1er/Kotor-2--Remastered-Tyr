void main()
{
	int nRandom;
	int nStrangerHead = GetGlobalNumber("Stranger_Head");
	int nStrangerSaber = GetGlobalNumber("Stranger_Saber");
	int nAppearance = 91;
	object oSaber;
	
	if (nStrangerHead == 0)
	{
		SetGlobalNumber("Stranger_Head", 1 + Random(105));	
		nStrangerHead = GetGlobalNumber("Stranger_Head");		
	}
	
	if (nStrangerHead < 91)
	{
		nAppearance = 90 + nStrangerHead;
	}
	else if (nStrangerHead >= 91 && nStrangerHead < 97)
	{
		nAppearance = 543 + (nStrangerHead - 91);
	}
	else if (nStrangerHead >= 97 && nStrangerHead < 100)
	{
		nAppearance = 578 + (nStrangerHead - 97);
	}
	else if (nStrangerHead >= 100)
	{
		nAppearance = 663 + (nStrangerHead - 100);
	}
	
	if (GetGlobalNumber("Stranger_Saber") == 0)
	{
		SetGlobalNumber("Stranger_Saber", 1 + Random(9));	
		nStrangerSaber = GetGlobalNumber("Stranger_Saber");
	}
	
	if (GetGoodEvilValue(OBJECT_SELF) <= 30)
	{
		oSaber = CreateItemOnObject("g_w_lghtsbr02", OBJECT_SELF);
	}
	else
	{
		switch (nStrangerSaber)
		{
			case 1:
			oSaber = CreateItemOnObject("g_w_lghtsbr01", OBJECT_SELF);
			break;
		
			case 2:
			oSaber = CreateItemOnObject("g_w_lghtsbr03", OBJECT_SELF);
			break;
		
			case 3:
			oSaber = CreateItemOnObject("g_w_lghtsbr04", OBJECT_SELF);
			break;
		
			case 4:
			oSaber = CreateItemOnObject("g_w_lghtsbr05", OBJECT_SELF);
			break;
		
			case 5:
			oSaber = CreateItemOnObject("g_w_lghtsbr07", OBJECT_SELF);
			break;
		
			case 6:
			oSaber = CreateItemOnObject("g_w_lghtsbr08", OBJECT_SELF);
			break;
		
			case 7:
			oSaber = CreateItemOnObject("g_w_lghtsbr09", OBJECT_SELF);
			break;
		
			case 8:
			oSaber = CreateItemOnObject("g_w_lghtsbr10", OBJECT_SELF);
			break;
		
			case 9:
			oSaber = CreateItemOnObject("g_w_lghtsbr11", OBJECT_SELF);
			break;		
		}
	}
	
	ChangeObjectAppearance(OBJECT_SELF, nAppearance);
	ActionEquipItem(oSaber, INVENTORY_SLOT_RIGHTWEAPON, 1);	
}