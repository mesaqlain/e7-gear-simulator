from set_directory_function import set_directory
set_directory()

import unittest
import json
from src.stats import Stat 

STATS = json.loads(open('data/stats.json', 'r').read())

class TestStat(unittest.TestCase):

    def setUp(self):
        self.stat = Stat()
        
    def tearDown(self):
        self.stat = None

    def test_valid_int_stat_id_0(self):
        """Test whether a valid int returns the correct dictionary"""
        stat = self.stat.get_stat_by_id(0)
        expected_stat = STATS['0']
        self.assertEqual(stat, expected_stat, "Valid int stat ID should return the correct dictionary")
        
    def test_valid_str_stat_id_0(self):
        """Test whether a valid str returns the correct dictionary"""
        stat = self.stat.get_stat_by_id('0')
        expected_stat = STATS['0']
        self.assertEqual(stat, expected_stat, "Valid int stat ID should return the correct dictionary")

    def test_valid_int_stat_id_7(self):
        """Test whether a valid int returns the correct dictionary"""
        stat = self.stat.get_stat_by_id(7)
        expected_stat = STATS['7']
        self.assertEqual(stat, expected_stat, "Valid int stat ID should return the correct dictionary")
        
    def test_valid_str_stat_id_7(self):
        """Test whether a valid str returns the correct dictionary"""
        stat = self.stat.get_stat_by_id('7')
        expected_stat = STATS['7']
        self.assertEqual(stat, expected_stat, "Valid int stat ID should return the correct dictionary")

    def test_invalid_int_stat_id(self):
        """Test whether an invalid int raises ValueError"""
        with self.assertRaises(ValueError): 
            self.stat.get_stat_by_id(100)

    def test_invalid_str_stat_id(self):
        """Test whether an invalid str raises ValueError"""
        with self.assertRaises(ValueError): 
            self.stat.get_stat_by_id('100')
        
    def test_invalid_neg_stat_id(self):
        """Test whether an invalid negative int raises ValueError"""
        with self.assertRaises(ValueError): 
            self.stat.get_stat_by_id(-1)
        
    def test_invalid_large_stat_id(self):
        """Test whether an invalid large int raises ValueError"""
        with self.assertRaises(ValueError): 
            self.stat.get_stat_by_id(1000000)
            
    def test_invalid_str_random_stat_id(self):
        """Test whether an invalid random str raises ValueError"""
        with self.assertRaises(ValueError): 
            self.stat.get_stat_by_id('Health')
        
    def test_invalid_none_stat_id(self):
        """Test whether None raises ValueError"""
        with self.assertRaises(ValueError): 
            self.stat.get_stat_by_id(None)
    
    def test_valid_int_stat_id_stored_val(self):
        """Test whether the Stat object holds the correct selected_stat_id with a valid int input"""
        stat = self.stat.get_stat_by_id(0)
        expected_id = '0'
        expected_key = 'attack_flat'
        expected_stat_type = 'mainstat'
        expected_gear_type = None
        self.assertEqual(self.stat.stat_id, expected_id, "Valid int stat ID should return expected_id of '0'")
        self.assertEqual(self.stat.stat_key, expected_key, "Valid int stat ID should return expected_key of 'attack_flat'")
        self.assertEqual(self.stat.stat_type, expected_stat_type, "If no stat_type provided, it should be 'mainstat'")
        self.assertIsNone(self.stat.gear_type, "If no gear_type provided, it should be None")
        
        
    def test_valid_str_stat_id_stored_val(self):
        """Test whether the Stat object holds the correct selected_stat_id with a valid str input"""
        stat = self.stat.get_stat_by_id('7')
        expected_id = '7'
        expected_key = 'crit_damage'
        expected_stat_type = 'mainstat'
        expected_gear_type = None
        self.assertEqual(self.stat.stat_id, expected_id, "Valid int stat ID should return selected_stat_id of '0'")
        self.assertEqual(self.stat.stat_key, expected_key, "Valid int stat ID should return expected_key of 'crit_damage'")
        self.assertEqual(self.stat.stat_type, expected_stat_type, "If no stat_type provided, it should be 'mainstat'")
        self.assertIsNone(self.stat.gear_type, "If no gear_type provided, it should be None")

        
    def test_valid_str_stat_id_stored_val_extra_attribtues(self):
        """Test whether the Stat object holds the correct class attributes with a valid str input"""
        stat = self.stat.get_stat_by_id(10, stat_type='substat', gear_type='boots')
        expected_id = '10'
        expected_key = 'speed_flat'
        expected_stat_type = 'substat'
        expected_gear_type = 'boots'
        self.assertEqual(self.stat.stat_id, expected_id, "Valid int stat ID should return selected_stat_id of '0'")
        self.assertEqual(self.stat.stat_key, expected_key, "Valid int stat ID should return expected_key of 'crit_damage'")
        self.assertEqual(self.stat.stat_type, expected_stat_type, "If no stat_type provided, it should be 'mainstat'")
        self.assertEqual(self.stat.gear_type, expected_gear_type, "If no gear_type provided, it should be None")
        
        
    def test_valid_str_stat_id_stored_val_extra_attribtues_2(self):
        """Test whether the Stat object holds the correct class attributes with a valid str input"""
        stat = self.stat.get_stat_by_id(9, stat_type='mainstat', gear_type='ring')
        expected_id = '9'
        expected_key = 'eff_res'
        expected_stat_type = 'mainstat'
        expected_gear_type = 'ring'
        self.assertEqual(self.stat.stat_id, expected_id, "Valid int stat ID should return selected_stat_id of '0'")
        self.assertEqual(self.stat.stat_key, expected_key, "Valid int stat ID should return expected_key of 'crit_damage'")
        self.assertEqual(self.stat.stat_type, expected_stat_type, "If no stat_type provided, it should be 'mainstat'")
        self.assertEqual(self.stat.gear_type, expected_gear_type, "If no gear_type provided, it should be None")
        
        
    def test_invalid_str_stat_id_stored_val_extra_attribtues_3(self):
        """Test whether we get an error when we try to get incorrect combination of stats with gear_type"""
        gear_types = ['weapon', 'armor', 'helm', 'necklace', 'ring', 'boots']
        stat_types = ['mainstat', 'substat', 'substat', 'mainstat', 'mainstat', 'mainstat']
        stat_ids = [3, 0, 2, 8, 10, 6]
        for i in range(len(gear_types)):
            gear_type = gear_types[i]
            stat_type = stat_types[i]
            stat_id = stat_ids[i]
            with self.assertRaises(ValueError, msg=f"Gear type {gear_type} cannot have stat {stat_id} as {stat_type}."):
                self.stat.get_stat_by_id(stat_id, stat_type, gear_type)
        
if __name__ == '__main__':
    unittest.main()
