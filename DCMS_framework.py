from tqdm import tqdm
import math
import random
import time
import os
import sys

# DCMS framework #
# Made by Hkaar #

# Variables and lists
## System variables
default_system_name = 'system' 
default_color_scheme = "\033[1;37;48m"
default_error_message = 'Error 404! command/function is not defined command list!'

run = False
framewrk_version = 0.0223
framewrk_last_date = (2020, 12, 15, 22, 50, 4, 4, 362, 0)

## Command & addtional variables
utc_result = time.struct_time(time.gmtime())

## String variables
letters = "abcdefghijklmn opqrstuvwxyz_ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
encrypted_str = ''
decrypted_str = ''

## Color Variables
Red_Text = "\033[1;31;48m"
Blue_Text = "\033[1;34;48m"
Yellow_Text = "\033[1;33;48m"
White_Text = "\033[1;37;48m"
Green_Text = "\033[1;32;48m"
Cyan_Text = "\033[1;36;48m"
Purple_Text = "\033[1;35;48m"

# Functions
## Basic functions
def time_delay(seconds):
	time.sleep(float(seconds))

def countdown(seconds, text):
	while seconds:
		mins, secs = divmod(seconds, 60)
		timer = '{:02d}:{:02d}'.format(mins, secs)
		print(timer, end="\r")
		time_delay(1)
		seconds -= 1

	print(text)

def load_bar(seconds, text):
	for i in tqdm(range(0, 100), desc=text):
		time_delay(seconds)

def slowprint(s):
  for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(1./10)

## Additional functions
def del_key(dictionary, key):
	dictionary.pop(key, None)

def append_key(dictionary, key, value):
	dictionary[key] = value

def cipher(message, key):
	global encrypted_str
	encrypted_str = ''

	if key > 22:
		min_num = key - 22
		key -= min_num

	if key < -4:
		plus_num = key + 4
		key -= plus_num

	for chars in message:
		if chars in letters:
			num = letters.find(chars)
			num += key
			encrypted_str += letters[num]

		else:
			encrypted_str += chars

def decipher(message, key):
	global decrypted_str
	decrypted_str = ''
	
	if key > 22:
		min_num = key - 22
		key -= min_num

	if key < -4:
		plus_num = key + 4
		key -= plus_num

	for chars in message:
		if chars in letters:
			num = letters.find(chars)
			num -= key
			decrypted_str += letters[num]

		else:
			decrypted_str += chars

## Command functions
def clear():
	if os.name == "nt":
		os.system('cls')
	else:
		os.system('clear')

def pause():
	pause = input("Press any key to continue \n")

def delay():
	seconds = input("How many seconds? ")
	time_delay(seconds)

def ep_time():
	print("Seconds since epoch is:", time.time())

def lcl_time():
	print("Current local time is: " + (time.ctime()))

def utc_time():
	print("Current utc time is:", time.asctime(utc_result))

def cipher_ter():
	input_str = input("Input message: ")
	input_key = int(input("Enter a key[0-22]: "))
	cipher(input_str, input_key)

	print("The encrypted result is:", encrypted_str)

def decipher_ter():
	input_str = input("Input message: ")
	input_key = int(input("Enter a key[0-22]: "))
	decipher(input_str, input_key)

	print("The decrypted result is:", decrypted_str)

def framewrk_ver():
	print("Current framework version: " + str(framewrk_version))
	print("Current version release date:", time.asctime(framewrk_last_date))

def framewrk_syscolor():
	global default_color_scheme

	new_syscolor = input("New color: ").lower()
	Y_n = input("Change color to " + new_syscolor + "[y/n] ").lower()

	if Y_n == 'y':
		if new_syscolor in color_dict:
			time_delay(2)
			default_color_scheme = color_dict[new_syscolor]
			print(default_color_scheme + "Sucessfully changed the color to " + new_syscolor + "!")

		else:
			print("Error 304! Entered color type is considered invalid!")

	else:
		print("Aborting changes!")

## System functions
def load_sys(plus_dict, sys_name, sys_color):
	global default_system_name
	global default_color_scheme
	global run

	time_delay(0.5)
	os.system('clear')

	for i in tqdm(range(0, 100), desc=White_Text + "Starting up"):
		command_dict.update(plus_dict)

		if not sys_name == '' or not sys_name == "":
			default_system_name = sys_name

		sys_color = sys_color.lower()
		if sys_color in color_dict:
			default_color_scheme = color_dict[sys_color]

		run = True
		time_delay(0.03)

	time_delay(2)
	print("done!..")
	os.system('clear')

def shut_sys():
	global run

	load_bar(0.05, White_Text + "Getting ready")
	time_delay(2)

	for i in tqdm(range(0, 100), desc=White_Text + "Shutting down"):
		run = False
		time_delay(0.03)

	time_delay(2.5)
	os.system('clear')

# Dictionaries
command_dict = {
	'clear': clear,
	'pause': pause,
	'delay': delay,
	'time': ep_time,
	'time -lcl': lcl_time,
	'time -utc': utc_time,
	'cipher': cipher_ter, 
	'decipher': decipher_ter,
	'framewrk -ver': framewrk_ver,
	'framewrk -syscolor': framewrk_syscolor,
	'shutdown': shut_sys,
}
color_dict = {
	'red': Red_Text,
	'green': Green_Text,
	'yellow': Yellow_Text,
	'blue': Blue_Text,
	'purple': Purple_Text,
	'cyan': Cyan_Text,
	'white': White_Text
}
# Default run function
def run(dict_plus, sys_name, sys_color):
	load_sys(dict_plus, sys_name, sys_color)

	while run:
		command = input(default_color_scheme + "~/" + default_system_name + "~#")

		if command in command_dict:
			try:
				command_dict[command]()

			except:
				print("Error!", sys.exc_info()[0], "has occurred!")

		else:
			print(default_error_message)
