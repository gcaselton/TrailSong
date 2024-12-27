"""
Module name: KML Test

Description: Unit tests for the `kml_processing` module.

Tests include:
- `test_extract_data`: Verifies that the extraction of coordinates and names from a KML file works correctly.
- `test_select_kml_file`: Tests the file selection dialog to ensure it returns the expected file path.

Author: George Caselton
Last updated: 13/08/2024

Test status as of 18/08/2024: PASS
"""

import unittest
from unittest.mock import patch, MagicMock
from kml_processing import extract_data, select_kml_file

class TestKMLProcessing(unittest.TestCase):

    @patch('lxml.etree.parse')
    def test_extract_data(self, mock_parse):
        # Define mock XML structure
        mock_root = MagicMock()
        mock_tree = MagicMock()
        mock_parse.return_value = mock_tree
        mock_tree.getroot.return_value = mock_root
        
        # Define namespaces and mock XPath returns
        namespaces = {'kml': 'http://www.opengis.net/kml/2.2'}
        
        # Mock coordinates and name
        mock_coordinates_elem = MagicMock()
        mock_coordinates_elem.text = "30.0,10.0,0 31.0,11.0,0"
        mock_name_elem = MagicMock()
        mock_name_elem.text = "Parkrun"

        # Setup mock xpath return values
        mock_root.xpath.side_effect = lambda path, namespaces: [mock_coordinates_elem] if 'coordinates' in path else [mock_name_elem]
        
        # Call the function
        coords, name = extract_data('fake_path.kml')
        
        # Assertions
        expected_coords = [(10.0, 30.0), (11.0, 31.0)]
        self.assertEqual(coords, expected_coords)
        self.assertEqual(name, "Parkrun")
        
        mock_parse.assert_called_once_with('fake_path.kml')
        mock_root.xpath.assert_any_call('//kml:coordinates', namespaces=namespaces)
        mock_root.xpath.assert_any_call('//kml:name', namespaces=namespaces)

    @patch('tkinter.filedialog.askopenfilename')
    @patch('tkinter.Tk')
    def test_select_kml_file(self, mock_tk, mock_askopenfilename):
        # Mock the file dialog to return a test file path
        mock_askopenfilename.return_value = 'test.kml'
        mock_tk.return_value.withdraw = MagicMock()
        
        # Call the function
        file_path = select_kml_file()
        
        # Assertions
        self.assertEqual(file_path, 'test.kml')
        mock_askopenfilename.assert_called_once_with(title="Select a KML File", filetypes=[("KML files", "*.kml")])
        mock_tk.assert_called_once()

if __name__ == '__main__':
    unittest.main()
