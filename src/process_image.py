from Color import Color
import green_screen
import cv2
import custom_io


def main():
    img = custom_io.get_image("./backgrounds/color_chart.png")
    bg = custom_io.get_image("./backgrounds/london2.jpg")
    cv2.imshow(green_screen.process_frame(img, bg, Color("green")))
    k = cv2.waitKey(10)
    if k == 27:
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
