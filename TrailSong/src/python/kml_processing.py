"""
Module name: KML Processing

Description: Utility functions to open a dialog box and then extract coordinates from a KML file.

Author: George Caselton
Last updated: 18/08/2024
"""


from lxml import etree
import tkinter as tk
from ANSI_formats import *
from tkinter import filedialog

def extract_data(kml_file_path):
    """
    Extract coordinates and name from a KML file.
    
    :param kml_file_path: Path to the KML file
    :return: A tuple containing a list of coordinates and the name
    """
    try:
        # Parse the KML file
        tree = etree.parse(kml_file_path)
        root = tree.getroot()

        # Define namespaces
        namespaces = {
            'kml': 'http://www.opengis.net/kml/2.2'
        }

        coordinates = []

        # Find all <coordinates> elements
        for coord_elem in root.xpath('//kml:coordinates', namespaces=namespaces):
            coords_text = coord_elem.text.strip()
            for coord in coords_text.split():
                try:
                    # Ignore elevation points in the KML (these are sometimes 0)
                    lon, lat, _ = map(float, coord.split(','))
                    coordinates.append((lat, lon))
                except ValueError:
                    # Handle the case where conversion to float fails
                    continue

        parkrun_name = None

        # Find the <name> element
        name_elem = root.xpath('//kml:name', namespaces=namespaces)
        if name_elem:
            parkrun_name = name_elem[0].text.strip()

        return coordinates, parkrun_name

    except Exception as e:
        print(f'{error_msg} {e}')
        return [], None


def select_kml_file():
    """
    Open a file dialog to select a KML file and return its path.
    
    :return: Path to the selected KML file
    """
    root = tk.Tk()
    root.withdraw() 

    # Open dialog box to prompt user for KML file
    return filedialog.askopenfilename(title="Select a KML File", filetypes=[("KML files", "*.kml")])  

