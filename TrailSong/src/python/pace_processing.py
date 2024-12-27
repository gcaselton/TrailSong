"""
Module name: Pace Processing

Description: Module containing functions related to pace data processing.

Functions:
- pace_to_bpm(gender, ability, age, paces): Converts paces to BPM using linear transformation.
- ungendered_stats(ability, age): Computes average and world record paces by averaging male and female statistics.
- extract_data_from_file(file_path): Reads and extracts gender, ability, age, and paces from a specified file.
- select_pace_file(): Opens a file dialog for selecting a pace data file.

Author: George Caselton
Last updated: 13/08/2024

"""

import tkinter as tk
from tkinter import filedialog
from ANSI_formats import *
from global_pace_stats import average_5k_paces_by_age, world_record_5k_paces_by_age

def pace_to_bpm(gender, ability, age, paces):
    """
    Convert paces (measured in seconds per km) to beats per minute (BPM) for a given gender, ability level, and age.
    This function uses the linear equation y = mx + b to compare the user's pace to that of the average for their age/gender/ability.
    In this equation, y is the BPM, m is the gradient, x is the pace, and b is the y-intercept.

    :param gender (string): Gender of the runner ('M' for male, 'F' for female, 'O' for other).
    :param ability (string): Running ability level ('Beginner', 'Novice', 'Intermediate', 'Advanced', 'Elite').
    :param age (string): Age of the runner.
    :param paces (list): List of paces (in seconds per km) to convert to BPM.
    :return: List of BPM values corresponding to the input paces.
    """
    # Defining minimum and maximum ages of 10 and 90
    if int(age) < 10:
        age_key = '10'
    elif int(age) > 90:
        age_key = '90'
    else:
        # Your age group is the nearest multiple of 5 below your age
        age_key = str(int(age) - int(age) % 5)

    average_pace = 0
    world_record_pace = 0

    # Use ungendered statistics if gender is 'O', otherwise use gender-specific data
    if gender == 'O':
        average_pace, world_record_pace = ungendered_stats(ability, age_key)
    else:
        gender_key = 'Men' if gender == 'M' else 'Women'
        average_pace = average_5k_paces_by_age[gender_key][age_key][ability]
        world_record_pace = world_record_5k_paces_by_age[gender_key][age_key]
    
    # Define average and maximum BPM values
    average_bpm = 125
    maximum_bpm = 200

    # Calculate the slope (m) and intercept (b) for the linear equation y = mx + b
    m = (maximum_bpm - average_bpm) / (world_record_pace - average_pace)
    b = average_bpm - (m * average_pace)

    # Compute BPM values for each pace
    tempos = [(m * pace) + b for pace in paces]
    
    return tempos

def ungendered_stats(ability, age):
    """
    This function averages the male and female times to give ungendered stats for average 5k pace and world record 5k pace.

    :param ability (string): Running ability level ('Beginner', 'Novice', 'Intermediate', 'Advanced', 'Elite').
    :param age (string): Age of the runner.
    :return: A tuple containing the average pace and world record pace for both genders combined.
    """
    # Retrieve male and female average paces and world record paces.
    male_avg = average_5k_paces_by_age['Men'][age][ability]
    male_WR = world_record_5k_paces_by_age['Men'][age]
    female_avg = average_5k_paces_by_age['Women'][age][ability]
    female_WR = world_record_5k_paces_by_age['Women'][age]

    # Calculate the ungendered average and world record paces.
    ungendered_avg = (male_avg + female_avg) / 2
    ungendered_WR = (male_WR + female_WR) / 2

    return ungendered_avg, ungendered_WR

def extract_data_from_file(file_path):
    """
    Extract gender, ability, age, and paces from a text file.

    :param file_path (string): Path to the text file containing pace data.
    :return: A tuple containing gender, ability, age, and a list of paces, or None if the file is invalid.
    """
    try:
        # Attempt to read the file
        with open(file_path, 'r') as f:
            user_data = f.read()
    except Exception as e:
        print(f'{error_msg} {e}')
        return None


    data = user_data.split()

    # Check if the file contains enough data
    if len(data) < 8:
        print(f'{error_msg} Incomplete data in file')
        return None

    # Extract the data fields
    age = data[0]
    ability = data[1]
    gender = data[2]
    
    # Validate them, or print error messages
    if not age.isdigit():
        print(f'{error_msg} Invalid age format: {age}')
    elif gender not in {'M', 'F', 'O'}:
        print(f'{error_msg} Invalid gender format: {gender}')
    elif ability not in average_5k_paces_by_age['Men']['10'].keys():
        print(f'{error_msg} Invalid ability level: {ability}')
    
    # Convert pace times from 'mins:secs' format to seconds
    paces = []
    for pace in data[3:]:
        try:
            mins, secs = pace.split(':')
            pace_in_secs = int(mins) * 60 + int(secs)
            paces.append(pace_in_secs)
        except ValueError:
            print(f'{error_msg} Invalid pace format: {pace}')
            return None

    return gender, ability, age, paces

def select_pace_file():

    root = tk.Tk()
    root.withdraw() 

    # Open a file dialog to prompt the user to select the pace data file
    return filedialog.askopenfilename(title='Select pace data file', filetypes=[('Text files', '*.txt')])
