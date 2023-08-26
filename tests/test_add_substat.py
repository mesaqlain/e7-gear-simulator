from set_directory_function import set_directory
set_directory()

# Imports
import unittest
import json
import random
from src.gear import Gear
from src.utilities import convert_int_to_str

class TestAddSubstat(unittest.TestCase):
    """
    Test adding a substat to a gear
    """

    def test_already_4_subs(self):
        """
        We should get an error if the gear already has 4 substats
        """
        gear = Gear()
        gear.create_gear(gear_grade='epic')
        
        # Check that there are 4 substat id's
        self.assertEqual(len(gear.substat_ids), 4)
        
        with self.assertRaises(ValueError):
            gear.add_substat()
            
            
    def test_add_to_rare(self):
        """
        Try adding new substat to rare gear, should be able to add twice. 
        Check that the values are in expected based on gear_type.
        Check that there are no duplicates
        """
        for i in range(1000):
            gear = Gear()
            gear.create_gear(gear_grade='rare', gear_type='armor', substat_ids=[10, 9])

            expected_new_substat_ids = [2, 3, 5, 6, 7, 8]

            # Check that there are 4 substat id's
            self.assertEqual(len(gear.substat_ids), 2)

            gear.add_substat()
            # After adding a substat, we should now have 3
            self.assertEqual(len(gear.substat_ids), 3)
            new_sub_id = gear.substats[2].stat_id
            self.assertIn(new_sub_id, convert_int_to_str(expected_new_substat_ids))

            gear.add_substat()
            # Should now have 4
            self.assertEqual(len(gear.substat_ids), 4)
            new_sub_id2 = gear.substats[3].stat_id
            self.assertIn(new_sub_id2, convert_int_to_str(expected_new_substat_ids))
            
            # Check that there are no duplicates
            substat_id_set = set(gear.substat_ids)
            mainstat_id_set = set([gear.mainstat_id])
            all_id_set = substat_id_set.union(mainstat_id_set)  
            self.assertEqual(len(all_id_set), 5)
            
            
    def test_add_to_heroic(self):
        """
        Try adding new substat to heroic gear, should be able to add once. 
        Check that the values are in expected based on gear_type.
        Check that there are no duplicates
        """
        for i in range(1000):
            gear = Gear()
            gear.create_gear(gear_grade='heroic', gear_type='weapon', substat_ids=[1, 6, 9])

            expected_new_substat_ids = [2, 3, 7, 8, 10]

            # Check that there are 4 substat id's
            self.assertEqual(len(gear.substat_ids), 3)

            gear.add_substat()
            # After adding a substat, we should now have 4
            self.assertEqual(len(gear.substat_ids), 4)
            new_sub_id = gear.substats[3].stat_id
            self.assertIn(new_sub_id, convert_int_to_str(expected_new_substat_ids))
            
            # Check that there are no duplicates
            substat_id_set = set(gear.substat_ids)
            mainstat_id_set = set([gear.mainstat_id])
            all_id_set = substat_id_set.union(mainstat_id_set)  
            self.assertEqual(len(all_id_set), 5)
            
            
    def test_add_to_heroic_more_than_4(self):
        """
        If we try adding substats to a heroic gear twice, we'll get an error
        """
        gear = Gear()
        gear.create_gear(gear_grade='heroic', gear_type='weapon', substat_ids=[1, 6, 9])
        with self.assertRaises(ValueError):
            gear.add_substat()
            gear.add_substat()
            
            
    def test_add_to_rare_more_than_4(self):
        """
        If we try adding substats to a heroic gear twice, we'll get an error
        """
        gear = Gear()
        gear.create_gear(gear_grade='rare', gear_type='weapon', substat_ids=[1, 6])
        with self.assertRaises(ValueError):
            gear.add_substat()
            gear.add_substat()
            gear.add_substat()
            
            
if __name__ == '__main__':
    unittest.main()