import cv2 as cv

img = cv.imread('./Resources/Photos/cat.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# simple tresdholding
threshold, thresh = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)
cv.imshow('Simple Threshold', thresh)

# Inverse tresdholding
threshold, threshinv = cv.threshold(gray, 100, 255, cv.THRESH_BINARY_INV)
cv.imshow('Inverse Threshold', threshinv)

# adaptive tresdholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY, 11,8)
cv.imshow('Adaptive', adaptive_thresh)

cv.waitKey(0)