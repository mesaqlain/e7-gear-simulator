import json

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
        # Convert the provided ID to a string
        str_id = str(stat_id)
        # Iterate through each entry in STATS dict
        for s in STATS:
            # Check if the given ID exists in the current section
            if str_id in s:
                # Return the stat dictionary associated with the ID
                return STATS[str_id]
        # Return None if the provided ID doesn't match any stat
        return None