import json
import random

with open('data/types.json', 'r') as types_file:
    TYPES = json.load(types_file)
with open('data/sets.json', 'r') as sets_file:
    SETS = json.load(sets_file)
with open('data/tiers.json', 'r') as tiers_file:
    TIERS = json.load(tiers_file)
with open('data/grades.json', 'r') as grades_file:
    GRADES = json.load(grades_file)
with open('data/stats.json', 'r') as stats_file:
    STATS = json.load(stats_file)
    
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


def get_random_set():
    """
    Returns a random gear set from sets.json
    Rates of choosing a particular grade can be edited in prep_data_GRADES.py
    
    Returns:
        str 
    """
    gear_set = random.choice(list(SETS.keys()))
                        
    return gear_set    


def convert_int_to_str(obj):
    """
    Function that takes all entries in a list and converts them to str
    as long as the elements are int type or str representing an int.
    If only one int is provided, it converts it to str and returns it.
    If a string is a number, it is also returned as is.

    Returns: list of str
    """
    if obj == []:
        return []

    if isinstance(obj, int):
        return [str(obj)]

    elif isinstance(obj, str) and obj.isdigit():  # Check if the string is a number
        return [obj]

    elif isinstance(obj, list):
        result = []
        for o in obj:
            if isinstance(o, int):
                result.append(str(o))
            elif isinstance(o, str) and o.isdigit():
                result.append(o)
            else:
                raise TypeError(
                    f"Invalid element in the list: {o}. Expected int or string representing a number.")
        return result

    else:
        raise TypeError(
            "Invalid input type. Expected int, str, or list of integers/strings.")
        
        
def get_random_gear_type():
    """
    Returns a random gear type ('weapon', 'helm', 'armor', 'necklace', 'ring', 'boots')
    
    Returns:
        str 
    """
    gear_type = random.choice(list(TYPES.keys()))
                              
    return gear_type    
        
    
def get_gear_type_from_subs(gear_type=None, substat_ids=None):
    """
    Retrieves a gear type based on given substat_id's restriction.
    Gets a random gear type and if substat_ids is None or an empty list, returns the random gear_type.
    If substat_id's are provided, it keeps rolling new gear_type until the provided id's are all in the 
    pool of allowed substats for that gear type.
    """
    from src.validation_utils import validate_gear_type, validate_substat_ids

    # Validate inputs
    gear_type = validate_gear_type(gear_type)
    substat_ids = validate_substat_ids(substat_ids)

    # Get a random gear type if none provided
    if gear_type is None:
        gear_type = get_random_gear_type()

    if substat_ids is not None and substat_ids != []:
        # Get the pool of allowed substats for the gear type
        valid_substats = convert_int_to_str(TYPES[gear_type]['substat'])

        # loop to check if all the id's in the substat_ids list are
        # present in the valid_substats list.
        while not all(
                substat_id in valid_substats for substat_id in substat_ids):
            gear_type = get_random_gear_type()
            valid_substats = convert_int_to_str(TYPES[gear_type]['substat'])

    return gear_type


def get_random_stat_id(gear_type=None, stat_type='substat'):
    """
    Get a random stat_id from available pool of stat_ids based on gear_type.
    
    Args:
        gear_type (str): type of gear - 'weapon', 'helm', 'armor', 'necklace', 'ring', 'boots'
        stat_type (str): 'mainstat' or 'substat'
        
    Returns:
        random stat_id (str)
    
    """
    from src.validation_utils import validate_gear_type, validate_stat_type
    
    # Validate inputs
    stat_type = validate_stat_type(stat_type)
    gear_type = validate_gear_type(gear_type)

    pool = []  # Initialize an empty list to store available IDs

    # If no item type provided, pick any stat from list of main stats or
    # substats
    if gear_type is None:
        pool = list(STATS.keys())
    else:
        # Get the pool of id's available for this gear_type
        pool = list(set(TYPES[gear_type][stat_type]))

    # If the pool is empty, no stats are available, so return None
    if pool == []:
        return None

    # Choose a random ID from the pool and fetch the associated stat
    random_stat_id = random.choice(pool)
    
    return str(random_stat_id)


def get_non_overlapping_stat_id(selected_stats = [], gear_type=None, stat_type='substat'):
    """
    Retrieves a new stat that is not already in the selected list of stats.

    Args:
        selected_stats (list): List containing valid stat id's (default: empty list [])
        stat_type (str): The type of stat - 'mainstat' or 'substat only' (default: 'substat')
        gear_type (str): The type of gear - 'weapon', 'helm', 'armor', 'necklace',
                'ring', or 'boots' only. (default: None)
    
    Returns:
        random stat_id (str)
    """
    from src.validation_utils import validate_gear_type, validate_stat_type, validate_selected_stats

    # Validate inputs:
    selected_stats = validate_selected_stats(selected_stats)
    stat_type = validate_stat_type(stat_type)
    gear_type = validate_gear_type(gear_type)

    # Get a random stat
    random_stat_id = get_random_stat_id(gear_type, stat_type)

    # If the random stat already exists in given selected stats
    while random_stat_id in selected_stats:
        # Get a new random stat while above condition is True
        random_stat_id = get_random_stat_id(gear_type, stat_type)

    return str(random_stat_id)


def check_valid_pool(gear_type=None, stat_type='mainstat', stat_ids=[]):
    """
    Checks whether the stat_id's of a given stat_type are in the valid pool of id's for given gear type.
    Raises ValueError if the given stat_ids are not ihe valid pool.
    """
    # Validate inputs
    from src.validation_utils import validate_gear_type, validate_stat_type, validate_stat_id

    stat_type = validate_stat_type(stat_type)
    stat_ids = [validate_stat_id(s) for s in convert_int_to_str(stat_ids)]

    if gear_type is None:
        raise ValueError("gear_type cannot be none.")
    else:
        gear_type = validate_gear_type(gear_type)
    
    valid_pool = convert_int_to_str(TYPES[gear_type][stat_type])
    
    if any(s not in valid_pool for s in stat_ids):
        raise ValueError(f"{gear_type} cannot have one or more of the {stat_type}(s) provided.")
