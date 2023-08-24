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
        self.substats = None
        self.mainstat_id = None
        self.substat_ids = None
        
        
    def __str__(self):
        """Str representation of class"""
        return (
            f"Type: {self.gear_type}\n"
            f"Grade: {self.gear_grade}\n"
            f"Set: {self.gear_set}\n"
            f"Level: {self.gear_level}\n"
            f"Tier: {self.gear_tier}\n"
            f"Enhance Level: {self.enhance_level}\n"
            f"Reforged: {self.is_reforged}\n"
            f"Mainstat: {self.mainstat}\n"
            f"Substats: {self.substats}\n"
            f"Mainstat IDs: {self.mainstat_id}\n"
            f"Substat IDs: {self.substat_ids}"
        )

        
    def create_gear(self, gear_type=None, gear_grade=None, gear_set=None, gear_level=85,
                    mainstat_id=None, substat_ids=None):
        """
        Method to create a new gear. If arguments are set to None, a completely random gear of
        level 85 is created.
        """

        # Validate Inputs
        self.gear_set = validate_gear_set(gear_set)
        self.gear_level = validate_gear_level(gear_level)
        self.gear_tier = get_gear_tier(self.gear_level)

        self.mainstat_id = validate_mainstat_id(
            mainstat_id, substat_ids)

        self.substat_ids = validate_substat_ids(
            substat_ids, mainstat_id)

        # Get an appropriate gear_grade, if no substats or mainstats provided,
        # should be completely random, otherwise get a gear_type based on provided
        # mainstats and/or substats
        self.gear_grade = validate_gear_grade(
            gear_grade, 
            mainstat_id=self.mainstat_id, 
            substat_ids=self.substat_ids)
        starting_substats = GRADES[self.gear_grade]['starting_substats']

        # Get an appropriate gear_type, if no mainstats or substats provided,
        # should be completely random, otherwise get a gear_type based on provided
        # mainstats and/or substats
        self.gear_type = self.get_gear_type(
            gear_type, self.mainstat_id, self.substat_ids)

        return self
    
    
    def get_gear_type(self, gear_type=None, mainstat_id=None, substat_ids=None):
        """
        Retrieves a random gear type based on provided mainstat_id and substat_id.
        Used in the create_gear() method in Gear() class.
        
        Args:
            gear_type (str): Type of gear
            mainstat_id (int or str): Valid stat id [0, 10]
            substat_id (int or list of int): List of valid substat id's, can take up to 4 substat_id's
            
        Returns:
           gear_type (str)
        """
        # Validate inputs
        gear_type = validate_gear_type(gear_type)

        if mainstat_id is not None:
            mainstat_id = validate_mainstat_id(mainstat_id, substat_ids)

        if substat_ids is not None:
            substat_ids = validate_substat_ids(substat_ids, mainstat_id)

        # If no args provided, get a random gear type
        if mainstat_id is None and substat_ids is None and gear_type is None:
            gear_type = get_random_gear_type()
            return gear_type

        # If mainstat_id is provided
        if mainstat_id is not None:
            # If gear_type is not provided
            if gear_type is None:
                # Get a random gear_type
                gear_type = get_random_gear_type()
                # Ensure that mainstat is in the allowed pool of mainstats for gear_type
                while int(mainstat_id) not in TYPES[gear_type]['mainstat']:
                    gear_type = get_random_gear_type()
                    # If substat_id's are provided, ensure that the substat_id's
                    # are in the allowed pool of substats for gear_type
                    if substat_ids is not None:
                        gear_type = get_gear_type_from_subs(gear_type, substat_ids)

            # If gear_type is provided
            else:
                # Check if provided mainstat is allowed in provided gear_type
                if int(mainstat_id) not in TYPES[gear_type]['mainstat']:
                    raise ValueError(f"{gear_type} cannot have {mainstat_id} as mainstat.")
                # If substat_id's are provided, ensure that the substat_id's are
                # in the allowed pool of substats for gear_type
                if substat_ids is not None and any(s not in convert_int_to_str(
                    TYPES[gear_type]['substat']) for s in substat_ids):
                    raise ValueError(f"{gear_type} cannot have one or more of these substats")

        # If mainstat_id is not provided    
        else: 
            # If gear_type is not provided
            if gear_type is None:
                gear_type = get_random_gear_type()
                # If substat_id's are provided, ensure that the substat_id's
                # are in the allowed pool of substats for gear_type
                if substat_ids is not None:
                    gear_type = get_gear_type_from_subs(gear_type, substat_ids)

            # If gear_type is provided
            else:
                # If substat_id's are provided, ensure that the substat_id's are
                # in the allowed pool of substats for gear_type
                if substat_ids is not None and any(s not in convert_int_to_str(
                    TYPES[gear_type]['substat']) for s in substat_ids):
                    raise ValueError(f"{gear_type} cannot have one or more of these substats")

        return gear_type
    
    
    