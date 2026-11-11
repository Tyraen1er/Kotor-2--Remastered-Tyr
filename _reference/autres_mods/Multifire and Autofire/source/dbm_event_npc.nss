//////////////////////////////////////////////////////////////////////////////////
/*	darthbdaman npc combat event runner

	This is a unified npc event runner for all of my mods
	
	It runs the various execute scripts that they rely on
	
	If an execute script does not exist, it will be skipped,
	allowing for easy patchless compatbility
	
	Currently Supports
	- Feat Restoration and Rebalance
	- Multifire and Autofire
	- Sentinel Sneak Attack with Multiclassing
	
	darthbdaman 2025-04-21														*/
//////////////////////////////////////////////////////////////////////////////////

void main() {
	ExecuteScript("atosht_heart", OBJECT_SELF);
}