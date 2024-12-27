"""
Module name: Pace MAIN

Description: Main script for processing pace data and converting it to BPM.

This script prompts the user to select a text file containing pace data, extract relevant information,
convert the paces to beats per minute (BPM), and save the results to text files. It uses functions from the `pace_processing`
module to perform the pace-to-BPM conversion and functions from the `data_processing` module to handle file writing.

Functions:
- main(): Main function to execute the script's functionality.

Author: George Caselton
Last updated: 13/08/2024
"""

import os
from pace_processing import *
from data_processing import write_to_file
from ANSI_formats import *

def main(data_file_path=None):
    """
    This main function can be called with a parameter, data_file_path (string), which bypasses opening the dialog
    box for users to choose a file. This is useful when doing performance testing.
    """
    
    # Open dialog box to select pace data
    if data_file_path is None:
        data_file_path = select_pace_file()

    # Prints error message and ends program if none selected
    if not data_file_path:
        print(f'{error_msg} No file selected.')
        return
    
    # Extract the root file name, removing the '.txt'
    file_name = os.path.basename(data_file_path)[:-4]

    # Extract data and print to console
    data_result = extract_data_from_file(data_file_path)

    # Check if any errors occurred during extraction
    if data_result is None:
        return
    else:
        gender, ability, age, paces = data_result
    
    print(f'Gender: {gender}\nAbility: {ability}\nAge: {age}\nPaces: {paces}')

    # Map to tempo and print to console
    tempos = pace_to_bpm(gender, ability, age, paces)
    print(f'Tempos: {tempos}')
        
    # Write the data to text files in the pd/inputs directory
    write_to_file(tempos, 'bpm')
    write_to_file(file_name, 'data_name')

    # Print success message
    print(f'{success_msg}\nOpen pace_MAIN.pd to hear the result.')

if __name__ == '__main__':
    main()