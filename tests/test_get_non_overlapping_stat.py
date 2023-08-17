from set_directory_function import set_directory
set_directory()

import unittest
import json
import random
from tests.test_functions import * 
from src.validation_utils import *

STATS = json.loads(open('data/stats.json', 'r').read())

class TestNonOverlappingStat(unittest.TestCase):
    
    def test_non_overlapping_stat_empty(self):
        """Test whether each stat is selected at least once when input is empty"""
        selected_stats = []
        selected_stat_ids = set()

        # Generate 1000 random stats for 'weapon' gear type
        for _ in range(1000):
            stat = get_non_overlapping_stat(selected_stats)
            selected_stat_ids.add(str(stat['id']))  # Convert id to string before adding to set
            # Verify that the generated stat is a valid entry in STATS
            self.assertTrue(stat in STATS.values(), f"Generated stat has an invalid ID: {stat['id']}")

        # Ensure that all id's are selected
        expected_stat_ids = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'}
        missing_stat_ids = expected_stat_ids - selected_stat_ids
        extra_stat_ids = selected_stat_ids - expected_stat_ids

        self.assertFalse(missing_stat_ids, f"The following stat IDs were not selected: {missing_stat_ids}")
        self.assertFalse(extra_stat_ids, f"The following extra stat IDs were selected: {extra_stat_ids}")

    def test_non_overlapping_stat_none(self):
        """Test whether each stat is selected at least once when input is empty"""
        selected_stats = None
        selected_stat_ids = set()

        # Generate 1000 random stats for 'weapon' gear type
        for _ in range(1000):
            stat = get_non_overlapping_stat(selected_stats)
            selected_stat_ids.add(str(stat['id']))  # Convert id to string before adding to set
            # Verify that the generated stat is a valid entry in STATS
            self.assertTrue(stat in STATS.values(), f"Generated stat has an invalid ID: {stat['id']}")

        # Ensure that all id's are selected
        expected_stat_ids = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'}
        missing_stat_ids = expected_stat_ids - selected_stat_ids
        extra_stat_ids = selected_stat_ids - expected_stat_ids

        self.assertFalse(missing_stat_ids, f"The following stat IDs were not selected: {missing_stat_ids}")
        self.assertFalse(extra_stat_ids, f"The following extra stat IDs were selected: {extra_stat_ids}")
        
        
    def test_non_overlapping_stat_single(self):
        """Test whether all stats other than the chosen stat is selected at least once"""
        selected_stats = [get_random_stat()]
        selected_stat_id = str(selected_stats[0]['id'])
        non_overlapping_stat_ids = set()

        # Generate 1000 random stats for 'weapon' gear type
        for _ in range(1000):
            stat = get_non_overlapping_stat(selected_stats)
            non_overlapping_stat_ids.add(str(stat['id']))  # Convert id to string before adding to set
            # Verify that the generated stat is a valid entry in STATS
            self.assertTrue(stat in STATS.values(), f"Generated stat has an invalid ID: {stat['id']}")

        # Ensure that all other id's are selected
        expected_stat_ids = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'} - {selected_stat_id}  # Use set difference
        missing_stat_ids = expected_stat_ids - non_overlapping_stat_ids
        extra_stat_ids = non_overlapping_stat_ids - expected_stat_ids

        self.assertFalse(missing_stat_ids, f"The following stat IDs were not selected: {missing_stat_ids}")
        self.assertFalse(extra_stat_ids, f"The following extra stat IDs were selected: {extra_stat_ids}")
        
    def test_non_overlapping_stat_two_elements(self):
        """Test whether all stats other than the chosen two stats are selected at least once"""
        selected_stats = [STATS['10'], STATS['3']]
        selected_stat_ids = {'5', '3'} # id's we don't expect to see
        non_overlapping_stat_ids = set()

        # Generate 1000 non-overlapping stats 
        for _ in range(1000):
            stat = get_non_overlapping_stat(selected_stats)
            non_overlapping_stat_ids.add(str(stat['id']))  # Convert id to string before adding to set
            # Verify that the generated stat is a valid entry in STATS
            self.assertTrue(stat in STATS.values(), f"Generated stat has an invalid ID: {stat['id']}")

        # Ensure that all other id's are selected
        expected_stat_ids = {'0', '1', '2', '4', '5', '6', '7', '8', '9'}  
        missing_stat_ids = expected_stat_ids - non_overlapping_stat_ids
        extra_stat_ids = non_overlapping_stat_ids - expected_stat_ids

        self.assertFalse(missing_stat_ids, f"The following stat IDs were not selected: {missing_stat_ids}")
        self.assertFalse(extra_stat_ids, f"The following extra stat IDs were selected: {extra_stat_ids}")

        
    def test_non_overlapping_stat_three_elements(self):
        """Test whether all stats other than the chosen three stats are selected at least once"""
        selected_stats = [STATS['1'], STATS['7'], STATS['10']]
        selected_stat_ids = {'1', '7', '10'} # id's we don't expect to see
        non_overlapping_stat_ids = set()

        # Generate 1000 non-overlapping stats 
        for _ in range(1000):
            stat = get_non_overlapping_stat(selected_stats)
            non_overlapping_stat_ids.add(str(stat['id']))  # Convert id to string before adding to set
            # Verify that the generated stat is a valid entry in STATS
            self.assertTrue(stat in STATS.values(), f"Generated stat has an invalid ID: {stat['id']}")

        # Ensure that all other id's are selected
        expected_stat_ids = {'0', '2', '3', '4', '5', '6', '8', '9'}  
        missing_stat_ids = expected_stat_ids - non_overlapping_stat_ids
        extra_stat_ids = non_overlapping_stat_ids - expected_stat_ids

        self.assertFalse(missing_stat_ids, f"The following stat IDs were not selected: {missing_stat_ids}")
        self.assertFalse(extra_stat_ids, f"The following extra stat IDs were selected: {extra_stat_ids}")

    def test_non_overlapping_stat_three_elements_gear_type(self):
        """
        Test whether all stats other than the selected stats (considering gear_type restrictions)
        are chosen at least once. We use weapon as a gear type, which may never have DEF and DEF%
        """
        selected_stats = [STATS['1'], STATS['7'], STATS['10']]
        selected_stat_ids = {'1', '7', '10', '0', '4', '5'} # id's we don't expect to see because of doubles + gear restriction
        non_overlapping_stat_ids = set()

        # Generate 1000 non-overlapping stats 
        for _ in range(1000):
            stat = get_non_overlapping_stat(selected_stats, gear_type='weapon')
            non_overlapping_stat_ids.add(str(stat['id']))  # Convert id to string before adding to set
            # Verify that the generated stat is a valid entry in STATS
            self.assertTrue(stat in STATS.values(), f"Generated stat has an invalid ID: {stat['id']}")

        # Ensure that all other id's are selected
        expected_stat_ids = {'2', '3', '6', '8', '9'}  
        missing_stat_ids = expected_stat_ids - non_overlapping_stat_ids
        extra_stat_ids = non_overlapping_stat_ids - expected_stat_ids

        self.assertFalse(missing_stat_ids, f"The following stat IDs were not selected: {missing_stat_ids}")
        self.assertFalse(extra_stat_ids, f"The following extra stat IDs were selected: {extra_stat_ids}")
        
if __name__ == '__main__':
    unittest.main()
