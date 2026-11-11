
int StartingConditional()
{
    int iPayday;

    if(GetGlobalNumber("Bounty_Beast") > 0 || GetGlobalNumber("Bounty_Normal") > 0 || GetGlobalNumber("Bounty_Jedi") > 0)
    {
        return TRUE;
    }
    return FALSE;

}
