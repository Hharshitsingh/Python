import cv2 as cv

imgcapture = cv.VideoCapture(0)
results = True

while(results):
    ret, frame = imgcapture.read()
    cv.imwrite('test.png', frame)
    results = False
    print('done!')

imgcapture.release()