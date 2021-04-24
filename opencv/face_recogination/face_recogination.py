import cv2 as cv
import numpy as np
import os

recognizer = cv.face.LBPHFaceRecognizer_create()
recognizer.read('./trainer/trainer.yml')
cascadePath = './haarcascade_frontalface_default.xml'
faceCascade = cv.CascadeClassifier('./haarcascade_frontalface_default.xml')

font = cv.FONT_HERSHEY_TRIPLEX

id = 0

names = [0,1,2,3,4,5,6,7,8,9]
cam = cv.VideoCapture(0)
cam.set(3, 640)
cam.set(4, 480)

minW = 0.1*cam.get(3)
minH = 0.1*cam.get(3)

while True:
    ret, img = cam.read()
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray, 1.2, 5, 
        minSize = (int(minW), int(minH))
        )
    
    for (x,y,w,h) in faces:
        cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
        id, confidence = recognizer.predict(gray[y:y+h, x:x+w])
        
        if(confidence<100):
            id = names[id]
            confidence = f'{round(100-confidence)}%'
        else:
            id = "Unknown"
            confidence = f'No face Detect'
        
        cv.putText(img, str(id), (x+5, y+5),font,1,(255,0,0),2)
        # print(confidence)

    cv.imshow('camera', img)
    k = cv.waitKey(10) & 0xff
    if k == 27:
        break

print('[INFO]Exiting Program')
cam.release()
cv.destroyAllWindows()