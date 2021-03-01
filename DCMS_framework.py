from tqdm import tqdm
import random
import time
import os
import sys

# DCMS framework #
# Made by Hkaar #

# Variables
## System variables
framewrk_version = 0.0311
framewrk_last_date = (2021, 2, 23, 11, 30, 4, 0, 362, 0)

Letters = "abcdefghijklmn opqrstuvwxyz_ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

# Functions
## Basic functions
def time_delay(seconds):
	time.sleep(float(seconds))

def countdown(seconds, text=None):
	while seconds:
		mins, secs = divmod(seconds, 60)
		timer = f'{mins}:{secs}'
		print(timer, end="\r")
		time_delay(1)
		seconds -= 1
	if text != None:
		print(text)

def load_bar(seconds, text):
	for i in tqdm(range(0, 100), desc=text):
		time_delay(seconds)

def slowprint(string):
	for c in string + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.1)

def convert_list(entered_list, type_l):
	if type_l >= 1:
		if type_l >= 2:
			converted_list = '[\n'
		else:
			converted_list = '['
	else:
		converted_list = ''
	list_len = len(entered_list)

	for item in entered_list:
		converted_list += item
		if list_len > 1:
			if type_l == 2:
				converted_list += '\n'
			elif type_l == 3:
				converted_list += ',\n' 
			else:
				converted_list += ', '
			list_len -= 1

	if type_l >= 1:
		if type_l >= 2:
			converted_list += '\n]'
		else:
			converted_list += ']'
	return converted_list

def convert_dictionary(dictionary, str_type, type_d):
	def custom_key_str(str_type, dictionary, dict_key):
		custom_str_dict = {
		'[]': f"[{dictionary[dict_key]}]",		'()': f"({dictionary[dict_key]})",		':': f": {dictionary[dict_key]}",
		'-[]': f" [{dictionary[dict_key]}]",	'-()': f" ({dictionary[dict_key]})",	':[]': f":[{dictionary[dict_key]}]",
		'-:[]': f": [{dictionary[dict_key]}]",	'-:()': f": ({dictionary[dict_key]})",	':()': f":({dictionary[dict_key]})"
		}
		try:
			return custom_str_dict[str_type]
		except:
			raise Exception("Invalid entered string dict type!, maybe you want to use '[]','()',':'!")

	if type_d >= 1:
		if type_d >= 3:
			converted_dict = "{"
		else:
			converted_dict = "{\n"
	else:
		converted_dict = ""
	dict_len = len(dictionary)
	
	for key in dictionary:
		converted_dict += str(key)
		converted_dict += custom_key_str(str_type, dictionary, key)

		if type_d >= 2 and not type_d >= 3:
			if dict_len <= 1:
				converted_dict += '\n'
			else:
				converted_dict += ',\n'
		else:
			if type_d <= 0 and dict_len >= 2:
				converted_dict += ',\n'
			else:
				if dict_len >= 1 and not type_d >= 3:
					converted_dict += '\n'
				elif dict_len >= 2 and type_d >= 3:
					converted_dict += ', '
		dict_len -= 1
	if type_d >= 1:
		converted_dict += '}'
		
	return converted_dict

def get_key(dictionary, val):
	for key, value in dictionary.items():
		if val == value:
			return key

	return "Key doesn't exist!"	

def del_key(dictionary, key):
	dictionary.pop(key, None)

def append_key(dictionary, key, value):
	dictionary[key] = value

## Additional functions
def cipher(message, key):
	encrypted_str = ''
	message = message[::-1]

	if key > 22:
		min_num = key - 22
		key -= min_num

	if key < -4:
		plus_num = key + 4
		key -= plus_num

	for c in message:
		if c in Letters:
			enc_num = Letters.index(c)
			enc_num += key
			encrypted_str += Letters[enc_num]
		else:
			encrypted_str += c
	return encrypted_str

def decipher(message, key):
	decrypted_str = ''
	message = message[::-1]
	
	if key > 22:
		min_num = key - 22
		key -= min_num

	if key < -4:
		plus_num = key + 4
		key -= plus_num

	for c in message:
		if c in Letters:
			dec_num = Letters.index(c)
			dec_num -= key
			decrypted_str += Letters[dec_num]
		else:
			decrypted_str += c
	return decrypted_str

## Command functions
def clear():
	if os.name == "nt":
		os.system('cls')
	else:
		os.system('clear')

def pause():
	pause = input("Press any key to continue...\n")

def delay():
	seconds = int(input("How many seconds? "))
	countdown(seconds)

def ep_time():
	print(f"Seconds since epoch is: {time.time()}")

def lcl_time():
	print(f"Current local time is: {time.asctime(time.struct_time(time.localtime()))}")

