import cv2 as cv

face_cascade = cv.CascadeClassifier('C://Users/HARSHIT SINGH/Github/Python/opencv/face_detaction/haar_face.xml')

def detect():
    cap = cv.VideoCapture(0)
    while True:
        _, img = cap.read()
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        face = face_cascade.detectMultiScale(gray, 1.1, 2)
        for (x,y,w,h) in face:
            cv.rectangle(img, (x,y), (x+w,y+h), (255, 0, 0), 2)
            
        cv.imshow('Face Detect', img)

        if cv.waitKey(1) == 27:
            break
    cap.release()

detect()