from os import system, name
import greenScreen


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


if __name__ == '__main__':
    response = 0
    while(response != 4):
        response = print_menu()
        if response == 1:
            greenScreen.set_background()
        elif response == 2:
            greenScreen.start_video()
        elif response == 3:
            greenScreen.set_color()
