from set_directory_function import set_directory
set_directory()

import unittest
import json
from src.stats import Stat 

STATS = json.loads(open('data/stats.json', 'r').read())
TYPES = json.loads(open('data/types.json', 'r').read())

class TestStat(unittest.TestCase):

    def setUp(self):
        self.stat = Stat()
        
    def tearDown(self):
        self.stat = None

    def test_get_random_stat(self):
        """Test whether the randomly generated stats is in the STATS dictionary"""
        stat = self.stat.get_random_stat()
        stat_id = self.stat.stat_id
        stat_type = self.stat.stat_type
        gear_type = self.stat.gear_type
        self.assertIn(stat, STATS.values(), "Generated random stat should be in the STATS dictionary")
        self.assertIn(stat_id, STATS.keys(), "Generated random stat should have id from the STATS dict")
        self.assertIn(stat_type, 'mainstat', "Generated random stat should have stat_type = 'mainstat' if None")
        self.assertIsNone(gear_type, "Generated random stat should have gear_type None if None")

        
    def test_all_stats_selected(self):
        """Test whether all stats are selected at least once in 1000 random selections"""
        selected_stat_ids = set()  # Use a set to keep track of selected stat IDs

        for _ in range(1000):
            stat = self.stat.get_random_stat()
            selected_stat_ids.add(str(stat['id']))  # Add the ID of the selected stat
            stat = self.stat.get_random_stat()
            stat_id = self.stat.stat_id
            stat_type = self.stat.stat_type
            gear_type = self.stat.gear_type
            self.assertIn(stat, STATS.values(), "Generated random stat should be in the STATS dictionary")
            self.assertIn(stat_id, STATS.keys(), "Generated random stat should have id from the STATS dict")
            self.assertIn(stat_type, 'mainstat', "Generated random stat should have stat_type = 'mainstat' if None")
            self.assertIsNone(gear_type, "Generated random stat should have gear_type None if None")

        missing_stat_ids = set(STATS.keys()) - selected_stat_ids
        self.assertFalse(missing_stat_ids, f"The following stat IDs were not selected: {missing_stat_ids}")

        
    def test_all_stats_selected_2(self):
        """Test whether all stats are selected at least once in 1000 random selections by specifying stat_type = 'mainstat'"""
        selected_stat_ids = set()  # Use a set to keep track of selected stat IDs

        for _ in range(1000):
            stat = self.stat.get_random_stat(stat_type = 'mainstat')
            selected_stat_ids.add(str(stat['id']))  # Add the ID of the selected stat
            stat = self.stat.get_random_stat()
            stat_id = self.stat.stat_id
            stat_type = self.stat.stat_type
            gear_type = self.stat.gear_type
            self.assertIn(stat, STATS.values(), "Generated random stat should be in the STATS dictionary")
            self.assertIn(stat_id, STATS.keys(), "Generated random stat should have id from the STATS dict")
            self.assertIn(stat_type, 'mainstat', "Generated random stat should have stat_type = 'mainstat' if None")
            self.assertIsNone(gear_type, "Generated random stat should have gear_type None if None")

        missing_stat_ids = set(STATS.keys()) - selected_stat_ids
        self.assertFalse(missing_stat_ids, f"The following stat IDs were not selected: {missing_stat_ids}")

    def test_all_stats_selected_3(self):
        """Test whether all stats are selected at least once in 1000 random selections by specifying stat_type = 'substat'"""
        selected_stat_ids = set()  # Use a set to keep track of selected stat IDs

        for _ in range(1000):
            stat = self.stat.get_random_stat(stat_type = 'substat')
            selected_stat_ids.add(str(stat['id']))  # Add the ID of the selected stat

        missing_stat_ids = set(STATS.keys()) - selected_stat_ids
        self.assertFalse(missing_stat_ids, f"The following stat IDs were not selected: {missing_stat_ids}")

    def test_weapon_gear_type(self):
        """Test whether only stat id 0 is selected for 'weapon' gear type"""
        selected_stat_ids = set()

        # Generate 1000 random stats for 'weapon' gear type
        for _ in range(1000):
            stat = self.stat.get_random_stat(gear_type='weapon')
            selected_stat_ids.add(str(stat['id']))  # Convert id to string before adding to set

        # Ensure only stat id 0 is selected
        expected_stat_ids = {'0'}
        # expected_stat_ids = {'0', '1'} # This is a fail case to test that 1 is never chosen
        missing_stat_ids = expected_stat_ids - selected_stat_ids
        extra_stat_ids = selected_stat_ids - expected_stat_ids

        self.assertFalse(missing_stat_ids, f"The following stat IDs were not selected: {missing_stat_ids}")
        self.assertFalse(extra_stat_ids, f"The following extra stat IDs were selected: {extra_stat_ids}")
        
    def test_helm_gear_type(self):
        """Test whether only stat id 2 is selected for 'helm' gear type"""
        selected_stat_ids = set()

        # Generate 1000 random stats for 'weapon' gear type
        for _ in range(1000):
            stat = self.stat.get_random_stat(gear_type='helm')
            selected_stat_ids.add(str(stat['id']))  # Convert id to string before adding to set

        # Ensure only stat id 2 is selected
        expected_stat_ids = {'2'}
        # expected_stat_ids = {'2', '1'} # This is a fail case to test that 1 is never chosen
        missing_stat_ids = expected_stat_ids - selected_stat_ids
        extra_stat_ids = selected_stat_ids - expected_stat_ids

        self.assertFalse(missing_stat_ids, f"The following stat IDs were not selected: {missing_stat_ids}")
        self.assertFalse(extra_stat_ids, f"The following extra stat IDs were selected: {extra_stat_ids}")
        
    def test_armor_gear_type(self):
        """Test whether only stat id 2 is selected for 'armor' gear type"""
        selected_stat_ids = set()

        # Generate 1000 random stats for 'weapon' gear type
        for _ in range(1000):
            stat = self.stat.get_random_stat(gear_type='armor')
            selected_stat_ids.add(str(stat['id']))  # Convert id to string before adding to set

        # Ensure only stat id 4 is selected
        expected_stat_ids = {'4'}
        # expected_stat_ids = {'2', '1'} # This is a fail case to test that 1 is never chosen
        missing_stat_ids = expected_stat_ids - selected_stat_ids
        extra_stat_ids = selected_stat_ids - expected_stat_ids

        self.assertFalse(missing_stat_ids, f"The following stat IDs were not selected: {missing_stat_ids}")
        self.assertFalse(extra_stat_ids, f"The following extra stat IDs were selected: {extra_stat_ids}")
        
    def test_necklace_gear_type(self):
        """Test whether only stat id's 0,1,2,3,4,5,6,7 are selected for 'necklace' gear type"""
        selected_stat_ids = set()

        # Generate 1000 random stats for 'weapon' gear type
        for _ in range(1000):
            stat = self.stat.get_random_stat(gear_type='necklace')
            selected_stat_ids.add(str(stat['id']))  # Convert id to string before adding to set

        # Ensure correct id's are selected
        expected_stat_ids = {'0', '1', '2', '3', '4', '5', '6', '7'}
        missing_stat_ids = expected_stat_ids - selected_stat_ids
        extra_stat_ids = selected_stat_ids - expected_stat_ids

        self.assertFalse(missing_stat_ids, f"The following stat IDs were not selected: {missing_stat_ids}")
        self.assertFalse(extra_stat_ids, f"The following extra stat IDs were selected: {extra_stat_ids}")

    def test_ring_gear_type(self):
        """Test whether only stat id's 0,1,2,3,4,5,8,9 are selected for 'necklace' gear type"""
        selected_stat_ids = set()

        # Generate 1000 random stats for 'weapon' gear type
        for _ in range(1000):
            stat = self.stat.get_random_stat(gear_type='ring')
            selected_stat_ids.add(str(stat['id']))  # Convert id to string before adding to set

        # Ensure correct id's are selected
        expected_stat_ids = {'0', '1', '2', '3', '4', '5', '8', '9'}
        missing_stat_ids = expected_stat_ids - selected_stat_ids
        extra_stat_ids = selected_stat_ids - expected_stat_ids

        self.assertFalse(missing_stat_ids, f"The following stat IDs were not selected: {missing_stat_ids}")
        self.assertFalse(extra_stat_ids, f"The following extra stat IDs were selected: {extra_stat_ids}")

    def test_boots_gear_type(self):
        """Test whether only stat id's 0,1,2,3,4,5,8,9 are selected for 'necklace' gear type"""
        selected_stat_ids = set()

        # Ensure correct id's are selected
        for _ in range(1000):
            stat = self.stat.get_random_stat(gear_type='boots')
            selected_stat_ids.add(str(stat['id']))  # Convert id to string before adding to set

        # Ensure only stat id 2 is selected
        expected_stat_ids = {'0', '1', '2', '3', '4', '5', '10'}
        missing_stat_ids = expected_stat_ids - selected_stat_ids
        extra_stat_ids = selected_stat_ids - expected_stat_ids

        self.assertFalse(missing_stat_ids, f"The following stat IDs were not selected: {missing_stat_ids}")
        self.assertFalse(extra_stat_ids, f"The following extra stat IDs were selected: {extra_stat_ids}")


    def test_weapon_gear_type_mainstat(self):
        """Test whether only stat id 0 is selected for 'weapon' gear type and stat_type = 'mainstat'"""
        selected_stat_ids = set()

        # Generate 1000 random stats for 'weapon' gear type
        for _ in range(1000):
            stat = self.stat.get_random_stat(stat_type='mainstat',gear_type='weapon')
            selected_stat_ids.add(str(stat['id']))  # Convert id to string before adding to set

        # Ensure only stat id 0 is selected
        expected_stat_ids = {'0'}
        # expected_stat_ids = {'0', '1'} # This is a fail case to test that 1 is never chosen
        missing_stat_ids = expected_stat_ids - selected_stat_ids
        extra_stat_ids = selected_stat_ids - expected_stat_ids

        self.assertFalse(missing_stat_ids, f"The following stat IDs were not selected: {missing_stat_ids}")
        self.assertFalse(extra_stat_ids, f"The following extra stat IDs were selected: {extra_stat_ids}")
        
    def test_helm_gear_type_mainstat(self):
        """Test whether only stat id 2 is selected for 'helm' gear type and stat_type = 'mainstat'"""
        selected_stat_ids = set()

        # Generate 1000 random stats for 'weapon' gear type
        for _ in range(1000):
            stat = self.stat.get_random_stat(stat_type='mainstat',gear_type='helm')
            selected_stat_ids.add(str(stat['id']))  # Convert id to string before adding to set

        # Ensure only stat id 2 is selected
        expected_stat_ids = {'2'}
        # expected_stat_ids = {'2', '1'} # This is a fail case to test that 1 is never chosen
        missing_stat_ids = expected_stat_ids - selected_stat_ids
        extra_stat_ids = selected_stat_ids - expected_stat_ids

        self.assertFalse(missing_stat_ids, f"The following stat IDs were not selected: {missing_stat_ids}")
        self.assertFalse(extra_stat_ids, f"The following extra stat IDs were selected: {extra_stat_ids}")
        
    def test_armor_gear_type_mainstat(self):
        """Test whether only stat id 2 is selected for 'armor' gear type and stat_type = 'mainstat'"""
        selected_stat_ids = set()

        # Generate 1000 random stats for 'weapon' gear type
        for _ in range(1000):
            stat = self.stat.get_random_stat(stat_type='mainstat',gear_type='armor')
            selected_stat_ids.add(str(stat['id']))  # Convert id to string before adding to set

        # Ensure only stat id 4 is selected
        expected_stat_ids = {'4'}
        # expected_stat_ids = {'2', '1'} # This is a fail case to test that 1 is never chosen
        missing_stat_ids = expected_stat_ids - selected_stat_ids
        extra_stat_ids = selected_stat_ids - expected_stat_ids

        self.assertFalse(missing_stat_ids, f"The following stat IDs were not selected: {missing_stat_ids}")
        self.assertFalse(extra_stat_ids, f"The following extra stat IDs were selected: {extra_stat_ids}")
        
    def test_necklace_gear_type_mainstat(self):
        """Test whether only stat id's 0,1,2,3,4,5,6,7 are selected for 'necklace' gear type and stat_type = 'mainstat'"""
        selected_stat_ids = set()

        # Generate 1000 random stats for 'weapon' gear type
        for _ in range(1000):
            stat = self.stat.get_random_stat(stat_type='mainstat',gear_type='necklace')
            selected_stat_ids.add(str(stat['id']))  # Convert id to string before adding to set

        # Ensure correct id's are selected
        expected_stat_ids = {'0', '1', '2', '3', '4', '5', '6', '7'}
        missing_stat_ids = expected_stat_ids - selected_stat_ids
        extra_stat_ids = selected_stat_ids - expected_stat_ids

        self.assertFalse(missing_stat_ids, f"The following stat IDs were not selected: {missing_stat_ids}")
        self.assertFalse(extra_stat_ids, f"The following extra stat IDs were selected: {extra_stat_ids}")

    def test_ring_gear_type_mainstat(self):
        """Test whether only stat id's 0,1,2,3,4,5,8,9 are selected for 'ring' gear type and stat_type = 'mainstat'"""
        selected_stat_ids = set()

        # Generate 1000 random stats for 'weapon' gear type
        for _ in range(1000):
            stat = self.stat.get_random_stat(stat_type='mainstat',gear_type='ring')
            selected_stat_ids.add(str(stat['id']))  # Convert id to string before adding to set

        # Ensure correct id's are selected
        expected_stat_ids = {'0', '1', '2', '3', '4', '5', '8', '9'}
        missing_stat_ids = expected_stat_ids - selected_stat_ids
        extra_stat_ids = selected_stat_ids - expected_stat_ids

        self.assertFalse(missing_stat_ids, f"The following stat IDs were not selected: {missing_stat_ids}")
        self.assertFalse(extra_stat_ids, f"The following extra stat IDs were selected: {extra_stat_ids}")

    def test_boots_gear_type_mainstat(self):
        """Test whether only stat id's 0,1,2,3,4,5,8,9 are selected for 'boots' gear type and stat_type = 'mainstat'"""
        selected_stat_ids = set()

        # Ensure correct id's are selected
        for _ in range(1000):
            stat = self.stat.get_random_stat(stat_type='mainstat',gear_type='boots')
            selected_stat_ids.add(str(stat['id']))  # Convert id to string before adding to set

        # Ensure only stat id 2 is selected
        expected_stat_ids = {'0', '1', '2', '3', '4', '5', '10'}
        missing_stat_ids = expected_stat_ids - selected_stat_ids
        extra_stat_ids = selected_stat_ids - expected_stat_ids

        self.assertFalse(missing_stat_ids, f"The following stat IDs were not selected: {missing_stat_ids}")
        self.assertFalse(extra_stat_ids, f"The following extra stat IDs were selected: {extra_stat_ids}")

        
    def test_weapon_gear_type_substat(self):
        """Test whether only stat id 0 is selected for 'weapon' gear type and stat_type = 'substat'"""
        selected_stat_ids = set()

        # Generate 1000 random stats for 'weapon' gear type
        for _ in range(1000):
            stat = self.stat.get_random_stat(stat_type='substat',gear_type='weapon')
            selected_stat_ids.add(str(stat['id']))  # Convert id to string before adding to set

        # Ensure that correct substats are selected
        expected_stat_ids = {'1', '2', '3', '6', '7', '8', '9', '10'}
        missing_stat_ids = expected_stat_ids - selected_stat_ids
        extra_stat_ids = selected_stat_ids - expected_stat_ids

        self.assertFalse(missing_stat_ids, f"The following stat IDs were not selected: {missing_stat_ids}")
        self.assertFalse(extra_stat_ids, f"The following extra stat IDs were selected: {extra_stat_ids}")
        
    def test_helm_gear_type_substat(self):
        """Test whether only stat id 2 is selected for 'helm' gear type and stat_type = 'substat'"""
        selected_stat_ids = set()

        # Generate 1000 random stats for 'weapon' gear type
        for _ in range(1000):
            stat = self.stat.get_random_stat(stat_type='substat',gear_type='helm')
            selected_stat_ids.add(str(stat['id']))  # Convert id to string before adding to set

        # Ensure that correct substats are selected
        expected_stat_ids = {'0', '1', '3', '4', '5', '6', '7', '8', '9', '10'}
        missing_stat_ids = expected_stat_ids - selected_stat_ids
        extra_stat_ids = selected_stat_ids - expected_stat_ids

        self.assertFalse(missing_stat_ids, f"The following stat IDs were not selected: {missing_stat_ids}")
        self.assertFalse(extra_stat_ids, f"The following extra stat IDs were selected: {extra_stat_ids}")
        
    def test_armor_gear_type_substat(self):
        """Test whether only stat id 2 is selected for 'armor' gear type and stat_type = 'substat'"""
        selected_stat_ids = set()

        # Generate 1000 random stats for 'weapon' gear type
        for _ in range(1000):
            stat = self.stat.get_random_stat(stat_type='substat',gear_type='armor')
            selected_stat_ids.add(str(stat['id']))  # Convert id to string before adding to set

        # Ensure that correct substats are selected
        expected_stat_ids = {'2','3', '5', '6', '7', '8', '9', '10'}
        missing_stat_ids = expected_stat_ids - selected_stat_ids
        extra_stat_ids = selected_stat_ids - expected_stat_ids

        self.assertFalse(missing_stat_ids, f"The following stat IDs were not selected: {missing_stat_ids}")
        self.assertFalse(extra_stat_ids, f"The following extra stat IDs were selected: {extra_stat_ids}")
        
    def test_necklace_gear_type_substat(self):
        """Test whether only stat id's 0,1,2,3,4,5,6,7 are selected for 'necklace' gear type and stat_type = 'substat'"""
        selected_stat_ids = set()

        # Generate 1000 random stats for 'weapon' gear type
        for _ in range(1000):
            stat = self.stat.get_random_stat(stat_type='substat',gear_type='necklace')
            selected_stat_ids.add(str(stat['id']))  # Convert id to string before adding to set

        # Ensure that correct substats are selected
        expected_stat_ids = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'}
        missing_stat_ids = expected_stat_ids - selected_stat_ids
        extra_stat_ids = selected_stat_ids - expected_stat_ids

        self.assertFalse(missing_stat_ids, f"The following stat IDs were not selected: {missing_stat_ids}")
        self.assertFalse(extra_stat_ids, f"The following extra stat IDs were selected: {extra_stat_ids}")

    def test_ring_gear_type_substat(self):
        """Test whether only stat id's 0,1,2,3,4,5,8,9 are selected for 'ring' gear type and stat_type = 'substat'"""
        selected_stat_ids = set()

        # Generate 1000 random stats for 'weapon' gear type
        for _ in range(1000):
            stat = self.stat.get_random_stat(stat_type='substat',gear_type='ring')
            selected_stat_ids.add(str(stat['id']))  # Convert id to string before adding to set

        # Ensure that correct substats are selected
        expected_stat_ids = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'}
        missing_stat_ids = expected_stat_ids - selected_stat_ids
        extra_stat_ids = selected_stat_ids - expected_stat_ids

        self.assertFalse(missing_stat_ids, f"The following stat IDs were not selected: {missing_stat_ids}")
        self.assertFalse(extra_stat_ids, f"The following extra stat IDs were selected: {extra_stat_ids}")

    def test_boots_gear_type_substat(self):
        """Test whether only stat id's 0,1,2,3,4,5,8,9 are selected for 'boots' gear type and stat_type = 'substat'"""
        selected_stat_ids = set()

        # Ensure correct id's are selected
        for _ in range(1000):
            stat = self.stat.get_random_stat(stat_type='substat',gear_type='boots')
            selected_stat_ids.add(str(stat['id']))  # Convert id to string before adding to set

        # Ensure that correct substats are selected
        expected_stat_ids = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'}
        missing_stat_ids = expected_stat_ids - selected_stat_ids
        extra_stat_ids = selected_stat_ids - expected_stat_ids

        self.assertFalse(missing_stat_ids, f"The following stat IDs were not selected: {missing_stat_ids}")
        self.assertFalse(extra_stat_ids, f"The following extra stat IDs were selected: {extra_stat_ids}")

        
    def test_invalid_stat_type_mixed(self):
        """Test whether an invalid stat_type (int, str, random str) raises ValueError"""
        invalid_stat_types = [111, '111', 'health']
        for stat_type in invalid_stat_types:
            with self.assertRaises(ValueError):
                self.stat.get_random_stat(stat_type=stat_type)
                
    def test_invalid_gear_type_mixed(self):
        """Test whether an invalid gear_type (int, str, random str) raises ValueError"""
        invalid_gear_types = [111, '1', 'Sword']
        for gear_type in invalid_gear_types:
            with self.assertRaises(ValueError):
                self.stat.get_random_stat(gear_type=gear_type)

    def test_invalid_inputs_both(self):
        """Test whether invalid gear_type and stat_type combination raises ValueError"""
        with self.assertRaises(ValueError):
            self.stat.get_random_stat(stat_type='Sword', gear_type=111)

    def test_ring_gear_type_mainstat_selected_stat_id(self):
        """
        Test whether a randomly selected stat for 'ring' gear type and stat_type = 'mainstat'
        holds the correct id value in self.selected_stat
        """
        for _ in range(1000):
            stat = self.stat.get_random_stat(stat_type='mainstat',gear_type='ring')
            expected_id = str(stat['id'])
            expected_key = str(stat['key_stat'])
            self.assertEqual(self.stat.stat_id, expected_id, f"Valid int stat ID should return selected_stat_id {expected_id}")
            self.assertEqual(self.stat.stat_key, expected_key, f"Valid int stat ID should return stat_key {expected_key}")
            self.assertEqual(self.stat.stat_type, 'mainstat', f"Valid int stat ID should return stat type 'mainstat'")
            self.assertEqual(self.stat.gear_type, 'ring', f"Valid int stat ID should return gear type 'ring'")

    def test_helm_gear_type_substat_selected_stat_id(self):
        """
        Test whether a randomly selected stat for 'helm' gear type and stat_type = 'substat'
        holds the correct id value in self.selected_stat
        """
        for _ in range(1000):
            stat = self.stat.get_random_stat(stat_type='substat',gear_type='helm')
            expected_id = str(stat['id'])
            expected_key = str(stat['key_stat'])
            self.assertEqual(self.stat.stat_id, expected_id, f"Valid int stat ID should return selected_stat_id of {expected_id}")
            self.assertEqual(self.stat.stat_key, expected_key, f"Valid int stat ID should return stat_key {expected_key}")
            self.assertEqual(self.stat.stat_type, 'substat', f"Valid int stat ID should return stat type 'substat'")
            self.assertEqual(self.stat.gear_type, 'helm', f"Valid int stat ID should return gear type 'helm'")

if __name__ == '__main__':
    unittest.main()
