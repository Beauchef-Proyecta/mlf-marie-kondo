print('holiss')
import numpy as np
import cv2
import sys
sys.path.append('/home/pi/mlf/api')

from client import ClientWrapper
c = ClientWrapper()

class Detector:
    x_origin = 263
    y_origin = 371

    width_mm = 515
    height_mm = 390

    def __init__(self, img_size=None):
        self.img = None
        self.img_size = img_size

        # Initialize some images used in processing
        self.img_gray = None
        self.img_blur = None
        self.img_edges = None
        self.img_dst = None
        self.img_rotated = None
    
    def get_frame(self): 
        img = c.get_single_frame()
        cv2.imwrite('frame.jpg', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print('Frame guardado')

    def work_with(self, img_path, resize=False):
        self.img = cv2.imread(img_path)
        if resize:
            self.img = cv2.resize(self.img, self.img_size, interpolation=cv2.INTER_LINEAR)
        
        #Rotate 2.5 degrees
        (h, w) = self.img.shape[:2]
        (cX, cY) = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D((cX, cY), 2.5, 1.0)
        self.img = cv2.warpAffine(self.img, M, (w, h))

        cv2.imwrite('image.jpg', self.img)
        print('tenemos imagen')


    def get_img(self, process="img"):
        return getattr(self, process)

    def process_image(self):
        # Convert to grayscale
        img_gray = cv2.cvtColor(self.img_masked, cv2.COLOR_BGR2GRAY)
        self.img_gray = img_gray

        # Blur the image for better edge detection
        img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)
        self.img_blur = img_blur

        # Canny Edge Detection
        edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200)
        self.img_edges = edges
        
        # Pixel expansion
        # Structure 5 × Square structure element of 5
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        # expand
        dst = cv2.dilate(edges, kernel=kernel)
        self.img_dst = dst

        # erode
        erode = cv2.erode(dst, None, iterations=1)
        self.img_erode = erode

    def centroid_detection(self):
        # Apply mask
        img = np.copy(self.img)
        img_mask = cv2.imread('images/mask_workspace.png')
        self.img_mask = cv2.cvtColor(img_mask, cv2.COLOR_BGR2GRAY)
        self.img_masked = cv2.bitwise_and(img, img, mask=self.img_mask)

        self.process_image()

        # contours
        contours, hierarchy = cv2.findContours(erode, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        # Filter unwanted contours
        self.contours = []
        for contour in contours:
            moments = cv2.moments(contour)
            contour_area = moments["m00"]
            if contour_area > 370 and contour_area < 430:
                self.contours.append(contour)


        coordinates = []

        # Centroid coordinates
        for contour in self.contours:
            moments = cv2.moments(contour)

            x_coord = int(moments['m10']/moments['m00'])
            y_coord = int(moments['m01']/moments['m00'])
            coordinates.append((x_coord, y_coord))

        return coordinates


    def get_contours(self):
        return self.contours


    def draw_contours(self):
        image_copy = self.img.copy()

        cv2.drawContours(
            image=image_copy,
            contours=self.contours,
            contourIdx=-1,
            color=(0, 255, 0),
            lineType=cv2.LINE_AA)

        cv2.imshow('Contours on original image', image_copy)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


    def show_img(self, process="img"):
        """process tiene que ser el nombre de alguna de las imágenes guardadas en la clase."""
        img = self.get_img(process)

        cv2.imshow(f"{process}", img)
        cv2.waitKey(0)

        cv2.destroyAllWindows()


    def show_centroid(self):
        coordinates = self.centroid_detection()
        new_img = self.img.copy()
        for coordinate in coordinates:
            new_img = cv2.rectangle(new_img, coordinate, coordinate, (0,255,0), 8)

        cv2.imshow("Centroid detection", new_img)
        cv2.waitKey(0)

        cv2.destroyAllWindows()
    


