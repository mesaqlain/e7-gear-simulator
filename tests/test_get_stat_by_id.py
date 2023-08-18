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
        self.assertEqual(self.stat.selected_stat_id, expected_id, "Valid int stat ID should return selected_stat_id of '0'")

    def test_valid_str_stat_id_stored_val(self):
        """Test whether the Stat object holds the correct selected_stat_id with a valid str input"""
        stat = self.stat.get_stat_by_id('7')
        expected_id = '7'
        self.assertEqual(self.stat.selected_stat_id, expected_id, "Valid int stat ID should return selected_stat_id of '0'")

        
if __name__ == '__main__':
    unittest.main()
