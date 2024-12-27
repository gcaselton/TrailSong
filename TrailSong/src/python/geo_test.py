"""
Module name: Geo Test

Description: Unit tests for the `geo_processing` module.

Tests include:
- `get_srtm_elevation`: Verifies elevation retrieval from mocked SRTM data.
- `calculate_distance`: Checks distance calculation between two coordinates.

Tests use `unittest` and `unittest.mock` to isolate functionality.

Author: George Caselton
Last updated: 13/08/2024

Test status as of 18/08/2024: PASS

"""

import unittest
from unittest.mock import MagicMock, patch
from geo_processing import get_srtm_elevation, calculate_distance

class TestGeoProcessing(unittest.TestCase):
    
    @patch('srtm.get_data')
    def test_get_srtm_elevation(self, mock_get_data):
        # Creating a mock object for srtm_data
        mock_srtm_data = MagicMock()
        mock_get_data.return_value = mock_srtm_data
        
        # Test the get_elevation function on the known elevation of Mount Everest's peak
        known_elevation = 8848.0
        mock_srtm_data.get_elevation.return_value = known_elevation
        
        lat, lon = 27.9881, 86.9250 # Everest's coordinates
        elevation = get_srtm_elevation(lat, lon)
        
        # Assertions
        mock_get_data.assert_called_once()
        mock_srtm_data.get_elevation.assert_called_once_with(lat, lon)
        self.assertAlmostEqual(elevation, known_elevation, delta=5.0) # Delta allows some deviation

    def test_calculate_distance(self):

        # Test coordinates of London and Paris
        coords1 = (51.5074, -0.1278)  # London
        coords2 = (48.8566, 2.3522)   # Paris
        
        # Calculate distance
        distance = calculate_distance(coords1, coords2)
        
        # Known distance between London and Paris
        expected_distance = 343.0
        self.assertAlmostEqual(distance, expected_distance, delta=5.0)  # Allowing some deviation

if __name__ == '__main__':
    unittest.main()
