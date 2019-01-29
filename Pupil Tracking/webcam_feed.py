import numpy as np
import cv2
import time

def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print('clicked point (', x, y, ')')


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

# img = cv2.imread('test.jpg')


cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while (True):#while capturing video repeat this loop
    #save the video frame read into variable "frame"
    ret, frame = cap.read()
    if(not ret):
        break
    frame = cv2.flip( frame, 1 )
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    #show the video variable "frame" on a windows with
    #the title video frame
    cv2.imshow('Feed', frame)
    out.write(frame)

    key = cv2.waitKey(1) & 0xFF
    # print(key)
    if key == ord('q') or key == ord('Q'):
        break
    if key == ord('s') or key == ord('S'):
        # cv2.imwrite('C:\\Users\\devin\\Documents\\Year 4\\Fall 2018\\Senior Design\\Pupil Tracking\\input.jpg',frame)
        break


#Relase the camera
cap.release()

#close all the windows generated
cv2.destroyAllWindows()
