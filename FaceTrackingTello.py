from utlis import *
from cv2 import cv2

w,h = 360,240
pid = [0.5,0.5,0]
pError = 0
startCounter = 0

myDrone = initializeTello()

while True:

    ## Flight
    if startCounter == 0:
        myDrone.takeoff()
        startCounter = 1

    ## Step 1 Stream Video to Computer
    img = telloGetFrame(myDrone,w,h)

    ## Step 2 Find and Track Face
    img, info = findFace(img)
    print(info[0][0])

    cv2.imshow('Image', img)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        myDrone.land()
        break
    
    ## Step 3 PID Control
    pError = trackFace(myDrone,info,w,pid,pError)
