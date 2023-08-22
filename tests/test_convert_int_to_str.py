from set_directory_function import set_directory
set_directory()

import unittest
from src.utilities import convert_int_to_str

class TestConvertIntToStr(unittest.TestCase):
    
    def test_valid_inputs(self):
        """
        Check valid inputs against expected results.
        Case 1: Small int
        Case 2: Large int
        Case 3: neg int
        Case 4: list of ints
        Case 5: list of a single int
        """
        valid_inputs = [1, 1000, -1, [1, 5, -3], [1]]
        expected_outputs = [['1'], ['1000'], ['-1'], ['1', '5', '-3'], ['1']]
        for i, input_val in enumerate(valid_inputs):
            with self.subTest(input_val=input_val):
                output = convert_int_to_str(input_val)
                expected_output = expected_outputs[i]
                self.assertEqual(output, expected_output, f"Output - {output} doesn't match input - {input_val}")

                
    def test_invalid_inputs(self):
        """
        Check valid inputs against expected results.
        Case 1: str
        Case 2: list containing both str and int
        Case 3: list containing a str
        """
        invalid_inputs = ['1', ['1', 2], ['3']]
        for i in invalid_inputs:
            with self.subTest(input_val=i):
                with self.assertRaises(ValueError, msg="{input_val} did not raise a ValueError"):
                    convert_int_to_str(i)
                
                
if __name__ == '__main__':
    unittest.main()