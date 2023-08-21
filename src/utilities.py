import json
import random

TIERS = json.loads(open('data/tiers.json', 'r').read())
GRADES = json.loads(open('data/grades.json', 'r').read())
STATS = json.loads(open('data/stats.json', 'r').read())


def get_random_grade():
    """
    Returns a random gear grade ('rare', 'heroic', 'epic')
    Rates of choosing a particular grade can be edited in prep_data_GRADES.py
    
    Returns:
        str 
    """
    grade = random.choices(
        list(
            GRADES.keys()),
        weights=[
            grade['weight'] for grade in GRADES.values()])[0]
    return grade    


def get_gear_tier(gear_level):
    """
    Gets gear tier based on provided gear level. 
    Lvl 58-71: Tier 5
    Lvl 72-85: Tier 6
    Lvl 86-100: Tier 7
    
    Args:
        gear_level (int): Level of the gear
        
    Returns:
        (int) Tier of gear (5, 6 or 7)
    """
    # Import the function
    from src.validation_utils import validate_gear_level
    
    # Validate gear level
    gear_level = validate_gear_level(gear_level)
    
    # Loop through tiers dictionary
    for t in TIERS:  
        # Check if the level is in the level range in each section
        if gear_level in TIERS[t]['level_range']:
            # If the level matches, then return that tier value
            tier = TIERS[t]['gear_tier']
            
    return tier


def get_mod_value(stat_id, gear_level=85, 
                  rolled=None, mod_type='greater'):
    """
    Get the modification value of a stat based on its gear_level, rolled count, and mod_type.
    It chooses a random value from a range of values for the given criteria.
    Args:
        stat_id: valid stat_id of stat
        gear_level (int): level of gear, between 58 and 100 (default = 85)
        rolled (int): number of times a gear has been rolled when enhancing (default: None = 0)
        mod_type (str): type of modification stone used - 'greater' or 'lesser' (default: 'greater')

    Returns:
        int : modified stat value
    """
    
    # Import the functions
    from src.validation_utils import validate_stat_id, validate_gear_level
    from src.validation_utils import validate_rolled, validate_mod_type
    
    # Validate inputs:
    stat_id = validate_stat_id(stat_id)
    gear_level = validate_gear_level(gear_level)
    rolled = validate_rolled(rolled)
    mod_type = validate_mod_type(mod_type)
    
    # Get the stat info
    stat = STATS[stat_id]
    # Get the appropriate mod value ranges
    values = stat['mod_vals'][mod_type]

    # If gear level is <= 88, use the first index values
    if gear_level <= 88:
        values_88 = values[0][rolled]
        value = random.choice(values_88)

    # For reforged items with gear level = 90
    elif gear_level == 90:
        values_90 = values[1][rolled]
        value = random.choice(values_90)

    else:
        raise ValueError("Invalid gear level, cannot modify.")

    return value


def get_stat_value(stat_id, stat_type='mainstat',
                   gear_level=85, gear_grade=None):
    """
    Get the value of a stat based on its stat_id, stat_type, gear_level, and gear_grade.
    It chooses a random value from a range of values for the given criteria.
    Args:
        stat_id: valid stat_id of stat
        gear_level (int): level of gear, between 58 and 100 (default = 85)
        gear_grade (str): grade of gear

    Returns:
        int : parsed stat value
    """
    # Import the functions
    from src.validation_utils import validate_stat_id, validate_stat_type
    from src.validation_utils import validate_gear_level, validate_gear_grade
    
    # Validate inputs
    stat_id = validate_stat_id(stat_id)
    stat_type = validate_stat_type(stat_type)
    gear_level = validate_gear_level(gear_level)
    gear_grade = validate_gear_grade(gear_grade)

    # Get gear tier (-5 to get proper index)
    gear_tier = get_gear_tier(gear_level)

    # Access information from the stat object
    var = STATS[stat_id]['vars'][stat_type]
    # Get value type
    type_ = var['type']
    # Get the value(s)
    values = var['values'][gear_grade][gear_tier - 5]

    # rand for substats usually
    if type_ == 'rand':
        # Corresponding Rates
        rates = var['rates'][gear_grade][gear_tier - 5]
        # Get a value based on the rates
        value = random.choices(values, rates)[0]
    # fixed for mainstats usually
    elif type_ == 'fixed':
        value = values

    return value


def get_reforge_increase(stat_id, stat_type, rolled):
    """
    Get the value by which a stat will increase by when an item has been reforged.
    
    Args:
        stat_id (int) : valid stat id from the stats.json file
        stat_type (str): 'mainstat' or 'substat'
        rolled (int): value between 0 and 5.
    """
    
    # Import the functions
    from src.validation_utils import validate_stat_id, validate_stat_type, validate_rolled

    # Validate inputs
    stat_id = validate_stat_id(stat_id)
    stat_type = validate_stat_type(stat_type)
    rolled = validate_rolled(rolled)
    
    # Get reforge_increase value
    reforge_increase = STATS[stat_id]['reforge'][stat_type][rolled]
    
    return reforge_increase
