import random
from set_directory_function import set_directory
set_directory()
from src.utilities import *
from src.validation_utils import *


def get_stat_by_id(stat_id):
    """
    Retrieves stat data based on given ID.

    Args:
        stat_id (int): The id of the stat to retrieve (refer to STATS.json for id).

    Returns:
        dict: Stat data
    """
    # Validate the stat_id input
    stat_id = validate_stat_id(stat_id)
    # Iterate through each entry in STATS dict
    for s in STATS:
        # Check if the given ID exists in the current section
        if stat_id in s:
            # Return the stat dictionary associated with the ID
            return STATS[stat_id]
    # Return None if the provided ID doesn't match any stat
    return None


def get_random_stat(stat_type='mainstat', gear_type=None):
    """
    Retrieves data on a random stat chosen from the pool of available
    mainstats or substats from given gear_type.

    Args:
        stat_type (str): The type of stat - 'mainstat' or 'substat only'.
        gear_type (str): The type of gear - 'weapon', 'helm', 'armor', 'necklace',
            'ring', or 'boots' only.

    Returns:
        dict: Stat data
    """

    # Validate inputs
    stat_type = validate_stat_type(stat_type)
    gear_type = validate_gear_type(gear_type)

    pool = []  # Initialize an empty list to store available IDs

    # If no item type provided, pick any stat from list of main stats or
    # substats
    if gear_type is None:
        # Use set union to merge the available IDs into the pool list
        pool = list(set(STATS))
    else:
        # Get the pool of id's possible for this item_type
        pool = list(set(TYPES[gear_type][stat_type]))

    # If the pool is empty, no stats are available, so return None
    if pool == []:
        return None

    # Choose a random ID from the pool and fetch the associated stat
    return get_stat_by_id(stat_id=random.choice(pool))


def test_get_non_overlapping_stat(
        selected_stats=[], stat_type='substat', gear_type=None):
    """
    Retrieves a new stat that is not already in the selected list of stats.

    Args:
        selected_stats (list): List containing stat id's (default: empty list [])
        stat_type (str): The type of stat - 'mainstat' or 'substat only' (default: 'substat')
            (in almost every case it will be 'substat' for this function, hence default)
        gear_type (str): The type of gear - 'weapon', 'helm', 'armor', 'necklace',
                'ring', or 'boots' only. (default: None)

    Returns:
        dict: Stat data
    """

    # Validate inputs:
    selected_stats = validate_selected_stats(selected_stats)
    stat_type = validate_stat_type(stat_type)
    gear_type = validate_gear_type(gear_type)

    # Get a random stat
    stat = get_random_stat(stat_type, gear_type)

    # If the stat we got in the previous line exists in our selected stats,
    # get a new random stat
    while any(stat['id'] == int(a) for a in selected_stats):
        # Get a new random stat as long as above condition is True
        stat = get_random_stat(stat_type, gear_type)

    return stat


def get_reforge_increase(stat_id, stat_type, rolled):
    """
    Get the value by which a stat will increase by when an item has been reforged.
    
    Args:
        stat_type (str): 'mainstat' or 'substat'
        rolled (int): value between 0 and 5.
    """
    # Validate inputs
    stat_id = validate_stat_id(stat_id)
    stat_type = validate_stat_type(stat_type)
    rolled = validate_rolled(rolled)
    
    # Get reforge_increase value
    reforge_increase = STATS[stat_id]['reforge'][stat_type][rolled]
    
    return reforge_increase


def test_get_mod_value(stat_id, gear_level=85, rolled=None, mod_type='greater'):
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


