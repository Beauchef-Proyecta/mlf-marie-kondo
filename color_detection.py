import cv2
import numpy as np

class ColorDetector:
    black = [np.array([0,0,0]), np.array([350,55,100])]

    def __init__(self):
        self.img = None
        self.hsv = None
    
    def load_img(self, img):
        self.img = img
        self.hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    def detection(self, color=black):
        self.mask = cv2.inRange(self.img, self.black[0], self.black[1])
        self.res = cv2.bitwise_and(self.img, self.img, mask = self.mask)

    def show_imgs(self):
        cv2.imshow('frame', self.img)
        cv2.imshow('mask', self.mask)
        cv2.imshow('res',self.res)

        cv2.waitKey(0)
        cv2.destroyAllWindows()