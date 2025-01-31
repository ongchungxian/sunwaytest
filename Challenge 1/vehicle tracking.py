import cv2
import os
import re
import imutils
import numpy as np
from os.path import isfile, join
import matplotlib.pyplot as plt

vid_name = '1'
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
pathIn = 'contours_{}/'.format(vid_name)
pathIn2 = 'plates_{}/'.format(vid_name)

for i in range(len(col_images)-1):
    ### vehicle detection ###
    # find difference between every two frames
    grayA = cv2.cvtColor(col_images[i], cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(col_images[i+1], cv2.COLOR_BGR2GRAY)
    diff_image = cv2.absdiff(grayB, grayA)
    
    # convert to binary image using threshold
    ret, thresh = cv2.threshold(diff_image, 15, 255, cv2.THRESH_BINARY)
    
    # image dilation
    dilated = cv2.dilate(thresh,kernel,iterations = 1)
    
    # find contours
    contours, hierarchy = cv2.findContours(dilated.copy(), cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    
    # store contours in array
    valid_cntrs = []
    for cntr in contours:
        x,y,w,h = cv2.boundingRect(cntr)
        if (cv2.contourArea(cntr) >= (length/20)*(width/40)):
            # avoid contours that are too small
            if (cv2.contourArea(cntr) < (length/25)*(width/45)):
                break
            valid_cntrs.append(cntr)
            

    # add contours to original frames
    v = col_images[i].copy()
    cv2.drawContours(v, valid_cntrs, -1, (127,200,0), 2)
    
    cv2.putText(v, "vehicles detected: " + str(len(valid_cntrs)), (100, 50), font, 2.0, (0, 180, 0), 2)
    cv2.line(v, (0, 80),(256,80),(100, 255, 255))
    cv2.imwrite(pathIn+str(i)+'.png',v)  
    ### vehicle detection ###