def test_get_stat_value(stat_id, stat_type='mainstat',
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


def test_get_gear_type(gear_type=None, mainstat_id=None, substat_ids=None):
    """
    Retrieves a random gear type based on provided mainstat_id and substat_id.
    Used in the create_gear() method in Gear() class.
    Args:
        gear_type (str): Type of gear
        mainstat_id (int or str): Valid stat id [0, 10]
        substat_id (int or list of int): List of valid substat id's, can take up to 4 substat_id's
    """
    # Validate inputs
    gear_type = validate_gear_type(gear_type)
    
    if mainstat_id is not None:
        mainstat_id = validate_stat_id(mainstat_id)
    
    if substat_ids is not None:
        substat_ids = validate_substat_ids(substat_ids, mainstat_id)
        
    # If no args provided, get a random gear type
    if mainstat_id is None and substat_ids is None and gear_type is None:
        gear_type = get_random_gear_type()
        return gear_type
    
    # If mainstat_id is provided
    if mainstat_id is not None:
        # If gear_type is not provided
        if gear_type is None:
            # Get a random gear_type
            gear_type = get_random_gear_type()
            # Ensure that mainstat is in the allowed pool of mainstats for gear_type
            while int(mainstat_id) not in TYPES[gear_type]['mainstat']:
                gear_type = get_random_gear_type()
                # If substat_id's are provided, ensure that the substat_id's
                # are in the allowed pool of substats for gear_type
                if substat_ids is not None:
                    gear_type = get_gear_type_from_subs(gear_type, substat_ids)
        
        # If gear_type is provided
        else:
            # Check if provided mainstat is allowed in provided gear_type
            if int(mainstat_id) not in TYPES[gear_type]['mainstat']:
                raise ValueError(f"{gear_type} cannot have {mainstat_id} as mainstat.")
            # If substat_id's are provided, ensure that the substat_id's are
            # in the allowed pool of substats for gear_type
            if substat_ids is not None and any(s not in convert_int_to_str(
                TYPES[gear_type]['substat']) for s in substat_ids):
                raise ValueError(f"{gear_type} cannot have one or more of these substats")
    
    # If mainstat_id is not provided    
    else: 
        # If gear_type is not provided
        if gear_type is None:
            gear_type = get_random_gear_type()
            # If substat_id's are provided, ensure that the substat_id's
            # are in the allowed pool of substats for gear_type
            if substat_ids is not None:
                gear_type = get_gear_type_from_subs(gear_type, substat_ids)
        
        # If gear_type is provided
        else:
            # If substat_id's are provided, ensure that the substat_id's are
            # in the allowed pool of substats for gear_type
            if substat_ids is not None and any(s not in convert_int_to_str(
                TYPES[gear_type]['substat']) for s in substat_ids):
                raise ValueError(f"{gear_type} cannot have one or more of these substats")
                
    return gear_type


def test_get_mainstat_id(mainstat_id=None, substat_ids=None, gear_type=None):
    """
    Get a mainstat_id based on provided substat_ids and gear_type.
    Gear_type cannot be none. If no substat_ids or mainstat_ids are provided, an appropriate random
    mainstat_id is chosen from the available pool of id's for given gear_type.
    If substat_id's are provided, mainstat_id is chosen in a way so as not to be same as substat id.
    Args:
        mainstat_id (int or st): valid mainstat id from range(0, 11)
        substat_ids (int/str or list of int/str): valid list of substat id(s) from range(0,11)
        gear_type (str): valid gear type from types.json: 'weapon', 'helm', 'armor', 'necklace', 'ring', or 'boots'
    """
    # gear_type cannot be none for this function
    if gear_type is None:
        raise ValueError(
            "Please provide a valid gear type: 'weapon', 'helm', 'armor', 'necklace', 'ring', or 'boots'.")
    else:
        gear_type = validate_gear_type(gear_type)

    # Available pool of id's for given gear_type (convert to str)
    mainstat_pool = convert_int_to_str(list(TYPES[gear_type]['mainstat']))
    substats_pool = convert_int_to_str(list(TYPES[gear_type]['substat']))

    # If no substat_ids provided
    if substat_ids is None:
        # If no mainstat id provided
        if mainstat_id is None:
            # Pick a random mainstat
            mainstat_id = random.choice(mainstat_pool)
        # If mainstat id is provided
        else:
            mainstat_id = validate_mainstat_id(mainstat_id)
            if mainstat_id not in mainstat_pool:
                raise ValueError(
                    f"{gear_type} cannot have stat with id {mainstat_id}.")
    # If substat_ids are provided
    else:
        # Validate substats
        substat_ids = validate_substat_ids(substat_ids)
        if any(s not in substats_pool for s in substat_ids):
            raise ValueError(
                "One or more of the substats cannot be added to this gear_type.")
        # If no mainstat id provided
        if mainstat_id is None:
            # Pick a random mainstat
            mainstat_id = random.choice(mainstat_pool)
            # If randomly chosen mainstat is already in provided substats
            # get a new random mainstat
            while mainstat_id in substat_ids:
                mainstat_id = random.choice(mainstat_pool)
        # If mainstat id is provided
        else:
            mainstat_id = validate_mainstat_id(mainstat_id)
            if mainstat_id in substat_ids:
                raise ValueError(
                    "Mainstat id and substat id cannot share same stats.")
            if mainstat_id not in mainstat_pool:
                raise ValueError(
                    f"{gear_type} cannot have stat with id {mainstat_id}.")

    return mainstat_id


def test_get_substat_ids(mainstat_id=None, substat_ids=None, gear_type=None, gear_grade=None):
    """
    Get substat_ids based on provided gear_type, gear_grade, mainstat_id, and potential other provided substat_ids.
    Gear_type, gear_grade, and mainstat_id cannot be none. Substat_id's are optional.
    If no substat_ids are provided, gear type appropriate random substat_ids are chosen to fill the starting
    number of substats for given gear grade. General restrictions apply, such as mainstat cannot be same as substats,
    duplicate substats are not allowed, cannot have more than 4 substats, and a grade cannot have more substats
    than the allowed starting substats number.

    Args:
        mainstat_id (int or st): valid mainstat id from range(0, 11)
        substat_ids (int/str or list of int/str): valid list of substat id(s) from range(0,11)
        gear_type (str): valid gear type from types.json: 'weapon', 'helm', 'armor', 'necklace', 'ring', or 'boots'
        gear_grade (str): valid gear grade from grades.json: 'normal', 'good', 'rare', 'heroic', 'epic'
    """
    # gear_type cannot be none for this function
    if gear_type is None:
        raise ValueError(
            "Please provide a valid gear type: 'weapon', 'helm', 'armor', 'necklace', 'ring', or 'boots'.")
    else:
        gear_type = validate_gear_type(gear_type)

    # gear_grade cannot be none for this function
    if gear_grade is None:
        raise ValueError(
            "Please provide a valid gear grade: 'normal', 'good', 'rare', 'heroic', or 'epic'.")
    else:
        gear_grade = validate_gear_grade(gear_grade, mainstat_id, substat_ids)

    # mainstat_id cannot be none for this function
    if mainstat_id is None:
        raise ValueError(
            "Please provide a valid mainstat id.")
    else:
        mainstat_id = validate_mainstat_id(mainstat_id, substat_ids, gear_type)

    # Validate substat_ids:
    substat_ids = validate_substat_ids(substat_ids, mainstat_id, gear_type)

    # Available pool of id's for given gear_type (convert to str)
    substats_pool = convert_int_to_str(list(TYPES[gear_type]['substat']))
    
    # Number of starting substats allowed on gear
    starting_substats = GRADES[gear_grade]['starting_substats']

    # Number of substats that still needs to be added to gear:
    subs_remaining = starting_substats - len(substat_ids)
    
    # Initialize gear pool list which will hold both mainstat and substat ids:
    gear_pool = substat_ids + [mainstat_id]

    # Add new non-overlapping substats until we have the appropriate number of 
    # starting substats
    for i in range(subs_remaining):
        new_substat_id = get_non_overlapping_stat_id(gear_pool, gear_type=gear_type, stat_type='substat')
        substat_ids.append(new_substat_id)
        gear_pool.append(new_substat_id)
        
    return substat_ids


def test_get_stat(stat_id=None, stat_type='mainstat', gear_type=None, gear_grade=None, 
             gear_level=85, mod=False, rolled=None, mod_type='greater', show_reforged=False):
    """
    Get stat method for Gear() class to retrieve stat information based on given attributes. Stat_id must be provided
    """
    # Initialize an empty stat class object
    stat = Stat()
    # Get the stat info by id
    stat.get_stat_by_id(stat_id, stat_type, gear_type)
    # Parse the stat (get a specific value)
    stat.parse_stat(stat_type, gear_type, gear_grade, 
                   gear_level, mod, rolled, mod_type)
    # Get formatted text
    stat.format_stat(show_reforged=show_reforged)
    
    return stat