from Color import Color
import greenScreen
import time
import UI
import IO
import os


def main():
    response = ''
    background = None
    color = Color('green')

    start_dir = os.getcwd()
    print(start_dir)
    time.sleep(2)
    IO.correct_working_directory(start_dir)
    while '4' not in response:
        response = UI.print_menu()
        if '1' in response:
            background = UI.prompt_for_background()
        elif '2' in response:
            save = UI.prompt_for_save()
            greenScreen.run_gs(save, background, color)
        elif '3' in response:
            color = UI.prompt_for_color()
        elif '4' in response:
            return
        else:
            print("\nInput not recognized, please try again.\n")
            time.sleep(2)


if __name__ == '__main__':
    main()
