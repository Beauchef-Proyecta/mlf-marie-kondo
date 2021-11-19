import numpy as np
import cv2


class Detector:
    def __init__(self, img_size=(360, 640)):
        self.img = None
        self.img_size = img_size

        # Initialize some images used in processing
        self.img_mask = None
        self.img_masked = None
        self.img_gray = None
        self.img_blur = None
        self.img_edges = None
        self.img_dst = None
    

    def load_img(self, img, resize=True):
        self.img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        if resize:
            self.img = cv2.resize(self.img, self.img_size, interpolation=cv2.INTER_LINEAR)


    def get_img(self, process="img"):
        return getattr(self, process)

    def centroid_detection(self):
        # Apply mask
        img = np.copy(self.img)
        self.img_mask = cv2.imread('images/mask_workspace.png')
        self.img_masked = cv2.bitwise_and(img, img, mask=self.img_mask)

        # Convert to graycsale
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

        # contours
        self.contours, _ = cv2.findContours(erode, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Centroid coordinates
        moments = cv2.moments(dst, binaryImage=True)

        x_coord = int(moments['m10']/moments['m00'])
        y_coord = int(moments['m01']/moments['m00'])

        return x_coord, y_coord


    def get_contours(self):
        return self.contours


    def show_img(self, process="img"):
        """process tiene que ser el nombre de alguna de las imágenes guardadas en la clase."""
        img = self.get_img(process)

        cv2.imshow(f"{process}", img)
        cv2.waitKey(0)

        cv2.destroyAllWindows()



    def show_centroid(self):
        x, y = self.centroid_detection()
        coords = cv2.rectangle(self.img, (x, y), (x, y), (0,255,0), 10)

        cv2.imshow("Centroid detection", coords)
        cv2.waitKey(0)

        cv2.destroyAllWindows()

