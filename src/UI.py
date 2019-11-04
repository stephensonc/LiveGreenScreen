from os import system, name
import greenScreen


def print_menu():
    clear_screen()
    print("Menu:")
    print("1. Start Video")
    print("2. Choose Background")
    print("3. Stop Video")
    print("4. Exit")
    return int(input())


def clear_screen():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


if __name__ == '__main__':
    response = 0
    while(response != 4):
        response = print_menu()
        if response == 1:
            greenScreen.start_video()
        elif response == 2:
            filepath = input("Please enter the name of the file: ")
            print("Getting image")
            greenScreen.set_background("../backgrounds/" + filepath)
        elif response == 3:
            print("Stopping video")
