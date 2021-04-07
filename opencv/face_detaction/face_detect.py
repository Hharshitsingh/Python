import cv2 as cv

img = cv.imread('../Resources/Photos/group 1.jpg')
cv.imshow('pic', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

# faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

print(f"Number of face Found = {len(faces_rect)}")

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (150,100,250),thickness=2)


cv.imshow('Detected Face', img)

cv.waitKey(0)