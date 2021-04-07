import cv2 as cv


def rescaleFrame(frame, scale=0.2):
    # image, videos and live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    # live videos
    capture.set(3,width)
    capture.set(3,height)
    dimensions = (width,height)







img = cv.imread('./Resources/Photos/cat_large.jpg')
resied_img = rescaleFrame(img)
cv.imshow('Cat', resied_img)
cv.waitKey(0)


capture = cv.VideoCapture('./Resources/Videos/dog.mp4')
while True:
    isTrue, frame = capture.read()

    frame_resize = rescaleFrame(frame)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resize)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
