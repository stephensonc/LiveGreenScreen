import cv2
import numpy as np
import time

background = 0
bg_dimensions = 0
has_set_background = False


def start_video():
    global background
    cap = cv2.VideoCapture(0)
    time.sleep(3)
    if not has_set_background:
        success, background = cap.read()
    else:
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, bg_dimensions[0])
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, bg_dimensions[1])
    while(cap.isOpened()):
        if not has_set_background:
            success, img = cap.read()
            if not success:
                break
            cv2.imshow('No Background Set (Press esc to close)', img)
            k = cv2.waitKey(10)
            if k == 27:
                cv2.destroyAllWindows()
                break
        else:
            success, img = cap.read()
            if not success:
                break

            # Converting from BGR to HSV
            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

            # Generating mask to detect green
            lower_green_bound = np.array([33, 15, 15])
            upper_green_bound = np.array([75, 255, 255])
            mask1 = cv2.inRange(hsv, lower_green_bound, upper_green_bound)

            # Mask refining
            # mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN,
            #                          np.ones((3, 3), np.uint8), 2)
            # mask1 = cv2.dilate(mask1, np.ones((3, 3), np.uint8), 1)
            mask2 = cv2.bitwise_not(mask1)

            # Generating the final output
            res1 = cv2.bitwise_and(background, background, mask=mask1)
            res2 = cv2.bitwise_and(img, img, mask=mask2)
            final_output = cv2.addWeighted(res1, 1, res2, 1, 0)
            cv2.imshow('Green Screen (Press esc to close)', final_output)
            # cv2.imshow('Mask1', mask1)  # DEBUG
            # cv2.imshow('Mask2', mask2)  # DEBUG
            k = cv2.waitKey(10)
            if k == 27:
                cap.release()
                cv2.destroyAllWindows()
                break


def set_background():
    global background, bg_dimensions, has_set_background
    while True:  # This loop sanitizes inputs
        path_to_image = "../backgrounds/" + \
            input("Please enter the name of the file: ")
        print("Getting image")
        background = cv2.imread(path_to_image, cv2.IMREAD_COLOR)
        if(background is None):
            print("\nImage reading failed, please try again.\n")
        else:
            break
    has_set_background = True
    bg_dimensions = background.shape
    print(bg_dimensions)
    while True:
        cv2.imshow('Background image (Press esc to close)', background)
        k = cv2.waitKey(10)
        if k == 27:
            cv2.destroyAllWindows()
            break
