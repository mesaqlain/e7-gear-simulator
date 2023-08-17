import json
import random
from src.validation_utils import *

# Import Data on STATS
STATS = json.loads(open('data/stats.json', 'r').read())
TYPES = json.loads(open('data/types.json', 'r').read())


class Stat:
    """A class to represent the statistics that are added to a gear."""

    def __init__(self):
        """Initializes the Stat object."""
        self.data = None

    def get_stat_by_id(self, stat_id):
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
        return self.get_stat_by_id(stat_id=random.choice(pool))

    def get_non_overlapping_stat(
        self, selected_stats=[], stat_type='substat', gear_type=None):
        """
        Retrieves a new stat that is not already in the selected list of stats.

        Args:
            selected_stats (list): List containing Stat objects (default: empty list [])
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
        stat = self.get_random_stat(stat_type, gear_type)

        # If the stat we got in the previous line exists in our selected stats,
        # get a new random stat
        while any(stat['id'] == a['id'] for a in selected_stats):
            # Get a new random stat as long as above condition is True
            stat = self.get_random_stat(stat_type, gear_type)

        return stat