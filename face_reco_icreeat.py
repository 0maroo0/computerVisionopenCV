import cv2 as cv
import numpy as np



facedete =cv.CascadeClassifier('face_hair.xml')

player = ['mohamed','marwan']

feratured= np.load('feratured.npy', allow_pickle=True)
labels=np.load('labels.npy', allow_pickle=True)

face_reco = cv.face.LBPHFaceRecognizer_create()
face_reco.read('face_trained.yml')


img =cv.imread('01.jpg')


gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)

faces_react_reco = facedete.detectMultiScale(gray,1.1,4)
i =0
for (x,y,w,h) in faces_react_reco:
        faces_roi =gray[y:y+h ,x:x+h]

        label , cinfid = face_reco.predict(faces_roi)
        print(f'label ={label} confid {cinfid} ')
        cv.putText(img , str(player[label]),( 20 +(i*20),20+(i*20)) , cv.FONT_HERSHEY_COMPLEX,1.0 ,(0.255,0), thickness=2 )
        cv.putText(img , str(player[label]),( 20,20) , cv.FONT_HERSHEY_COMPLEX,1.0 ,(0.255,255), thickness=2 )

        cv.rectangle(img,(x,y) , (x+w,y+h) , (0,255,0), thickness=2)
        i +=1


cv.imshow('test', img) 

cv.waitKey(0)