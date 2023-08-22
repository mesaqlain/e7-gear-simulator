from set_directory_function import set_directory
set_directory()

import unittest
import json
import random
from tests.test_class_gear_v1 import Gear 
from src.validation_utils import *

SETS = json.loads(open('data/sets.json', 'r').read())

class TestNonOverlappingStat(unittest.TestCase):
    
    
    def setUp(self):
        self.gear = Gear()
        
        
    def tearDown(self):
        self.gear = None
    
    
    def test_initial_attributes(self):
        """
        Tests whether the initial values of the attributes are as we expect
        """
        self.assertIsNone(self.gear.gear_type)
        self.assertIsNone(self.gear.gear_grade)
        self.assertIsNone(self.gear.gear_set)
        self.assertEqual(self.gear.gear_level, 85, "gear level should be 85")
        self.assertEqual(self.gear.gear_tier, 6, "gear tier should be 6")
        self.assertEqual(self.gear.enhance_level, 0, "enhance level should be 0")
        self.assertFalse(self.gear.is_reforged)
        self.assertIsNone(self.gear.mainstat)
        self.assertIsNone(self.gear.substats)
        
        
    def test_create_gear_default(self):
        """
        Tests whether the initial values of the attributes are as we expect when we use 
        create_gear() method
        """
        self.gear.create_gear()
        self.assertIsNone(self.gear.gear_type)
        self.assertIn(self.gear.gear_set, list(SETS.keys()))
        self.assertEqual(self.gear.gear_level, 85, "gear level should be 85")
        self.assertEqual(self.gear.gear_tier, 6, "gear tier should be 6")
        self.assertIsNone(self.gear.mainstat)
        self.assertIsNone(self.gear.substats)
        
        
    def test_create_gear_specify_1(self):
        """
        Tests whether the initial values of the attributes are as we expect when we use 
        create_gear() method with gear_type='weapon'
        """
        self.gear.create_gear(gear_type='weapon')
        self.assertEqual(self.gear.gear_type, 'weapon')
        self.assertIn(self.gear.gear_set, list(SETS.keys()))
        self.assertEqual(self.gear.gear_level, 85, "gear level should be 85")
        self.assertEqual(self.gear.gear_tier, 6, "gear tier should be 6")
        self.assertIsNone(self.gear.mainstat)
        self.assertIsNone(self.gear.substats)
        
        
    def test_create_gear_specify_2(self):
        """
        Tests whether the initial values of the attributes are as we expect when we use 
        create_gear() method with gear_type='weapon', gear_set='health'
        """
        self.gear.create_gear(gear_type='weapon', gear_set='health')
        self.assertEqual(self.gear.gear_type, 'weapon')
        self.assertEqual(self.gear.gear_set, 'health')
        self.assertEqual(self.gear.gear_level, 85, "gear level should be 85")
        self.assertEqual(self.gear.gear_tier, 6, "gear tier should be 6")
        self.assertIsNone(self.gear.mainstat)
        self.assertIsNone(self.gear.substats)
        
        
    def test_create_gear_specify_3(self):
        """
        Tests whether the initial values of the attributes are as we expect when we use 
        create_gear() method with gear_type='weapon', gear_set='health', gear_level=90
        """
        self.gear.create_gear(gear_type='weapon', gear_set='health', gear_level=90)
        self.assertEqual(self.gear.gear_type, 'weapon')
        self.assertEqual(self.gear.gear_set, 'health')
        self.assertEqual(self.gear.gear_level, 90, "gear level should be 85")
        self.assertEqual(self.gear.gear_tier, 7, "gear tier should be 7")
        self.assertIsNone(self.gear.mainstat)
        self.assertIsNone(self.gear.substats)
        
        
    def test_create_gear_specify_4(self):
        """
        Tests whether the initial values of the attributes are as we expect when we use 
        create_gear() method with gear_type='weapon', gear_set='health', gear_level=90,
        gear_grade='heroic'
        """
        self.gear.create_gear(gear_type='weapon', gear_set='health', gear_level=90, gear_grade='heroic')
        self.assertEqual(self.gear.gear_type, 'weapon')
        self.assertEqual(self.gear.gear_set, 'health')
        self.assertEqual(self.gear.gear_grade, 'heroic')
        self.assertEqual(self.gear.gear_level, 90, "gear level should be 85")
        self.assertEqual(self.gear.gear_tier, 7, "gear tier should be 7")
        self.assertIsNone(self.gear.mainstat)
        self.assertIsNone(self.gear.substats)
        
        
    def test_create_gear_specify_5(self):
        """
        Tests whether the initial values of the attributes are as we expect when we use 
        create_gear() method with gear_type='weapon', gear_set='health', gear_level=90,
        gear_grade='heroic', mainstat_id=4
        """
        self.gear.create_gear(gear_type='weapon', gear_set='health', gear_level=90, gear_grade='heroic',
                             mainstat_id=4)
        self.assertEqual(self.gear.gear_type, 'weapon')
        self.assertEqual(self.gear.gear_set, 'health')
        self.assertEqual(self.gear.gear_grade, 'heroic')
        self.assertEqual(self.gear.gear_level, 90, "gear level should be 85")
        self.assertEqual(self.gear.gear_tier, 7, "gear tier should be 7")
        self.assertEqual(self.gear.mainstat_id, '4', "mainstat id should be 4")
        self.assertIsNone(self.gear.substat_ids)
        self.assertIsNone(self.gear.mainstat)
        self.assertIsNone(self.gear.substats)
        
        
    def test_create_gear_specify_6(self):
        """
        Tests whether the initial values of the attributes are as we expect when we use 
        create_gear() method with gear_type='weapon', gear_set='health', gear_level=90,
        gear_grade='heroic', mainstat_id=4, substat_ids=[1,2,3,4]
        """
        self.gear.create_gear(gear_type='weapon', gear_set='health', gear_level=90, gear_grade='heroic',
                             mainstat_id=0, substat_ids=[1,2,3,4])
        self.assertEqual(self.gear.gear_type, 'weapon')
        self.assertEqual(self.gear.gear_set, 'health')
        self.assertEqual(self.gear.gear_grade, 'heroic')
        self.assertEqual(self.gear.gear_level, 90, "gear level should be 85")
        self.assertEqual(self.gear.gear_tier, 7, "gear tier should be 7")
        self.assertEqual(self.gear.mainstat_id, '0', "mainstat id should be 0")
        self.assertEqual(self.gear.substat_ids, ['1', '2', '3', '4'], "substat id's should be ['1', '2', '3', '4']")
        self.assertIsNone(self.gear.mainstat)
        self.assertIsNone(self.gear.substats)
        
        
    def test_create_gear_specify_7(self):
        """
        Tests whether the initial values of the attributes are as we expect when we use 
        create_gear() method with gear_type='weapon', gear_set='health', gear_level=90,
        gear_grade='heroic', substat_ids=[1,2,3,4] (no mainstat_id provided)
        """
        self.gear.create_gear(gear_type='weapon', gear_set='health', gear_level=90, gear_grade='heroic',
                             substat_ids=[1,2,3,4])
        self.assertEqual(self.gear.gear_type, 'weapon')
        self.assertEqual(self.gear.gear_set, 'health')
        self.assertEqual(self.gear.gear_grade, 'heroic')
        self.assertEqual(self.gear.gear_level, 90, "gear level should be 85")
        self.assertEqual(self.gear.gear_tier, 7, "gear tier should be 7")
        self.assertIsNone(self.gear.mainstat_id)
        self.assertEqual(self.gear.substat_ids, ['1', '2', '3', '4'], "substat id's should be ['1', '2', '3', '4']")
        self.assertIsNone(self.gear.mainstat)
        self.assertIsNone(self.gear.substats)
        
        
    def test_create_gear_specify_invalid_1(self):
        """
        Tests whether we get ValueError when we mainstat is in substat
        """
        with self.assertRaises(ValueError):
            self.gear.create_gear(gear_type='weapon', gear_set='health', gear_level=90, 
                                  gear_grade='heroic', mainstat_id=3, substat_ids=[1,2,3,4])
            
            
    def test_create_gear_specify_invalid_2(self):
        """
        Tests whether we get ValueError when we there aer duplicates in substats
        """
        with self.assertRaises(ValueError):
            self.gear.create_gear(gear_type='weapon', gear_set='health', gear_level=90, 
                                  gear_grade='heroic', mainstat_id=3, substat_ids=[1,2,4,4])

            
if __name__ == '__main__':
    unittest.main()
