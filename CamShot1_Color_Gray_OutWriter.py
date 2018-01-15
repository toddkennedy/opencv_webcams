# Sentdex. (2015, December 17). Intro and loading Images - OpenCV with Python
# for Image and Video Analysis 1. Retrieved from
# https://www.youtube.com/watch?v=Jvf5y21ZqtQ&index=2&list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq

import cv2
import numpy as np

cap = cv2.VideoCapture(0) # The (0) represents webcam that comes with computer

# cap = cv2.VideoCapture(1) # The (1) represents an external USB webcam

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    out.write(frame)

    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
out.release()
cv2.destroyAllWindows()
