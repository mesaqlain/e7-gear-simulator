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
        """Test whether an invalid int returns None"""
        stat_invalid = self.stat.get_stat_by_id(100)
        self.assertIsNone(stat_invalid, "Invalid stat ID should return None")

    def test_invalid_str_stat_id(self):
        """Test whether an invalid str returns None"""
        stat_invalid = self.stat.get_stat_by_id('100')
        self.assertIsNone(stat_invalid, "Invalid stat ID should return None")
        
    def test_invalid_neg_stat_id(self):
        """Test whether an invalid negative int returns None"""
        stat_invalid = self.stat.get_stat_by_id(-1)
        self.assertIsNone(stat_invalid, "Invalid neg stat ID should return None")
        
    def test_invalid_large_stat_id(self):
        """Test whether an invalid large int returns None"""
        stat_invalid = self.stat.get_stat_by_id(1000000)
        self.assertIsNone(stat_invalid, "Invalid large int stat ID should return None")

if __name__ == '__main__':
    unittest.main()
