import numpy as np
import time
import cv2
import custom_io
import ui

DILATE_SIZE = 2


# Outputs img with all pixels with the detected color replaced with the
#     corresponding pixels from a background image
# Parameters:
# img: A numpy array of pixels in a given source image in BGR format
# bg_img: A numpy array of pixels in a background image of the user's choice
# color: a Color object that stores an acceptable range of hsv values for a
#     color
# Returns:
# final_output: img, but with all pixels containing the detected color replaced
#     with the corresponding pixels from a background image
def process_frame(img, bg_img, color):
    bg_shape = (bg_img.shape[1], bg_img.shape[0])
    # Resize image to reflect bagckround size
    img = cv2.resize(img, bg_shape)
    # Converting from BGR to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # mask to detect color
    mask1 = cv2.inRange(hsv, color.min_val, color.max_val)
    # Mask refining
    mask1 = cv2.morphologyEx(
        mask1, cv2.MORPH_OPEN, np.ones((DILATE_SIZE, DILATE_SIZE), np.uint8), 2
    )
    mask1 = cv2.dilate(mask1, np.ones((DILATE_SIZE, DILATE_SIZE), np.uint8), 1)
    mask2 = cv2.bitwise_not(mask1)
    # resizing masks
    # mask1 = cv2.resize(mask1, bg_shape)
    # mask2 = cv2.resize(mask2, bg_shape)
    # Generating the final output
    res1 = cv2.bitwise_and(bg_img, bg_img, mask=mask1)
    res2 = cv2.bitwise_and(img, img, mask=mask2)
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)
    return final_output


# Called once from Main and loops internally to process and display images
# Parameters:
# save_video: boolean from user that indicates if they want to save a video
# bg_img: a numpy array in which each element represents a pixel in BGR format
# color: a Color object that stores an acceptable range of hsv values for a
#     color
# Displays processed images to the screen
def run_gs(save_video, bg_img, color):
    cap = cv2.VideoCapture(0)
    time.sleep(3)
    if bg_img is None:
        path = [".", "backgrounds", "london2.jpg"]
        bg_img = custom_io.get_image(path)
    bg_dimensions = bg_img.shape
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, bg_dimensions[0])
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, bg_dimensions[1])
    if save_video:
        name = ui.prompt_for_filename(False)
        vid = custom_io.create_video(name, bg_dimensions[1], bg_dimensions[0])
    print("Detecting: " + color.name)
    print(bg_dimensions)
    while cap.isOpened():
        success, img = cap.read()
        if not success:
            break
        output_image = process_frame(img, bg_img, color)
        output_image = cv2.flip(output_image, 1)

        # This next line removes a toolbar on the top and bottom of the screen
        cv2.namedWindow(
            "Green Screen (Press esc to close)",
            flags=cv2.WINDOW_Gui_NORMAL + cv2.WINDOW_AUTOSIZE,
        )
        cv2.imshow("Green Screen (Press esc to close)", output_image)
        if save_video:
            custom_io.save_image_to_video(vid, output_image)
        k = cv2.waitKey(10)
        if k == 27:
            if save_video:
                vid.release()
            cap.release()
            cv2.destroyAllWindows()
            break
