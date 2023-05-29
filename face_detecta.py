import cv2 as cv 
import numpy as np





img = cv.imread('kabalaw.jpg')

#cv.imshow('testmaske',img) 


gray= cv.cvtColor(img , cv.COLOR_BGR2GRAY)
# cv.imshow('testmaske',gray) 


facedete =cv.CascadeClassifier('face_hair.xml')


face_react = facedete.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=1)
print(f'Number of faces found = {len(face_react)}')

print(facedete)

for (x,y,w,h) in face_react:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)
    if facedete!=0:
        cv.putText(img,'it\'s person',org=(x,y), fontFace=cv.FONT_ITALIC, fontScale=1, thickness=3, color=(0,255,0))

cv.imshow('Detected Faces', img)

cv.waitKey(0)