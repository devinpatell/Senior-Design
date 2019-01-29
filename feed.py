import CoDrone
drone = CoDrone.CoDrone()
drone.pair(drone.Nearest)

import numpy as np
import cv2

#Capture video from the Wifi Connection to FPV module
#RTSP =(Real Time Streaming Protocol)
cap = cv2.VideoCapture('rtsp://192.168.100.1/cam1/mpeg4')
# cap = cv2.VideoCapture(0)
fps = cv2.CAP_PROP_FPS
#Create a while loop to grab frame by frame of video
while (cap.isOpened()):#while capturing video repeat this loop
    #save the video frame read into variable "frame"
    ret, frame = cap.read()
    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #frame = cv2.decolor(frame)



    #show the video variable "frame" on a windows with
    #the title video frame
    #cv2.imshow('Windows Name', frameThatyouWanttoDisplay)
    cv2.imshow('Video Frame', frame)


    #In order to quit the while loop click q or Q
    #to break out of the loop
    key = cv2.waitKey(1) & 0xFF
    # print(key)
    if key == ord('q'):
        cv2.imwrite('C:\\Users\\devin\\Documents\\Year 4\\Fall 2018\\Senior Design\\feed_image.jpg',frame)
        break



#Relase the camera
cap.release()

#close all the windows generated
cv2.destroyAllWindows()
