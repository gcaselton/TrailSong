# TrailSong

## Overview

TrailSong is a prototype software which uses data sonification to transform running data into sounds and music.
The system is run using a combination of Python modules and Pure Data (PD) patches, and is split into 2 main functions:

1. Turn a 5km Parkrun route into an 'audible elevation profile', allowing users to hear the topography of the run.
2. Use users' pace data to generate short musical compositions which characterise the user's run.

Instructions on using both functions can be found in the *Usage* section of this document.

## Installation

It is recommended that the Python side of the project be run from inside an IDE (such as VS Code), as the terminal outputs make use of ANSI escape codes for formatting, which can be temperamental in the Windows command line.

1. In order to run the system, both [Python](https://www.python.org/downloads/) and [Pure Data](https://puredata.info/downloads/pure-data) (vanilla) will need to be installed. This project was built and tested on Pure Data version 0.55.0 and Python version 3.12.5.
2. Navigate to the root directory of the project (`trailsong/`)
3. To install the required dependencies, run the following command: `pip install -r requirements.txt`

You are now ready to run the system.

## Usage
### Downloading KML files
---
For the elevation sonification, you will be asked to select a KML file, which is the running route you wish to sonify. Some examples are included in this package in the `example_data/elevation/` folder, but you can also download one of your choice from the [Parkrun website](https://www.parkrun.org.uk/events/events/#geo=2.42/51.55/3.2) by following these instructions:

1. Choose a Parkrun event from the map
2. At the top of the page, click on 'course'
3. On the route map, click on the share icon, then 'Embed on my site'
4. Click the three dots on the red banner, then 'Download KML'
5. Make sure to tick the 'Export as KML instead of KMZ' option
6. Click 'OK' to complete the download

### Elevation Sonification
---
To use this part of the system, run the `elevation_MAIN.py` script. 

It will prompt you to select a KML file from your directory, which is the running route you wish to sonify. Some routes are currently incompatible with the software as their lengths are calculated as something other than 5km. If this is the case, you will be asked to re-run the program and select another KML file.

Upon successfully extracting the data, a line graph will display the elevation profile. **You will need to close this window in order for the rest of the program to execute.**

The sonified data will be sent to PD.

In PD, open `elevation_MAIN.pd`. The name of the chosen Parkrun should be displayed below the graph.

Click the 'PLAY' button to start/stop the sonified elevation profile, or click the 'RECORD' button to select a destination and file name for the audio recorder to write a WAV file to.

In this sonification, the pitch of the pulses corresponds to the elevation (higher pitch = higher elevation) and the rate of pulse occurrance corresponds to the steepness of the gradient. You will hear a chord play every time a kilometre is passed, and the number of times the chord is played corresponds to the kilometre passed.

Feel free to click on any of the sub-patches to explore the mechanics of the system. If you would like more information on any of the objects in PD, right-click on one and select 'help'.

### Pace Sonification
---
For this feature, you can eiter create your own data file to use, or use one of the examples in `example_data/pace/`.

If creating your own, you will need to create a text file containing the age, ability level, gender, and 5k pace times for the runner.
The ability level must be one of the following: Beginner, Novice, Intermediate, Advanced, Elite. Gender must be either 'M', 'F', or 'O' for other, should you wish to skip the gendered categorisation. The split pace times must be in minutes per km, and each data field should be on a new line, as in the example below. The order of the data fields matters, so please follow this format:

28\
Novice\
M\
4:58\
5:02\
5:10\
5:03\
5:07

Run `pace_MAIN.py` and select the text file of data you wish to sonify.

If it's valid, the sonified data will be sent to PD.

In PD, open `pace_MAIN.pd`. Similarly to the elevation sonification, you have the option to play or record the composition.

In this sonification, the pace correlates to the tempo (faster pace = faster tempo) and the rest of the musical elements are randomly generated.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

For further details or questions, please contact George Caselton at g.caselton2@newcastle.ac.uk.
