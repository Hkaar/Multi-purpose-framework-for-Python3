from DCMS_framework import *

# DCMS a front-end for the DCMS_framework #
# Made by Hkaar #

# Variables & Lists
## System variables
version = 0.0134
last_date = (2021, 2, 19, 14, 30, 5, 4, 362, 0)

## String variables
dcms_help = f"""
DCMS terminal- version {version}, a front-end for the DCMS framework
-version {framewrk_version} executing commands within the list. NOTE! some
packages are modify for extra use and some are added but generally
not steering away from the framework.

Some sample commands are:
-] clear                -] pause
-] delay                -] time ..(type)
"""

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
	framewrk_run(dcms_plus, 'DCMS', 'white')