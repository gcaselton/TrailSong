"""
Module name: ANSI Formats

Description: This file contains ANSI escape codes to format text output to the console.

Author: George Caselton
Last updated: 18/08/2024
"""
# ANSI codes for console output colours
BOLD_RED = '\033[31;1m'
GREEN = '\033[32m'
RESET = '\033[0m'

error_msg = f'{BOLD_RED}Error:{RESET}'

success_msg = f'{GREEN}Sonified data successfully sent to Pure Data!{RESET}'
