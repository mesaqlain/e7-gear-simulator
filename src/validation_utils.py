import json
import random
from src.utilities import *


# Import data
with open('data/types.json', 'r') as types_file:
    TYPES = json.load(types_file)
with open('data/stats.json', 'r') as stats_file:
    STATS = json.load(stats_file)
    
    
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
        
    if rolled is not None:
        if rolled > 0 and stat_type == 'mainstat':
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
    
    # In case of ints provided in list, convert each element to str    
    selected_stats = convert_int_to_str(selected_stats)

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


def validate_gear_grade_input(gear_grade):
    """
    This is a helper function that is used inside the validate_gear_grade() function to 
    check whether the input is a str and whether it is one of the valid gear grade entries from
    the grades.json file.
    """
    # Valid gear grades
    valid_gear_grades = list(GRADES.keys())

    # Check if input is str, raise TypeError otherwise
    if not isinstance(gear_grade, str):
        raise TypeError("Gear grade must be a str input.")
    # Check if input is one of the valied gear_grades, raise ValueError otherwise
    if gear_grade.lower() not in valid_gear_grades:
        raise ValueError(
            "Gear grade must be a str from 'normal', 'good', 'rare', 'heroic', 'epic'")
    return gear_grade.lower()


def validate_gear_grade(gear_grade=None, mainstat_id=None, substat_ids=None):
    """
    Validates gear_grade by checking if the grade is one of the values stored in GRADES.keys().
    Currently  ['normal', 'good', 'rare', 'heroic', 'epic'] 
    If no gear_grade or substat_id's are provided, get a random gear_grade.
    If substat_id's are provided, ensure that the chosen gear_grade fits the number of starting
    substats.

    Args:
        gear_grade (str): spcify gear grade
        mainstat_id (int or str): Valid stat id [0, 10]
        substat_id (int or list of int): List of valid substat id's, can take up to 4 substat_id's

    Returns:
        gear_grade (str)
    """
    # If substat_id is provided
    if substat_ids is not None:
        substat_ids = validate_substat_ids(
            substat_ids=substat_ids, mainstat_id=mainstat_id)
        no_of_subs = len(substat_ids)

        # If gear_grade is provided
        if gear_grade is not None:
            gear_grade = validate_gear_grade_input(gear_grade)
            starting_substats = GRADES[gear_grade]['starting_substats']
            # Raise ValueError if the number of starting substats exceeds what's allowed
            # on provided gear_type (e.g. Heroic gear cannot start with 4 substats)
            if starting_substats < no_of_subs:
                raise ValueError(
                    f"Invalid gear grade provided, {gear_grade} cannot have {no_of_subs} starting substats.")

        # If gear_grade is not provided:
        else:
            gear_grade = get_random_grade()
            starting_substats = GRADES[gear_grade]['starting_substats']
            
            # Keep rolling until we get a gear_grade that satisfies the
            # starting_substats criteria
            while starting_substats < no_of_subs:
                gear_grade = get_random_grade()
                starting_substats = GRADES[gear_grade]['starting_substats']
    
    # If substat_id is not provided:
    else:
        
        # If gear_grade is provided:
        if gear_grade is not None:
            gear_grade = validate_gear_grade_input(gear_grade)
                
        # If gear_grade is not provided:
        else:
            gear_grade = get_random_grade()

    return gear_grade


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

def validate_gear_set(gear_set):
    """
    Validates gear_set by checking if the input is a str and if it is one of the
    sets from the sets.json file
    
    Args:
        gear_set (str): Set name
        
    Returns:
        gear_set (str)
    """
    if gear_set is None:
        gear_set = get_random_set()
    
    if not isinstance(gear_set, str) or gear_set.lower() not in list(SETS.keys()):
        raise ValueError("Gear set must be a str and one of the values from sets.json")
        
    return gear_set.lower()


