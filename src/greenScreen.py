import cv2
import numpy as np
import time

background = 0


def start_video():
    cap = cv2.VideoCapture(0)
    time.sleep(3)
    count = 0
    while(cap.isOpened()):
        ret, img = cap.read()
        if not ret:
            break
        count += 1
        # img = np.flip(img,axis=1)

        # Converting the color space from BGR to HSV
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # Generating mask to detect green color
        lower_green_bound = np.array([33, 15, 15])
        upper_green_bound = np.array([75, 255, 255])
        mask1 = cv2.inRange(hsv, lower_green_bound, upper_green_bound)

        # Refining the mask corresponding to the detected red color
        mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN,
                                 np.ones((3, 3), np.uint8), 2)
        mask1 = cv2.dilate(mask1, np.ones((3, 3), np.uint8), 1)
        mask2 = cv2.bitwise_not(mask1)

        # Generating the final output
        res1 = cv2.bitwise_and(background, background, mask=mask1)
        res2 = cv2.bitwise_and(img, img, mask=mask2)
        final_output = cv2.addWeighted(res1, 1, res2, 1, 0)
        cv2.imshow('Green Screen (Press esc to close)', final_output)
        # cv2.imshow('Mask1', mask1)
        # cv2.imshow('Mask2', mask2)
        k = cv2.waitKey(10)
        if k == 27:
            break


def set_background(path_to_image):
    global background
    background = cv2.imread(path_to_image, cv2.IMREAD_COLOR)
    # while True:
    #     cv2.imshow('Background image', background)
    #     k = cv2.waitKey(10)
    #     if k == 27:
    #         break
