"""
Module name: Performance Tests

Description: Performance tests for the elevation_MAIN and pace_MAIN scripts.

Tests include:
- Timing each of the main functions (excluding user input as this cannot be timed).
- Iterating through each script 10 times and averaging the elapsed time.

Author: George Caselton
Last updated: 13/08/2024

Test status as of 18/08/2024: PASS
Details: 
- Average time elapsed during elevation_MAIN: 1.5971 seconds
- Average time elapsed during pace_MAIN: 0.0012 seconds

"""

import timeit
from elevation_MAIN import main as elev_main
from pace_MAIN import main as pace_main

# Example file paths for testing
example_kml = 'src/example_data/elevation/Tawd Valley parkrun.kml'
example_pace_data = 'src/example_data/pace/example_1.txt'

def elev_wrapper():
    """
    Wrapper function to call elev_main with args that disable user input.
    """
    elev_main(kml_file_path=example_kml, show_graph=False)

def pace_wrapper():
    """
    Wrapper function to call pace_main with args that disable user input.
    """
    pace_main(data_file_path=example_pace_data)

def performance_test(wrapper_function):
    """
    Measure and print the average processing time of the provided wrapper function.

    :param wrapper_function: Callable function to be timed.
    """
    # Time the function execution over 10 iterations
    total_time = timeit.timeit(wrapper_function, number=10)
    
    # Calculate average time per call
    avg_processing_time = total_time / 10
    
    # Print results
    print(f'Average time elapsed during {wrapper_function.__name__}: {avg_processing_time:.4f} seconds')


if __name__ == '__main__':
    # Run performance tests for both scripts
    performance_test(pace_wrapper)
    performance_test(elev_wrapper)
