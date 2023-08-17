from set_directory_function import set_directory
set_directory()

import unittest
import json
from src.validation_utils import is_valid_stat_entry

STATS = json.loads(open('data/stats.json', 'r').read())

class TestValidStatEntry(unittest.TestCase):

    def test_valid_stat_entry(self):
        """Test whether valid stat entries from stats.json are correctly identified"""
        for i in STATS:
            valid_entry = STATS[i]
            self.assertTrue(is_valid_stat_entry(valid_entry))
            
    def test_invalid_stat_entry(self):
        """
        Test whether invalid stat entries are correctly identified.
        List contains int, str, list, """
        invalid_entries = [1, 'stats', [1, 2, 'health'], None]
        for i in invalid_entries:
            self.assertFalse(is_valid_stat_entry(i))
            
    def test_invalid_stat_entry_dict(self):
        """
        Test whether invalid stat entries that are dict are correctly identified.
        """
        invalid_entries = [{}, {'stat' : 'health'}, {'id' : 1}, {'id' : 1, 'text' : 'Hello'}]
        for i in invalid_entries:
            self.assertFalse(is_valid_stat_entry(i))

if __name__ == '__main__':
    unittest.main()
