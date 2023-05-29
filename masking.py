import cv2 as cv 
import numpy as np 

img = cv.imread('dig.jpg')
blank =np.zeros((500,500,3), dtype='uint8')

massk =cv.circle(blank , (img.shape[1]//2+45,img.shape[0]//2),100,cv.COLORMAP_WINTER,-1)
cv.imshow('blbank',massk) 


maksed = cv.bitwise_and(img,massk)
cv.imshow('testmaske',maksed) 

cv.waitKey(0)