import cv2
import numpy as np

cap=cv2.VideoCapture(0)
yellow_lower = np.array([22, 93, 0])
yellow_upper = np.array([45, 255, 255])

while True:
    ret, frame= cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
    mask = cv2.inRange(hsv,yellow_lower, yellow_upper)
    cv2.imshow('mask', mask)
    cv2.imshow('frame',frame)
    if cv2.waitKey(10)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()