from set_directory_function import set_directory
set_directory()

import unittest
from src.validation_utils import validate_substat_ids, validate_stat_id
from src.utilities import convert_int_to_str


class TestValidateSubstatID(unittest.TestCase):
    
    def test_valid_inputs(self):
        """
        Check valid inputs against expected results.
        Case 1: Valid stat_id
        Case 2: Valid stat_id
        Case 3: List of 4 valid stat_ids
        Case 4: List of 3 valid stat_ids
        Case 5: List of 2 valid stat_ids
        Case 6: List of 1 valid stat_id
        """
        valid_inputs = [1, 10, [1, 2, 3, 4], [4, 5, 6], [3, 4], [7]]
        expected_outputs = [['1'], ['10'], ['1', '2', '3', '4'], ['4', '5', '6'], ['3', '4'], ['7']]
        for i, input_val in enumerate(valid_inputs):
            with self.subTest(input_val=input_val):
                output = validate_substat_ids(input_val)
                expected_output = expected_outputs[i]
                self.assertEqual(output, expected_output, f"Output - {output} doesn't match input - {input_val}")
                
                
    def test_valid_inputs_with_mainstat(self):
        """
        Check valid inputs against expected results.
        Case 1: Valid stat_id
        Case 2: Valid stat_id
        Case 3: List of 4 valid stat_ids
        Case 4: List of 3 valid stat_ids
        Case 5: List of 2 valid stat_ids
        Case 6: List of 1 valid stat_id
        """
        valid_inputs = [1, 10, [1, 2, 3, 4], [4, 5, 6], [3, 4], [7]]
        valid_mainstats = [2, 9, 5, 7, 2, 5]
        expected_outputs = [['1'], ['10'], ['1', '2', '3', '4'], ['4', '5', '6'], ['3', '4'], ['7']]
        for i, input_val in enumerate(valid_inputs):
            with self.subTest(input_val=input_val):
                output = validate_substat_ids(input_val)
                expected_output = expected_outputs[i]
                self.assertEqual(output, expected_output, f"Output - {output} doesn't match input - {input_val}")
                
                
    def test_valid_inputs_with_mainstat_with_gear_type(self):
        """
        Check valid inputs against expected results.
        Case 1: Valid stat_id
        Case 2: Valid stat_id
        Case 3: List of 4 valid stat_ids
        Case 4: List of 3 valid stat_ids
        Case 5: List of 2 valid stat_ids
        Case 6: List of 1 valid stat_id
        """
        valid_inputs = [1, 10, [1, 2, 3, 4], [4, 5, 6], [3, 4], [7]]
        valid_mainstats = [2, 9, 5, 7, 2, 10]
        expected_outputs = [['1'], ['10'], ['1', '2', '3', '4'], ['4', '5', '6'], ['3', '4'], ['7']]
        valid_gear_types = ['helm', 'ring', 'boots', 'necklace', 'ring', 'boots']
        for i, input_val in enumerate(valid_inputs):
            with self.subTest(input_val=input_val):
                output = validate_substat_ids(input_val, gear_type = valid_gear_types[i])
                expected_output = expected_outputs[i]
                self.assertEqual(output, expected_output, f"Output - {output} doesn't match input - {input_val}")

                
    def test_invalid_inputs(self):
        """
        Check valid inputs against expected results.
        Case 1: neg int
        Case 2: large int, invalid stat_id
        #Case 4: str
        Case 5: List of 5 entries
        Case 6: List of 2 elements with 2 duplicates 
        Case 7: List of 4 elements with 2 duplicates
        Case 8: List of 4 elements with 2 duplicates 
        Case 9: List of 3 elements with 3 duplicates
        Case 10: List of 4 elements with 4 duplicates
        """
        invalid_inputs = [-1, 1000, [1, 2, 3, 4, 5], [1, 1], [1, 1, 3, 4], [2, 3, 4, 2], [3, 3, 3], [4, 4, 4, 4]]

        for i in invalid_inputs:
            with self.subTest(input_val=i):
                with self.assertRaises(ValueError, msg="{input_val} did not raise a ValueError"):
                    validate_substat_ids(i)
                
                
    def test_invalid_inputs_with_mainstat(self):
        """
        Check valid inputs against expected results.
        Case 1: neg int
        Case 2: large int, invalid stat_id
        Case 3: str
        Case 4: str
        Case 5: List of 5 entries
        Case 6: List of 2 elements with 2 duplicates 
        Case 7: List of 4 elements with 2 duplicates
        Case 8: List of 4 elements with 2 duplicates 
        Case 9: List of 3 elements with 3 duplicates
        Case 10: List of 4 elements with 4 duplicates
        """
        invalid_inputs = [1, 10, [1, 2, 3, 4], [4, 5, 6], [3, 4], [7]]
        invalid_mainstats = [1, 10, 3, 4, 3, 7]

        for i, val in enumerate(invalid_inputs):
            with self.subTest(input_val=val):
                with self.assertRaises(ValueError, msg="{input_val} did not raise a ValueError"):
                    validate_substat_ids(val, invalid_mainstats[i])     
                    
                    
    def test_invalid_inputs_with_gear_type(self):
        """
        Check valid substats but invalid mainstats with gear type.
        """
        valid_inputs = [[10, 2, 3, 9], [1, 5, 6, 3], [4], [1], [0]]
        invalid_mainstats = [2, 9, 0, 7, 9]
        # valid_mainstats = [4, 0, 2, 6, 8]
        invalid_gear_types = ['armor', 'weapon', 'helm', 'ring', 'necklace']

        for i, val in enumerate(valid_inputs):
            with self.subTest(input_val=val):
                with self.assertRaises(ValueError, msg="{input_val} did not raise a ValueError"):
                    validate_substat_ids(val, invalid_mainstats[i], gear_type = invalid_gear_types[i])     
                    

    def test_invalid_inputs_with_gear_type_2(self):
        """
        Check valid mainstats but invalid substats with gear type.
        """
        invalid_substats = [[10, 2, 3, 1], [0, 5, 6, 3], [4, 3, 2], [1, 6, 8, 9], [10, 3, 4, 8]]
        valid_mainstats = [4, 0, 2, 6, 8]
        invalid_gear_types = ['armor', 'weapon', 'helm', 'ring', 'necklace']

        for i, val in enumerate(invalid_substats):
            with self.subTest(input_val=val):
                with self.assertRaises(ValueError, msg="{input_val} did not raise a ValueError"):
                    validate_substat_ids(val, valid_mainstats[i], gear_type = invalid_gear_types[i])     
                    
if __name__ == '__main__':
    unittest.main()