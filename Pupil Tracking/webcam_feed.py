import numpy as np
import cv2
import time


RECORD_VIDEO = False

def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print('clicked point (', x, y, ')')


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# pick which haar cascade to use
# eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')


# start live stream
cap = cv2.VideoCapture(0)
# start output stream and set fourcc
if RECORD_VIDEO:
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while (True):#while capturing video repeat this loop
    #save the video frame read into variable "frame"
    ret, frame = cap.read()
    # if frame didn't capture
    if(not ret):
        break
    # since its a webcam feed, flip the frame vertically
    frame = cv2.flip( frame, 1 )
    # grayscale frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detect faces
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    # assert len(faces) < 2
    if(len(faces) < 1):
        continue
    # grab bouding box data for first face detected
    (x,y,w,h) = faces[0]
    # draw bounding box
    frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    # grab the greyscale bounding box of the face
    roi_gray = gray[y:y+h, x:x+w]
    # grab the regular colored bounding box of the face
    roi_color = frame[y:y+h, x:x+w]
    # detect eyes in the greyscale bounding box of the face
    eyes = eye_cascade.detectMultiScale(roi_gray)

    # list of ROIs for the eyes
    roi_eyes = []
    # grab bouding box data for each eye
    for (ex,ey,ew,eh) in eyes:
        # draw bouding box over each eye
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        # add the bouding box of the eye to the list of eye ROIs
        roi_eyes.append(roi_color[ey:ey+eh, ex:ex+ew])
    # for every eye ROI
    for i in range(len(roi_eyes)):
        # grab width and height
        height, width = roi_eyes[i].shape[:2]
        # resize each eye's bounding box by a scalar of 5
        roi_eyes[i] = cv2.resize(roi_eyes[i],(5*width, 5*height), interpolation = cv2.INTER_AREA)
        # apply GaussianBlur
        roi_eyes[i] = cv2.GaussianBlur(roi_eyes[i], (5, 5), 0)
        # grayscale each eye bouding box
        roi_eyes[i] = cv2.cvtColor(roi_eyes[i], cv2.COLOR_BGR2GRAY)
        # show the bouding box of each eye
        cv2.imshow(str(i), roi_eyes[i])
    #show the video variable "frame"
    cv2.imshow('Feed', frame)
    # if record mode is on, save the new frame with the bounding boxes drawn on it
    if RECORD_VIDEO:
        out.write(frame)

    key = cv2.waitKey(1) & 0xFF
    # if q or Q, quit live feed
    if key == ord('q') or key == ord('Q'):
        break
    # if s or S, take a screenshot of the frame
    if key == ord('s') or key == ord('S'):
        # cv2.imwrite('C:\\Users\\devin\\Documents\\Year 4\\Fall 2018\\Senior Design\\Pupil Tracking\\input.jpg',frame)
        break


#Relase the camera
cap.release()

#close all the windows generated
cv2.destroyAllWindows()
