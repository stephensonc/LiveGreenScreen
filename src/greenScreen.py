import numpy as np
import cv2
import IO
import UI

dilate_size = 3


def process_frame(img, bg_img, color):
    bg_shape = (bg_img.shape[1], bg_img.shape[0])
    # Resize image to reflect bagckround size
    img = cv2.resize(img, bg_shape)
    # Converting from BGR to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # mask to detect color
    mask1 = cv2.inRange(hsv, color.min_val, color.max_val)
    # Mask refining
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN,
                             np.ones((dilate_size, dilate_size), np.uint8), 2)
    mask1 = cv2.dilate(mask1, np.ones((dilate_size, dilate_size), np.uint8), 1)
    mask2 = cv2.bitwise_not(mask1)
    mask1 = cv2.resize(mask1, bg_shape)
    mask2 = cv2.resize(mask2, bg_shape)
    # Generating the final output
    res1 = cv2.bitwise_and(bg_img, bg_img, mask=mask1)
    res2 = cv2.bitwise_and(img, img, mask=mask2)
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)
    return final_output


def live_gs(save_video, bg_img, color):
    print("Detecting: " + color.name)
    cap = cv2.VideoCapture(0)
    if bg_img is None:
        bg_img = IO.get_image('./backgrounds/london2.jpg')
    bg_dimensions = bg_img.shape
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, bg_dimensions[0])
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, bg_dimensions[1])
    if save_video:
        name = UI.prompt_for_filename()
        vid = IO.create_video(name, bg_dimensions[1], bg_dimensions[0])
    print(bg_dimensions)
    while(cap.isOpened()):
        success, img = cap.read()
        img = cv2.flip(img, 1)
        if not success:
            break
        output_image = process_frame(img, bg_img, color)
        cv2.imshow('Green Screen (Press esc to close)', output_image)
        if save_video:
            IO.save_image_to_video(vid, img)
        k = cv2.waitKey(10)
        if k == 27:
            if save_video:
                vid.release()
            cap.release()
            cv2.destroyAllWindows()
            break
