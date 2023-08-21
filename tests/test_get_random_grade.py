from set_directory_function import set_directory
set_directory()

import random
import json
import unittest
from src.utilities import get_random_grade

GRADES = json.loads(open('data/grades.json', 'r').read())

class TestGetRandomGrade(unittest.TestCase):
    
    def test_get_random_grade(self):
        """
        Test whether the get_random_grade function returns a str that is in 
        ['normal', 'good', 'rare', 'heroic', 'epic'] and whether the rates are accurate.
        """
        # Initialize starting values of 0, which will be incremented when they are chosen
        normal = 0
        good = 0
        rare = 0
        heroic = 0
        epic = 0
        
        # number of iterations
        iters = 100000
        expected_results = list(GRADES.keys())
        
        for i in range(1, iters):
            pick_grade = get_random_grade()
            self.assertIn(pick_grade, expected_results, f"Grade {pick_grade} is not in {expected_results}")
                
            if pick_grade == 'normal':
                normal += 1
            elif pick_grade == 'good':
                good += 1
            elif pick_grade == 'rare':
                rare += 1
            elif pick_grade == 'heroic':
                heroic += 1
            elif pick_grade == 'epic':
                epic += 1
                
        # Calculate rates based on simulation
        normal_rates = normal/iters
        print(f"Normal Rates: {normal_rates}")
        good_rates = good/iters
        print(f"Good Rates: {good_rates}")
        rare_rates = rare/iters
        print(f"Rare Rates: {rare_rates}")
        heroic_rates = heroic/iters
        print(f"Heroic Rates: {heroic_rates}")
        epic_rates = epic/iters
        print(f"Epic Rates: {epic_rates}")

        # Actual rates as entered in GRADES.json
        actual_normal_rates = GRADES['normal']['weight']
        actual_good_rates = GRADES['good']['weight']
        actual_rare_rates = GRADES['rare']['weight']
        actual_heroic_rates = GRADES['heroic']['weight']
        actual_epic_rates = GRADES['epic']['weight']

        # Check rates using assertAlmostEqual
        self.assertAlmostEqual(normal_rates, actual_normal_rates, delta=0.02, msg="Common rate not within tolerance")
        self.assertAlmostEqual(good_rates, actual_good_rates, delta=0.02, msg="Good rate not within tolerance")
        self.assertAlmostEqual(rare_rates, actual_rare_rates, delta=0.02, msg="Rare rate not within tolerance")
        self.assertAlmostEqual(heroic_rates, actual_heroic_rates, delta=0.02, msg="Heroic rate not within tolerance")
        self.assertAlmostEqual(epic_rates, actual_epic_rates, delta=0.02, msg="Epic rate not within tolerance")


if __name__ == '__main__':
    unittest.main()
