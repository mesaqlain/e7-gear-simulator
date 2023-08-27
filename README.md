# Epic Seven Gear Simulator

## 1 Intro
This is an ongoing project to create an app in python that will simulate the generation of items (better known as gear in the community), same as those found in the mobile game Epic Seven. The app has the following functionalities:
* **Create** an item (either completely random or specific attributes)
* **Enhance** an item
* **Reforge** an item
* **Modify** an item
* Each of the features mentioned above follows restrictions regarding **stats** (such as which stats are allowed on a specific type of gear)

The features are explained in depth in their respective sections.

## 2 Requirements / Imports
* No external libraries required to use this package.
* pandas (only for data_prep modules in /data folder)
* DeepDiff (only for certain test modules)

## 3 Useage / Directions

### 3.1 Creating a Gear

Use the notebook [Epic7GearSimulator](https://github.com/mesaqlain/e7_items/blob/main/Epic7GearSimulator.ipynb) to run the codes. The notebook also shows some examples.

**Create a Random Gear**
1. The Gear class needs to be imported from /src/gear.py.
2. First instantiate a Gear() object, e.g. `gear = Gear()`
3. You can create a new completely random gear if you don't provide any parameters using the method `.create_gear()`, e.g. `gear.create_gear()`.
4. Chaining the method `.print_gear()` will show the gear contents, e.g. `gear.create_gear().print_gear()`.
5. You can **enhance** a gear by 1 level by using the method `.enhance_gear()`, e.g. `gear.enhance_gear().print_gear()`. (details in section 6.1)
    * You can also enhance a gear to +15 directly by using the `enhance_gear_max()` method; this only works on +0 gear (gear that has not been enhanced at all).
6. Once a gear has been enhanced to +15, you have options to reforge or modify a gear.
7. You can **reforge** a gear by using the `.reforge_gear()` method, e.g. `gear.reforge_gear().print_gear()`. (details in section 6.2)
8. You can **modify** a gear (before or after reforge) by using the method `.modify_gear()`. (details in section 6.3)
    * modify_gear() takes in 3 arguments - stat_index, mod_stat_id, and mod_type.
    * **stat_index** is a number from 1 to 4, indicating which substat on the gear you want to replace.
    * **mod_stat_id** is the index of the stat you want to replace with (details on which id refers to which stat in section 5.1).
    * **mod_type** is 'greater' by default. Another option is 'lesser'.
    * e.g. `gear.modify_gear(1, 10).print_gear` - modify the 1st substat on the gear with the Speed substat (and mod_type is greater by default).
    * Please note that usual restrictions apply when trying to add a new substat to a gear (such as no duplicates allowed, must be available in the available pool of substats for the gear_type).
    * Once you modify a gear, you are only allowed to further modify the already modified substat; other substats on that gear are now fixed in stone and may not be modified.

**Create a Gear with Specific Attributes**
1. `from src.gear import Gear`
2. `gear = Gear()`
3. `.create_gear()` takes in several arguments -
    * gear_type = 'weapon', 'helm', 'armor', 'necklace', 'ring', or 'boots'. If none provided, it randomly selects one. (details in section 4.1)
    * gear_grade = 'rare', 'heroic', 'epic'. (details in section 4.4)
    * gear_set = If none provided, randomly selects one. Check section 4.2 for available gear sets.
    * gear_level = Default is 85, but accepts any level between 58 and 100.
    * mainstat_id = An integer containing one of the stat id's from 0 to 10. If none provided, it'll randomly select an id that is in the available pool of mainstats for the gear_type; it'll also not select any mainstat that is already in the substats if substats have been provided. (details on which id refers to which stat in section 5.1)
    * substat_ids = List of up to 4 integers (from 0 to 10). If none provided, it'll randomly select **n** id's that are in the available pool of substats for the gear_type, where **n** is the number of starting substats allowed on given (or randomly selected) gear type; it'll also not select any substat that is already in the mainstat if mainstat has been provided. (details on which id refers to which stat in section 5.1)
    * The method will raise an error if trying to add mainstats or substats that are not allowed on a specific gear type, if duplicate substats or more than 4 substats are provided, or if the number of provided substats exceed what is allowed as starting substats for given gear grade. (details in section 5.2)
    * e.g. `gear.create_gear(gear_type='weapon', gear_grade='epic', gear_set='speed', substat_ids=[10, 1, 3]` - create an **Epic** grade, **Speed** set, **Weapon**. Since no level is provided, default 85 is used. Notice that mainstat is not provided, so it'll pick the only available mainstat for weapon gear types - flat attack (or we could have specified mainstat=0). 3 substat id's are provided - Speed, Attack %, and Healtth %, which are all in the available pool of substats for Weapon gear type. The given gear grade is Epic (so there must be 4 starting substats); as we provided only 3 substats, it'll randomly pick the 4th substat following the usual gear restrictions.
4. Once the gear has been created, you can enhance, reforge, or modify as before with the random gear.

A few more examples are shown in the [Epic7GearSimulator](https://github.com/mesaqlain/e7_items/blob/main/Epic7GearSimulator.ipynb) notebook.

### 3.2 Further Customize the Gear
While the above methods of enhancing, reforging and modifying strictly follow the rules in place in the Epic 7 game, you are able to further customize any of the mainstat or substats if you wish by using the methods in the Stat() class.
1. When you create a gear, the gear.mainstat attribute holds one **Stat** object that may be modified using Stat class methods; the gear.substats attribute holds up to 4 **Stat** objects that may be similarly modified.
2. `stat.stat_id` holds the id of the stat (from 0 to 10)
3. `stat.stat_key` holds the stat_key of the stat (check section 5.1 for sta details)
4. `stat.value` holds the value of stat, e.g. `gear.mainstat.value = 100` will set the value of the mainstat to 100.
5. `stat.rolled` holds the count of how many times a stat has been rolled when enhancing, e.g. `gear.substats[0].rolled = 3` will set the rolled count of the 0th index stat to 3.
6. If you do change the rolled count, you may want to update the `stat.reforge_increase` value as well, as it does not update automatically but depends on the rolled count and the stat_type, e.g. `stat.reforge_increase = get_reforge_increase(stat.stat_id, stat.stat_type, stat.rolled)`. get_reforge_increase() function may be found in [utilities.py](https://github.com/mesaqlain/e7_items/blob/main/src/utilities.py)
7. You may also want to enhance stats by choice, in which case you could use the `.enhance_stat()` method, e.g. `gear.substats[0].enhance.stat()` - this will enhance the substat at the 0th index.
8. Finally, you may want to update the display of the text description by using the `.format_stat()` method, e.g. `gear.substats[0].format_stat()`.

A few examples of modifying a stat within the gear is shown in the [Epic7GearSimulator](https://github.com/mesaqlain/e7_items/blob/main/Epic7GearSimulator.ipynb) notebook.
          
### 3.3 Data Preparation
The data preparation modules and the json files created by these modules are found in the /data folder. More information on what values to use from this data is found in sections 4 and 5. The scripts could be modified to add new information as the game gets updated with new sets or tiers.
* [TYPES](https://github.com/mesaqlain/e7_items/blob/main/data/prep_data_TYPES.py): Contains data on gear types.
* [TIERS](https://github.com/mesaqlain/e7_items/blob/main/data/prep_data_TIERS.py): Contains data on gear tiers.
* [GRADES](https://github.com/mesaqlain/e7_items/blob/main/data/prep_data_GRADES.py): Contains data on gear grades.
* [SETS](https://github.com/mesaqlain/e7_items/blob/main/data/prep_data_SETS.py): Contains data on gear sets.
* [STATS](https://github.com/mesaqlain/e7_items/blob/main/data/prep_data_STATS.py): Contains data on the stats that show up on gear.

### 3.4 Testing
The testing modules are found in the [tests](https://github.com/mesaqlain/e7_items/blob/main/tests/) folder. The testing process is documented in this [notebook](https://github.com/mesaqlain/e7_items/blob/main/Epic7GearSimulator_Tests_Documentation.ipynb). 

### 3.5 Upcoming Features
* UI to use this package more conveniently.

## 4 Item / Gear Attributes
Gear in Epic Seven have several attributes: **Type**, **Grade**, **Set**, **Tier** (derived from **Level**), **Main Stats**, and **Sub Stats**.

### 4.1 Type
A gear could be one of the following types (check section on Stats for abbreviations):
* **Weapon**:
  * Mainstat restrictions: Can only have *ATK* as main stat.
  * Substat restrictions: Cannot have *ATK*, *DEF*, or *DEF%* in substats. 
* **Helm**:
  * Mainstat restrictions: Can only have *HP* as main stat.
  * Substat restrictions: Cannot have *HP* in substats. 
* **Armor**:
  * Mainstat restrictions: Can only have *DEF* as main stat.
  * Substat restrictions: Cannot have *ATK*, *ATK%* or *DEF* in substats. 
* **Necklace**:
  * Mainstat restrictions: Cannot have EFF, ER, or SPD as main stat.
  * Substat restrictions: Can have any stat (except for the main stat) in substats. 
* **Ring**:
  * Mainstat restrictions: Cannot have CRIT, CDMG, or SPD as main stat.
  * Substat restrictions: Can have any stat (except for the main stat) in substats. 
* **Boots**:
  * Mainstat restrictions: Cannot have CRIT, CDMG, EFF, or ER as main stat .
  * Substat restrictions: Can have any stat (except for the main stat) in substats.
 
Gear Types data is stored in the **TYPES.json** file. Preparation of the data is found in the *prep_data_TYPES.py* script.

### 4.2 Set
A gear could belong to one of the following sets: Health, Defense, Speed, Attack, Critical, Hit, Destruction, Lifesteal, Counter, Resist, Unity, Rage, Immunity, Revenge, Penetration, Injury, Protection, or Torrent. Each set provides a specific bonus to a stat or adds some status when enough number of gear belonging to the set is equipped by a hero. For instance, equipping 2 pieces of Health set gear provides +15% HP to a hero, equipping 4 pieces of Speed set gear provides +25% SPD, and so on.  

Currently any Gear type / level, or tier can belong to any set, so there are no restrictions regarding sets when it comes to creating an item (unless a set is specified). An additional functionality could be added by specifying which **Hunt** stage each set can be acquired from.

For details on the sets, refer to the *pre_data_SETS.py* script. Gear Sets data is stored in the **SETS.json** file.

### 4.3 Level / Tier

A gear has a **Level** (also referred to as iLvl) range from 1 to 90 currently in the game. This app, however, only allows gear of levels between 58 and 100. This is because the official website does not publish the probability rates for gear of lower levels; additionally, most people would not care to use this app for gear below level 85 anyway.

Depending on the level of the item, the gear is assigned a **Tier**.  Tiers go from 1 to 7 (this app allows use of only Tiers 5-7. The Tier affects the possible roll ranges of the stats, so it is an important attribute. Higher tier gear are more likely to roll a higher value for a stat compared to a lower tier gear.

The tiers we have published rates for and use in this app are:
* Tier 5: Levels 58-71
* Tier 6: Levels 72-85
* Tier 7: Levels 86-100

Level is an important restriction when it comes to **Reforging** a gear. Only Level 85 gear may be reforged.

Gear Tiers data is stored in the **TIERS.json** file. Preparation of the data is found in the *prep_data_TIERS.py* script.

### 4.4 Grade

A gear could be one of the following grades:
* **Normal**:
  * Starting Substats: 0
  * Color: White
  * Weight: 0
* **Good**:
  * Starting Substats: 1
  * Color: Green
  * Weight: 0
* **Rare**:
  * Starting Substats: 2
  * Color: Blue
  * Weight: 0.35
* **Heroic**:
  * Starting Substats: 3
  * Color: Purple
  * Weight: 0.53
* **Epic**:
  * Starting Substats: 4
  * Color: Red
  * Weight: 0.12
 
The color attribute is not currently implemented or used. The max number of substats for any grade of gear is currently 4 in the game. The weight refers to the probability of acquiring a certain grade of gear when an item is randomly generated. These numbers are taken from the crafting section of the game. So, when an item is randomly generated without specifying the grade, there is a 35% probability that it will be a Rare gear with 2 starting substats, 53% probability that it will be a Heroic gear with 3 starting substats, and 12% probability that it will be an Epic gear with 4 (max) starting substats.

Gear Grade also affect the roll ranges and corresponding probability rates, so it has additional useage outside of specifying starting substats.

Gear Grades data is stored in the **GRADES.json** file. Preparation of the data is found in the *prep_data_GRADES.py* script.

## 5 Stats
### 5.1 Stat Descriptions

Currently, gear in Epic Seven can have the following stats as main stat or substats. The name in parenthesis is the name by which that stat is referred to under the 'key_stat' key in the STATS.json file.

* **Attack**: This modifies the Attack (ATK) stat of a hero, and can either be *ATK* (id: 0; key_stat: attack_flat) or *ATK% (id: 1; key_stat: attack_percent)
* **Health**: This modifies the Health (HP) stat of a hero, and can either be *HP* (id: 2; key_stat: health_flat) or *HP%* (id: 3; key_stat: health_percent)
* **Defense**: This modifies the Defense (DEF) stat of a hero, and can either be *DEF* (id: 4; key_stat: defense_flat) or *DEF%* (id: 5; key_stat: defense_percent)
* **Critical Chance**: This modifies the Crit Chance (CRIT) stat of a hero, and is represented by CRIT (id: 6; key_stat: crit_rate)
* **Critical Damage**: This modifies the Crit Damage (CDMG) stat of a hero, and is represented by CDMG (id: 7; key_stat: crit_damage)
* **Effectiveness**: This modifies the Effectiveness (EFF) stat of a hero, and is represented by EFF (id: 8; key_stat: eff)
* **Effect Resistance**: This modifies the Effect Resistance (ER) stat of a hero, and is represented by ER (id: 9; key_stat: eff_res)
* **Speed**: This modifies the Speed (SPD) stat of a hero, and is represented by SPD (id: 10; key_stat: speed_flat)

### 5.2 Stat Restrictions
There are restrictions on whether a specific Gear **Type** can have certain stats as main stats or substats. Please refer to section 4.1 Type to check these restrictions. 

A general restriction of stats on an item is that stats may not be duplicated on a gear. For instance, it is impossible to have two or more lines of Speed or two or more lines of Attack. Note that ATK and ATK%, HP and HP%, and DEF and DEF% are not duplicates, so a gear may have both flat and percent of a specific type (assuming they don't violate TYPE specific restrictions). Similarly, the stat that has been assigned as the mainstat may not repeat in the substats. For instance, Weapons always have ATK as a mainstat, so it may never have ATK as a substat (ATK% on the other hand is perfectly fine and allowed).

### 5.3 Stat Values
When creating a gear and a stat is added to the gear (either as mainstat or substat), the value of the stat depends on the **Grade** and **Tier** of the gear. The mainstat value is usually ('type' key) fixed for a given Grade and Type, but the substat value is taken from a range of values ('type' = rand). For instance, for a Level 85 (Tier 6) Epic Gear, speed as a substat can be anywhere from 2 to 5 (the corresponding probability rates are stored in the STATS.json file). Another example is that for Level 85 (Tier 6) Boots (of any Grade), speed as a starting mainstat will always be 8 regardless of item grade; Level 90 (Tier 7) Boots on the other hand will have starting speed of 9 as mainstat (again, regardless of Grade).

### 5.4 Gear Score Multiplier
Each stat also has a gear score multiplier ('gscore' key) that is used or calculating the gear score of a gear. For instance, each point in speed has a gscore mutliplier of 2, i.e. 4 speed gives (4x2) 8 gear score.

### 5.5 Enhance Values
When a gear is **Enhanced** from +0 to +15 (refer to Enhance section), the main stat goes up by a multiplier based on the level. For details check the enhance_mainstat() function. At every +3 level of enhancement, a substat value may go up, the value it goes up by depends on the Grade and Tier. Under the 'substat' key, 'values' key have three subkeys for the grades: 'Rare', 'Heroic', and 'Epic'. Each of these subkeys is a list of length 3, with index 0 referring to Tier 5, index 1 referring to Tier 6, and index 2 referring to Tier 7 values. The corresponding probability rates of choosing any of these values is stored in the 'rates' key.

### 5.6 Reforge Values
When a gear is **Reforged**, the values of both the main stats and (usually) all the substats increase (refer to Reforging section). This info is stored under the 'reforge' key, which has 3 subkeys: 'mainstat', 'substat', and 'modded'. The 'mainstat' key has only one value - when an item is reforged, this value replaces the previous value. The 'substat' key has 6 values, each index referring to how many times a stat has been rolled on a +15 gear. For instance, if Speed is one of the substats on a gear, and it has rolled oned time, then the index 1 value under the 'substat' key is used to raise the Speed stat by when reforging. 'modded' key also has 6 values similar to 'substat' key and is used in the same way, only when the stat has been modded. Incidentally, these values are the same as 'substat' values, so regardless of whether an item has been modded or not, it goes up by the same value when it has been reforged.

### 5.7 Modify Values
When a substat of a gear is **Modified**, the value of the substat changes based on how many times that stat has rolled (refer to Modify section). These values are stored in the 'mod_vals' key. There are two subkeys: 'greater' or 'lesser' depending on what type of modification gem is chosen. Each of these subkeys is a list of length two - the first index refers to values for gear that is level 88 or below, the second index refers to values for gear that is level 90. Each of these indices, in turn, is a list of length 6, with the indices here referring to how many items an item has been rolled. For instance, if a **greater** modification is performed on a substat that has **rolled 2 times** on a **Level 90 gear**, the value from the 'greater' key, index=1 (because level 90), and in turn index=2 (rolled two times) is chosen. i.e.. STATS['0]['mod_vals]['greater'][1][2]

Note that the specifics of how these stats (such as flat or percent) affect a hero's stats are beyond the scope of this app. Gear Stats data is stored in the **STATS.json** file. Preparation of the data is found in the *prep_data_STATS.py* script.

## 6 Gear Upgrade System
Epic Seven allows upgrading/modifying gear through Enhancing, Reforging, and Modification.

### 6.1 Enhance System
Every gear starts at enhance level = 0. Every time a gear is enhanced, it's enhance level goes up by +1, up to +15 (which is the max enhance level). A gear must be +15 level of enhancement before it may be reforged or modified.

**6.1.1 Mainstat**

At every enhance level, the value of the main stat goes up by a certain multiplier on the base value (value at enhance level = 0); for the specific multiplier values check the enhance_mainstat() function.

**6.1.2 Substats**

At every three enhance levels (+3, +6, +9, +12, +15), a random substat on the gear is chosen to go up in value (based on values picked from 'substat' > 'values' > 'Rare'/'Heroic'/'Epic' > index referring to Tier of gear, with rates take from corresponding 'rates' values). For Heroic gear (which has 3 starting substats), at +12, a new substat is added. For Rare gear (which has 2 starting substats), at +9 and +12, new substats are added. The added substats follow the general and gear type specific restrictions.

### 6.2 Reforge System

A gear may only be reforged if it is item level 85 and it is at enhance level +15. When a gear is reforged, its level goes up from 85 to 90. The mainstat value is changed to the value found under 'reforge'>'mainstat' (no addition needed, the value is simply replaced). The current substat value increases by (so addition needed) the value found under 'reforge'>'substat' depending on the number of times the stat has rolled (0 to 5). If a stat has rolled 0 times, the 0th index value is taken; if a stat has rolled 5 times, the 5th index value is taken from 'substat', and so on (This goes for both modded and non-modded substats). A gear may be reforged only once.

### 6.3 Modification System

A gear may only be modified if it is at enhance level +15. When a gear is modified, one of the 4 substats is chosen to be replaced by another (or the same) chosen substat (following general and type specific restrictions). Only one substat on a gear may be modified. So, if a gear has been modified, only the stat that had been modified already may be further modified. Any other stats on that gear may not be modified. 

The modification values are taken from the 'mod_vals' key, which have two subkeys - 'greater' and 'lesser'. Each of these subkeys is a list of length two - the first index refers to values for gear that is level 88 or below, the second index refers to values for gear that is level 90. Each of these indices, in turn, is a list of length 6, with the indices here referring to how many items an item has been rolled. For instance, if a **greater** modification is performed on a substat that has **rolled 2 times** on a **Level 90 gear**, the value from the 'greater' key, index=1 (because level 90), and in turn index=2 (rolled two times) is chosen. i.e.. STATS['0]['mod_vals]['greater'][1][2]

## References:
* **Substat Roll Rates**: [Epic Seven Official Site](https://page.onstove.com/epicseven/global/view/7902683)
* **Modification Values**: [Epic Seven Official Discord](https://i.imgur.com/YYcbWCi.png)
* **Other General Information**: [Epic 7x](https://epic7x.com/equipment-tutorial/)

