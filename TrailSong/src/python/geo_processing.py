"""
Module name: Geo Processing

Description: Utility functions to retreive the elevation of the given coordinates and calculate the distance between two points.

Author: George Caselton
Last updated: 18/08/2024
"""

import srtm
from geopy.distance import geodesic

# Function to get elevation from SRTM data
def get_srtm_elevation(lat, lon):
    # Load SRTM data
    srtm_data = srtm.get_data()
    
    # Get elevation for the specified coordinates
    elevation = srtm_data.get_elevation(lat, lon)
    
    return elevation

# Function which calculates the distance between two sets of coordinates
def calculate_distance(coords1, coords2):
    return geodesic(coords1, coords2).kilometers
