import json
import random
from src.validation_utils import *

# Import Data on STATS
STATS = json.loads(open('data/stats.json', 'r').read())
TYPES = json.loads(open('data/types.json', 'r').read())


class Stat:
    """A class to represent the statistics that are added to a gear."""

    def __init__(self):
        """
        Initializes the Stat object.
        Args:
            stat_id (int or str): The id of the stat to retrieve (refer to STATS.json for id).
            stat_type (str): The type of stat - 'mainstat' or 'substat only'.
            gear_type (str): The type of gear - 'weapon', 'helm', 'armor', 'necklace',
                    'ring', or 'boots' only. (default: None)
            rolled (int): value between 0 and 5; how many times a stat rolled when enhancing
            reforge_increase (int) : The value by which a stat increases when reforging

        """
        self.data = None
        self.stat_id = None
        self.stat_type = 'mainstat'
        self.gear_type = None
        self.rolled = None
        self.reforge_increase = None

    def get_stat_by_id(self, stat_id):
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
                # Return the stat dictionary associated with the ID
                return stat_data
        # Return None if the provided ID doesn't match any stat
        return None

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
        self.stat_type = stat_type
        self.gear_type = gear_type

        return random_stat
    
    def get_reforge_increase(self, rolled):
        """
        Get the value by which a stat will increase by when an item has been reforged.

        Args:
            rolled (int): value between 0 and 5; how many times a stat rolled when enhancing
        """
        # Validate inputs
        rolled = validate_rolled(rolled)
        
        if self.stat_id is not None and self.stat_id in STATS:
        # Get reforge_increase value
            self.reforge_increase = STATS[self.stat_id]['reforge'][self.stat_type][rolled]
            return self.reforge_increase
        else:
            raise ValueError("Invalid stat_id or missing self.stat_id")
        
