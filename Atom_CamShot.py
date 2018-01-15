# Reference:
# Sentdex. (2015, December 31). Edge Detection and Gradients - OpenCV with
# Python for Image and Video Analysis 10. Retrieved October 28, 2017 from
# https://www.youtube.com/watch?v=CJMCoAsK-h0&list=PLhN5_Op27hzUA5NsXwkgSqX05IFBT8aEe&index=18

import cv2
import numpy as np

cap = cv2.VideoCapture(0) # The (0) represents webcam that comes with computer

# cap = cv2.VideoCapture(1) # The (1) represents an external USB webcam

while True:
#    ret, frame = cap.read()
    _, frame = cap.read()

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
