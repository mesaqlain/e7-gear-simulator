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