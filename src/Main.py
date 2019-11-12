import greenScreen
from Color import Color
import time
import UI


def main():
    response = 0
    background = None
    color = Color('green')
    # print("Color: ", color.name, "min_val: ",
    #       color.min_val, "max_val", color.max_val)
    time.sleep(3)
    while(response != 4):
        response = UI.print_menu()
        if response == 1:
            background = UI.prompt_for_background()
        elif response == 2:
            save = UI.prompt_for_save()
            greenScreen.live_gs(save, background, color)
        elif response == 3:
            color = UI.prompt_for_color()
        else:
            return


if __name__ == '__main__':
    main()
