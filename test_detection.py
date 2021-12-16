import cv2
from detection import Detector

cube = cv2.imread('images/img1.png')

detector = Detector()
detector.load_img(cube)
detector.centroid_detection()
detector.show_centroid()
