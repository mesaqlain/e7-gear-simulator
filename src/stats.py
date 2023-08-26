import json
import random
from src.validation_utils import *
from src.utilities import *

# Import Data 
STATS = json.loads(open('data/stats.json', 'r').read())
TYPES = json.loads(open('data/types.json', 'r').read())
GRADES = json.loads(open('data/grades.json', 'r').read())
TIERS = json.loads(open('data/tiers.json', 'r').read())


class Stat:
    """A class to represent the statistics that are added to a gear."""

    def __init__(self):
        """
        Initializes the Stat object.
        Args:
            stat_id (int or str): The id of the stat to retrieve (refer to STATS.json for id).
            stat_key (str): The name of the stat
            stat_type (str): The type of stat - 'mainstat' or 'substat only'.
            gear_type (str): The type of gear - 'weapon', 'helm', 'armor', 'necklace',
                    'ring', or 'boots' only. (default: None)
            gear_grade (str): The grade of the gear ('normal', 'good', 'rare', heroic', 'epic')
            gear_level (int): The level of the gear
            gear_tier (int): The tier of the gear (5, 6, 7)
            rolled (int): value between 0 and 5; how many times a stat rolled when enhancing
            reforge_increase (int) : The value by which a stat increases when reforging
            text (str): Text description of the stat
            value_key (str): The value key which is replaced in the text
            modded (bool): Boolean specifying whether the gear has been modded or not
            text_formatted (str): Formatted text showing concise description of the stat

        """
        self.stat_id = None
        self.stat_key = None
        self.stat_type = 'mainstat'
        self.gear_type = None
        self.gear_grade = None
        self.gear_level = 85
        self.gear_tier = None
        self.rolled = 0
        self.reforge_increase = None
        self.text = None
        self.value = None
        self.value_key = None
        self.modded = False
        self.text_formatted = None
        
    def __str__(self):
        """Str representation of class"""
        return (
            f"ID: {self.stat_id}\n"
            f"Stat: {self.stat_key}\n"
            f"Stat Type: {self.stat_type}\n"
            f"Gear Type: {self.gear_type}\n"
            f"Grade: {self.gear_grade}\n"
            f"Level: {self.gear_level}\n"
            f"Tier: {self.gear_tier}\n"
            f"Rolled Count: {self.rolled}\n"
            f"Reforge Value: {self.reforge_increase}\n"
            f"Text: {self.text}\n"
            f"Value: {self.value}\n"
            f"Value Key: {self.value_key}\n"
            f"Modded: {self.modded}\n"
            f"Formatted Text: {self.text_formatted}"
        )
        

    def get_stat_by_id(self, stat_id, stat_type=None, gear_type=None):
        """
        Retrieves stat data based on given ID.

        Args:
            stat_id (int or str): The id of the stat to retrieve (refer to STATS.json for id).

        Returns:
            dict: Stat data
        """
        # Validate the stat_id input
        stat_id = validate_stat_id(stat_id) 
        
        # Iterate through each entry in STATS dict
        for stat_data in STATS.values():
            if str(stat_data['id']) == stat_id:
                # Store the selected_stat_id value
                self.stat_id = stat_id
                self.stat_key = str(stat_data['key_stat'])
                
                # Assign class attributes if values are provided
                if stat_type is not None:
                    self.stat_type = validate_stat_type(stat_type)
                if gear_type is not None:
                    self.gear_type = validate_gear_type(gear_type, stat_id=self.stat_id, stat_type=self.stat_type)

                # Return the stat dictionary associated with the ID
                return stat_data
        
        # Raise a ValueError if the provided ID doesn't match any stat
        raise ValueError(f"No stat found with ID {stat_id}")

    
    def get_random_stat(self, stat_type='mainstat', gear_type=None):
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
        random_stat = self.get_stat_by_id(stat_id=random.choice(pool))

        # Set the class attribute
        self.stat_id = str(random_stat['id'])
        self.stat_key = str(random_stat['key_stat'])
        self.stat_type = stat_type
        self.gear_type = gear_type

        return random_stat


    def get_non_overlapping_stat(
        self, selected_stats=[], stat_type='substat', gear_type=None):
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
        random_stat = self.get_random_stat(stat_type, gear_type)

        # If the stat we got in the previous line exists in our selected stats,
        # get a new random stat
        while any(random_stat['id'] == int(a) for a in selected_stats):
            # Get a new random stat as long as above condition is True
            random_stat = self.get_random_stat(stat_type, gear_type)

        # Set the selected_stat_id attribute
        self.stat_id = str(random_stat['id'])
        self.stat_key = str(random_stat['key_stat'])
        self.stat_type = stat_type
        self.gear_type = gear_type

        return random_stat
    

#     def get_reforge_increase(self, rolled):
#         """
#         Get the value by which a stat will increase by when an item has been reforged.
#         (This function has been moved outside of the Stat class to utilities.py)

#         Args:
#             rolled (int): value between 0 and 5; how many times a stat rolled when enhancing
#         """
#         # Validate inputs
#         rolled = validate_rolled(rolled)
        
