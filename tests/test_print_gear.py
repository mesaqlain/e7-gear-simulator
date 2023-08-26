from set_directory_function import set_directory
set_directory()

# Imports
import unittest
from unittest.mock import patch  
import json
import random
from src.gear import Gear 
from src.stats import Stat

class TestPrintGear(unittest.TestCase):
    """
    Test the print_gear() method to make sure we get desired outputs
    """
    
    def test_print_gear_rare(self):
        """Test whether we get expected output for rare gear"""
        
        gear = Gear()
        gear.create_gear(gear_grade='rare', gear_level=70, gear_type='weapon', gear_set='attack', 
                         substat_ids=['10', '8'])
        
        # Set some arbitrary values
        gear.mainstat.value = 300
        gear.substats[0].value = 4
        gear.substats[1].value = 7

        expected_output = (
            "---\n"
            "+0 Rare Weapon (Lv 70)\n"
            "Attack Set\n"
            "---\n"
            "MAIN STAT:\n"
            "300 Attack\n"
            "---\n"
            "SUBSTATS:\n"
            "4 (4) Speed\n"
            "7% (8%) Effectiveness\n"
        )
        print("Output from print_gear() method:")
        gear.print_gear()
        print("Output from expected_output:")
        print(expected_output)

        with patch('builtins.print') as mock_print:
            gear.print_gear()
            # Capture all calls to print in mock_print.call_args_list
            calls = [call[0][0] for call in mock_print.call_args_list]
            captured_output = '\n'.join(calls)  # Concatenate captured lines

            # Normalize the strings for comparison
            captured_output = captured_output.strip()  # Remove leading/trailing whitespace
            captured_output = captured_output.replace('\r\n', '\n')  # Normalize newline characters

            expected_output = expected_output.strip()  # Remove leading/trailing whitespace

            self.assertEqual(captured_output, expected_output)
            
            
    def test_print_gear_heroic(self):
        """
        Test whether we get expected output for heroic gear that has been reforged and have some 
        enhancement levels.
        """
        
        gear = Gear()
        gear.create_gear(gear_grade='heroic', gear_level=85, gear_type='necklace', gear_set='speed', 
                         mainstat_id=6, substat_ids=['1', '7', '10'])
        
        # Set some arbitrary values
        gear.mainstat.value = 30
        gear.substats[0].value = 20
        gear.substats[1].value = 34
        gear.substats[2].value = 8
        gear.is_reforged = True
        gear.enhance_level = 5


        expected_output = (
            "---\n"
            "+5 Heroic Necklace (Lv 85)\n"
            "Speed Set\n"
            "---\n"
            "MAIN STAT:\n"
            "30% Crit Chance\n"
            "---\n"
            "SUBSTATS:\n"
            "20% Attack\n"
            "34% Crit Damage\n"
            "8 Speed\n"
        )
        print("Output from print_gear() method:")
        gear.print_gear()
        print("Output from expected_output:")
        print(expected_output)

        with patch('builtins.print') as mock_print:
            gear.print_gear()
            # Capture all calls to print in mock_print.call_args_list
            calls = [call[0][0] for call in mock_print.call_args_list]
            captured_output = '\n'.join(calls)  # Concatenate captured lines

            # Normalize the strings for comparison
            captured_output = captured_output.strip()  # Remove leading/trailing whitespace
            captured_output = captured_output.replace('\r\n', '\n')  # Normalize newline characters

            expected_output = expected_output.strip()  # Remove leading/trailing whitespace

            self.assertEqual(captured_output, expected_output)     
            
            
    def test_print_gear_epic(self):
        """
        Test whether we get expected output for epic gear that has been reforged and have some 
        enhancement levels.
        """
        
        gear = Gear()
        gear.create_gear(gear_grade='epic', gear_level=90, gear_type='ring', gear_set='destruction', 
                         mainstat_id=9, substat_ids=['1', '7', '2', '0'])
        
        # Set some arbitrary values
        gear.mainstat.value = 300
        gear.substats[0].value = 20
        gear.substats[1].value = 34
        gear.substats[2].value = 8
        gear.substats[3].value = 8
        gear.is_reforged = True
        gear.enhance_level = 15


        expected_output = (
            "---\n"
            "+15 Epic Ring (Lv 90)\n"
            "Destruction Set\n"
            "---\n"
            "MAIN STAT:\n"
            "300% Effect Resistance\n"
            "---\n"
            "SUBSTATS:\n"
            "20% Attack\n"
            "34% Crit Damage\n"
            "8 Health\n"
            "8 Attack"
        )
        print("Output from print_gear() method:")
        gear.print_gear()
        print("Output from expected_output:")
        print(expected_output)

        with patch('builtins.print') as mock_print:
            gear.print_gear()
            # Capture all calls to print in mock_print.call_args_list
            calls = [call[0][0] for call in mock_print.call_args_list]
            captured_output = '\n'.join(calls)  # Concatenate captured lines

            # Normalize the strings for comparison
            captured_output = captured_output.strip()  # Remove leading/trailing whitespace
            captured_output = captured_output.replace('\r\n', '\n')  # Normalize newline characters

            expected_output = expected_output.strip()  # Remove leading/trailing whitespace

            self.assertEqual(captured_output, expected_output)              
        
        
if __name__ == '__main__':
    unittest.main()