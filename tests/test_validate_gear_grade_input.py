from set_directory_function import set_directory
set_directory()

import unittest
from src.validation_utils import validate_gear_grade_input

class TestValidateGearGrade(unittest.TestCase):

    def test_validate_gear_grade_1(self):
        """Test valid gear_grade when written in lower case, upper case, or mixed case"""
        valid_gear_grades = ['normal', 'good', 'rare', 'heroic', 'epic'] 
        for gear_grade in valid_gear_grades:
            self.assertEqual(validate_gear_grade_input(gear_grade), gear_grade.lower())

            
    def test_validate_gear_grade_2(self):
        """Test valid gear_grade when written in lower case, upper case, or mixed case"""
        valid_gear_grades = ['Normal', 'Good', 'Rare', 'Heroic', 'Epic'] 
        for gear_grade in valid_gear_grades:
            self.assertEqual(validate_gear_grade_input(gear_grade), gear_grade.lower())
            
            
    def test_validate_gear_grade_3(self):
        """Test valid gear_grade when written in lower case, upper case, or mixed case"""
        valid_gear_grades = ['NORMAL', 'GOOD', 'RARE', 'HEROIC', 'EPIC'] 
        for gear_grade in valid_gear_grades:
            self.assertEqual(validate_gear_grade_input(gear_grade), gear_grade.lower())

            
    def test_validate_gear_grade_4(self):
        """Test valid gear_grade when written in lower case, upper case, or mixed case"""
        valid_gear_grades = ['norMAL', 'GooD', 'rARe', 'HeRoIc', 'ePIC']
        for gear_grade in valid_gear_grades:
            self.assertEqual(validate_gear_grade_input(gear_grade), gear_grade.lower())
        
        
    def test_validate_gear_grade_invalid_1(self):
        """Test invalid gear written as some str"""
        invalid_gear_grades = ['mainstats', 'SUBSTATS', 'subs', 'Main', 'stATs', 'stat']
        for gear_grade in invalid_gear_grades:
            with self.assertRaises(ValueError):
                validate_gear_grade_input(gear_grade)
                
                            
    def test_validate_gear_grade_invalid_2(self):
        """Test invalid gear in a wrong type"""
        invalid_gear_grades = [1, None, -1]
        for gear_grade in invalid_gear_grades:
            with self.assertRaises(TypeError):
                validate_gear_grade_input(gear_grade)
                
                
if __name__ == '__main__':
    unittest.main()
