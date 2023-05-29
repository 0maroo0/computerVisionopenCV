import cv2 as cv 
import numpy as np


img = cv.imread('dig.jpg')

cv.imshow('testmaske',img) 

gray= cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('testmaske',gray) 

lap =cv.Laplacian(gray ,cv.CV_64F)
lap =np.uint8(np.absolute(lap))
cv.imshow('lab' ,lap)

soblecx =cv.Sobel(gray ,cv.CV_64F,1,0)
soblecy =cv.Sobel(gray ,cv.CV_64F,0,1)
cv.imshow('sobelx' ,soblecx)
cv.imshow('sobely' ,soblecy)
combined_soble= cv.bitwise_or(src1=soblecx, src2=soblecy)
cv.imshow('sobely' ,combined_soble)

canny= cv.Canny(gray,150,175)
cv.imshow('sobely' ,canny)

 
cv.waitKey(0)