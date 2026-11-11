Multifire, Autofire, and Superior Feats (TSL)

Author: darthbdaman
Contact: darth@darthbdaman.com

Current Version: v1.2.0

Release Date: September 20, 2025
Prior Version Release Date: May 3, 2025
Original Release Date: April 23, 2025

Summary:

	In the original Star Wars d20 roleplaying game that KotOR is very loosely based off of, the Blaster Rifle type and
	Repeating Blaster types had unique functions that allowed them to make multiple attacks per round, at a penalty.
	
	KotOR was originally going to include a similar function for the Heavy Weapons group, but it is unimplemented,
	leaving Heavy Weapons as generally equivalent or inferior to Blaster Rifles. There are multiple mods which have
	attempted to restore this, but they are generally buggy, have awkward interactions with force speed, and only seek
	to restore the game functionality, and do not attempt to expand into the areas covered by the original roleplaying game.
	
	This mod implements the bonus attacks and penalties for using multifire (Blaster Rifles) and autofire (Heavy Weapons).
	Multifire allows making one extra attack per round, but all attacks made during the round suffer a -4 attack penalty.
	Autofire allows making two extra attacks per round, but all attacks made during the round suffer a -6 attack penalty.
	Unlike in the roleplaying game, these are not optional, and cannot be toggled off.
	
	These penalties can be offset however. Inspired by feats in the roleplaying game, and how KotOR adapted other feats,
	this mod implements a new Multishot feat tree, which has 3 ranks, which increase attack when using Rifles or Heavy Weapons
	by +2, +1, and +1 respectively. This tree acts as an equivalent to Two-Weapon Fighting and Dueling for these weapons.
	
	Due to hardcoded limitations with how extra attacks can be granted within the game, Rifles and Heavy Weapons can never
	make more than 3 attack when using Power Blast or Sniper Shot, or making a regular attack. Rapid Shot can grant a
	maximum of 4 attacks. If Master Speed (or Fury) is used, these limitations will obviously be a problem. As a solution,
	this mod will automatically reduce the penalties of multifire and autofire depending on how many attacks the player
	should have. For example, if Knight Speed (or Improved Fury) is used with a Blaster Rifle, both attacks will stack
	properly, and will all be made at a -4 penalty, while if Master Speed (or Master Fury) is used with a Heavy Weapon,
	autofire will be disabled, and 3 attacks will be made without any penalty being suffered. The Multishot feat will continue
	to increase attack bonus while Speed is active.
	
	One the (many) complaints made about characters options in TSL, is the extreme disparity in feats support for different
	options. Two-Weapon Fighting and Lightsabers get high level advanced feats on the Weapon Master and Marauder, but no other
	options are available. This mod corrects that, by adding Superior Weapon Focus feats for Blaster Pistols, Blaster Rifles, and
	Melee Weapons. It also adds a Superior Dueling line, as well as a Superior Multishot line, to continue the earlier tree introduced
	by this mod. The Focus feats all add +1 to attack rolls per level, while the Dueling feats add +1-4 to damage, and  +1 to attacks
	rolls and AC perk rank. The AC bonus is implemented as a Shield Bonus (i.e. think a magical shield from Neverwinter Nights).
	This should stack with all other AC bonuses. The Superior Multishot tree, grants +1, +1, and +2 to attack rolls respectively.
	
	The bug that allows Finesse: Melee Weapons to affect Lightsabers is fixed. The bonus from that feat will be removed if the
	character has Finesse: Melee Weapons, but not Finesse: Lightsaber. Either feat will allow Dexterity modifier to be added to
	attack rolls for Unarmed attacks as well, as there was previously no way to do this.
	
	All of these changes are implemented in a heartbeat script, that runs every second on the player and companions,
	and on NPCs during combat events. You will have to close the inventory and reopen it after changing your equipment,
	to make sure that all of the effects are properly applied. This is the only way of doing changes like this unfortunately.

Install/Uninstall:

	Run the installer.exe file. If you are on Linux or Mac, appropriate HoloPatcher installers can be found on DeadlyStream.

	During install you can choose to install 4 different versions of the mod. Only install 1 of them at at time. The different
	options allow you to apply multiple attacks to both Heavy Weapons and Rifles, give only Heavy Weapons 3 attacks or 2 attacks,
	and to install a version that does not give additional attacks to either, only adding the various feat changes and new feats
	from this mod. The options that add extra attacks to a weapon type, will reduce that weapons damage to match KotOR 1.
	
	See the docs folder for more information.

Compatibility:
	
	This mod uses a k_ai_master.ncs Heartbeat script and will likely have compatibility issues with
	other mods that use similar implementations. They will likely need compatibility patching.
	
	Fully compatible with Improved AI (ver 1.2.3 or higher). You must install Improved AI AFTER all of my mods, and let its k_ai_master.ncs file replace mine.
	
	This mod is included in my Feat Restoration and Class Rebalance mod, and this version is therefore not compatible.

	See the mod page for updated compatibility information.

Special Thanks/Acknowledgements:

	KOTOR Tool – Fred Tetra
	DeNCS – JdNoa & Dashus
	DLGEditor – tk102
	K-GFF – tk102
	TSL Patcher – stoffe
	KotOR Scripting Tool - Blue
	Holocron Toolset and HoloPatcher – Cortisol & th3w1zard1
