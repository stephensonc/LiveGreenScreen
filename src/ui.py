"""This file contains all functions relating to the user interface."""
import os
import time
from os import system, name
from Color import Color
import custom_io


def print_menu():
    """Print the main menu."""
    clear_screen()
    print("Menu:")
    print("1. Choose Background")
    print("2. Start Video")
    print("3. Change Color to Detect")
    print("4. Exit")
    return input()


def clear_screen():
    """Clear the screen."""
    if name == "nt":  # For windows users
        system("cls")
    else:
        system("clear")  # for Linux and Mac


def prompt_for_color():
    """Set the color to detect during program runtime."""
    invalid = True
    while invalid:
        clear_screen()
        print("Choose a color for your screen:")
        print("1. Green")
        print("2. Blue")
        response = input()
        if "1" in response or "GREEN" in response.upper():
            invalid = False
            print("Setting color to green")
            return Color("green")
        elif "2" in response or "BLUE" in response.upper():
            invalid = False
            print("Setting color to blue")
            time.sleep(2)
            return Color("blue")
        print("Response: ", '"', response, '"', " not found, please try again")
        time.sleep(2)


def prompt_for_save():
    """Asks if the user wants to save a video"""
    response = input("Do you want to save a video? (y/N) ").upper()
    return True if "Y" in response else False


# Parameters:
# from_dir: boolean, specifies if a selection is to be made from a directory
def prompt_for_filename(from_dir):
    """Asks the user to input a file name."""
    if from_dir:
        folder = os.path.join(".", "backgrounds")
        print("Please enter the name of the file you would like to open")
        print(folder, ":", "\n", os.listdir(folder), "\n\n")
        return input()
    return input("Please enter the name of your file (no extension): ")


def prompt_for_background():
    """Prompts the user for a background image and returns it"""
    while True:
        path_to_image = [".", "backgrounds", prompt_for_filename(True)]
        background = custom_io.get_image(path_to_image)
        if background is None:
            print("\nImage reading failed, please try again.\n")
            time.sleep(2)
        else:
            break
    return background