#         if self.stat_id is not None and self.stat_id in STATS:
#         # Get reforge_increase value
#             self.reforge_increase = STATS[self.stat_id]['reforge'][self.stat_type][rolled]
#             return self.reforge_increase
#         else:
#             raise ValueError("Invalid stat_id or missing self.stat_id")
        

    def parse_stat(self, stat_type=None, gear_type=None, gear_grade=None, 
                   gear_level=85, mod=False, rolled=None, mod_type='greater'):
        """
        Parses a stat based on its type ('substat' or 'mainstat') and given gear grade and level.
        Also checks whether modification is being applied and parses the appropriate mod value based on rolled count.

        Args:
            stat_type (str): The type of stat - 'mainstat' or 'substat only' (default: 'substat')
            gear_type (str): The type of gear - 'weapon', 'helm', 'armor', 'necklace',
                'ring', or 'boots' only.
            gear_grade (str): grade of the gear - 'normal', 'good', 'rare', 'heroic', 'epic' (default: None)
            gear_level (int): level of gear, between 58 and 100 (default: 85)
            mod (bool): boolean specifying whether this is a modded stat or not (default: False)
            rolled (int): number of times a stat has been rolled when enhancing (default: None = 0)
            mod_type (str): type of modification - 'greater' or 'lower' (default: 'greater')

        Returns:
            dict: parsed Stat data
        """

        # Check if stat exists before trying to parse it
        if self.stat_id is None:
            raise ValueError("Cannot parse until a stat has been fetched.")

        # Use the specified gear_type if provided, otherwise use the class attribute
        if gear_type is not None:
            self.gear_type = validate_gear_type(gear_type)

        # Use the specified stat_type if provided, otherwise use the class attribute
        if stat_type is not None:
            self.stat_type = validate_stat_type(stat_type, mod = mod, rolled = rolled)
            
        # Get the corresponding stat from stats dict based on id
        stat = STATS[self.stat_id]
        
        # Validate inputs and assign attributes:
        self.text = stat['text']
        self.gear_grade = validate_gear_grade(gear_grade)
        self.gear_level = validate_gear_level(gear_level)
        self.gear_tier = get_gear_tier(gear_level)
        self.rolled = validate_rolled(rolled, self.stat_type)
        mod = validate_mod(mod, self.stat_type)
        mod_type = validate_mod_type(mod_type)

        # Parse modified stat
        if mod:
            self.modded = True
            value = get_mod_value(
                self.stat_id,
                self.gear_level,
                self.rolled,
                mod_type)
        # Parse non-modified stat
        else:
            value = get_stat_value(
                self.stat_id,
                self.stat_type,
                self.gear_level,
                self.gear_grade)

        # Assign Parsed attributes
        self.value = value
        self.value_key = stat['vars'][self.stat_type]['key']

        # Reforge increase value
        self.reforge_increase = get_reforge_increase(
            self.stat_id, self.stat_type, self.rolled)

        return self
    

    def format_stat(self, show_reforged=False):
        """
        Returns a concise representation of the stat value.
        
        Args:
            show_reforged (bool): Whether to show the reforged value or not
        """

        # Get the original 'text' description from the parsed stat
        text = self.text

        if self.stat_type == 'mainstat':
            reforged_value = self.reforge_increase
        else:
            reforged_value = self.value + self.reforge_increase

        # Replace 'key' with 'value' in the text
        text = text.replace(self.value_key, str(self.value))

        # If we want to show reforged value in parenthesis next to current stat
        if show_reforged:
            if self.stat_id in ['1', '3', '5', '6', '7', '8', '9']:
                # Make sure there is a % for the percent stats
                text = text.replace('<B>', '(' + str(reforged_value) + '%) ')
            else:
                # If it's a flat stat, empty string for <B> key
                text = text.replace('<B>', '(' + str(reforged_value) + ') ')
        else:
            # If we don't want to show reforged value
            text = text.replace('<B>', '')

        if self.modded:
            text = text + ' (modded)'
        
        # Assign attribute
        self.text_formatted = text

        # Return the formatted text representation of the parsed stat
        return text
    
    
    def enhance_stat(self, enhance_level=0):
        """
        Method to enhance a stat.

        Args:
            enhance_level (int) : Current level of enhancement on the gear

        Returns:
            self
        """
        # Validate inputs
        enhance_level = validate_enhance_level(enhance_level)

        # Get stat attributes
        stat_type = self.stat_type
        stat_id = self.stat_id
        gear_level = self.gear_level
        gear_tier = get_gear_tier(gear_level)
        gear_grade = self.gear_grade
        
        # Enhancement for mainstat
        if stat_type == 'mainstat':
            mainstat_multiplier = [
                1.2,
                1.4,
                1.6,
                1.8,
                2,
                2.2,
                2.4,
                2.6,
                2.8,
                3,
                3.3,
                3.6,
                3.9,
                4.25,
                5]
            # Get the base value at enhance level 0
            base_value = get_stat_value(stat_id, 'mainstat', gear_level, gear_grade)
            # Get enhanced value at new enhance level
            enhanced_value = round(base_value * mainstat_multiplier[enhance_level])

            # Assign the new value
            self.value = enhanced_value
            # Update formatted text
            self.format_stat()

        # Enhancement for substat
        else:
            pass
            # Get an enhanced stat value
            enhanced_value = get_stat_value(stat_id, 'substat', gear_level, gear_grade)

            # Add the enhanced value to current value:
            self.value += enhanced_value
            # Update rolled count:
            self.rolled += 1
            # Update reforge increase value
            self.reforge_increase = get_reforge_increase(
                stat_id, stat_type, self.rolled)
            # Update formatted text
            self.format_stat()

        return self