import cv2
from color_detection import ColorDetector

cube = cv2.imread('images/working_img.png')

detector = ColorDetector()
detector.load_img(cube)
detector.detection()

detector.show_imgs()