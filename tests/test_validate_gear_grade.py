from set_directory_function import set_directory
set_directory()

import unittest
from src.validation_utils import validate_gear_grade

class TestValidateGearGrade(unittest.TestCase):

    def test_validate_gear_grade_1(self):
        """Test valid gear_grade when written in lower case, upper case, or mixed case"""
        valid_gear_grades = ['normal', 'good', 'rare', 'heroic', 'epic'] 
        for gear_grade in valid_gear_grades:
            self.assertEqual(validate_gear_grade(gear_grade), gear_grade.lower())

            
    def test_validate_gear_grade_2(self):
        """Test valid gear_grade when written in lower case, upper case, or mixed case"""
        valid_gear_grades = ['Normal', 'Good', 'Rare', 'Heroic', 'Epic'] 
        for gear_grade in valid_gear_grades:
            self.assertEqual(validate_gear_grade(gear_grade), gear_grade.lower())
            
            
    def test_validate_gear_grade_3(self):
        """Test valid gear_grade when written in lower case, upper case, or mixed case"""
        valid_gear_grades = ['NORMAL', 'GOOD', 'RARE', 'HEROIC', 'EPIC'] 
        for gear_grade in valid_gear_grades:
            self.assertEqual(validate_gear_grade(gear_grade), gear_grade.lower())

            
    def test_validate_gear_grade_4(self):
        """Test valid gear_grade when written in lower case, upper case, or mixed case"""
        valid_gear_grades = ['norMAL', 'GooD', 'rARe', 'HeRoIc', 'ePIC']
        for gear_grade in valid_gear_grades:
            self.assertEqual(validate_gear_grade(gear_grade), gear_grade.lower())
            
            
    def test_validate_gear_grade_normal(self):
        """Test valid gear grade is empty or None (normal gear cannot have any starting subtats)"""
        input_gear_grade = 'normal'
        substat_id_list = [None, []]
        
        for substat_id in substat_id_list:
            self.assertEqual(validate_gear_grade(input_gear_grade, substat_ids = substat_id), input_gear_grade)
                    
    def test_validate_gear_grade_good(self):
        """Test valid gear_grade=good (good gear cannot have more than 1 starting subs)"""
        input_gear_grade = 'good'
        substat_id_list = [None, [], [1], 1]
        
        for substat_id in substat_id_list:
            self.assertEqual(validate_gear_grade(input_gear_grade, substat_ids = substat_id), input_gear_grade)
                
                
    def test_validate_gear_grade_rare(self):
        """Test valid gear_grade=rare (rare gear cannot have more than 2 starting subs)"""
        input_gear_grade = 'rare'
        substat_id_list = [None, [], [1], 1, [10, 5], [3, 6]]
        
        for substat_id in substat_id_list:
            self.assertEqual(validate_gear_grade(input_gear_grade, substat_ids = substat_id), input_gear_grade)
                
                
    def test_validate_gear_grade_heroic(self):
        """Test valid gear_grade=heroic (heroic gear cannot have more than 3 starting subs)"""
        input_gear_grade = 'heroic'
        substat_id_list = [None, [], [1], 1, [10, 5], [3, 6], [4, 5, 1], ['0', '3', '10']]
        
        for substat_id in substat_id_list:
            self.assertEqual(validate_gear_grade(input_gear_grade, substat_ids = substat_id), input_gear_grade)
            
            
    def test_validate_gear_grade_epic(self):
        """Test valid gear_grade=epic (epic gear cannot have more than 3 starting subs)"""
        input_gear_grade = 'epic'
        substat_id_list = [None, [], [1], 1, [10, 5], [3, 6], [4, 5, 1], ['0', '3', '10'], [1, 4, 5, 0], [10, 9, '7', '3']]
        
        for substat_id in substat_id_list:
            self.assertEqual(validate_gear_grade(input_gear_grade, substat_ids = substat_id), input_gear_grade)
                
                
    def test_validate_gear_grade_input_non_with_subs(self):
        """Test valid gear_grade=epic (epic gear cannot have more than 3 starting subs)"""
        input_gear_grade = None
        expected_gear_grades = ['rare', 'heroic', 'epic']
        substat_id_list = [None, [], [1], 1, [10, 5], [3, 6], [4, 5, 1], ['0', '3', '10'], [1, 4, 5, 0], [10, 9, '7', '3']]
        
        for substat_id in substat_id_list:
            self.assertIn(validate_gear_grade(input_gear_grade, substat_ids = substat_id), expected_gear_grades)
                
                
    def test_validate_gear_grade_invalid_1(self):
        """Test invalid gear written as some str"""
        invalid_gear_grades = ['mainstats', 'SUBSTATS', 'subs', 'Main', 'stATs', 'stat']
        for gear_grade in invalid_gear_grades:
            with self.assertRaises(ValueError):
                validate_gear_grade(gear_grade)
                
                
    def test_validate_gear_grade_invalid_normal(self):
        """Test invalid gear grade when gear is normal and we have more than 0 substats"""
        input_gear_grade = 'normal'
        substat_id_list = [1, [1], [2, 3], [5, 10, 0], [4, 10, 3, 5]]
        for substat_id in substat_id_list:
            with self.assertRaises(ValueError):
                validate_gear_grade(input_gear_grade, substat_ids=substat_id)
                
                
    def test_validate_gear_grade_invalid_good(self):
        """Test invalid gear grade when gear is good and we have more than 1 substats"""
        input_gear_grade = 'good'
        substat_id_list = [[2, 3], [5, 10, 0], [4, 10, 3, 5]]
        for substat_id in substat_id_list:
            with self.assertRaises(ValueError):
                validate_gear_grade(input_gear_grade, substat_ids=substat_id)

                
    def test_validate_gear_grade_invalid_rare(self):
        """Test invalid gear grade when gear is rare and we have more than 2 substats"""
        input_gear_grade = 'good'
        substat_id_list = [[5, 10, 0], [4, 10, 3, 5]]
        for substat_id in substat_id_list:
            with self.assertRaises(ValueError):
                validate_gear_grade(input_gear_grade, substat_ids=substat_id)

                
    def test_validate_gear_grade_invalid_heroic(self):
        """Test invalid gear grade when gear is heroic and we have more than 3 substats"""
        input_gear_grade = 'heroic'
        substat_id_list = [[5, 10, 0, 3], [4, 10, 3, 5]]
        for substat_id in substat_id_list:
            with self.assertRaises(ValueError):
                validate_gear_grade(input_gear_grade, substat_ids=substat_id)
                
                
    def test_validate_gear_grade_invalid_heroic_duplicates(self):
        """Test invalid gear grade when gear is heroic and we have duplicates"""
        input_gear_grade = 'heroic'
        substat_id_list = [[5, 3, 3], [1, 1, 1]]
        for substat_id in substat_id_list:
            with self.assertRaises(ValueError):
                validate_gear_grade(input_gear_grade, substat_ids=substat_id)
                
                
    def test_validate_gear_grade_invalid_heroic_main_clash(self):
        """Test invalid gear grade when gear is heroic and we have clash in mainstat and substats"""
        input_gear_grade = 'heroic'
        substat_id_list = [[5, 1, 4], [1, 2, 3]]
        mainstat_id_list = [1, 2]
        for i, substat_id in enumerate(substat_id_list):
            with self.assertRaises(ValueError):
                validate_gear_grade(input_gear_grade, substat_ids=substat_id, mainstat_id=mainstat_id_list[i])
                
                
    def test_validate_gear_grade_invalid_heroic_too_many_subs(self):
        """Test invalid gear grade when there are too many subs"""
        input_gear_grade = 'heroic'
        substat_id_list = [[5, 1, 4, 1, 2, 3], [1, 2, 3]]
        mainstat_id_list = [1, 2]
        for i, substat_id in enumerate(substat_id_list):
            with self.assertRaises(ValueError):
                validate_gear_grade(input_gear_grade, substat_ids=substat_id, mainstat_id=mainstat_id_list[i])
                
                
    def test_validate_gear_grade_invalid_too_many_subs_no_grade(self):
        """Test invalid gear grade when there are too many subs"""
        substat_id_list = [[5, 1, 4, 1, 2, 3], [1, 2, 3]]
        mainstat_id_list = [1, 2]
        for i, substat_id in enumerate(substat_id_list):
            with self.assertRaises(ValueError):
                validate_gear_grade(None, substat_ids=substat_id, mainstat_id=mainstat_id_list[i])
                
                
    def test_validate_gear_grade_no_gear_grade_provided(self):
        """Test valid gear_grade=None (we should get the appropriate gear grade based on numbe of substats):"""
        expected_gear_grades = [
            ['rare', 'heroic', 'epic'],
            ['rare', 'heroic', 'epic'],
            ['rare', 'heroic', 'epic'],
            ['rare', 'heroic', 'epic'],
            ['rare', 'heroic', 'epic'],
            ['rare', 'heroic', 'epic'],
            ['heroic', 'epic'],
            ['heroic', 'epic'],
            ['epic'],
            ['epic']
        ]
        substat_id_list = [None, [], [1], 1, [10, 5], [3, 6], [4, 5, 1], ['0', '3', '10'], [1, 4, 5, 0], [10, 9, '7', '3']]
        
        for i, substat_id in enumerate(substat_id_list):
            for j in range(100):
                with self.subTest(substat_id = substat_id):
                    self.assertIn(validate_gear_grade(None, substat_ids = substat_id), expected_gear_grades[i])

                
if __name__ == '__main__':
    unittest.main()
