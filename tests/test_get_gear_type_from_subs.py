from set_directory_function import set_directory
set_directory()

import unittest
import json
from src.utilities import get_gear_type_from_subs 

with open('data/types.json', 'r') as types_file:
    TYPES = json.load(types_file)

class TestGetGearTypeFromSubs(unittest.TestCase):
    
    def test_default(self):
        """
        Default args, so gear_type = None and substat_ids=None
        This implies substat_ids is an empty list and we'll get a completely random gear
        """
        expect_gear_types = set(TYPES.keys())
        picked_gear_types = set()
        
        for i in range(10000):
            gear_type = get_gear_type_from_subs()
            picked_gear_types.add(gear_type)
            self.assertIn(gear_type, list(expect_gear_types), f"{gear_type} is not in expect_gear_types")
        
        missing = expect_gear_types - picked_gear_types 
        extra = picked_gear_types - expect_gear_types
        
        self.assertFalse(missing, f"The following values were not selected: {missing}")
        self.assertFalse(extra, f"The following extra values were selected: {extra}")
        
        
    def test_no_subs_1(self):
        """
        gear_type = 'weapon' and substat_ids=None
        This implies substat_ids is an empty list and we'll always get 'weapon' back
        """
        expect_gear_types = set(['weapon'])
        picked_gear_types = set()
        
        for i in range(10000):
            gear_type = get_gear_type_from_subs(gear_type='weapon')
            picked_gear_types.add(gear_type)
            self.assertIn(gear_type, list(expect_gear_types), f"{gear_type} is not in expect_gear_types")
        
        missing = expect_gear_types - picked_gear_types 
        extra = picked_gear_types - expect_gear_types
        
        self.assertFalse(missing, f"The following values were not selected: {missing}")
        self.assertFalse(extra, f"The following extra values were selected: {extra}")
        
        
    def test_no_subs_2(self):
        """
        gear_type = 'ring' and substat_ids=None
        This implies substat_ids is an empty list and we'll always get 'ring' back
        """
        expect_gear_types = set(['ring'])
        picked_gear_types = set()
        
        for i in range(10000):
            gear_type = get_gear_type_from_subs(gear_type='ring')
            picked_gear_types.add(gear_type)
            self.assertIn(gear_type, list(expect_gear_types), f"{gear_type} is not in expect_gear_types")
        
        missing = expect_gear_types - picked_gear_types 
        extra = picked_gear_types - expect_gear_types
        
        self.assertFalse(missing, f"The following values were not selected: {missing}")
        self.assertFalse(extra, f"The following extra values were selected: {extra}")
        
        
    def test_no_subs_3(self):
        """
        gear_type = 'ring' and substat_ids=None
        This implies substat_ids is an empty list and we'll always get 'ring' back
        """
        expect_gear_types = set(['ring'])
        picked_gear_types = set()
        
        for i in range(10000):
            gear_type = get_gear_type_from_subs(gear_type='ring', substat_ids=[])
            picked_gear_types.add(gear_type)
            self.assertIn(gear_type, list(expect_gear_types), f"{gear_type} is not in expect_gear_types")
        
        missing = expect_gear_types - picked_gear_types 
        extra = picked_gear_types - expect_gear_types
        
        self.assertFalse(missing, f"The following values were not selected: {missing}")
        self.assertFalse(extra, f"The following extra values were selected: {extra}")
        
        
    def test_no_type_1(self):
        """
        gear_type = None and substat_ids=[0,2,4]
        Those substats are not allowed on weapons, armor, and helm, so we can expect to never pick those
        """
        expect_gear_types = set(['ring', 'necklace', 'boots'])
        picked_gear_types = set()
        
        for i in range(10000):
            gear_type = get_gear_type_from_subs(substat_ids=[0, 2, 4])
            picked_gear_types.add(gear_type)
            self.assertIn(gear_type, list(expect_gear_types), f"{gear_type} is not in expect_gear_types")
        
        missing = expect_gear_types - picked_gear_types 
        extra = picked_gear_types - expect_gear_types
        
        self.assertFalse(missing, f"The following values were not selected: {missing}")
        self.assertFalse(extra, f"The following extra values were selected: {extra}")
        
        
    def test_no_type_2(self):
        """
        gear_type = None and substat_ids=[0]
        Those substats are not allowed on weapons and armor, so we can expect to never pick those
        """
        expect_gear_types = set(['ring', 'necklace', 'boots', 'helm'])
        picked_gear_types = set()
        
        for i in range(10000):
            gear_type = get_gear_type_from_subs(substat_ids=0)
            picked_gear_types.add(gear_type)
            self.assertIn(gear_type, list(expect_gear_types), f"{gear_type} is not in expect_gear_types")
        
        missing = expect_gear_types - picked_gear_types 
        extra = picked_gear_types - expect_gear_types
        
        self.assertFalse(missing, f"The following values were not selected: {missing}")
        self.assertFalse(extra, f"The following extra values were selected: {extra}")
        
        
    def test_type_n_subs_1(self):
        """
        gear_type = 'weapon' and substat_ids=[0]
        Those substats are not allowed on weapons (even though we specify it) and armor, 
        so we can expect to never pick those
        """
        expect_gear_types = set(['ring', 'necklace', 'boots', 'helm'])
        picked_gear_types = set()
        
        for i in range(10000):
            gear_type = get_gear_type_from_subs(gear_type='weapon', substat_ids=[0])
            picked_gear_types.add(gear_type)
            self.assertIn(gear_type, list(expect_gear_types), f"{gear_type} is not in expect_gear_types")
        
        missing = expect_gear_types - picked_gear_types 
        extra = picked_gear_types - expect_gear_types
        
        self.assertFalse(missing, f"The following values were not selected: {missing}")
        self.assertFalse(extra, f"The following extra values were selected: {extra}")
        
        
    def test_type_n_subs_2(self):
        """
        gear_type = 'ring' and substat_ids=[10, 6, 7, 3]
        Those substats are allowed everywhere, including on the ring,
        so we can expect to always get ring
        """
        expect_gear_types = set(['ring'])
        picked_gear_types = set()
        
        for i in range(10000):
            gear_type = get_gear_type_from_subs(gear_type='ring', substat_ids=[10, 6, 7, 3])
            picked_gear_types.add(gear_type)
            self.assertIn(gear_type, list(expect_gear_types), f"{gear_type} is not in expect_gear_types")
        
        missing = expect_gear_types - picked_gear_types 
        extra = picked_gear_types - expect_gear_types
        
        self.assertFalse(missing, f"The following values were not selected: {missing}")
        self.assertFalse(extra, f"The following extra values were selected: {extra}")
        
        
    def test_type_n_subs_3(self):
        """
        gear_type = 'weapon' and substat_ids=[0, 3, 10, 8]
        0 isn't allowed on weapon and armor, but the other stats are all allowed elsewhere
        so we can expect to always get anything but weapon or armor
        """
        expect_gear_types = set(['ring', 'helm', 'boots', 'necklace'])
        picked_gear_types = set()
        
        for i in range(10000):
            gear_type = get_gear_type_from_subs(gear_type='weapon', substat_ids=[0, 3, 10, 8])
            picked_gear_types.add(gear_type)
            self.assertIn(gear_type, list(expect_gear_types), f"{gear_type} is not in expect_gear_types")
        
        missing = expect_gear_types - picked_gear_types 
        extra = picked_gear_types - expect_gear_types
        
        self.assertFalse(missing, f"The following values were not selected: {missing}")
        self.assertFalse(extra, f"The following extra values were selected: {extra}")
        
                
if __name__ == '__main__':
    unittest.main()
