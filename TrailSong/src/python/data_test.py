"""
Module name: Data Test

Description: Unit tests for the `data_processing` module.

Tests include:
- `test_interpolate_data`: Checks that the interpolation method works as expected.
- `test_map_value`: Tests that values are being accurately mapped.
- 'test_calculate_differences': Checks that the function correctly calculates the difference between 2 points.

Author: George Caselton
Last updated: 13/08/2024

Test status as of 18/08/2024: PASS

"""

import unittest
import numpy as np
from data_processing import interpolate_data, map_value, calculate_differences
class TestDataProcessing(unittest.TestCase):
    
    def test_interpolate_data(self):

        # Test the `interpolate_data` function to ensure it correctly interpolates data points.
        
        x_data = [1, 2, 3]
        y_data = [2, 4, 6]
        n_data_points = 5
        
        interpolated_x_data, interpolated_y_data = interpolate_data(x_data, y_data, n_data_points)
        
        # Expected results
        expected_x = np.linspace(1, 3, num=5)
        expected_y = np.array([2, 3, 4, 5, 6])
        
        np.testing.assert_array_almost_equal(interpolated_x_data, expected_x)
        np.testing.assert_array_almost_equal(interpolated_y_data, expected_y)
    
    def test_map_value(self):
        
        # Test the `map_value` function to verify correct value mapping.
       
        value = 5
        min_value = 0
        max_value = 10
        min_result = 0
        max_result = 100
        
        result = map_value(value, min_value, max_value, min_result, max_result)
        
        self.assertEqual(result, 50.0)  # 5 mapped from 0-10 to 0-100

    def test_calculate_differences(self):
    
        # Test the `calculate_differences` function to ensure it calculates differences correctly.
        
        data = [10, 20, 30, 40]
        expected_differences = [0, 10, 10, 10]
        
        differences = calculate_differences(data)
        
        self.assertEqual(differences, expected_differences)

if __name__ == '__main__':
    unittest.main()
