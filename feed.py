import CoDrone
from CoDrone import Direction,Degree
drone = CoDrone.CoDrone()
drone.connect()

import numpy as np
import cv2

## wifi password 12345678




def leftKey():
    print( "Left key pressed")
    drone.set_roll(-60)
    drone.move(.4)


def rightKey():
    print( "Right key pressed")
    drone.set_roll(40)
    drone.move(.4)

def upKey():
    print( "up key pressed")
    drone.set_pitch(40)
    drone.move(.4)


def downKey():
    print( "down key pressed")
    drone.set_pitch(-40)
    drone.move(.4)

def wKey():
    print( "w key pressed")
    drone.set_throttle(100)
    drone.move(.4)

def sKey():
    print( "s key pressed")
    drone.set_throttle(-80)
    drone.move(.4)


def aKey():
    print( "a key pressed")
    drone.set_yaw(-40)
    drone.move(.4)

def dKey():
    print( "d key pressed")
    drone.set_yaw(40)
    drone.move(.4)




def takeoff():
    print("take off like kodak black")
    drone.takeoff()

def land():
    print("landing")
    drone.set_throttle(-20)
    drone.move(1)
    drone.land()
def turn360():
    drone.rotate180()



runkey = { 255: None, ord('d') :dKey,32: takeoff, ord('t') : land, ord('i') : upKey,
          ord('j') : leftKey, ord('k') : downKey, ord('l') : rightKey, ord('w') : wKey, ord('s') : sKey,
          ord('a') : aKey, ord('o'):turn360}





#Capture video from the Wifi Connection to FPV module
#RTSP =(Real Time Streaming Protocol)
cap = cv2.VideoCapture('rtsp://192.168.100.1/cam1/mpeg4')
# cap = cv2.VideoCapture(0)
fps = cv2.CAP_PROP_FPS
#Create a while loop to grab frame by frame of video
while (True):#while capturing video repeat this loop
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
    if key == ord('q') or key == ord('Q'):
        break
    else:
        func = runkey.get(key)
        if func:
            func()






#Relase the camera
cap.release()
drone.disconnect()
print("drone was disconnected")


#close all the windows generated
cv2.destroyAllWindows()
