from Color import Color
import green_screen
import time
import ui
import custom_io
import os


def main():
    response = ""
    background = None
    color = Color("green")

    start_dir = os.getcwd()
    # print(start_dir)
    # time.sleep(2)
    custom_io.correct_working_directory(start_dir)
    while "4" not in response or "EXIT" not in response.upper():
        response = ui.print_menu()
        if "1" in response or "BACKGROUND" in response.upper():
            background = ui.prompt_for_background()
        elif "2" in response or "START" in response.upper():
            save = ui.prompt_for_save()
            green_screen.run_gs(save, background, color)
        elif "3" in response or "CHANGE" in response.upper():
            color = ui.prompt_for_color()
        elif "4" in response:
            return
        else:
            print("\nInput not recognized, please try again.\n")
            time.sleep(2)


if __name__ == "__main__":
    main()
