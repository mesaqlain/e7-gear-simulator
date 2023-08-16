import json
import random
from src.validation_utils import *

# Import Data on STATS
STATS = json.loads(open('data/stats.json', 'r').read())


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
            gear_type (str): The type of gear - 'Weapon', 'Helm', 'Armor', 'Necklace',
                'Ring', or 'Boots' only.

        Returns:
            dict: Stat data
        """

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