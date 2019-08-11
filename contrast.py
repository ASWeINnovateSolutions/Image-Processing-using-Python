import cv2
import numpy as np
import math 

img =cv2.imread("low_contrast_1.jpg",cv2.IMREAD_GRAYSCALE)
height = img.shape[0]
width = img.shape[1]
print(height)
print(width)
contrast =1.3

for i in np.arange(height):
    for j in np.arange(width):
        a = img.item(i,j)
        b = math.ceil(contrast*a)
        if b>255:
            b = 255
        img.itemset((i,j),b)

cv2.imshow("New Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
