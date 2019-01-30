import numpy as np
import cv2
import time


RECORD_VIDEO = False

def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print('clicked point (', x, y, ')')


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

# img = cv2.imread('test.jpg')


cap = cv2.VideoCapture(0)
if RECORD_VIDEO:
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
    # assert len(faces) < 2
    if(len(faces) < 1):
        continue
    (x,y,w,h) = faces[0]
    frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = frame[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    if len(eyes) > 2:
        continue
    roi_eyes = []
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        roi_eyes.append(roi_color[ey:ey+eh, ex:ex+ew])
    for i in range(len(roi_eyes)):
        height, width = roi_eyes[i].shape[:2]
        roi_eyes[i] = cv2.resize(roi_eyes[i],(5*width, 5*height), interpolation = cv2.INTER_AREA)
        roi_eyes[i] = cv2.GaussianBlur(roi_eyes[i], (5, 5), 0)

        # roi_eyes[i] = cv2.cvtColor(roi_eyes[i], cv2.COLOR_BGR2GRAY)
        # _, roi_eyes[i] = cv2.threshold(roi_eyes[i],127,255,cv2.THRESH_BINARY)
        cv2.imshow(str(i), roi_eyes[i])
    # cv2.imshow('ROI', roi_color)
    #show the video variable "frame" on a windows with
    #the title video frame
    cv2.imshow('Feed', frame)
    if RECORD_VIDEO:
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
