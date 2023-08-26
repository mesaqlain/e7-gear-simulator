import json
import random
from src.validation_utils import *
from src.utilities import *
from src.stats import Stat

# Import Data 
with open('data/types.json', 'r') as types_file:
    TYPES = json.load(types_file)
with open('data/sets.json', 'r') as sets_file:
    SETS = json.load(sets_file)
with open('data/tiers.json', 'r') as tiers_file:
    TIERS = json.load(tiers_file)
with open('data/grades.json', 'r') as grades_file:
    GRADES = json.load(grades_file)
with open('data/stats.json', 'r') as stats_file:
    STATS = json.load(stats_file)
    
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
        self.substats = []
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
        
        # Get an appropriate mainstat_id based on gear_type. If no mainstat or substats
        # are provided, get a random mainstat that is in the available pool for given gear type.
        # If substats are provided, non duplicate mainstat is chosen
        self.mainstat_id = self.get_mainstat_id(
            self.mainstat_id, self.substat_ids, self.gear_type)
        
        # Get substats based on gear_type, mainstat_id, and other substat_ids. If no mainstat or substats
        # are provided, get n random non-overlapping substats that is in the available pool for given gear type.
        # If substats are provided, non duplicate mainstat is chosen
        self.substat_ids = self.get_substat_ids(
            self.mainstat_id,
            self.substat_ids,
            self.gear_type,
            self.gear_grade)
        
        self.mainstat = self.get_stat(self.mainstat_id, 'mainstat', self.gear_type, self.gear_grade,
                                     self.gear_level)
        
        if len(self.substat_ids) > 0:
            for i in self.substat_ids:
                self.substats.append(self.get_stat(i, 'substat', self.gear_type, self.gear_grade,
                                     self.gear_level))
            
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
            mainstat_id = validate_stat_id(mainstat_id)

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
    
    
    def get_mainstat_id(self, mainstat_id=None, substat_ids=None, gear_type=None):
        """
        Get a mainstat_id based on provided substat_ids and gear_type.
        Gear_type cannot be none. If no substat_ids or mainstat_ids are provided, an appropriate random
        mainstat_id is chosen from the available pool of id's for given gear_type.
        If substat_id's are provided, mainstat_id is chosen in a way so as not to be same as substat id.
        Args:
            mainstat_id (int or st): valid mainstat id from range(0, 11)
            substat_ids (int/str or list of int/str): valid list of substat id(s) from range(0,11)
            gear_type (str): valid gear type from types.json: 'weapon', 'helm', 'armor', 'necklace', 'ring', or 'boots'
        """
        # gear_type cannot be none for this function
        if gear_type is None:
            raise ValueError(
                "Please provide a valid gear type: 'weapon', 'helm', 'armor', 'necklace', 'ring', or 'boots'.")
        else:
            gear_type = validate_gear_type(gear_type)

        # Available pool of id's for given gear_type (convert to str)
        mainstat_pool = convert_int_to_str(list(TYPES[gear_type]['mainstat']))
        substats_pool = convert_int_to_str(list(TYPES[gear_type]['substat']))

        # If no substat_ids provided
        if substat_ids is None:
            # If no mainstat id provided
            if mainstat_id is None:
                # Pick a random mainstat
                mainstat_id = random.choice(mainstat_pool)
            # If mainstat id is provided
            else:
                mainstat_id = validate_mainstat_id(mainstat_id)
                if mainstat_id not in mainstat_pool:
                    raise ValueError(
                        f"{gear_type} cannot have stat with id {mainstat_id}.")
        # If substat_ids are provided
        else:
            # Validate substats
            substat_ids = validate_substat_ids(substat_ids)
            if any(s not in substats_pool for s in substat_ids):
                raise ValueError(
                    "One or more of the substats cannot be added to this gear_type.")
            # If no mainstat id provided
            if mainstat_id is None:
                # Pick a random mainstat
                mainstat_id = random.choice(mainstat_pool)
                # If randomly chosen mainstat is already in provided substats
                # get a new random mainstat
                while mainstat_id in substat_ids:
                    mainstat_id = random.choice(mainstat_pool)
            # If mainstat id is provided
            else:
                mainstat_id = validate_mainstat_id(mainstat_id)
                if mainstat_id in substat_ids:
                    raise ValueError(
                        "Mainstat id and substat id cannot share same stats.")
                if mainstat_id not in mainstat_pool:
                    raise ValueError(
                        f"{gear_type} cannot have stat with id {mainstat_id}.")

        return mainstat_id    
    
    
    def get_substat_ids(self, mainstat_id=None, substat_ids=None, gear_type=None, gear_grade=None):
        """
        Get substat_ids based on provided gear_type, gear_grade, mainstat_id, and potential other provided substat_ids.
        Gear_type, gear_grade, and mainstat_id cannot be none. Substat_id's are optional.
        If no substat_ids are provided, gear type appropriate random substat_ids are chosen to fill the starting
        number of substats for given gear grade. General restrictions apply, such as mainstat cannot be same as substats,
        duplicate substats are not allowed, cannot have more than 4 substats, and a grade cannot have more substats
        than the allowed starting substats number.

        Args:
            mainstat_id (int or st): valid mainstat id from range(0, 11)
            substat_ids (int/str or list of int/str): valid list of substat id(s) from range(0,11)
            gear_type (str): valid gear type from types.json: 'weapon', 'helm', 'armor', 'necklace', 'ring', or 'boots'
            gear_grade (str): valid gear grade from grades.json: 'normal', 'good', 'rare', 'heroic', 'epic'
        """
        # gear_type cannot be none for this function
        if gear_type is None:
            raise ValueError(
                "Please provide a valid gear type: 'weapon', 'helm', 'armor', 'necklace', 'ring', or 'boots'.")
        else:
            gear_type = validate_gear_type(gear_type)

        # gear_grade cannot be none for this function
        if gear_grade is None:
            raise ValueError(
                "Please provide a valid gear grade: 'normal', 'good', 'rare', 'heroic', or 'epic'.")
        else:
            gear_grade = validate_gear_grade(gear_grade, mainstat_id, substat_ids)

        # mainstat_id cannot be none for this function
        if mainstat_id is None:
            raise ValueError(
                "Please provide a valid mainstat id.")
        else:
            mainstat_id = validate_mainstat_id(mainstat_id, substat_ids, gear_type)

        # Validate substat_ids:
        substat_ids = validate_substat_ids(substat_ids, mainstat_id, gear_type)

        # Available pool of id's for given gear_type (convert to str)
        substats_pool = convert_int_to_str(list(TYPES[gear_type]['substat']))

        # Number of starting substats allowed on gear
        starting_substats = GRADES[gear_grade]['starting_substats']

        # Number of substats that still needs to be added to gear:
        subs_remaining = starting_substats - len(substat_ids)

        # Initialize gear pool list which will hold both mainstat and substat ids:
        gear_pool = substat_ids + [mainstat_id]

        # Add new non-overlapping substats until we have the appropriate number of 
        # starting substats
        for i in range(subs_remaining):
            new_substat_id = get_non_overlapping_stat_id(gear_pool, gear_type=gear_type, stat_type='substat')
            substat_ids.append(new_substat_id)
            gear_pool.append(new_substat_id)

        return substat_ids
    
    
    def get_stat(self, stat_id=None, stat_type='mainstat', gear_type=None, gear_grade=None, 
             gear_level=85, mod=False, rolled=None, mod_type='greater', show_reforged=False):
        """
        get_stat method for Gear() class to retrieve stat information based on given attributes. All attributes must be provided.
        
        Args:
            stat_id (str or int): valid stat id (0 to 10)
            stat_type (str): The type of stat - 'mainstat' or 'substat only' (default: 'mainstat')
            gear_type (str): The type of gear - 'weapon', 'helm', 'armor', 'necklace',
                'ring', or 'boots' only.
            gear_grade (str): grade of the gear - 'normal', 'good', 'rare', 'heroic', 'epic' (default: None)
            gear_level (int): level of gear (58 to 100) (default: 85)
            mod (bool): boolean specifying whether this is a modded stat or not (default: False)
            rolled (int): number of times a stat has been rolled when enhancing (default: None = 0)
            mod_type (str): type of modification - 'greater' or 'lower' (default: 'greater')
            show_reforged (bool): whether to show the reforged value for formatted text (default: False)

        """
        # Initialize an empty stat class object
        stat = Stat()
        # Get the stat info by id
        stat.get_stat_by_id(stat_id, stat_type, gear_type)
        # Parse the stat (get a specific value)
        stat.parse_stat(stat_type, gear_type, gear_grade, 
                       gear_level, mod, rolled, mod_type)
        # Get formatted text
        stat.format_stat(show_reforged=show_reforged)

        return stat
    
    
    def get_gear_score(self):
        """
        Calculate the standardizd gear score of an item
        Args:
            gear (Gear): gear object

        Returns:
            list of two values -
                first value is gear score before reforge
                second value is gear score after reforge
        """
        # Initialize variables, which will increase as we loop through the stats
        gear_score = 0
        reforged_score = 0

        # Loop through each substat and add to the score variables
        for s in self.substats:
            # ID of the stat
            s_id = str(s.stat_id)
            # Parsed value
            s_val = s.value

            # Calculate the gear score before reforge:
            gear_score += s_val * STATS[s_id]['gscore']

            # Stat value after reforge
            s_val_ref = s_val + s.reforge_increase
            # Calculate the gear score after reforge based on stat multiplier
            reforged_score += s_val_ref * STATS[s_id]['gscore']

        return [round(gear_score), round(reforged_score)]
    
    
    def print_gear(self):
        """
        Print the contents of the gear gear. 
        Displays the enhancement level, gear grade, type, and level on first line.
        Displays the MAINSTAT next.
        Displays the SUBSTAT(S) last.
        """
        print('---')
        print(
            f"+{self.enhance_level} {self.gear_grade.capitalize()} {self.gear_type.capitalize()} (Lv {self.gear_level})")
        print(f"{self.gear_set.capitalize()} Set")

        print('---')
        print('MAIN STAT:')
        print(self.mainstat.format_stat())

        print('---')
        # Singular/Plurarl
        if len(self.substats) == 1:
            print('SUBSTAT:')
        else:
            print('SUBSTATS:')

        for s in self.substats:
            # If gear has been reforged, no need to show reforged stats
            print(s.format_stat(show_reforged=not self.is_reforged))
        
        # Get Gear Score
        gear_score = self.get_gear_score()
        
        print('---')
        if self.is_reforged:
            print(f'GEAR SCORE: {gear_score[0]}')
        else:
            print(f'GEAR SCORE: {gear_score[0]} ({gear_score[1]})')
            
            
    def add_substat(self, verbose = False):
        """
        Adds a new substat to the gear that isn't already in the mainstat or substats.
        """
        # Current number of substats on gear
        no_of_substats = len(self.substat_ids)

        if no_of_substats == 4:
            raise ValueError("Gear already has maximum number of allowed substats.")

        # Available pool of id's for given gear_type (convert to str)
        substats_pool = convert_int_to_str(list(TYPES[self.gear_type]['substat']))

        # Initialize gear pool list which will hold both mainstat and substat ids:
        gear_pool = self.substat_ids + [self.mainstat_id]

        # Get a new non-overlapping substat 
        new_substat_id = get_non_overlapping_stat_id(gear_pool, gear_type=self.gear_type, stat_type='substat')
        self.substat_ids.append(new_substat_id)
        new_substat = self.get_stat(new_substat_id, 'substat', self.gear_type, self.gear_grade,
                                         self.gear_level)
        self.substats.append(new_substat)

        if verbose:
            print(f'New Substat Added: {new_substat.text_formatted}!')

        return self
    
    
    def enhance_gear(self, verbose = False):
        """
        Method to enhance a gear.
        """
        # Current enhance level:
        enhance_level = self.enhance_level

        # Check if gear is already at max enhance level
        if enhance_level == 15:
            print("Gear is already at maximum enhancement level!")

        else:
            # Enhance mainstat
            self.mainstat.enhance_stat(enhance_level)

            # Enhance Substat Conditions
            # Rare Gear
            if self.gear_grade == 'rare' and (enhance_level == 8 or enhance_level == 11):
                self.add_substat(verbose = verbose)

            elif self.gear_grade == 'heroic' and (enhance_level == 11):
                self.add_substat(verbose = verbose)

            elif ((enhance_level + 1) % 3) == 0:  # Enhance only at 3 level increments
                random_substat = random.choice(self.substats)
                random_substat_value_before = random_substat.value
                # Enhance
                random_substat.enhance_stat(enhance_level)
                random_substat_value_after = random_substat.value            

                if verbose:
                    # Difference in value
                    enhanced_value = random_substat_value_after - random_substat_value_before
                    text = '+' + \
                        random_substat.text + ' Increase!'
                    text = text.replace(
                        '<A>', str(enhanced_value)).replace(
                        '<B>', '')
                    print(text)

            # Update enhancement level
            self.enhance_level += 1
            # If gear is at +15
            if self.enhance_level == 15:
                print("Gear has been fully enhanced to +15!")

        return self