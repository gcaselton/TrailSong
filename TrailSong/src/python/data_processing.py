"""
Module name: Data Processing

Description: A collection of utility functions for data processing, interpolation, and file handling.

Functions:
    - interpolate_data(x_data, y_data, n_data_points): Interpolates data to create a denser dataset.
    - plot_graph(x_data, x_label, y_data, y_label): Plots a scatter and line graph of the data.
    - map_value(value, min_value, max_value, min_result, max_result): Maps a value from one range to another.
    - calculate_differences(data): Computes the differences between consecutive values in a list.
    - write_to_file(data, file_name): Writes formatted data to a file for use in Pure Data.

Author: George Caselton
Last updated: 18/08/2024
"""

import matplotlib.pylab as plt
import numpy as np
import os
from scipy.interpolate import interp1d

def interpolate_data(x_data, y_data, n_data_points):
    """
    Interpolates the given data to create a densified dataset.

    Args:
        x_data (list or np.ndarray): The x-coordinates of the original data points.
        y_data (list or np.ndarray): The y-coordinates of the original data points.
        n_data_points (int): The number of data points to generate in the interpolated dataset.

    Returns:
        tuple: Two numpy ndarrays containing the interpolated x and y data points.
    """
    # Ensure x_data and y_data are numpy arrays
    x_data = np.array(x_data)
    y_data = np.array(y_data)

    # Create an interpolation function using linear interpolation
    interp_func = interp1d(x_data, y_data, kind='linear')

    # Generate interpolated x data points
    interpolated_x_data = np.linspace(min(x_data), max(x_data), num=n_data_points)

    # Apply interpolation function to get interpolated y data points
    interpolated_y_data = interp_func(interpolated_x_data)

    return interpolated_x_data, interpolated_y_data

def plot_graph(x_data, x_label, y_data, y_label):
    """
    Plots a graph of the data. 
    The displayed graph must be exited for any further code to run.

    Args:
        x_data (list or np.ndarray): The x-coordinates of the data points.
        y_data (list or np.ndarray): The y-coordinates of the data points.
        x_label (str): The label for the x-axis.
        y_label (str): The label for the y-axis.
    """
    plt.scatter(x_data, y_data)  # Scatter plot of the data points
    plt.plot(x_data, y_data, linestyle='-', color='blue')  # Line plot of the data
    plt.xlabel(x_label)  # Set x-axis label
    plt.ylabel(y_label)  # Set y-axis label
    plt.show()  # Display the plot

def map_value(value, min_value, max_value, min_result, max_result):
    """
    Maps a value from one range to another.

    Args:
        value (float): The value to be mapped.
        min_value (float): The minimum value of the input range.
        max_value (float): The maximum value of the input range.
        min_result (float): The minimum value of the output range.
        max_result (float): The maximum value of the output range.

    Returns:
        float: The mapped value in the output range.
    """
    # Clip value to be within min and max input values
    if value > max_value:
        value = max_value
    elif value < min_value:
        value = min_value

    # Calculate the mapped value
    result = min_result + (value - min_value) / (max_value - min_value) * (max_result - min_result)
    return result

def calculate_differences(data):
    """
    Calculate the differences between consecutive values in a list.

    Parameters:
    data (list): A list of numerical values.

    Returns:
    list: A list of differences between consecutive values in the input data.
    """
    
    differences = []

    differences.append(0) # First value will be 0 to align in with the input list

    for i in range(1, len(data)):
        difference = data[i] - data[i-1]
        differences.append(difference)

    return differences

def write_to_file(data, file_name):
    """
    Writes data to a text file, formatted for use with Pure Data (Pd).

    Args:
        data (list or str): The data to be written to the file. If it's a list, each item is written on a new line.
        file_name (str): The name of the file to be created (without extension).

    Notes:
        If `data` is a list, each entry is written with a prefix '0', the file_name, and a semicolon to indicate the end of the message.
    """
    # Define the output directory and file path
    output_dir = '../pd/inputs'
    this_dir = os.path.dirname(__file__)
    file_path = os.path.join(this_dir, output_dir, f'{file_name}.txt')

    # Write data to the file
    with open(file_path, 'w') as f:
        if isinstance(data, list):
            for datum in data:
                # Write each data point to a new line with the required format for Pd
                f.write(f'0 {file_name} {datum};\n')
        else:
            # Write single data entry if data is not a list
            f.write(data)