def validate_substat_ids(substat_ids=None, mainstat_id=None, gear_type = None):
    """
    Validates the given substat ids. Converts integers to strings. 
    Raises ValueError if more than 4 stat_ids provided, or if duplicates are provided.
    Raises ValueError if mainstat id is in substat id.
    
    Args:
        stat_id (int or list of ints):
        
    Returns:
        stat_id (str)
    """
    
    if substat_ids is None:
        return []
    
    substat_ids_str = convert_int_to_str(substat_ids)

    # Get length of substats list (how many subs provided)
    len_ = len(substat_ids_str)

    # Check if more than 4 subs are provided:
    if len_ > 4:
        raise ValueError("Please provide up to 4 sub stats only.")
        
    # Check if valid substat id's are provided
    valid_substat_ids = [validate_stat_id(s) for s in substat_ids_str]
    
    # Check if duplicate substat id's are provided
    if mainstat_id is not None:
        mainstat_id = validate_stat_id(mainstat_id)
        if mainstat_id in valid_substat_ids:
            raise ValueError("Mainstat and substat cannot have same stats.")
        if gear_type is not None:
            check_valid_pool(gear_type, 'mainstat', mainstat_id)
        
    if len_ != len(set(valid_substat_ids)):
        raise ValueError("Cannot add duplicate substats to a gear.")
        
    # Make sure that gear_type doesn't clash with substats
    if gear_type is not None:
        check_valid_pool(gear_type, 'substat', valid_substat_ids)
        
    return valid_substat_ids


def validate_mainstat_id(mainstat_id=None, substat_ids=None, gear_type=None):
    """
    Validates the given mainstat ids. Converts result to str. 
    Raises ValueError if mainstat id is not a valid stat_id or if the mainstat 
    is also present in the substats.
    
    Args:
        stat_id (int or str):
        
    Returns:
        mainstat_id (str)
    """
    # If no mainstat id is provided, return None
    if mainstat_id is None:
        return None
    
    # If a mainstat id is provided
    else:
        # Check that provided mainstat id is a valid input
        mainstat_id = validate_stat_id(mainstat_id)
        # If no substat ids are provided, ensure that mainstat id is a valid id 
        if substat_ids is None:
            # Make sure that gear_type doesn't clash with mainstats
            if gear_type is not None:
                check_valid_pool(gear_type, 'mainstat', mainstat_id)
            return mainstat_id
        # If substat ids are provided, make sure that the mainstat isn't in the substats
        else:
            # Check if valid substat id's are provided
            substat_ids_str = convert_int_to_str(substat_ids)
            valid_substat_ids = [validate_stat_id(s) for s in substat_ids_str]
            # Checking if mainstat is in substat list
            if mainstat_id in valid_substat_ids:
                raise ValueError("Mainstat and substat cannot have same stats.")
            # If it isn't validate the mainstat id
            else:
                # Make sure that gear_type doesn't clash with mainstats
                if gear_type is not None:
                    check_valid_pool(gear_type, 'substat', valid_substat_ids)
                return mainstat_id
                
    # Make sure that gear_type doesn't clash with mainstats
    if gear_type is not None:
        check_valid_pool(gear_type, 'mainstat', mainstat_id)
                
    return mainstat_id


def validate_enhance_level(enhance_level=None):
    """
    Validates the input enhance level. Input must be int between 0 and 15
    """
    # If none provided, set to 0
    if enhance_level is None:
        enhance_level = 0
    # If provided, check that it's an int between 0 and 15
    else:
        if not isinstance(enhance_level, int):
            raise TypeError("Enhance Level must be an int.")
        elif enhance_level not in list(range(0, 16)):
            raise ValueError("Enhance Level must be between 0 and 15")
            
    return enhance_level


def validate_stat_index(stat_index = None):
    """
    Validates the input enhance level. Input must be int between 0 and 15
    """
    # If none provided, raise error
    if stat_index is None:
        raise ValueError("Please provided a valid Stat Index between 1 to 4.")
        
    # If provided, check that it's an int between 1 and 4
    else:
        if not isinstance(stat_index, int):
            raise TypeError("Stat Index must be an int.")
        elif stat_index not in list(range(1, 5)):
            raise ValueError("Stat Index must be between 1 and 4.")
            
    return stat_index