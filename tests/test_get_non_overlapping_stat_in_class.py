from set_directory_function import set_directory
set_directory()

import unittest
import json
import random
from src.validation_utils import *
from src.stats import Stat

STATS = json.loads(open('data/stats.json', 'r').read())

class TestNonOverlappingStatInClass(unittest.TestCase):
    
    def setUp(self):
        self.stat = Stat()
        
    def tearDown(self):
        self.stat = None
    
    def test_non_overlapping_stat_empty(self):
        """Test whether each stat is selected at least once when input is empty, instantiated inside a Stat object"""
        selected_stats = []
        selected_stat_ids = set()

        # Generate 1000 random stats for 'weapon' gear type
        for _ in range(1000):
            stat = self.stat.get_non_overlapping_stat(selected_stats)
            selected_stat_ids.add(str(stat['id']))  # Convert id to string before adding to set
            # Verify that the generated stat is a valid entry in STATS
            self.assertTrue(stat in STATS.values(), f"Generated stat has an invalid ID: {stat['id']}")
            stat_id = self.stat.stat_id
            stat_type = self.stat.stat_type
            gear_type = self.stat.gear_type
            self.assertIn(stat_id, STATS.keys(), "Non-overlapping-stat should have id from the STATS dict")
            self.assertIn(stat_type, 'substat', "Non-overlapping-stat should have stat_type = 'substat' if None")
            self.assertIsNone(gear_type, "Non-overlapping-stat should have gear_type None if None")


        # Ensure that all id's are selected
        expected_stat_ids = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'}
        missing_stat_ids = expected_stat_ids - selected_stat_ids
        extra_stat_ids = selected_stat_ids - expected_stat_ids

        self.assertFalse(missing_stat_ids, f"The following stat IDs were not selected: {missing_stat_ids}")
        self.assertFalse(extra_stat_ids, f"The following extra stat IDs were selected: {extra_stat_ids}")

    def test_non_overlapping_stat_none(self):
        """Test whether each stat is selected at least once when input is empty, instantiated inside a Stat object"""
        selected_stats = None
        selected_stat_ids = set()

        # Generate 1000 random stats for 'weapon' gear type
        for _ in range(1000):
            stat = self.stat.get_non_overlapping_stat(selected_stats)
            selected_stat_ids.add(str(stat['id']))  # Convert id to string before adding to set
            # Verify that the generated stat is a valid entry in STATS
            self.assertTrue(stat in STATS.values(), f"Generated stat has an invalid ID: {stat['id']}")
            stat_id = self.stat.stat_id
            stat_type = self.stat.stat_type
            gear_type = self.stat.gear_type
            self.assertIn(stat_id, STATS.keys(), "Non-overlapping-stat should have id from the STATS dict")
            self.assertIn(stat_type, 'substat', "Non-overlapping-stat should have stat_type = 'mainstat' if None")
            self.assertIsNone(gear_type, "Non-overlapping-stat should have gear_type None if None")


        # Ensure that all id's are selected
        expected_stat_ids = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'}
        missing_stat_ids = expected_stat_ids - selected_stat_ids
        extra_stat_ids = selected_stat_ids - expected_stat_ids

        self.assertFalse(missing_stat_ids, f"The following stat IDs were not selected: {missing_stat_ids}")
        self.assertFalse(extra_stat_ids, f"The following extra stat IDs were selected: {extra_stat_ids}")
        
        
    def test_non_overlapping_stat_single(self):
        """
        Test whether all stats other than the chosen stat is selected at least once, 
        instantiated inside a Stat object
        """
        selected_stats = [random.choice([str(key) for key in STATS.keys()])]
        selected_stat_ids = set(selected_stats)
        non_overlapping_stat_ids = set()

        # Generate 1000 random stats 
        for _ in range(1000):
            stat = self.stat.get_non_overlapping_stat(selected_stats)
            non_overlapping_stat_ids.add(str(stat['id']))  # Convert id to string before adding to set
            # Verify that the generated stat is a valid entry in STATS
            self.assertTrue(stat in STATS.values(), f"Generated stat has an invalid ID: {stat['id']}")
            stat_id = self.stat.stat_id
            stat_type = self.stat.stat_type
            gear_type = self.stat.gear_type
            self.assertIn(stat_id, STATS.keys(), "Non-overlapping-stat should have id from the STATS dict")
            self.assertIn(stat_type, 'substat', "Non-overlapping-stat should have stat_type = 'substat' if None")
            self.assertIsNone(gear_type, "Non-overlapping-stat should have gear_type None if None")


        # Ensure that all other id's are selected
        expected_stat_ids = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'} - selected_stat_ids  # Use set difference
        missing_stat_ids = expected_stat_ids - non_overlapping_stat_ids
        extra_stat_ids = non_overlapping_stat_ids - expected_stat_ids

        self.assertFalse(missing_stat_ids, f"The following stat IDs were not selected: {missing_stat_ids}")
        self.assertFalse(extra_stat_ids, f"The following extra stat IDs were selected: {extra_stat_ids}")
        
    def test_non_overlapping_stat_two_elements(self):
        """
        Test whether all stats other than the chosen two stats are selected at least once,
        instantiated inside a Stat object"""
        selected_stats = ['10', '3']
        selected_stat_ids = {'10', '3'} # id's we don't expect to see
        non_overlapping_stat_ids = set()

        # Generate 1000 non-overlapping stats 
        for _ in range(1000):
            stat = self.stat.get_non_overlapping_stat(selected_stats)
            non_overlapping_stat_ids.add(str(stat['id']))  # Convert id to string before adding to set
            # Verify that the generated stat is a valid entry in STATS
            self.assertTrue(stat in STATS.values(), f"Generated stat has an invalid ID: {stat['id']}")
            stat_id = self.stat.stat_id
            stat_type = self.stat.stat_type
            gear_type = self.stat.gear_type
            self.assertIn(stat_id, STATS.keys(), "Non-overlapping-stat should have id from the STATS dict")
            self.assertIn(stat_type, 'substat', "Non-overlapping-stat should have stat_type = 'substat' if None")
            self.assertIsNone(gear_type, "Non-overlapping-stat should have gear_type None if None")

        # Ensure that all other id's are selected
        expected_stat_ids = {'0', '1', '2', '4', '5', '6', '7', '8', '9'}  
        missing_stat_ids = expected_stat_ids - non_overlapping_stat_ids
        extra_stat_ids = non_overlapping_stat_ids - expected_stat_ids

        self.assertFalse(missing_stat_ids, f"The following stat IDs were not selected: {missing_stat_ids}")
        self.assertFalse(extra_stat_ids, f"The following extra stat IDs were selected: {extra_stat_ids}")

        
        
    def test_non_overlapping_stat_two_elements_mixed_entries(self):
        """
        Test whether all stats other than the chosen two stats are selected at least once,
        instantiated inside a Stat object, and when entries are mixed"""
        selected_stats = [4, '6']
        selected_stat_ids = {'4', '6'} # id's we don't expect to see
        non_overlapping_stat_ids = set()

        # Generate 1000 non-overlapping stats 
        for _ in range(1000):
            stat = self.stat.get_non_overlapping_stat(selected_stats)
            non_overlapping_stat_ids.add(str(stat['id']))  # Convert id to string before adding to set
            # Verify that the generated stat is a valid entry in STATS
            self.assertTrue(stat in STATS.values(), f"Generated stat has an invalid ID: {stat['id']}")
            stat_id = self.stat.stat_id
            stat_type = self.stat.stat_type
            gear_type = self.stat.gear_type
            self.assertIn(stat_id, STATS.keys(), "Non-overlapping-stat should have id from the STATS dict")
            self.assertIn(stat_type, 'substat', "Non-overlapping-stat should have stat_type = 'substat' if None")
            self.assertIsNone(gear_type, "Non-overlapping-stat should have gear_type None if None")

        # Ensure that all other id's are selected
        expected_stat_ids = {'0', '1', '2', '3', '5', '7', '8', '9', '10'}  
        missing_stat_ids = expected_stat_ids - non_overlapping_stat_ids
        extra_stat_ids = non_overlapping_stat_ids - expected_stat_ids

        self.assertFalse(missing_stat_ids, f"The following stat IDs were not selected: {missing_stat_ids}")
        self.assertFalse(extra_stat_ids, f"The following extra stat IDs were selected: {extra_stat_ids}")
        
        
    def test_non_overlapping_stat_three_elements(self):
        """
        Test whether all stats other than the chosen three stats are selected at least once,
        instantiated inside a Stat object, entries are mixed str and int
        """
        selected_stats = [1, '7', 10]
        selected_stat_ids = {'1', '7', '10'} # id's we don't expect to see
        non_overlapping_stat_ids = set()

        # Generate 1000 non-overlapping stats 
        for _ in range(1000):
            stat = self.stat.get_non_overlapping_stat(selected_stats)
            non_overlapping_stat_ids.add(str(stat['id']))  # Convert id to string before adding to set
            # Verify that the generated stat is a valid entry in STATS
            self.assertTrue(stat in STATS.values(), f"Generated stat has an invalid ID: {stat['id']}")
            stat_id = self.stat.stat_id
            stat_type = self.stat.stat_type
            gear_type = self.stat.gear_type
            self.assertIn(stat_id, STATS.keys(), "Non-overlapping-stat should have id from the STATS dict")
            self.assertIn(stat_type, 'substat', "Non-overlapping-stat should have stat_type = 'substat' if None")
            self.assertIsNone(gear_type, "Non-overlapping-stat should have gear_type None if None")


        # Ensure that all other id's are selected
        expected_stat_ids = {'0', '2', '3', '4', '5', '6', '8', '9'}  
        missing_stat_ids = expected_stat_ids - non_overlapping_stat_ids
        extra_stat_ids = non_overlapping_stat_ids - expected_stat_ids

        self.assertFalse(missing_stat_ids, f"The following stat IDs were not selected: {missing_stat_ids}")
        self.assertFalse(extra_stat_ids, f"The following extra stat IDs were selected: {extra_stat_ids}")

    def test_non_overlapping_stat_three_elements_gear_type(self):
        """
        Test whether all stats other than the selected stats (considering gear_type restrictions)
        are chosen at least once. We use weapon as a gear type, which may never have DEF and DEF%,
        instantiated inside a Stat object
        """
        selected_stats = [1, 7, '10']
        selected_stat_ids = {'1', '7', '10', '0', '4', '5'} # id's we don't expect to see because of doubles + gear restriction
        non_overlapping_stat_ids = set()

        # Generate 1000 non-overlapping stats 
        for _ in range(1000):
            stat = self.stat.get_non_overlapping_stat(selected_stats, gear_type='weapon')
            non_overlapping_stat_ids.add(str(stat['id']))  # Convert id to string before adding to set
            # Verify that the generated stat is a valid entry in STATS
            self.assertTrue(stat in STATS.values(), f"Generated stat has an invalid ID: {stat['id']}")
            stat_id = self.stat.stat_id
            stat_type = self.stat.stat_type
            gear_type = self.stat.gear_type
            self.assertIn(stat_id, STATS.keys(), "Non-overlapping-stat should have id from the STATS dict")
            self.assertIn(stat_type, 'substat', "Non-overlapping-stat should have stat_type = 'substat' if None")
            self.assertIn(gear_type, 'weapon', "Non-overlapping-stat should have gear type = 'weapon'")

        # Ensure that all other id's are selected
        expected_stat_ids = {'2', '3', '6', '8', '9'}  
        missing_stat_ids = expected_stat_ids - non_overlapping_stat_ids
        extra_stat_ids = non_overlapping_stat_ids - expected_stat_ids

        self.assertFalse(missing_stat_ids, f"The following stat IDs were not selected: {missing_stat_ids}")
        self.assertFalse(extra_stat_ids, f"The following extra stat IDs were selected: {extra_stat_ids}")

    def test_non_overlapping_stat_three_elements_gear_type_selected_stat_id(self):
        """
        Test whether all stats other than the selected stats (considering gear_type restrictions)
        are chosen at least once. We use weapon as a gear type, which may never have DEF and DEF%,
        instantiated inside a Stat object
        """
        selected_stats = ['1', 7, 10]

        # Generate 1000 non-overlapping stats 
        for _ in range(1000):
            stat = self.stat.get_non_overlapping_stat(selected_stats, gear_type='weapon')
            expected_id = (str(stat['id']))  # Convert id to string before adding to set
            expected_stat_type = 'substat'
            expected_gear_type = 'weapon'
            # Verify that the generated stat is a valid entry in STATS
            self.assertEqual(self.stat.stat_id, expected_id, f"Valid int stat ID should return stat_id of {expected_id}")
            self.assertEqual(self.stat.stat_type, expected_stat_type, f"Valid int stat ID should return stat_type of {expected_stat_type}")
            self.assertEqual(self.stat.gear_type, expected_gear_type, f"Valid int stat ID should return gear_type of {expected_gear_type}")
        
if __name__ == '__main__':
    unittest.main()
