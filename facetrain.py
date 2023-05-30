import os 
import cv2 as cv
import numpy as np

player = ['mohamed','marwan']

DIR =r'E:\cv2\face'

facedete =cv.CascadeClassifier('face_hair.xml')


feratured=[]
labels=[]

def player_train():
    for person in player:
        path=os.path.join(DIR,person)
        label =player.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path,img)


            img_arr =cv.imread(img_path)
            gray =cv.cvtColor(img_arr,cv.COLOR_BGR2GRAY)

            face_react = facedete.detectMultiScale(gray,scaleFactor =1.1,minNeighbors=1)

            for (x,y,w,h) in face_react:
                 faces_roi =gray[y:y+h ,x:x+w]
                 feratured.append(faces_roi)
                 labels.append(label)
#                cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

player_train()
print("done trainging")

feratured = np.array(feratured, dtype='object')
labels = np.array(labels)

face_reco = cv.face.LBPHFaceRecognizer_create()

face_reco.train(feratured,labels)

face_reco.save('face_trained.yml')
np.save('feratured.npy', feratured)
np.save('labels.npy', labels)
