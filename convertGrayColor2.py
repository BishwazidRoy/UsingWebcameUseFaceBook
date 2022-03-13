import cv2
import numpy as np

cap=cv2.VideoCapture(0)
yellow_lower = np.array([22, 93, 0])
yellow_upper = np.array([45, 255, 255])

while True:
    ret, frame= cap.read()
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',gray)
    if cv2.waitKey(10)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()