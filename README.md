# Epic Seven Gear Simulator

## 1 Intro
This is an ongoing project to create an app in python that will simulate the generation of items (better known as gear in the community), same as those found in the mobile game Epic Seven. The app has the following functionalities:
* **Create** an item (either completely random or specific attributes)
* **Enhance** an item
* **Reforge** an item
* **Modify** an item
* Each of the features mentioned above follows restrictions regarding **stats** (such as which stats are allowed on a specific type of gear)

The features are explained in depth in their respective sections.

## 2 Requirements

## 3 Useage / Directions

## 4 Item / Gear Description
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

Note: Revenge, Penetration, Injury, Protection, and Torrent still need to be added.

### 4.3 Level / Tier

A gear has a **Level** (also referred to as iLvl) range from 1 to 90 currently in the game. This app, however, only allows gear of levels between 58 and 100. This is because the official website does not publish the probability rates for gear of lower levels; additionally, most people would not care to use this app for gear below level 85 anyway.

Depending on the level of the item, the gear is assigned a **Tier**.  Tiers go from 1 to 7 (this app allows use of only Tiers 5-7. The Tier affects the possible roll ranges of the stats, so it is an important attribute. Higher tier gear are more likely to roll a higher value for a stat compared to a lower tier gear.

The tiers we have published rates for and use in this app are:
* Tier 5: Levels 58-71
* Tier 6: Levels 72-85
* Tier 7: Levels 86-100

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
