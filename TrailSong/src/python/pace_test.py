"""
Module name: Pace Test

Description: Unit tests for the `pace_processing` module.

Tests include:
- `test_pace_to_bpm`: Validates that the function correctly converts paces to BPM using mocked average and world record paces.
- `test_extract_data_from_file`: Ensures that the function correctly parses data from a mock file.
- `test_select_pace_file`: Verifies that the file selection dialog works as expected and returns the correct file path.

Author: George Caselton
Last updated: 13/08/2024

Test status as of 18/08/2024: PASS

"""

import unittest
from unittest.mock import patch, mock_open
from pace_processing import pace_to_bpm, extract_data_from_file, select_pace_file
from global_pace_stats import average_5k_paces_by_age, world_record_5k_paces_by_age

class TestPaceProcessing(unittest.TestCase):

    def test_pace_to_bpm(self):

        # Mock data
        gender = 'M'
        gender_key = 'Men'
        ability = 'Beginner'
        age = '20'
        paces = [300, 250, 200, 210, 220]

        # Calculate expected BPM values
        average_bpm = 125
        maximum_bpm = 200
        average_pace = average_5k_paces_by_age[gender_key][age][ability]
        world_record_pace = world_record_5k_paces_by_age[gender_key][age]

        m = (maximum_bpm - average_bpm) / (world_record_pace - average_pace)
        b = average_bpm - (m * average_pace)

        expected_bpm = [(m * pace) + b for pace in paces]

        # Test the function
        result_bpm = pace_to_bpm(gender, ability, age, paces)

        # Assert the results
        for r, e in zip(result_bpm, expected_bpm):
            self.assertAlmostEqual(r, e, delta=0.1)

    @patch('builtins.open', new_callable=mock_open, read_data='30 Beginner M 5:00 4:30 4:00 4:30 5:00')
    def test_extract_data_from_file(self, mock_file):
        # Expected data
        expected_gender = 'M'
        expected_ability = 'Beginner'
        expected_age = '30'
        expected_paces = [300, 270, 240, 270, 300]

        # Test the function
        gender, ability, age, paces = extract_data_from_file('dummy_path.txt')

        # Assert the results
        self.assertEqual(gender, expected_gender)
        self.assertEqual(ability, expected_ability)
        self.assertEqual(age, expected_age)
        self.assertEqual(paces, expected_paces)

    @patch('tkinter.filedialog.askopenfilename', return_value='dummy_path.txt')
    @patch('tkinter.Tk')
    def test_select_pace_file(self, mock_tk, mock_askopenfilename):
        # Test the file dialog
        file_path = select_pace_file()
        
        # Assert the file path is correct
        self.assertEqual(file_path, 'dummy_path.txt')
        mock_askopenfilename.assert_called_once_with(title="Select pace data file", filetypes=[("Text files", "*.txt")])

if __name__ == '__main__':
    unittest.main()
