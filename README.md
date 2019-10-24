#### Warma's loot filter

A semi-minimal loot filter without intrusive visuals.

#### Concept

This loot filter is designed to be rather minimal - it only deviates slightly from the game's initial visual style and
aims to show almost all items which could be of any value. It shows all rares and most relevant crafting recipes,
but further highlights more useful itemns.

In addition, as it was designed during the era when loot filters were still big resource hogs, the script is designed
to be more lightweight than any of the other filters I've tried so far. This means that there is only light economic
filtering implemented at the moment - currently only for Divination Cards.

#### Main features

* Moderately reduced clutter. White or magic items except for the very best maxlvl bases are never ever shown, not even while leveling.
* Rares are always shown. There is colour- and font size coding for chaos- and regal-recipe worthy rares and rares with good bases. Rares ineglible for chaos recipe are faded.
* Currency font size is large. I want to make currency picking easy, because I'm OCD enough to pick anything better than an orb of Alteration. Weakest currencies are faded.
* Everything is sound-coded based on type. Currency is also sound-coded based on value. Apart from the currency, there is no economic tiering.
* Recipes for chromatics, glassblowers, jewelers and chisels are displayed.
* Non-quality flasks are not shown, except for special flasks.
* Chancing recipes are NOT highlighted by default. Edit the relevant block to alter this.
* Strict version hides all but the best rares, some crafting recipes and some currency shards.

#### Visual features

* From a visual design perspective, colors are used more liberally than in the base game, which may be a problem for purists. However, they are made to be distinctive and color by item type exclusively. Brighness signifies value within a type.
* Jewels, uniques, rares, currency etc. use something akin to their default ingame colour scheme, except brighter. Special items which do not have a default scheme, have been coloured to be easily distinguishable.
* Most backgrounds are coloured, unlike in the base game. Typically the background color is a darker version of the base colour.

#### Items shown as good bases

"Siege Axe" "Vaal Hatchet" "Runic Hatchet"
"Ezomyte Axe" "Vaal Axe" "Fleshripper"
"Thicket Bow" "Imperial Bow" "Harbinger Bow"
"Eye Gouger" "Imperial Claw" "Terror Claw" "Gemini Claw"
"Ambusher" "Platinum Kris" "Imperial Skean" "Sai"
"Legion Hammer" "Nightmare Mace" "Behemoth Mace"
"Opal Sceptre" "Void Sceptre" "Sambar Sceptre"
"Piledriver" "Meatgrinder" "Terror Maul" "Coronal Maul"
"Lathi" "Judgement Staff" "Eclipse Staff"
"Corsair Sword" "Eternal Sword" "Tiger Hook"
"Spiraled Foil" "Jewelled Foil" "Dragoon Sword"
"Reaver Sword" "Lion Sword" "Exquisite Blade"
"Imbued Wand" "Opal Wand" "Prophecy Wand" "Profane Wand"
"Royal Burgonet" "Eternal Burgonet"
"Sinner Tricorne" "Lion Pelt"
"Hubris Circlet"
"Pig-Faced Bascinet" "Nightmare Bascinet"
"Prophet Crown" "Praetor Crown"
"Vaal Mask" "Deicide Mask"
"Astral Plate" "Glorious Plate"
"Zodiac Leather" "Assassin's Garb"
"Vaal Regalia"
"Full Dragonscale" "Triumphant Lamellar"
"Saint's Hauberk" "Saintly Chainmail"
"Sadist Garb" "Carnal Armour"
"Sacrificial Garb"
"Vaal Greaves" "Titan Greaves"
"Stealth Boots" "Slink Boots"
"Sorcerer Boots"
"Dragonscale Boots"
"Crusader Boots"
"Murder Boots"
"Vaal Gauntlets" "Titan Gauntlets"
"Stealth Gloves" "Slink Gloves"
"Sorcerer Gloves"
"Dragonscale Gauntlets"
"Crusader Gloves"
"Murder Mitts"
"Crusader Buckler" "Imperial Buckler"
"Fossilised Spirit Shield" "Harmonic Spirit Shield" "Titanium Spirit Shield"
"Spike-Point Arrow Quiver" "Broadhead Arrow Quiver"

