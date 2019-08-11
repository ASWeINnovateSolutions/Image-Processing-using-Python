#min filter

import cv2
import numpy as np 

img = cv2.imread("cat.jpg",0)
img_out = img.copy()

height = img.shape[0]
width = img.shape[1]

for i in np.arange(3, height-3):
    for j in np.arange(3, width-3):
        min = 255
        for k in np.arange(-3,4):
            for l in np.arange(-3,4):
                if img.item(i+k,j+l)<min:
                    min = img.item(i+k,j+l)
        img_out.itemset((i,j),min)

cv2.imshow("New_Cat",img_out)
cv2.waitKey()
cv2.destroyAllWindows()
