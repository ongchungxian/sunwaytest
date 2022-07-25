import cv2
import os
import re
import imutils
import numpy as np
from os.path import isfile, join
import matplotlib.pyplot as plt


vid_name = '3'
vid = vid_name + '.mp4'
# split video into frames
capture = cv2.VideoCapture('video/'+vid)

frameNo = 0
 
while (frameNo < 50):
    success, frame = capture.read()
 
    if success:
        cv2.imwrite(f'frames_{vid_name}/{frameNo}.jpg', frame)
    else:
        break
 
    frameNo = frameNo+1
 
capture.release()

col_frames = os.listdir('frames_{}/'.format(vid_name))

col_images=[]

for i in col_frames:
    img = cv2.imread('frames_{}/'.format(vid_name)+i)
    col_images.append(img)

i = 0

length = col_images[i].shape[0]
width = col_images[i].shape[1]



# kernel for image dilation
kernel = np.ones((5,5),np.uint8)

# font style
font = cv2.FONT_HERSHEY_SIMPLEX

# directory to save the output frames
pathIn = 'plates_{}/'.format(vid_name)

for i in range(len(col_images)-1):
    ### license plate detection ###
    gray = cv2.cvtColor(col_images[i], cv2.COLOR_BGR2GRAY)
    # filter for denoising
    gray = cv2.bilateralFilter(gray, 11, 17, 17)
    # edge detection
    edged = cv2.Canny(gray, 30, 200) 
    cntrs, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    l = col_images[i].copy()
    
    valid_cntrs = []
    for cntr in cntrs:
        if (cv2.contourArea(cntr) >= (length/10)*(width/10)):
            # avoid contours that are too small
            if (cv2.contourArea(cntr) < (length/20)*(width/20)):
                break
            valid_cntrs.append(cntr)
    for cntr in valid_cntrs:
        perimeter = cv2.arcLength(cntr, True)
        approx = cv2.approxPolyDP(cntr, 0.018 * perimeter, True)
        if len(approx) == 4: 
            x,y,w,h = cv2.boundingRect(cntr) 
            # crops the image to only containing the license plate
            new_img=l[y:y+h,x:x+w]
            cv2.imwrite('plate'+'.png',new_img)
            i+=1
            break

    cv2.drawContours(l, valid_cntrs, -1, (200,0,0), 3)
    plt.imshow(l)
    plt.show()
    cv2.putText(l, "plates detected: " + str(len(cntrs)), (100, 50), font, 2.0, (180, 0, 0), 2)
    cv2.imwrite(pathIn+str(i)+'.png',l)  
    ### license plate detection ###