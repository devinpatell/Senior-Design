from tkinter import *

import matplotlib
matplotlib.use('TkAgg')
import CoDrone

drone = CoDrone.CoDrone()


main = Tk()


def leftKey(event):
    print( "Left key pressed")
    drone.set_roll(-60)
    drone.move(.4)


def rightKey(event):
    print( "Right key pressed")
    drone.set_roll(40)
    drone.move(.4)

def upKey(event):
    print( "up key pressed")
    drone.set_pitch(40)
    drone.move(.4)


def downKey(event):
    print( "down key pressed")
    drone.set_pitch(-40)
    drone.move(.4)

def wKey(event):
    print( "w key pressed")
    drone.set_throttle(100)
    drone.move(.4)

def sKey(event):
    print( "s key pressed")
    drone.set_throttle(-80)
    drone.move(.4)


def aKey(event):
    print( "a key pressed")
    drone.set_yaw(-40)
    drone.move(.4)

def dKey(event):
    print( "d key pressed")
    drone.set_yaw(40)
    drone.move(.4)

def connect(event):
    print("connecting")
    drone.connect()

def disconnect(event):
    drone.disconnect()
    print("disconnected")

def takeoff(event):
    print("take off like kodak black")
    drone.takeoff()

def land(event):
    print("landing")
    drone.set_throttle(-20)
    drone.move(1)
    drone.land()

def cal(event):
    drone.calibrate()

frame = Frame(main, width=200, height=200)
frame.bind('<Left>', leftKey)
frame.bind('<Right>', rightKey)
frame.bind('<Up>', upKey)
frame.bind('<Down>', downKey)
frame.bind('c', connect)
frame.bind('q', disconnect)
frame.bind('w', wKey)
frame.bind('s', sKey)
frame.bind('a', aKey)
frame.bind('d', dKey)
frame.bind('<space>',takeoff)
frame.bind('b',cal)
frame.bind('l',land)
frame.focus_set()
frame.pack()
main.mainloop()