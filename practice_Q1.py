# import math
# import numpy as np
# import cv2
# import matplotlib.pyplot as plt 

# def applyMedianFilter(img, c, resolution):
#     idx = int(c/2)
#     new_img = np.zeros((resolution,resolution))
#     neighbours=[]
#     for i in range(1, resolution+1):
#         for j in range(idx, resolution+1):
#             print(i)
#             pLeft = img[i][j-1]
#             neighbours.append(pLeft)
#             pRight = img[i][j+1]
#             neighbours.append(pRight)
#             pTop = img[i-1][j]
#             neighbours.append(pTop)
#             pBottom = img[i+1][j]
#             neighbours.append(pBottom)
#             pTopLeft = img[i-1][j-1]
#             neighbours.append(pTopLeft)
#             pTopRight = img[i-1][j+1]   
#             neighbours.append(pTopRight)
#             pBottomLeft = img[i+1][j-1]
#             neighbours.append(pBottomLeft)
#             pBottomRight = img[i+1][j+1]
#             neighbours.append(pBottomRight)
#             neighbours.append(img[i][j])
#             neighbours.sort()
#             new_img[i-1][j-1] = neighbours[4]
#     return new_img
            
# def main():
#     img = cv2.imread("circuitboard.jpg",0)
#     img_out = img.copy()
#     resolution = img.shape[0]
#     img_out = np.array(img)

#     img_out = np.pad(img_out,((0,0),(0,0)), mode="constant", constant_values=0)
#     new_img = applyMedianFilter(img_out, 3, resolution)
    
#     cv2.imwrite("new_not.jpg",new_img)
#     cv2.imshow("IMAGE",new_img)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
# if __name__ == "__main__":
#     main()
import numpy as np
import cv2

img = cv2.imread('circuitboard.jpg', cv2.IMREAD_GRAYSCALE)
img_out = img.copy()

height = img.shape[0]
print(height)
width = img.shape[1]
print(width)
# for i in np.arange(3, height-3):
#     for j in np.arange(3, width-3):
#         neighbors = []
#         print(i)
#         for k in np.arange(-3, 4):
#             for l in np.arange(-3, 4):
#                 print(i)
#                 a = img.item(i+k, j+l)
#                 neighbors.append(a)
#         neighbors.sort()
#         median = neighbors[24]
#         b = median
#         img_out.itemset((i,j), b)

# cv2.imwrite('new_beast.jpg', img_out)

# cv2.imshow('image',img_out)
# cv2.waitKey(0)  
# cv2.destroyAllWindows()