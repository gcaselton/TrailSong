"""
Module Name: Global Pace Stats

Description: This python file is purely designed to hold the stats which are required to calibrate the 
pace to bpm conversion happening in pace_processing.py. There are two nested dictionaries: the first contains the average 5k paces (in seconds)
for each age group and gender. The second contains the world record 5k paces (in seconds) for each age group and gender.
The data was acquired at: https://runninglevel.com/running-times/5k-times

Author: George Caselton
Last Updated: 29/07/24
"""


# The average pace per km of a 5k run for each age group. The pace is in seconds.
average_5k_paces_by_age = {
    'Men': {
        '10': {'Beginner': 452, 'Novice': 378, 'Intermediate': 323, 'Advanced': 283, 'Elite': 253},
        '15': {'Beginner': 391, 'Novice': 327, 'Intermediate': 280, 'Advanced': 245, 'Elite': 219},
        '20': {'Beginner': 378, 'Novice': 316, 'Intermediate': 270, 'Advanced': 237, 'Elite': 212},
        '25': {'Beginner': 378, 'Novice': 316, 'Intermediate': 270, 'Advanced': 237, 'Elite': 212},
        '30': {'Beginner': 378, 'Novice': 316, 'Intermediate': 270, 'Advanced': 237, 'Elite': 212},
        '35': {'Beginner': 384, 'Novice': 321, 'Intermediate': 275, 'Advanced': 241, 'Elite': 215},
        '40': {'Beginner': 398, 'Novice': 333, 'Intermediate': 285, 'Advanced': 249, 'Elite': 223},
        '45': {'Beginner': 413, 'Novice': 345, 'Intermediate': 296, 'Advanced': 259, 'Elite': 232},
        '50': {'Beginner': 429, 'Novice': 359, 'Intermediate': 307, 'Advanced': 269, 'Elite': 241},
        '55': {'Beginner': 447, 'Novice': 374, 'Intermediate': 320, 'Advanced': 280, 'Elite': 251},
        '60': {'Beginner': 467, 'Novice': 390, 'Intermediate': 334, 'Advanced': 292, 'Elite': 262},
        '65': {'Beginner': 488, 'Novice': 408, 'Intermediate': 349, 'Advanced': 306, 'Elite': 274},
        '70': {'Beginner': 513, 'Novice': 429, 'Intermediate': 367, 'Advanced': 321, 'Elite': 288},
        '75': {'Beginner': 551, 'Novice': 461, 'Intermediate': 394, 'Advanced': 345, 'Elite': 309},
        '80': {'Beginner': 610, 'Novice': 510, 'Intermediate': 436, 'Advanced': 382, 'Elite': 342},
        '85': {'Beginner': 702, 'Novice': 587, 'Intermediate': 502, 'Advanced': 440, 'Elite': 394},
        '90': {'Beginner': 854, 'Novice': 714, 'Intermediate': 611, 'Advanced': 535, 'Elite': 479}
    },
    'Women': {
        '10': {'Beginner': 498, 'Novice': 423, 'Intermediate': 367, 'Advanced': 324, 'Elite': 292},
        '15': {'Beginner': 447, 'Novice': 380, 'Intermediate': 329, 'Advanced': 291, 'Elite': 262},
        '20': {'Beginner': 425, 'Novice': 362, 'Intermediate': 313, 'Advanced': 277, 'Elite': 249},
        '25': {'Beginner': 425, 'Novice': 362, 'Intermediate': 313, 'Advanced': 277, 'Elite': 249},
        '30': {'Beginner': 425, 'Novice': 362, 'Intermediate': 313, 'Advanced': 277, 'Elite': 249},
        '35': {'Beginner': 428, 'Novice': 364, 'Intermediate': 315, 'Advanced': 279, 'Elite': 251},
        '40': {'Beginner': 437, 'Novice': 372, 'Intermediate': 322, 'Advanced': 284, 'Elite': 256},
        '45': {'Beginner': 453, 'Novice': 385, 'Intermediate': 333, 'Advanced': 295, 'Elite': 265},
        '50': {'Beginner': 476, 'Novice': 405, 'Intermediate': 351, 'Advanced': 310, 'Elite': 279},
        '55': {'Beginner': 503, 'Novice': 428, 'Intermediate': 371, 'Advanced': 328, 'Elite': 295},
        '60': {'Beginner': 534, 'Novice': 454, 'Intermediate': 393, 'Advanced': 348, 'Elite': 313},
        '65': {'Beginner': 569, 'Novice': 484, 'Intermediate': 419, 'Advanced': 370, 'Elite': 334},
        '70': {'Beginner': 608, 'Novice': 517, 'Intermediate': 448, 'Advanced': 396, 'Elite': 357},
        '75': {'Beginner': 653, 'Novice': 556, 'Intermediate': 481, 'Advanced': 425, 'Elite': 383},
        '80': {'Beginner': 707, 'Novice': 601, 'Intermediate': 521, 'Advanced': 460, 'Elite': 415},
        '85': {'Beginner': 796, 'Novice': 677, 'Intermediate': 587, 'Advanced': 518, 'Elite': 467},
        '90': {'Beginner': 960, 'Novice': 816, 'Intermediate': 707, 'Advanced': 625, 'Elite': 563}
    }
}

# The world record 5k paces per km by age, pace is in seconds.
world_record_5k_paces_by_age = {
    'Men': {
        '10': 184,
        '15': 160,
        '20': 154,
        '25': 154,
        '30': 154,
        '35': 157,
        '40': 162,
        '45': 169,
        '50': 175,
        '55': 183,
        '60': 190,
        '65': 199,
        '70': 209,
        '75': 225,
        '80': 249,
        '85': 286,
        '90': 348
    },
    'Women': {
        '10': 207,
        '15': 186,
        '20': 177,
        '25': 177,
        '30': 177,
        '35': 178,
        '40': 182,
        '45': 188,
        '50': 198,
        '55': 209,
        '60': 222,
        '65': 236,
        '70': 253,
        '75': 272,
        '80': 294,
        '85': 331,
        '90': 399
    }
}