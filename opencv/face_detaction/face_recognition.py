import numpy as np
import cv2 as cv

haar_cascade = cv.CascadeClassifier('haar_face.xml')

people = ['Harshit Singh' ,'Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
# features = np.load('./features.npy', allow_pickel =True)
# lables = np.load('./labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('./face_trained.yml')

img = cv.imread('../Resources/Faces/val/Harshit Singh/2.png')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person', gray)

#Detect the face in thr image
faces_react = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
for (x,y,w,h) in faces_react:
    faces_roi = gray[y:y+h, x:x+h]

    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {label} with a confidence of {confidence}')

    cv.putText(img, str(people[label]), (50,50), cv.FONT_HERSHEY_COMPLEX, 1.0, (255,255,255), thickness=2)
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

cv.imshow('Detected Face', img)

cv.waitKey(0)