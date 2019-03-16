"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""

import numpy as np
import cv2
from gaze_tracking import GazeTracking
import time
from datetime import datetime


RECORD_VIDEO = False
USE_GESTURES = True

LEFT_LOOK = None
LEFT_LOOK_THRESHOLD = 3

RIGHT_LOOK = None
RIGHT_LOOK_THRESHOLD = 5

BLINKING_COUNT = 0

# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
gaze = GazeTracking()

# drone = CoDrone.CoDrone()
# drone.connect()

#Capture video from the Wifi Connection to FPV module
#RTSP =(Real Time Streaming Protocol)
# cap = cv2.VideoCapture('rtsp://192.168.100.1/cam1/mpeg4')
i = 0
print('start')
while True:
    current_time = time.time()
    if(LEFT_LOOK != None):
        if(current_time > (LEFT_LOOK + LEFT_LOOK_THRESHOLD)):
            LEFT_LOOK = None
    if(RIGHT_LOOK != None):
        if(current_time > (RIGHT_LOOK + RIGHT_LOOK_THRESHOLD)):
            RIGHT_LOOK = None


    gaze.refresh()
    frame = gaze.main_frame(True)
    h,w = frame.shape[:2]
    if gaze.is_blinking():
        BLINKING_COUNT += 1
    else:
        BLINKING_COUNT = 0
    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()
    cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (255, 0, 0), 1)
    cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (255, 0, 0), 1)

    if(BLINKING_COUNT > 30):
        print('EYES CLOSED')
        BLINKING_COUNT = 0

    if(left_pupil):
        left_x, _ = left_pupil
        if(LEFT_LOOK == None and left_x < (w-480)):
            print('Caputured Screenshot')
            # cv2.imwrite("C:\\Users\\devin\\Documents\\Year 4\\Senior Design\\Pictures\\" + str(datetime.now()).replace(' ','').replace(':','-') + '.jpg', drone_frame)
            LEFT_LOOK = time.time()

    if(right_pupil):
        right_x, _ = right_pupil
        if(RIGHT_LOOK == None and right_x > (w-200)):
            print('drone 360 degrees')
            RIGHT_LOOK = time.time()

    # if RECORD_VIDEO:
    #     out.write(frame)
    cv2.imshow("Feed", frame)
    key = cv2.waitKey(5) & 0xFF
    if key == 27 or key == ord('q') or key == ord('Q'):
        break

cv2.destroyAllWindows()
