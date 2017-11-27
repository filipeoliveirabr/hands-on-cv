import cv2
import numpy as np

def filter_my_contours(image,contours):
    filtered_contours = []
    ImageArea = image.shape[0] * image.shape[1]
    for i in contours:
        #Creiterio para filtro
        area = cv2.contourArea(i)
        if (area >= 0.10 *ImageArea) and (area <= 0.90 * ImageArea):
            filtered_contours.append(i)

    return filtered_contours

image    = cv2.imread('../resource/vertical.png')
blurred  = cv2.pyrMeanShiftFiltering(image,31,91) 
gray     = cv2.cvtColor(blurred,cv2.COLOR_BGR2GRAY)

ret , threshold = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow("Threshold",threshold)

_, contours,_     = cv2.findContours(threshold, cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
filtered_contours = filter_my_contours(image, contours)

(x,y,w,h) = cv2.boundingRect(filtered_contours[0])
image     = cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
cropped   = image[y:y+h,x:x+w]
cv2.imshow("Cropped Image",cropped)


print( "Number of contours detected-> %d  " % len(filtered_contours))
cv2.drawContours(image,filtered_contours,-1,(0,255,255),2)
cv2.namedWindow('Display',cv2.WINDOW_NORMAL)
cv2.imshow('Display',image)
cv2.waitKey()