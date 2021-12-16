import cv2
from detection import Detector

#cube = cv2.imread('images/img1.png')

detector = Detector()
detector.get_frame()
detector.work_with('frame.jpg') 
#detector.work_with('images/img1.png') #imagen guardada

#detector.centroid_detection()
#detector.show_centroid()
