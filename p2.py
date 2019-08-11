# import numpy as np 
# import cv2
# import matplotlib.pyplot as plt 

# def convolve_np(X,F):
#     X_height = X.shape[0]
#     X_width = X.shape[1]

#     F_height = F.shape[0]
#     F_width = F.shape[1]

#     H = (F_height-1)/2
#     W = (F_width-1)/2

#     out = np.zeros((X_height,X_width))

#     for i in range(H,X_height-H):
#         for j in range(W,X_width-W):
#             sum = 0
#             for k in range(-H,H+1):
#                 for l in range(-W,W+1):
#                     a = X[i+k,j+l]
#                     w = F[H+k,W+l]
#                     sum+=(w*a)
#         out[i,j] = sum
#     return out

# def main():
#     # img = np.array([[1,2,1],[1,2,1],[3,3,2]])
#     # filter = np.array([[1,1],[-1,-1]])
#     img = cv2.imread("pebbles.tif",0)
#     Hx = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
#     Hy = np.array([[-1,-1,-1],[0,0,0],[1,1,1]])
#     img_x = convolve_np(img,Hx)/6.0
#     img_y = convolve_np(img,Hy)/6.0
#     img_out = np.sqrt(np.power(img_x,2)+np.power(img_y,2))
#     img_out = (img_out/(np.max(img_out)))*255
#     cv2.imwrite("prewit.tif", img_out)
#     plt.imshow(img_out,cmap='gray')
#     plt.show()

# if __name__=="__main__":
#     main()


'''Prewit '''
import numpy as np
import cv2
from matplotlib import pyplot as plt
from convolve_np import convolve_np

img = cv2.imread('jet.jpg', cv2.IMREAD_GRAYSCALE)

height = img.shape[0]
width = img.shape[1]

Hx = np.array([[-1, 0, 1],
               [-1, 0, 1],
               [-1, 0, 1]])

Hy = np.array([[-1, -1, -1],
               [0, 0, 0],
               [1, 1, 1]])

img_x = convolve_np(img, Hx) / 8.0
img_y = convolve_np(img, Hy) / 8.0

img_out = np.sqrt(np.power(img_x, 2) + np.power(img_y, 2))

img_out = (img_out / np.max(img_out)) * 255

cv2.imwrite('edge_prewitt.tif', img_out)

plt.imshow(img_out, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()