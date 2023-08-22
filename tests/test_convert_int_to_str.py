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
        Case 6: str representation of int
        Case 7: list of single str representation of int
        Case 8: list of str representation of int
        Case 9: list of mixed int and str
        """
        
        valid_inputs = [1, 1000, -1, [1, 5, -3], [1], '1', ['1'], ['10', '20'], ['3', 4]]
        expected_outputs = [['1'], ['1000'], ['-1'], ['1', '5', '-3'], ['1'], ['1'], ['1'], ['10', '20'], ['3', '4']]
        for i, input_val in enumerate(valid_inputs):
            with self.subTest(input_val=input_val):
                output = convert_int_to_str(input_val)
                expected_output = expected_outputs[i]
                self.assertEqual(output, expected_output, f"Output - {output} doesn't match input - {input_val}")

                
    def test_invalid_inputs(self):
        """
        Check valid inputs against expected results.
        Case 1: some random str
        Case 2: random str
        Case 3: list containing an invalid str
        Case 4: list containing some valid entries and invalid entries
        """
        invalid_inputs = ['some str', 'one', ['two'], ['1', 2, 'some str']]
        for i in invalid_inputs:
            with self.subTest(input_val=i):
                with self.assertRaises(TypeError, msg="{input_val} did not raise a TypeError"):
                    convert_int_to_str(i)
                
                
if __name__ == '__main__':
    unittest.main()