import numpy as np
import cv2

# Read the original image
screw_img = cv2.imread('screw.jpg')
screw_img = cv2.resize(screw_img, (384, 288), interpolation=cv2.INTER_LINEAR)

glass_img = cv2.imread('glass.jpg')
glass_img = cv2.resize(glass_img, (384, 255), interpolation=cv2.INTER_LINEAR)


# Convert to graycsale
img_gray1 = cv2.cvtColor(screw_img, cv2.COLOR_BGR2GRAY)
img_gray2 = cv2.cvtColor(glass_img, cv2.COLOR_BGR2GRAY)
# Blur the image for better edge detection
img_blur1 = cv2.GaussianBlur(img_gray1, (3,3), 0)
img_blur2 = cv2.GaussianBlur(img_gray2, (3,3), 0)


# Canny Edge Detection
edges1 = cv2.Canny(image=img_blur1, threshold1=100, threshold2=200)
edges2 = cv2.Canny(image=img_blur2, threshold1=100, threshold2=200)


'''
# Binarization
ret, thresh = cv2.threshold(edges,10,255,cv2.THRESH_BINARY)
'''


# Pixel expansion
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))  # Structure 5 × Square structure element of 5
dst1 = cv2.dilate(edges1, kernel=kernel)  # expand
dst2 = cv2.dilate(edges2, kernel=kernel)  # expand


# Centroid coordinates
moments1 = cv2.moments(dst1, binaryImage=True)
moments2 = cv2.moments(dst2, binaryImage=True)

x1_coord = int(moments1['m10']/moments1['m00'])
y1_coord = int(moments1['m01']/moments1['m00'])
x2_coord = int(moments2['m10']/moments2['m00'])
y2_coord = int(moments2['m01']/moments2['m00'])


# Show the results
coords1 = cv2.rectangle(screw_img, (x1_coord,y1_coord), (x1_coord,y1_coord), (0,255,0), 10)
coords2 = cv2.rectangle(glass_img, (x2_coord,y2_coord), (x2_coord,y2_coord), (0,255,0), 10)
cv2.imshow("Screw centroid detection", coords1)
cv2.imshow("Glass centroid detection", coords2)

'''black_img = np.zeros((288, 384))
coords = cv2.rectangle(black_img, (x_coord,y_coord), (x_coord,y_coord), (255,0,0), 2)
#print(img_gray)
row1 = np.concatenate((img_gray,edges), axis=1)
row2 = np.concatenate((dst,coords), axis=1)
#images = np.concatenate((row1,row2), axis=0)

cv2.imshow("Image processing: grayscaled and edge detection", row1)
cv2.imshow("Image processing: white pixels expanded and centroid detection", row2)
'''
#cv2.imshow("Image processing", images)
cv2.waitKey(0)

cv2.destroyAllWindows()
