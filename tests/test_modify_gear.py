from set_directory_function import set_directory
set_directory()

# Imports
import unittest
import json
import random
from src.gear import Gear
import copy
from deepdiff import DeepDiff
from unittest.mock import patch

with open('data/stats.json', 'r') as stats_file:
    STATS = json.load(stats_file)

class TestModifyGear(unittest.TestCase):
    """
    Test the Modify Gear method.
    """
    
    def test_modify_non_enhanced_gear(self):
        """
        Modify should not work unless a gear is +15 enhancement level
        """
        input_levels = [70, 75, 80, 88, 90]        
        
        for l in input_levels:
            gear = Gear()
            gear.create_gear(gear_grade='epic', substat_ids=[10, 9, 5, 7], mainstat_id=3)
            gear.enhance_level = l
            
            gear_before = copy.copy(gear)
        
            with patch('builtins.print') as mock_print:

                gear.modify_gear(1, 10)

                # Check that the expected output is printed
                mock_print.assert_called_with("Cannot modify a gear that has not been enhanced to +15 yet.")

                # Compare the gear objects using DeepDiff
                diff = DeepDiff(gear, gear_before)
                self.assertTrue(not diff)  # If diff is empty, the objects are the same
    
    
    def test_modify_non_already_modded(self):
        """
        Modify should not work on a substat if another substat has been modified already
        """
        index_to_test = [0, 1, 2, 3]
        gear = Gear()
        gear.create_gear(gear_grade='epic', substat_ids=[10, 9, 5, 7], mainstat_id=3)
        gear.enhance_level = 15
        
        for i in index_to_test:
            # set the indexed substat as modded = True
            gear.substats[i].modded = True
            
            for j in range(len(index_to_test)):
                if j != i:
                    # Make a copy
                    gear_before = copy.copy(gear)

                    with patch('builtins.print') as mock_print:

                        gear.modify_gear(j+1, 8)

                        # Check that the expected output is printed
                        mock_print.assert_called_with("Cannot modify substat when another substat has been modified already.")

                        # Compare the gear objects using DeepDiff
                        diff = DeepDiff(gear, gear_before)
                        self.assertTrue(not diff, "Gear objects should remain the same when trying to modify a non-modded substat.")
                    
                    
    def test_modify_duplicate_sub(self):
        """
        Modify should not work on a substat if the same substat exists already.
        Test by trying to change the stat_index = 1 to subs that are in stat_index = 2, 3, and 4
        as well as in the mainstat.
        """
        stats_to_test = [9, 5, 7, 3]
        gear = Gear()
        gear.create_gear(gear_grade='epic', substat_ids=[10, 9, 5, 7], mainstat_id=3)
        gear.enhance_level = 15
        
        for i in stats_to_test:
            # Make a copy
            gear_before = copy.copy(gear)

            with patch('builtins.print') as mock_print:

                gear.modify_gear(1, i)

                # Check that the expected output is printed
                mock_print.assert_called_with("Cannot add a substat that already exists on the gear.")

                # Compare the gear objects using DeepDiff
                diff = DeepDiff(gear, gear_before)
                self.assertTrue(not diff, "Gear objects should remain the same when trying to modify a duplicate substat.")
                    
                    
    def test_invalid_sub(self):
        """
        Modify should not work if a substat that is not allowed in the available pool is added
        """
        input_gear_list = ['weapon', 'helm', 'armor']
        stats_to_test = ['4', '2', '1']
        
        for i, val in enumerate(input_gear_list):
            
            gear = Gear()
            gear.create_gear(gear_grade='epic', gear_type=input_gear_list[i])
            gear.enhance_level = 15

            with self.assertRaises(ValueError):
                gear.modify_gear(1, stats_to_test[i])
                
                
    def test_mock_gear_1(self):
        """
        Test reforge on a mock Lv 85 gear with mainstat=8 (effectiveness) and substats=[1,7,5,9].
        Substats are Atk %, crit damage, Speed, and effect resistance.
        We'll enhance some of the values manually and set fixed values afterwards so that we can expect the modded value.
        Attack % modded twice, so rolled is 2, and our modded value will be base on  that
        Crit damage modded once, so rolled is 1.
        Speed is modded twice, so rolled is 2.
        Eff_res is modded 0 times, so rolled is 0.
        """
                
        index_to_test = [0, 1, 2, 3]
        rolled_counts = [2, 1, 2, 0]
        
        indices_to_add = [0, 6, 4, 10]
                    
        # Expected Values Stored in variables
        atk_values_0 = STATS['0']['mod_vals']['greater'][0][0]
        atk_values_1 = STATS['0']['mod_vals']['greater'][0][1]
        atk_values_2 = STATS['0']['mod_vals']['greater'][0][2]
        
        crit_values_0 = STATS['6']['mod_vals']['greater'][0][0]
        crit_values_1 = STATS['6']['mod_vals']['greater'][0][1]
        crit_values_2 = STATS['6']['mod_vals']['greater'][0][2]
                           
        fdef_values_0 = STATS['4']['mod_vals']['greater'][0][0]
        fdef_values_1 = STATS['4']['mod_vals']['greater'][0][1]
        fdef_values_2 = STATS['4']['mod_vals']['greater'][0][2]

        spd_values_0 = STATS['10']['mod_vals']['greater'][0][0]
        spd_values_1 = STATS['10']['mod_vals']['greater'][0][1]
        spd_values_2 = STATS['10']['mod_vals']['greater'][0][2]

        expected_values_dict = {
            0: {
                0: atk_values_0,
                1: atk_values_1,
                2: atk_values_2
            },
            1: {
                0: crit_values_0,
                1: crit_values_1,
                2: crit_values_2
            },
            2: {
                0: fdef_values_0,
                1: fdef_values_1,
                2: fdef_values_2
            },
            3: {
                0: spd_values_0,
                1: spd_values_1,
                2: spd_values_2
            }
            
        }
                           
        for i, s_ind in enumerate(index_to_test):
            for j, a_ind in enumerate(indices_to_add):

                gear = Gear()
                gear.create_gear(mainstat_id=8, substat_ids=[1, 7, 5, 9], gear_type='ring')

                # Set enhance_level to +15 so we may reforge
                gear.enhance_level = 15

                # Enhance 5 substats, these should change their rolled value and reforge_increase value
                gear.substats[0].enhance_stat()
                gear.substats[0].enhance_stat()
                gear.substats[1].enhance_stat()
                gear.substats[2].enhance_stat()
                gear.substats[2].enhance_stat()
                           
                # Modify gear
                gear.modify_gear(s_ind+1, a_ind)

                # Calculate expected value based on rolled count and substat index
                rolled_count = rolled_counts[i]
                expected_value_list = expected_values_dict[j][rolled_count]

                # Check if the actual modified value matches the expected value
                self.assertIn(gear.substats[s_ind].value, expected_value_list)
                self.assertTrue(gear.substats[s_ind].modded)
                           

    def test_mock_gear_2(self):
        """
        Test reforge on a mock Lv 90 gear with mainstat=8 (effectiveness) and substats=[1,7,5,9].
        Substats are Atk %, crit damage, Speed, and effect resistance.
        We'll enhance some of the values manually and set fixed values afterwards so that we can expect the modded value.
        Attack % modded twice, so rolled is 2, and our modded value will be base on  that
        Crit damage modded once, so rolled is 1.
        Speed is modded twice, so rolled is 2.
        Eff_res is modded 0 times, so rolled is 0.
        """
                
        index_to_test = [0, 1, 2, 3]
        rolled_counts = [2, 1, 2, 0]
        
        indices_to_add = [0, 6, 4, 10]
                    
        # Expected Values Stored in variables (lesser and index = 1 becaues lv 90 gear)
        atk_values_0 = STATS['0']['mod_vals']['lesser'][1][0]
        atk_values_1 = STATS['0']['mod_vals']['lesser'][1][1]
        atk_values_2 = STATS['0']['mod_vals']['lesser'][1][2]
        
        crit_values_0 = STATS['6']['mod_vals']['lesser'][1][0]
        crit_values_1 = STATS['6']['mod_vals']['lesser'][1][1]
        crit_values_2 = STATS['6']['mod_vals']['lesser'][1][2]
                           
        fdef_values_0 = STATS['4']['mod_vals']['lesser'][1][0]
        fdef_values_1 = STATS['4']['mod_vals']['lesser'][1][1]
        fdef_values_2 = STATS['4']['mod_vals']['lesser'][1][2]

        spd_values_0 = STATS['10']['mod_vals']['lesser'][1][0]
        spd_values_1 = STATS['10']['mod_vals']['lesser'][1][1]
        spd_values_2 = STATS['10']['mod_vals']['lesser'][1][2]

        expected_values_dict = {
            0: {
                0: atk_values_0,
                1: atk_values_1,
                2: atk_values_2
            },
            1: {
                0: crit_values_0,
                1: crit_values_1,
                2: crit_values_2
            },
            2: {
                0: fdef_values_0,
                1: fdef_values_1,
                2: fdef_values_2
            },
            3: {
                0: spd_values_0,
                1: spd_values_1,
                2: spd_values_2
            }
            
        }
                           
        for i, s_ind in enumerate(index_to_test):
            for j, a_ind in enumerate(indices_to_add):

                gear = Gear()
                gear.create_gear(gear_level = 90, mainstat_id=8, substat_ids=[1, 7, 5, 9], gear_type='ring')

                # Set enhance_level to +15 so we may reforge
                gear.enhance_level = 15
                gear.is_refoged = True

                # Enhance 5 substats, these should change their rolled value and reforge_increase value
                gear.substats[0].enhance_stat()
                gear.substats[0].enhance_stat()
                gear.substats[1].enhance_stat()
                gear.substats[2].enhance_stat()
                gear.substats[2].enhance_stat()
                           
                # Modify gear
                gear.modify_gear(s_ind+1, a_ind, mod_type='lesser')

                # Calculate expected value based on rolled count and substat index
                rolled_count = rolled_counts[i]
                expected_value_list = expected_values_dict[j][rolled_count]

                # Check if the actual modified value matches the expected value
                self.assertIn(gear.substats[s_ind].value, expected_value_list)
                self.assertTrue(gear.substats[s_ind].modded)   
                
                
    def test_mock_gear_3(self):
        """
        Test reforge on a mock Lv 90 gear with mainstat=8 (effectiveness) and substats=[0, 6, 4, 10].
        We'll enhance some of the values manually and set fixed values afterwards so that we can expect the modded value.
        In this test, we'll replace the stat with the same stat and check if we get appropriate value back.
        """
                
        index_to_test = [0, 1, 2, 3]
        rolled_counts = [2, 1, 2, 0]
        indices_to_add = [0, 6, 4, 10]
                    
        # Expected Values Stored in variables (lesser and index = 1 becaues lv 90 gear)
        atk_values_0 = STATS['0']['mod_vals']['lesser'][1][0]
        atk_values_1 = STATS['0']['mod_vals']['lesser'][1][1]
        atk_values_2 = STATS['0']['mod_vals']['lesser'][1][2]
        
        crit_values_0 = STATS['6']['mod_vals']['lesser'][1][0]
        crit_values_1 = STATS['6']['mod_vals']['lesser'][1][1]
        crit_values_2 = STATS['6']['mod_vals']['lesser'][1][2]
                           
        fdef_values_0 = STATS['4']['mod_vals']['lesser'][1][0]
        fdef_values_1 = STATS['4']['mod_vals']['lesser'][1][1]
        fdef_values_2 = STATS['4']['mod_vals']['lesser'][1][2]

        spd_values_0 = STATS['10']['mod_vals']['lesser'][1][0]
        spd_values_1 = STATS['10']['mod_vals']['lesser'][1][1]
        spd_values_2 = STATS['10']['mod_vals']['lesser'][1][2]

        expected_values_dict = {
            0: {
                0: atk_values_0,
                1: atk_values_1,
                2: atk_values_2
            },
            1: {
                0: crit_values_0,
                1: crit_values_1,
                2: crit_values_2
            },
            2: {
                0: fdef_values_0,
                1: fdef_values_1,
                2: fdef_values_2
            },
            3: {
                0: spd_values_0,
                1: spd_values_1,
                2: spd_values_2
            }
            
        }
                           
        for i, s_ind in enumerate(index_to_test):
                gear = Gear()
                gear.create_gear(gear_level = 90, mainstat_id=8, substat_ids=[0, 6, 4, 10], gear_type='ring')

                # Set enhance_level to +15 so we may reforge
                gear.enhance_level = 15
                gear.is_refoged = True

                # Enhance 5 substats, these should change their rolled value and reforge_increase value
                gear.substats[0].enhance_stat()
                gear.substats[0].enhance_stat()
                gear.substats[1].enhance_stat()
                gear.substats[2].enhance_stat()
                gear.substats[2].enhance_stat()
                           
                # Modify gear
                gear.modify_gear(s_ind+1, indices_to_add[i], mod_type='lesser')

                # Calculate expected value based on rolled count and substat index
                rolled_count = rolled_counts[i]
                expected_value_list = expected_values_dict[i][rolled_count]

                # Check if the actual modified value matches the expected value
                self.assertIn(gear.substats[s_ind].value, expected_value_list)
                self.assertTrue(gear.substats[s_ind].modded)     
                
                
    def test_mock_gear_modify_then_reforge(self):
        """
        Test reforge on a mock Lv 85 gear with mainstat=8 (effectiveness) and substats=[0, 6, 4, 10].
        We'll enhance some of the values manually and set fixed values afterwards so that we can expect the modded value.
        In this test, we'll replace the stat with the same stat and check if we get appropriate value back.
        Afterwards, we'll reforge the gear and see if we get a proper increase in the refroged value, even though it's modded.
        """
                
        index_to_test = [0, 1, 2, 3]
        rolled_counts = [2, 1, 2, 0]
        indices_to_add = [0, 6, 4, 10]
                    
        # Expected Values Stored in variables (lesser and index = 1 becaues lv 90 gear)
        atk_values_0 = STATS['0']['mod_vals']['lesser'][0][0]
        atk_values_1 = STATS['0']['mod_vals']['lesser'][0][1]
        atk_values_2 = STATS['0']['mod_vals']['lesser'][0][2]
        atk_ref_0 = STATS['0']['reforge']['substat'][0]
        atk_ref_1 = STATS['0']['reforge']['substat'][1]
        atk_ref_2 = STATS['0']['reforge']['substat'][2]

        crit_values_0 = STATS['6']['mod_vals']['lesser'][0][0]
        crit_values_1 = STATS['6']['mod_vals']['lesser'][0][1]
        crit_values_2 = STATS['6']['mod_vals']['lesser'][0][2]
        crit_ref_0 = STATS['6']['reforge']['substat'][0]
        crit_ref_1 = STATS['6']['reforge']['substat'][1]
        crit_ref_2 = STATS['6']['reforge']['substat'][2]
                           
        fdef_values_0 = STATS['4']['mod_vals']['lesser'][0][0]
        fdef_values_1 = STATS['4']['mod_vals']['lesser'][0][1]
        fdef_values_2 = STATS['4']['mod_vals']['lesser'][0][2]
        fdef_ref_0 = STATS['4']['reforge']['substat'][0]
        fdef_ref_1 = STATS['4']['reforge']['substat'][1]
        fdef_ref_2 = STATS['4']['reforge']['substat'][2]

        spd_values_0 = STATS['10']['mod_vals']['lesser'][0][0]
        spd_values_1 = STATS['10']['mod_vals']['lesser'][0][1]
        spd_values_2 = STATS['10']['mod_vals']['lesser'][0][2]
        spd_ref_0 = STATS['10']['reforge']['substat'][0]
        spd_ref_1 = STATS['10']['reforge']['substat'][1]
        spd_ref_2 = STATS['10']['reforge']['substat'][2]
        

        expected_values_dict = {
            0: {
                0: [(atk_ref_0 + a) for a in atk_values_0],
                1: [(atk_ref_1 + a) for a in atk_values_1],
                2: [(atk_ref_2 + a) for a in atk_values_2]
            },
            1: {
                0: [(crit_ref_0 + a) for a in crit_values_0],
                1: [(crit_ref_1 + a) for a in crit_values_1],
                2: [(crit_ref_2 + a) for a in crit_values_2]
            },
            2: {
                0: [(fdef_ref_0 + a) for a in fdef_values_0],
                1: [(fdef_ref_1 + a) for a in fdef_values_1],
                2: [(fdef_ref_2 + a) for a in fdef_values_2]
            },
            3: {
                0: [(spd_ref_0 + a) for a in spd_values_0],
                1: [(spd_ref_1 + a) for a in spd_values_1],
                2: [(spd_ref_2 + a) for a in spd_values_2]
            }
        }
                           
        for i, s_ind in enumerate(index_to_test):
                with self.subTest(ind_t = i, ind_a = indices_to_add[i]):
                    gear = Gear()
                    gear.create_gear(gear_level = 85, mainstat_id=8, substat_ids=[0, 6, 4, 10], gear_type='ring')

                    # Set enhance_level to +15 so we may reforge
                    gear.enhance_level = 15

                    # Enhance 5 substats, these should change their rolled value and reforge_increase value
                    gear.substats[0].enhance_stat()
                    gear.substats[0].enhance_stat()
                    gear.substats[1].enhance_stat()
                    gear.substats[2].enhance_stat()
                    gear.substats[2].enhance_stat()

                    # Modify gear
                    gear.modify_gear(s_ind+1, indices_to_add[i], mod_type='lesser')
                    gear.reforge_gear()

                    # Calculate expected value based on rolled count and substat index
                    rolled_count = rolled_counts[i]
                    expected_value_list = expected_values_dict[i][rolled_count]

                    # Check if the actual modified value matches the expected value
                    self.assertIn(gear.substats[s_ind].value, expected_value_list)
                    self.assertTrue(gear.substats[s_ind].modded)     


                
if __name__ == '__main__':
    unittest.main()