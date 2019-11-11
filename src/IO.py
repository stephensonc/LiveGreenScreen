import cv2


def create_video(name, width, height):
    return cv2.VideoWriter('./videos/' + name + '.avi',
                           cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10,
                           width, height)


def save_image_to_video(vid, img):
    vid.write(img)
