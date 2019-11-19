from Color import Color
import greenScreen
import time
import UI


def main():
    response = ''
    background = None
    color = Color('green')
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
