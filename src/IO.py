import cv2
import os


# Creates a cv2 VideoWriter object to be used to store video
# Parameters:
# name: String representing a filename without an extension
# width: The width of the video frame
# height: The height of the video frame
# Returns:
# vid: a cv2 VideoWriter
def create_video(name, width, height):
    # print("width: ", width, "Height: ", height)
    vid = cv2.VideoWriter(os.path.join(".", "videos", name, ".avi"),
                          cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 30,
                          (width, height))
    return vid


# Writes img to a specified VideoWriter
# Parameters:
# vid: a cv2 VideoWriter object that creates video files
# img: a numpy array of pixels to write to a video file as an image
def save_image_to_video(vid, img):
    vid.write(img)


# Retrieves an image from the filesystem
def get_image(path_to_image):
    # print("Getting image")
    final_path = os.path.join(*path_to_image)
    try:
        img = cv2.imread(final_path, 1)
    except FileNotFoundError:
        print("File not found")
    return img


# Changes current directory to the top level directory of this project
# Parameters:
# directory: current directory as a string
def correct_working_directory(directory):
    sub_dirs = ('src', 'videos', 'backgrounds')
    try:
        for sub_dir in sub_dirs:
            if sub_dir in directory:
                    os.chdir('..')
    except NameError:
        print("Directory fixing failed")
