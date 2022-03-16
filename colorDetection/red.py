# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 17:28:10 2022

@author: Erdal
"""
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    low_red = np.array([161, 155, 84])
    high_red = np.array([179, 255, 255])    
    mask = cv2.inRange(hsv_frame, low_red, high_red)
    
    cv2.imshow("Output",mask)   
    
    if cv2.waitKey(30) & 0xFF== ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
