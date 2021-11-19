import cv2
from detection import Detector

cube = cv2.imread('images/working_img.png')

detector = Detector()
detector.load_img(cube)
detector.centroid_detection()

detector.show_imgs()