import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while True:
    ret,img = cap.read()
    if ret:
       # gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        hsv= cv.cvtColor(img, cv.COLOR_BGR2HSV)
        ub=np.array([50,40,40]) #umbral bajo 
        ua=np.array([80,255,255])# umbral alto 
        mask=cv.inRange(hsv,ub,ua)
        result = cv.bitwise_and(img,img,mask=mask)
        cv.imshow('Video',img)
        #cv.imshow('Video_gray',gray)

        k=cv.waitKey(1) & 0xFF # se tiene que apretar la tecla esc para que se cierre la ventana
        if k==27:
            break
    else:
        break


cap.release()
cv.destroyAllWindows()

  