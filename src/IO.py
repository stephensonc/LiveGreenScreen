import cv2


def create_video(name, width, height):
    print("width: ", width, "Height: ", height)
    vid = cv2.VideoWriter('./videos/' + name + '.avi',
                          cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 30,
                          width, height)
    return vid


def save_image_to_video(vid, img):
    vid.write(img)


def get_image(path_to_image):
    print("Getting image")
    return cv2.imread(path_to_image, 1)
