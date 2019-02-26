"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""
import numpy as np
import cv2
from gaze_tracking import GazeTracking

RECORD_VIDEO = False

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
gaze = GazeTracking()
import CoDrone
drone = CoDrone.CoDrone()
drone.connect()

#Capture video from the Wifi Connection to FPV module
#RTSP =(Real Time Streaming Protocol)
cap = cv2.VideoCapture('rtsp://192.168.100.1/cam1/mpeg4')
fps = cv2.CAP_PROP_FPS
i = 0

while True:
    i += 1
    ret, frame = cap.read()
    cv2.imshow('Drone Feed', frame)
    if i % 3 == 0:
        gaze.refresh()

        frame = gaze.main_frame(True)
        text = ""

        if gaze.is_blinking():
            text = "Blinking"
        elif gaze.is_right():
            text = "Looking right"
        elif gaze.is_left():
            text = "Looking left"
        elif gaze.is_center():
            text = "Looking center"

        cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (255, 0, 0), 2)

        left_pupil = gaze.pupil_left_coords()
        right_pupil = gaze.pupil_right_coords()
        cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (255, 0, 0), 1)
        cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (255, 0, 0), 1)

        if RECORD_VIDEO:
            out.write(frame)
        cv2.imshow("Feed", frame)


        if cv2.waitKey(1) == 27 or cv2.waitKey(1) == ord('q')or cv2.waitKey(1) == ord('Q'):
            break
# out.release()
drone.connect()
cv2.destroyAllWindows()
