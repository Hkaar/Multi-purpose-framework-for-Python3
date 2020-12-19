from DCMS_framework import *

# DCMS a front-end for the DCMS_framework #
# Made by Hkaar #

# Variables & Lists
## System variables
version = 0.0125
last_date = (2020, 12, 13, 12, 30, 5, 4, 362, 0)

## String variables
dcms_help = ("""
DCMS terminal front-end for the DCMS framework for executing
commands contain within a certain list that are defined by
default. Some commands here are custom and are only for this
terminal to show specific information.

Some sample commands are:
-] clear       -] delay
-] pause      
""")

# Functions
## System functions
def help_dcms():
	print(dcms_help)

def ver_dcms():
	print("Current terminal version: " + str(version))
	print("Current terminal release date:", time.asctime(last_date))
	print("Current framework version: " + str(framewrk_version))
	print("Current framework release date:", time.asctime(framewrk_last_date))

## Embeded application functions
def gen_num():
	min_num_range = int(input("Minimum number: "))
	max_num_range = int(input("Maximum number: "))

	gen_num = random.randint(min_num_range, max_num_range)
	print("The generated number was:", gen_num)

# Dictionaries
dcms_plus = {
	'help': help_dcms,
	'framewrk -ver': ver_dcms,
	'generate -num': gen_num,
}

# Main 
if __name__ == "__main__":
	del_key(command_dict, 'framewrk -ver')
	run(dcms_plus, 'system', 'white')