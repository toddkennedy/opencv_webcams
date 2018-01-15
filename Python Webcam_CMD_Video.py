# Reference:
# Bielinskas, V. (2017, June 1). Intro and loading Images - OpenCV with Python
# for Image and Video Analysis 1. Retrieved October 28, 2017
# from https://www.youtube.com/watch?v=1XTqE7LFQjI

import cv2, time

#1. Create an object. Zero for external camera
video = cv2.VideoCapture(0) # The (0) represents webcam that comes with computer

# video = cv2.VideoCapture(1) # The (1) represents an external USB webcam

a = 0

while True:

    a = a + 1

    #3. Create a frame object
    check, frame = video.read()

    print(check)
    print(frame) #Representing image

    #6. Converting to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #4. Show the frame!
    #cv2.imshow("Capturing", frame)
    cv2.imshow("Capturing", gray)

    #5. For press any key to out (miliseconds)
    #cv2.waitKey(0)

    #7. For play video
    key = cv2.waitKey(1)

    if key == ord('q'):
        break

#2. Shutdown the camera
video.release()
cv2.destroyAllWindows()
