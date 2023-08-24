from set_directory_function import set_directory
set_directory()

import unittest
from src.validation_utils import validate_mainstat_id, validate_stat_id
from src.utilities import convert_int_to_str


class TestValidateMainstatID(unittest.TestCase):
    
    def test_valid_inputs_1(self):
        """
        Check valid inputs of ints against expected results. substat_id=None
        """
        valid_inputs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected_outputs = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        
        for i, input_val in enumerate(valid_inputs):
            with self.subTest(input_val=input_val):
                output = validate_mainstat_id(input_val)
                expected_output = expected_outputs[i]
                self.assertEqual(output, expected_output, f"Output - {output} doesn't match input - {input_val}")
                
                
    def test_valid_inputs_1_gear(self):
        """
        Check valid inputs of ints against expected results. substat_id=None
        """
        valid_inputs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        valid_gear = ['weapon', 'ring', 'helm', 'necklace', 'armor', 'boots', 'necklace', 'necklace', 'ring', 'ring', 'boots']
        expected_outputs = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        
        for i, input_val in enumerate(valid_inputs):
            with self.subTest(input_val=input_val):
                output = validate_mainstat_id(input_val, gear_type =valid_gear[i])
                expected_output = expected_outputs[i]
                self.assertEqual(output, expected_output, f"Output - {output} doesn't match input - {input_val}")
                
                
    def test_valid_inputs_2(self):
        """
        Check valid inputs of str against expected results. substat_id=None
        """
        valid_inputs = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        expected_outputs = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        
        for i, input_val in enumerate(valid_inputs):
            with self.subTest(input_val=input_val):
                output = validate_mainstat_id(input_val)
                expected_output = expected_outputs[i]
                self.assertEqual(output, expected_output, f"Output - {output} doesn't match input - {input_val}")
                
                
    def test_valid_inputs_with_substat_gear_type(self):
        """
        Check valid inputs against expected results.
        """
        valid_inputs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        valid_substats = [1, [0, 2], [0, 10, 3], [0, 1, 6, 7], [3, 7, 8, 9], 0, 10, [3, 4], [7, 5, 3], [5, 8, 3, 4], 9]
        valid_gear = ['weapon', 'ring', 'helm', 'necklace', 'armor', 'boots', 'necklace', 'necklace', 'ring', 'ring', 'boots']
        expected_outputs = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        for i, input_val in enumerate(valid_inputs):
            with self.subTest(input_val=input_val):
                output = validate_mainstat_id(input_val, substat_ids=valid_substats[i], gear_type=valid_gear[i])
                expected_output = expected_outputs[i]
                self.assertEqual(output, expected_output, f"Output - {output} doesn't match input - {input_val}")

                
    def test_valid_inputs_with_substat_with(self):
        """
        Check valid inputs against expected results.
        """
        valid_inputs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        valid_substats = [1, [0, 2], [0, 10, 3], [0, 1, 6, 7], [0, 7, 8, 9], 0, 10, [3, 4], [7, 5, 3], [5, 8, 3, 4], 9]
        expected_outputs = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        for i, input_val in enumerate(valid_inputs):
            with self.subTest(input_val=input_val):
                output = validate_mainstat_id(input_val, substat_ids=valid_substats[i])
                expected_output = expected_outputs[i]
                self.assertEqual(output, expected_output, f"Output - {output} doesn't match input - {input_val}")

                
    def test_invalid_inputs(self):
        """
        Check valid inputs against expected results.
        Case 1: neg int
        Case 2: large int, invalid stat_id
        Case 4: str
        Case 5: List of 5 entries
        Case 6: List of 2 elements with 2 duplicates 
        Case 7: List of 4 elements with 2 duplicates
        Case 8: List of 4 elements with 2 duplicates 
        Case 9: List of 3 elements with 3 duplicates
        Case 10: List of 4 elements with 4 duplicates
        """
        invalid_inputs = [-1, 1000, 'some str', 
                          [1, 2, 3, 4, 5], [1, 1], [1, 1, 3, 4], [2, 3, 4, 2], [3, 3, 3], [4, 4, 4, 4]]

        for i in invalid_inputs:
            with self.subTest(input_val=i):
                with self.assertRaises(ValueError, msg="{input_val} did not raise a ValueError"):
                    validate_mainstat_id(i)
                
                
    def test_invalid_inputs_with_substat(self):
        """
        Checks whether we get an error if mainstat clashes with substats.
        """
        invalid_inputs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        invalid_substats = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        for i, val in enumerate(invalid_inputs):
            with self.subTest(input_val=val):
                with self.assertRaises(ValueError, msg="{input_val} did not raise a ValueError"):
                    validate_mainstat_id(val, invalid_substats[i])  
                    
                    
    def test_invalid_inputs_with_substat_2(self):
        """
        Checks whether we get an error if mainstat clashes with substats.
        """
        invalid_inputs = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        invalid_substats = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

        for i, val in enumerate(invalid_inputs):
            with self.subTest(input_val=val):
                with self.assertRaises(ValueError, msg="{input_val} did not raise a ValueError"):
                    validate_mainstat_id(val, invalid_substats[i])     
                    
                    
    def test_invalid_inputs_with_substat_2(self):
        """
        Checks whether we get an error if mainstat clashes with substats.
        """
        invalid_inputs = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        invalid_substats = [['0', 1, 2], ['1', 2, 3], ['2', 2], ['3', 5, 10], ['4', 0, 3, 2], ['5', 0], '6', '7', '8', '9', '10']

        for i, val in enumerate(invalid_inputs):
            with self.subTest(input_val=val):
                with self.assertRaises(ValueError, msg="{input_val} did not raise a ValueError"):
                    validate_mainstat_id(val, invalid_substats[i])     
                    
                    
    def test_invalid_inputs_with_substat_gear_type(self):
        """
        Valid main, invalid subs for given gear.
        """
        valid_inputs = [0, 2, 4]
        valid_substats = [4, [0, 1, 2], [0, 10, 3]]
        invalid_gear = ['weapon', 'helm', 'armor']
        
        for i, input_val in enumerate(valid_inputs):
            with self.subTest(input_val=input_val):
                with self.assertRaises(ValueError, msg="{input_val} did not raise a ValueError"):
                    validate_mainstat_id(input_val, valid_substats[i], gear_type=invalid_gear[i])     
                    
                    
    def test_invalid_inputs_with_mainstat_gear_type(self):
        """
        Valid subs, invalid mains for given gear.
        """
        valid_inputs = [1, 3, 5]
        valid_substats = [[1, 10, 9, 3], [0, 1, 3, 7], [10, 3, 5, 8]]
        invalid_gear = ['weapon', 'helm', 'armor']
        
        for i, input_val in enumerate(valid_inputs):
            with self.subTest(input_val=input_val):
                with self.assertRaises(ValueError, msg="{input_val} did not raise a ValueError"):
                    validate_mainstat_id(input_val, valid_substats[i], gear_type=invalid_gear[i])     
                    
                    
if __name__ == '__main__':
    unittest.main()