"""
Module name: Elevation MAIN

Description: Main script for processing elevation data and converting it to dimensions of sound.

In this case, elevation is converted to the pitch of a pulse, and the absolute gradient between each point is
converted to the rate of pulse occurance.

When run, the main() function prompts the user to select a KML file from which the elevation data and coordinates are
extracted. Optional parameters bypass the parts of the code which require user interaction, which is useful for performance testing.

Functions:
- main(): Main function to execute the script's functionality.

Author: George Caselton
Last updated: 18/08/2024
"""

from kml_processing import *
from geo_processing import *
from data_processing import *
from ANSI_formats import *

def main(kml_file_path=None, show_graph=True):
    """
    This main function can be called with parameters: data_file_path (string), which bypasses opening the dialog
    box for users to choose a file, and show_graph (boolean), which dictates whether a visual elevation profile is displayed.
    This is useful when doing performance testing.
    """

    # Prompt user to select KML file
    if kml_file_path is None:
        kml_file_path = select_kml_file()
    
    # Assess validity of file
    if kml_file_path:
        coordinates, parkrun_name = extract_data(kml_file_path)
        if coordinates:
            print(f"Successfully extracted {GREEN}{parkrun_name}{RESET}'s coordinates!")
        else:
            print(f"{error_msg} No valid data found in the KML file.")
            return
    else:
        print(f"{error_msg} No file selected.")
        return

    elevations = []

    # Add elevation points to a list
    for coords in coordinates:
        elevation = get_srtm_elevation(coords[0], coords[1])
        elevations.append(elevation)


    # Calculating the cumulative distance covered
    distances = [0.0]
    for i in range(1, len(coordinates)):
        coords1 = (coordinates[i-1][0], coordinates[i-1][1])
        coords2 = (coordinates[i][0], coordinates[i][1])
        distance = calculate_distance(coords1, coords2)
        distances.append(distances[-1] + distance)

    total_distance = distances[-1]

    print(f"Total distance covered: {total_distance:.4f} km")

    # Check if route is correct length, allowing for some deviation
    if (total_distance < 5*0.9 or total_distance > 5*1.1):
        print(f'{error_msg} route length is invalid, please re-run the program and select another KML file')
        return
    
    # Total race distance in metres
    race_distance = 5000

    # How many metres per data point
    resolution_in_m = 10

    # Number of data points
    n_data_points = int(race_distance / resolution_in_m)

    # Interpolate data
    distances, elevations = interpolate_data(distances, elevations, n_data_points)

    # Plot to see the data in line graph form
    if show_graph == True:
        plot_graph(distances, 'Distance (km)', elevations, 'Elevation (m)')
    
    # Setting minimums and maximums
    max_parkrun_elevation = 457
    min_parkrun_elevation = 0

    max_pitch = 880
    min_pitch = 110

    min_gradient = 0
    max_gradient = 5

    max_rate = 50
    min_rate = 250

    # Ignoring the polarity of the elevation change to get absolute gradients
    gradients = calculate_differences(elevations)
    abs_gradients = [abs(x) for x in gradients]

    rates = []
    pitches = []
    graph_data = []

    # Mapping data to sound dimensions
    for i in range(len(elevations)):

        rate = map_value(abs_gradients[i], min_gradient, max_gradient, min_rate, max_rate)
        rates.append(rate)

        pitch = map_value(elevations[i], min_parkrun_elevation, max_parkrun_elevation, min_pitch, max_pitch)
        pitches.append(pitch)

        normalised_data = map_value(elevations[i], min(elevations), max(elevations), 0, 1)
        graph_data.append(normalised_data)

    # Write the data to text files in the pd/inputs directory
    write_to_file(rates, 'rates')
    write_to_file(pitches, 'pitches')
    write_to_file(graph_data, 'graph_data')
    write_to_file(parkrun_name, 'parkrun_name')

    # Print success message
    print(f'{success_msg}\nOpen elevation_MAIN.pd to hear the result.')

if __name__ == '__main__':
    main()