import json

# Import data
TYPES = json.loads(open('data/types.json', 'r').read())
STATS = json.loads(open('data/stats.json', 'r').read())

def validate_stat_id(stat_id):
    """
    Validate and return stat_id as str.
    Raise ValueError if input for stat_id is None, if it is a str or int but not between 0 and 10.
    Valid inputs: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 
    (as of now, unless more stats are added later)
    """
    
    # Check if it's None
    if stat_id is None:
        raise ValueError("Stat ID cannot be None.")

    # Check if it's a string or integer in [0, 10]
    if not isinstance(stat_id, (str, int)) or str(stat_id) not in [key for key in STATS.keys()]:
        raise ValueError("Stat ID must be a string or integer in [0, 10].")

    return str(stat_id)


def validate_gear_type(gear_type):
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

    return gear_type

def validate_stat_type(stat_type):
    """
    Validate and return stat_type parameter in lower case.
    Raise ValueError if input for stat_type is not a string or invalid.
    Valid inputs: 'mainstat' or 'substat' in any case (default: 'mainstat')
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

    return stat_type
