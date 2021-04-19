import cv2 as cv
import numpy as np
from PIL import ImageGrab

def screenrecorder():
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    out = cv.VideoWriter('output.avi', fourcc,5.0, (1360, 768))

    while True:
        img = ImageGrab.grab()
        img_np = np.array(img)
        frame = cv.cvtColor(img_np, cv.COLOR_BGR2RGB)
        cv.imshow('Scrren Recoder', frame)
        out.write(frame)

        if cv.waitKey(1) == 27:
            break
    out.release()
    cv.destroyAllWindows

screenrecorder()