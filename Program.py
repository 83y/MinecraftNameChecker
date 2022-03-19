import requests
import time
import os
import colorama
import ctypes
import string
import aiohttp
import asyncio
from datetime import datetime
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

dict_before = "/Program Files"
dict_after = "Program Files/"
main_colour = Fore.YELLOW
warning_colour = Fore.RED
try:
	os.mkdir(os.getcwd() + dict_before)
except:
	pass

def program_exit(message = 'PRESS ANY KEY TO EXIT OUT'):
    print(message)
    os.system('pause >NULL')
    return 0

def name_checker():
    print(warning_colour + "Warning: " + main_colour + "Before you check, all current files (eg. invalid_names.txt) will be wiped when you go through with the name check\nEnter the file name you want to check names for (eg. names.txt): ")
    fileName = str(input())
    inputtedNames = open(fileName, "r")
    inputtedNames = inputtedNames.read()
    names = inputtedNames.split(",")
    count = 0
    file = open(dict_after + "invalid_names.txt", "a")
    file.truncate(0)
    file.close()
    while count < (len(names)):
        if names[count].isalnum() != True or len(names[count]) <= 2 or len(names[count]) > 16:
            file = open(dict_after + "invalid_names.txt", "a")
            file.write(names[count] + "\n")
            file.close()
            names.pop(count)
            count -= 1
        count += 1
    unchecked = len(names)
    checked = 0
    untaken = 0
    taken = 0
    ctypes.windll.kernel32.SetConsoleTitleW(f"Unchecked: {unchecked} Checked: {checked} Untaken: {untaken} Taken: {taken}")
    file = open(dict_after + "taken_names.txt", "a")
    file.truncate(0)
    file.close()
    file = open(dict_after + "untaken_names.txt", "a")
    file.truncate(0)
    file.close()

    for i in range (len(names)):
        temp_var = "https://api.mojang.com/users/profiles/minecraft/" + names[i]
        try:
            file = open(dict_after + "taken_names.txt", "a")
            response = requests.get(temp_var)
            response = response.json()
            file.write(response['name'] + "\n")
            file.close()
            print(Fore.RED + names[i] + " - Taken")
            taken += 1
        except:
            file = open(dict_after + "untaken_names.txt", "a")
            file.write(names[i] + "\n")
            file.close()
            print(Fore.GREEN + names[i] + " - Not Taken")
            untaken += 1
        file = open(dict_after + "database_of_names_checked.txt", "a")
        checked += 1
        unchecked -= 1
        ctypes.windll.kernel32.SetConsoleTitleW(f"Unchecked: {unchecked} Checked: {checked} Untaken: {untaken} Taken: {taken}")
        now = datetime.now()
        date_format = now.strftime("%d/%m/%Y %H:%M:%S")
        file.write(names[i] + " - " + date_format + "\n")
        file.close()
        time.sleep(1.1)

    print(main_colour + "Your name list have been successfully checked.")
    choice()

def name_joiner():
    print(main_colour + "The file must be structured like this for them to be joined:\n\nHere\nAre\nA\nfew\nnames\nEnter the name of the file you want to join (eg. names.txt):")
    fileName = str(input())
    file = open(fileName, "r")
    file = file.read()
    newFileNames = file.split("\n")
    seperator = ","
    newFileNames = seperator.join(newFileNames)
    newFile = fileName.split(".")
    newFile = newFile[0] + "_joined" + "." + newFile[1]
    newFile = open(newFile, "a")
    newFile.truncate(0)
    newFile.write(newFileNames)
    newFile.close()
    choice()

def choice():
    ctypes.windll.kernel32.SetConsoleTitleW("Program")
    print(main_colour + "1) Check Names\n2) (Join / Format) Names\n3) Search for a Name")
    choice = int(input())
    if choice == 1:
        name_checker()
    elif choice == 2:
        name_joiner()
    else:
        program_exit()

choice()

# Have it set a timer for when it checks all the names that were scanned in the last X minutes
# Give the single program a GUI
# Give proper formatting (text to ASCII)
# Have an option where it gives you the most recent popular searches
# Implement proxies (important)
# String manipulate names, eg. replace toe with t0e
