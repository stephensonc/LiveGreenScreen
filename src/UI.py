from os import system, name
from Color import Color
import IO


def print_menu():
    clear_screen()
    print("Menu:")
    print("1. Choose Background")
    print("2. Start Video")
    print("3. Change Color to Detect")
    print("4. Exit")
    return int(input())


def clear_screen():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


def prompt_for_color():
    clear_screen()
    print("Choose a color for your screen:")
    print("1. Green")
    print("2. Blue")
    response = int(input())
    if response == 1:
        return Color('green')
    elif response == 2:
        return Color('blue')
    else:
        print("Response not found, please try again")


def prompt_for_save():
    response = input("Do you want to save a video? (Y/N)").upper()
    if 'Y' in response:
        return True
    else:
        return False


def prompt_for_filename():
    return input("Please enter the name of your file: ")


def prompt_for_background():
    while True:
        path_to_image = "./backgrounds/" + prompt_for_filename()
        background = IO.get_image(path_to_image)
        if(background is None):
            print("\nImage reading failed, please try again.\n")
        else:
            break
    return background
