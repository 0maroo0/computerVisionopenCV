import cv2 as cv 
import numpy as np 


def rescale(frame , scale=1):
    width = int(frame.shape[1] *scale)
    height = int(frame.shape[0] *scale)
    dima =(width ,height)


    return  cv.resize(frame,dima,interpolation=cv.INTER_AREA)

blank =np.zeros((500,500,3), dtype='uint8')
blank[200:300,250:450]= 100,50,50
cv.imshow('blank',blank) 

circel =cv.circle(blank.copy() ,(200,200), 200,255,-1)

cv.imshow('cirvel', circel)
# img = cv.imread('dig.jpg')

# cv.rectangle(img,(0,0),(img.shape[1]//2,img.shape[0]//2),(0,255,0),thickness=3)
# cv.line(img,(img.shape[1]//2,img.shape[0]//2),((img.shape[1]//2)+50,(img.shape[1]//2)+50),(0,255,0),thickness=3)
# cv.putText(img , 'hello',org=(300,200), fontFace= cv.FONT_HERSHEY_DUPLEX ,color=(0,255,0) ,fontScale=1,  thickness=4)
# cv.imshow('blbank',img) 



cv.waitKey(0)