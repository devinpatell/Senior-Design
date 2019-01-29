import numpy as np
import cv2
import time

def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print('clicked point (', x, y, ')')


cap = cv2.VideoCapture(0)
time.sleep(1)
_, frame = cap.read()
frame = cv2.flip( frame, 1 )
roi = cv2.selectROI('Feed', frame, False)

# Crop image
# frame = frame[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]


while (True):#while capturing video repeat this loop
    #save the video frame read into variable "frame"
    ret, frame = cap.read()
    if(not ret):
        break
    frame = cv2.flip( frame, 1 )
    # Crop image
    frame = frame[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]

    #show the video variable "frame" on a windows with
    #the title video frame
    cv2.imshow('Feed', frame)


    key = cv2.waitKey(1) & 0xFF
    # print(key)
    if key == ord('q') or key == ord('Q'):
        break



#Relase the camera
cap.release()

#close all the windows generated
cv2.destroyAllWindows()
