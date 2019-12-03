from os import system, name
from Color import Color
import time
import IO
import os


# prints the main menu
def print_menu():
    clear_screen()
    print("Menu:")
    print("1. Choose Background")
    print("2. Start Video")
    print("3. Change Color to Detect")
    print("4. Exit")
    return input()


def clear_screen():
    if name == 'nt':  # For windows users
        system('cls')
    else:
        system('clear')  # for Linux and Mac


# TODO: Input handling so that color is never left unassigned
# sets the color detected by the program
def prompt_for_color():
    clear_screen()
    print("Choose a color for your screen:")
    print("1. Green")
    print("2. Blue")
    response = input()
    if '1' in response:
        return Color('green')
    elif '2' in response:
        return Color('blue')
    else:
        print("Response not found, please try again")
        return Color('green')


# Asks if the user wants to save a video
def prompt_for_save():
    response = input("Do you want to save a video? (y/N) ").upper()
    if 'Y' in response:
        return True
    else:
        return False


# Asks the user to input a filename
# Parameters:
# from_dir: boolean, specifies if a selection is to be made from a directory
def prompt_for_filename(from_dir):
    if from_dir:
        folder = os.path.join(".", "backgrounds")
        print("Please enter the name of the file you would like to open")
        print(folder, ":", "\n", os.listdir(folder), "\n\n")
        return input()
    else:
        return input("Please enter the name of your file (no extension): ")


# Prompts the user for a background image and returns it
def prompt_for_background():
    while True:
        path_to_image = [".", "backgrounds", prompt_for_filename(True)]
        background = IO.get_image(path_to_image)
        if(background is None):
            print("\nImage reading failed, please try again.\n")
            time.sleep(2)
        else:
            break
    return background
