import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('./Resources/Photos/cat.jpg')
# cv.imshow('Cat', img)

# BGR to greyscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('HSV', hsv)

# BGR to l*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow('LAB', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

plt.imshow(rgb)
plt.show()


# # HSV to BGR
# lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
# cv.imshow('LAB --> BGR', lab_bgr)



cv.waitKey(0)