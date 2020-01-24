#!/usr/bin/python36
import cv2
cap = cv2.VideoCapture(0)
ret ,photo = cap.read()
cv2.imwrite('/root/Desktop/myphoto.png',photo)
cv2.imshow('hi',photo)
cv2.waitKey()
cv2.destroyAllWindows()
cap.release()
