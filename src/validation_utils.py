import json
import random
from src.utilities import *


# Import data
TYPES = json.loads(open('data/types.json', 'r').read())
STATS = json.loads(open('data/stats.json', 'r').read())

def validate_stat_id(stat_id):
    """
    Validate and return stat_id as str.
    Raise ValueError if input for stat_id is None, if it is a str or int but not between 0 and 10.
    Valid inputs: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10  as str or int
    (as of now, unless more stats are added later)
    """
    
    # Check if it's None
    if stat_id is None:
        raise ValueError("Stat ID cannot be None.")

    # Check if it's a string or integer in [0, 10]
    if not isinstance(stat_id, (str, int)) or str(stat_id) not in [key for key in STATS.keys()]:
        raise ValueError("Stat ID must be a string or integer in [0, 10].")

    return str(stat_id)


def validate_gear_type(gear_type, stat_id=None, stat_type=None):
    """
    Validate and return gear_type parameter in lower case.
    Raise ValueError if input for gear_type is not a string or invalid.
    Valid inputs: 'Weapon', 'Helm', 'Armor', 'Necklace', 'Ring', 'Boots' in any case.
    """
    
    # Check if it's None
    if gear_type is None:
        return None

    # Check if it's a string
    if not isinstance(gear_type, str):
        raise ValueError("Gear type must be a string.")
            
    gear_type = gear_type.lower()
    
    if gear_type not in [key.lower() for key in TYPES.keys()]:
        raise ValueError(f"Invalid gear type '{gear_type}'. Valid gear types are: {', '.join(TYPES.keys())}")
        
    if stat_id is not None and stat_type is not None:
        # Validate inputs
        stat_id = validate_stat_id(stat_id)
        stat_type = validate_stat_type(stat_type)
        # Check the pool of stats for given stat_id and stat_type
        pool = list(TYPES[gear_type][stat_type])
        if int(stat_id) not in pool:
            raise ValueError(f"The gear type {gear_type} cannot have {stat_id} stat as {stat_type}.")

    return gear_type


def validate_stat_type(stat_type, mod = False, rolled = 0):
    """
    Validate and return stat_type parameter in lower case.
    Raise ValueError if input for stat_type is not a string or invalid.
    Args:
        stat_type (str): 'mainstat' or 'substat' in any case (default: 'mainstat')
        mod (bool, optional): True or False, set to True if this is a modded stat
    """
    
    # Check if it's None, default to 'mainstat'
    if stat_type is None:
        stat_type = 'mainstat'
        return stat_type

    # Check if it's a string
    if not isinstance(stat_type, str):
        raise ValueError("Stat type must be a string.")
    
    # Convert to lower case
    stat_type = stat_type.lower()
    
    if stat_type not in ['mainstat', 'substat']:
        raise ValueError(f"Invalid stat type '{stat_type}'. Valid stat types are: 'mainstat' or 'substat'")
        
    if stat_type == 'mainstat' and mod:
        raise ValueError("Mainstats cannot be modded")
        
    if rolled != 0 and stat_type == 'mainstat':
        raise ValueError("Mainstats cannot have rolled values.")
        
    return stat_type


def is_valid_stat_entry(stat_entry):
    """
    Helper function to check whether the input parameter is a valid entry from stats.json.
    Checks whether the entry is a dict, if it has the keys 'id', 'text', and 'key_stat'
    
    Args:
        stat_entry (dict): a Stat object
        
    Returns:
        boolean: True or False
    """
    return isinstance(stat_entry, dict) and 'id' in stat_entry and 'text' in stat_entry and 'key_stat' in stat_entry


def validate_selected_stats(selected_stats):
    """
    Validate and return selected_stats parameter used in get_non_overlapping_function().
    Accepts lists with valid stat id's.
    Empty list or None returns an empty list.

    Returns:
        list: empty or contains valid stat id's
    """

    # Check if it's None - return empty list
    if selected_stats is None or selected_stats == []:
        return []

    # Check if it's a string
    if not isinstance(selected_stats, list):
        raise ValueError("Selected stat_id's must be entered as a list.")

    # Check if all strings in the list are valid keys in STATS
    valid_keys = [str(key) for key in STATS.keys()]
    if not all(str(entry) in valid_keys for entry in selected_stats):
        raise ValueError("Invalid entry in the selected stats list.")

    return selected_stats


def validate_rolled(rolled, stat_type='substat'):
    """
    Validate and return rolled parameter.
    Raise ValueError if rolled is not an int in [0, 5].
    Valid inputs: 0, 1, 2, 3, 4, 5 (default: 0)
    
    Args:
        rolled (int): how many times a stat rolled 
    """
    # Check if it's None
    if rolled is None:
        return 0
    
    # Check if it's an int
    if not isinstance(rolled, int) or rolled not in range(6):
        raise ValueError("Rolled count must be integer in [0, 5].")
        
    if stat_type == 'mainstat' and rolled !=0:
        raise ValueError("Mainstats cannot have rolled values.")
        
    return rolled


def validate_mod(mod, stat_type=None):
    """
    Validates the mod parameter.
    
    Args:
        mod (bool): The mod parameter value.
        
    Returns:
        bool: The validated mod parameter value.
        
    Raises:
        ValueError: If mod is not a boolean value or if stat_type = 'mainstat'
    """
    if mod is None or not isinstance(mod, bool):
        raise ValueError("Mod parameter must be a boolean value (True or False).")
        
    if mod and stat_type is not None and stat_type == 'mainstat':
        raise ValueError("Mainstats cannot be modified.")
    
    return mod


def validate_mod_type(mod_type):
    """
    Validates the mod_type parameter.
    
    Args:
        mod_type (str): 'greater' or 'lesser' (the type of modification gem stone being used)
        
    Returns:
        str: 'greater' or 'lesser' (default: 'greater')
        
    Raises:
        ValueError: If mod is not a str and 'greater' or 'lesser'.
    """
    if mod_type is None:
        mod_type = 'greater'
        
    if not isinstance(mod_type, str) or mod_type.lower() not in ['greater', 'lesser']:
        raise ValueError("Mod type must be a str containing 'greater' or 'lesser'.")
    
    return mod_type.lower()


def validate_gear_grade(gear_grade):
    """
    Validates gear_grade by checking if the grade is one of the values stored in GRADES.keys().
    Currently  ['normal', 'good', 'rare', 'heroic', 'epic'] If no
    If no gear_grade provided, get a random gear_grade
    Args:
        gear_grade (str): spcify gear grade
        
    Returns:
        gear_grade (str)
    """
    
    # Get a random gear_grade if none provided
    if gear_grade is None:
        gear_grade = get_random_grade()
    
    valid_gear_grades = list(GRADES.keys())
    
    if not isinstance(gear_grade, str) or gear_grade.lower() not in valid_gear_grades:
        raise ValueError("Gear grade must be a str from 'normal', 'good', 'rare', 'heroic', 'epic'")
    
    return gear_grade.lower()


def validate_gear_level(gear_level):
    """
    Validates gear_level by checking if the input is an int in range(58,101).
    Default value is 85 if none provided.
    
    Args:
        gear_level (int): Lvl (or item/gear level) of the gear (default 85)
        
    Returns:
        gear_level (int)
    """
    if gear_level is None:
        gear_level = 85
    
    if not isinstance(gear_level, int) or not (58 <= gear_level <= 100):
        raise ValueError("Gear level must be an int between 58 and 100")
        
    return gear_level
