import cv2
import numpy as np

image = cv2.imread('4.jpg')
gauss_kernel = -1/256 * np.array([[1, 4, 6, 4, 1],
                                  [4, 16, 24, 16, 4],
                                  [6, 24, -476, 24, 6],
                                  [4, 16, 24, 16, 4],
                                  [1, 4, 6, 4, 1]]

)
sharp_kernel = np.array([[0,-1,0], 
                         [-1,5,-1],
                         [0,-1,0]])
sharp_kernel = 2/3 * sharp_kernel
gauss = cv2.filter2D(image, -1, gauss_kernel)
sharpened = cv2.filter2D(gauss, -1, sharp_kernel) 
cv2.imshow('Image Sharpening', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()