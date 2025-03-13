import cv2 as cv 
import numpy as np

img =cv.imread('Ejemplos/Ejemplo_OpenCV/ejemplo_Manzana.jpeg')   
hsv= cv.cvtColor(img, cv.COLOR_BGR2HSV)

ub=np.array([0,40,40]) #umbral bajo 
ua=np.array([10,255,255])# umbral alto 

ub1=np.array([170,40,40]) #umbral bajo 
ua1=np.array([180,255,255])# umbral alto 

mask1 = cv.inRange(hsv, ub, ua)
mask2 = cv.inRange(hsv, ub1, ua1)

mask = mask1 +mask2

result = cv.bitwise_and(img,img,mask=mask)

cv.imshow('mask',mask)
cv.imshow('mask1',mask1)
cv.imshow('mask2',mask2)
cv.imshow('hsv',hsv)
cv.imshow('result',result)
cv.waitKey(0)
cv.destroyAllWindows()