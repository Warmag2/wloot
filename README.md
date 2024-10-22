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
"Eye Gouger" "Imperial Claw" "Terror Claw" "Gemini Claw"
"Ambusher" "Sai"
"Platinum Kris" "Imperial Skean"
"Legion Hammer" "Nightmare Mace" "Behemoth Mace"
"Opal Sceptre" "Void Sceptre" "Sambar Sceptre"
"Corsair Sword" "Eternal Sword" "Tiger Hook"
"Spiraled Foil" "Jewelled Foil" "Dragoon Sword"
"Imbued Wand" "Opal Wand" "Profane Wand"
"Despot Axe" "Fleshripper"
"Thicket Bow" "Imperial Bow" "Harbinger Bow"
"Reaver Sword" "Lion Sword" "Exquisite Blade"
"Piledriver" "Meatgrinder" "Coronal Maul"
"Maelström Staff" "Judgement Staff" "Eclipse Staff"
"Astral Plate" "Glorious Plate" "Titan Plate" "Legion Plate"
"Zodiac Leather" "Assassin's Garb" "Supreme Leather" "Astral Leather"
"Vaal Regalia" "Arcane Vestment" "Nightweave Robe"
"Full Dragonscale" "Triumphant Lamellar" "Full Wyvernscale" "Marshall's Brigandine"
"Saint's Hauberk" "Saintly Chainmail" "Grand Ringmail" "Paladin's Hauberk"
"Sadist Garb" "Carnal Armour" "Sanguine Raiment" "Torturer Garb"
"Sacrificial Garb"
"Titan Greaves" "Precursor Greaves"
"Slink Boots" "Harpyskin Boots"
"Sorcerer Boots" "Sage Slippers"
"Dragonscale Boots" "Chimerascale Boots"
"Crusader Boots" "Martyr Boots"
"Murder Boots" "Infiltrator Boots"
"Titan Gauntlets" "Precursor Gauntlets"
"Slink Gloves" "Harpyskin Gloves"
"Sorcerer Gloves" "Sage Gloves"
"Dragonscale Gauntlets" "Chimerascale Gauntlets"
"Crusader Gloves" "Martyr Gloves"
"Murder Mitts" "Infiltrator Mitts"
"Royal Burgonet" "Eternal Burgonet" "General's Helmet" "Conqueror's Helmet"
"Sinner Tricorne" "Lion Pelt" "Dire Pelt" "Grizzly Pelt"
"Hubris Circlet" "Moonlit Circlet" "Sunfire Circlet"
"Pig-Faced Bascinet" "Nightmare Bascinet" "Knight Helm" "Conquest Helmet"
"Prophet Crown" "Praetor Crown" "Faithful Helmet" "Paladin Crown"
"Vaal Mask" "Deicide Mask" "Jester Mask" "Ancient Mask"
"Crusader Buckler" "Imperial Buckler" "Fossilised Spirit Shield" "Harmonic Spirit Shield" "Titanium Spirit Shield" "Supreme Spiked Shield" "Archon Kite Shield"
"Artillery Quiver" "Blazing Arrow Quiver" "Broadhead Arrow Quiver" "Heavy Arrow Quiver" "Primal Arrow Quiver" "Spike-Point Arrow Quiver" "Vile Arrow Quiver"

### Special bases ###

"Psychotic Axe" "Void Fangs" "Pneumatic Dagger" "Infernal Blade" "Boom Mace" "Alternating Sceptre" "Anarchic Spiritblade" "Accumulator Wand" "Apex Cleaver" "Solarine Bow" "Impact Force Propagator" "Banishing Blade" "Battery Staff" "Eventuality Rod" "Convoking Wand" "Royal Plate" "Syndicate's Garb" "Twilight Regalia" "Conquest Lamellar" "Sacred Chainmail" "Necrotic Armour" "Brimstone Treads" "Leviathan Greaves" "Stormrider Boots" "Velour Boots" "Dreamquest Slippers" "Warlock Boots" "Wyvernscale Boots" "Paladin Boots" "Fugitive Boots" "Phantom Boots" "Two-Toned Boots" "Spiked Gloves" "Thwarting Gauntlets"  "Leviathan Gauntlets" "Gripped Gloves" "Trapsetter Gloves" "Velour Gloves" "Fingerless Silk Gloves" "Nexus Gloves" "Warlock Gloves" "Wyvernscale Gauntlets" "Apothecary's Gloves" "Paladin Gloves" "Phantom Mitts" "Giantslayer Helmet" "Majestic Pelt" "Lich's Circlet" "Penitent Mask" "Haunted Bascinet" "Bone Helmet" "Archdemon Crown" "Divine Crown" "Blizzard Crown" "Torturer's Mask" "Heat-Attuned Tower Shield"

#### Special jewellry bases

"Astrolabe Amulet" "Blue Pearl Amulet" "Focused Amulet" "Marble Amulet" "Seaglass Amulet" "Simplex Amulet" "Bone Ring" "Cerulean Ring" "Cogwork Ring" "Composite Ring" "Geodesic Ring" "Helical Ring" "Iolite Ring" "Manifold Ring" "Nameless Ring" "Penumbra Ring" "Ratcheting Ring" "Shadowed Ring" "Opal Ring" "Steel Ring" "Vermillion Ring" "Crystal Belt" "Golden Obi" "Mechalarm Belt" "Micro-Distillery Belt" "Stygian Vise" "Vanguard Belt"

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
