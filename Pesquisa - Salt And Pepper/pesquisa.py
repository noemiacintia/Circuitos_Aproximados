import cv2 

img = cv2.imread('teste2.png')
img_median = cv2.medianBlur(img, 5)

cv2.imshow('img', img_median)
cv2.waitKey(0)
cv2.dstroyAllWindowns