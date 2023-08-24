from set_directory_function import set_directory
set_directory()

import unittest
import json
from src.validation_utils import validate_selected_stats
from src.utilities import convert_int_to_str

STATS = json.loads(open('data/stats.json', 'r').read())

class TestValidateSelectedStats(unittest.TestCase):
    
    def test_valid_selected_stats(self):
        """
        Test whether valid selected stats are correctly identified.
        Case 1: list containing one valid stat written as int
        Case 2: list containing one valid stat written as str
        Case 3: list containing multiple valid stats written as int
        Case 4: list containing multiple valid stats written as str
        Case 5: list containing multiple valid stats written as both int and str
        """
        valid_selected_stats_list = [
            [0], 
            ['1'],
            [2, 3, 7],
            ['4', '10'],
            [5, '7', 9]
        ]
        for i in valid_selected_stats_list:
            valid_selected_stats = i
            self.assertEqual(validate_selected_stats(valid_selected_stats), convert_int_to_str(valid_selected_stats))

    def test_invalid_selected_stats_none(self):
        """
        Test whether 'None' invalid selected stats return an empty list.
        """
        self.assertEqual(validate_selected_stats(None), [])
            
    def test_invalid_selected_stats_empty_list(self):
        """
        Test whether an empty list of selected stats return an empty list.
        """
        self.assertEqual(validate_selected_stats([]), [])

        
    def test_invalid_selected_stats(self):
        """
        Test whether valid selected stats are correctly identified.
        Case 1: some integer
        Case 2: some str
        Case 3: empty dictionary
        Case 4: some dictionary that do not contain valid stat entries
        """
        invalid_selected_stats_list = [
            1, 
            'health',
            {},
            {'stat' : 'health', 'id' : 1}
        ]
        for i in invalid_selected_stats_list:
            with self.assertRaises(ValueError):
                validate_selected_stats(i)

if __name__ == '__main__':
    unittest.main()
