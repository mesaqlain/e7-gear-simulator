from set_directory_function import set_directory
set_directory()

import json
import random
from src.validation_utils import *
from src.utilities import *

# Import Data 
STATS = json.loads(open('data/stats.json', 'r').read())
TYPES = json.loads(open('data/types.json', 'r').read())
GRADES = json.loads(open('data/grades.json', 'r').read())
TIERS = json.loads(open('data/tiers.json', 'r').read())
SETS = json.loads(open('data/sets.json', 'r').read())

class Gear():
    """
    Gear class that holds mainstats and substats with enhance, reforge, and modify methods
    """

    def __init__(self):
        """
        Initializes the Gear object.
        Args:

        """
        self.gear_type = None
        self.gear_grade = None
        self.gear_set = None
        self.gear_level = 85
        self.gear_tier = 6
        self.enhance_level = 0
        self.is_reforged = False
        self.mainstat = None
        self.mainstat_id = None
        self.substats = None
        self.substat_ids = None

    def create_gear(self, gear_type=None, gear_grade=None, gear_set=None, gear_level=85,
                    mainstat_id=None, substat_ids=None):
        """
        Method to create a new gear. If arguments are set to None, a completely random gear of
        level 85 is created.
        """

        # Validate Inputs
        self.gear_type = validate_gear_type(gear_type)
        self.gear_set = validate_gear_set(gear_set)
        self.gear_level = validate_gear_level(gear_level)
        self.gear_tier = get_gear_tier(self.gear_level)

        if gear_grade is not None:
            self.gear_grade = validate_gear_grade(gear_grade)
            # Number of starting substats the item will have
            starting_substats = GRADES[self.gear_grade]['starting_substats']

        if mainstat_id is not None:
            self.mainstat_id = validate_stat_id(mainstat_id)

        if substat_ids is not None:
            self.substat_ids = validate_substat_ids(substat_ids, self.mainstat_id)

        return self