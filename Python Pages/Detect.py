"""
Detect.py - runs Open CV + TensorFlow Litr (or another YOLO model) for person detection
camera.py - captures frames from a CSI or SUB camera
Main.py - runs the main loop, calls camera and detect, and sends data to the web server
"""
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()    # grab the latest frame from camera
    
    cv2.imshow("Camera", frame)  # display it in a window called "Camera"
    
    # wait 1ms between frames, quit if you press Q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()  # close the window cleanly when done