def utc_time():
	print(f"Current utc time is: {time.asctime(time.struct_time(time.gmtime()))}")

def cipher_cmd():
	input_str = input("Input message: ")
	input_key = int(input("Enter a key[0-22]: "))
	print("The encrypted result is:", cipher(input_str, input_key))

def decipher_cmd():
	input_str = input("Input message: ")
	input_key = int(input("Enter a key[0-22]: "))
	print("The decrypted result is:", decipher(input_str, input_key))

def framewrk_ver():
	print(f"Current framework version is: {framewrk_version}")
	print(f"Current version release date: {time.asctime(framewrk_last_date)}")

def framewrk_color_scheme():
	new_color_scheme = input("New color scheme: ").lower()
	confirm_change = input(f"Confirm changing color scheme to {new_color_scheme}[Y/n] ").lower()

	if confirm_change == 'y':
		if new_color_scheme in color_dict:
			time_delay(2)
			settings['COLOR_SCHEME'] = color_dict[new_color_scheme]
			print(f"{settings['COLOR_SCHEME']}Sucessfully changed the color scheme to {new_color_scheme}!")
		else:
			print("ERROR! Entered color scheme is considered invalid!")

def framewrk_naming_scheme():
	new_naming_scheme = input("New naming scheme: ")
	confirm_change = input(f"Confirm changing naming scheme to {new_naming_scheme}[Y/n] ").lower()

	if confirm_change == 'y':
		time_delay(2)
		settings['NAMING_SCHEME'] = new_naming_scheme
		print(f"Successfully changed the naming scheme to {new_naming_scheme}!")

def framewrk_ls_cmd():
	for key in command_dict:
		cmnd = key.split()
		if cmnd[0] == 'framewrk':
			pass
		else:
			print(f"-] {key}")

def framewrk_exit():
	clear()
	return False

# Dictionaries
settings = {
	'COLOR_SCHEME': "\033[1;32;48m",
	'NAMING_SCHEME': 'system',
}
command_dict = {
	'clear': clear,				'framewrk -ver': framewrk_ver,
	'pause': pause,				'framewrk -color': framewrk_color_scheme,
	'delay': delay,				'framewrk -name': framewrk_naming_scheme,
	'time': ep_time,			'framewrk -ls -cmd': framewrk_ls_cmd,
	'time -lcl': lcl_time,		'framewrk -exit': framewrk_exit,
	'time -utc': utc_time,
	'cipher': cipher_cmd, 
	'decipher': decipher_cmd,
	'exit': framewrk_exit,
}
color_dict = {
	'red': "\033[1;31;48m",			'red text':	"\033[1;31;48m",		'red_text': "\033[1;31;48m",
	'green': "\033[1;32;48m",		'green text': "\033[1;32;48m",		'green_text': "\033[1;32;48m",
	'yellow': "\033[1;33;48m",		'yellow text': "\033[1;33;48m",		'yellow_text': "\033[1;33;48m",
	'blue': "\033[1;34;48m",		'blue text': "\033[1;34;48m",		'blue_text': "\033[1;34;48m",
	'purple': "\033[1;35;48m",		'purple text': "\033[1;35;48m",		'purple_text': "\033[1;35;48m",
	'cyan': "\033[1;36;48m",		'cyan text': "\033[1;36;48m",		'cyan_text': "\033[1;36;48m",
	'white': "\033[1;37;48m",		'white text': "\033[1;37;48m",		'white_text': "\033[1;37;48m",
	'black': "\033[1;30;48m",		'black text': "\033[1;30;48m",		'black_text': "\033[1;30;48m",
}
# Default run function
def framewrk_run(dictionary=None, naming_scheme=None, color_scheme=None, process_counter=False):
	def load_run(dictionary, naming_scheme, color_scheme):
		clear()
		if color_scheme in color_dict:
			if color_scheme != None:
				settings['COLOR_SCHEME'] = color_dict[color_scheme.lower()]

		for i in tqdm(range(0, 100), desc=settings['COLOR_SCHEME'] + "Starting up"):
			if dictionary != None:
				command_dict.update(dictionary)
			if naming_scheme != None:
				settings['NAMING_SCHEME'] = naming_scheme
			time_delay(0.01)

		time_delay(1)
		clear()
	load_run(dictionary, naming_scheme, color_scheme)
	x = True

	if process_counter:
		print(f"The estimated program execution speed is: {time.process_time()} seconds!")

	while x:
		command = input(settings['COLOR_SCHEME'] + "~/" + settings['NAMING_SCHEME'] + "~#")

		if command in command_dict:
			if command_dict[command]() is False:
				x = False
		else:
			print(f"COMMAND ERROR! command-{command} does not exist!")
			