### Special bases ###

"Bone Helmet" "Convoking Wand" "Fingerless Silk Gloves" "Gripped Gloves" "Sacrificial Garb" "Spiked Gloves" "Two-Toned Boots"

### Items not shown as good bases but which are regardless decent in their class

"Hydrascale Boots" "Legion Boots" "Assassin's Boots" "Hydrascale Gauntlets" "Legion Gloves" "Assassin's Mitts" "Ezomyte Tower Shield" "Crusader Buckler" "Imperial Buckler" "Cardinal Round Shield" "Champion Kite Shield" "Archon Kite Shield" "Mirrored Spiked Shield" "Supreme Spiked Shield"

#### Items shown as good bases

"Siege Axe" "Runic Hatchet" "Vaal Axe" "Fleshripper" "Thicket Bow" "Imperial Bow" "Maraketh Bow" "Harbinger Bow" "Imperial Claw" "Gemini Claw" "Ambusher" "Platinum Kris" "Imperial Skean" "Sai" "Auric Mace" "Nightmare Mace" "Behemoth Mace" "Piledriver" "Meatgrinder" "Coronal Maul" "Opal Sceptre" "Void Sceptre" "Sambar Sceptre" "Vaal Sceptre" "Lathi" "Eclipse Staff" "Maelström Staff" "Judgement Staff" "Corsair Sword" "Eternal Sword" "Tiger Hook" "Harpy Rapier" "Spiraled Foil" "Jewelled Foil" "Reaver Sword" "Exquisite Blade" "Imbued Wand" "Opal Wand" "Prophecy Wand" "Profane Wand" "Royal Burgonet" "Eternal Burgonet" "Sinner Tricorne" "Lion Pelt" "Hubris Circlet" "Pig-Faced Bascinet" "Nightmare Bascinet" "Praetor Crown" "Deicide Mask" "Astral Plate" "Glorious Plate" "Zodiac Leather" "Assassin's Garb" "Vaal Regalia" "Full Dragonscale" "Triumphant Lamellar" "Saintly Chainmail" "Sadist Garb" "Carnal Armour" "Vaal Greaves" "Titan Greaves" "Stealth Boots" "Slink Boots" "Sorcerer Boots" "Dragonscale Boots" "Crusader Boots" "Murder Boots" "Vaal Gauntlets" "Titan Gauntlets" "Stealth Gloves" "Slink Gloves" "Sorcerer Gloves" "Dragonscale Gauntlets" "Crusader Gloves" "Murder Mitts" "Colossal Tower Shield" "Fossilised Spirit Shield" "Harmonic Spirit Shield" "Titanium Spirit Shield" "Spike-Point Arrow Quiver"

#### Items considered special jewellry bases

"Blue Pearl Amulet" "Cerulean Ring" "Crystal Belt" "Marble Amulet" "Opal Ring" "Steel Ring" "Stygian Vise" "Vanguard Belt" "Vermillion Ring"

#### Alert Sounds

* **Maps:** 2
* **Map fragements:** 11
* **Low currency shards:** 12 (alchemy, binding, chaos, engineer, horizon, regal)
* **High currency shards:** 16 (ancient, annullment, exalted, harbinger)
* **Low Currency:** 3 (jeweler/chisel/alch/chance/binding/horizon)
* **Mid Currency:** 1 (blessed, chaos, fusing, gcp, regal, scour, vaal)
* **High currency:** 13 (ancient, annullment, harbinger)
* **Super currency:** 5 (exa, divine)
* **Mirror of Kalandra:** 5 (really loud)
* **Cards:** 7
* **Uniques:** 6
* **Prophecies and Silver coins:** 9
* **Special crafting bases or items with craft-enabling or rare mods:** 14
* **League-specific items (in base game):** 8 (essences, breach items)
* **League-specific items (not in base game):** 15 (perandus coins, talismans, leaguestones)
* **Links>=6:** 4 
* **Sockets=6:** 10

#### Acknowledgements

Initally based on Ziggy's filter as it were in 2015. Heavily edited with Filtration and later on by hand.
Economic tiering for Divination Cards is taken from Neversink's filter and slightly edited to match my preferences. It will likely be updated by hand in the future.