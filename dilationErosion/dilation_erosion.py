# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 13:43:15 2022

@author: Erdal
"""

import cv2
import numpy as np

image=cv2.imread("eozbademci.png")

kernel=np.ones((5,5),np.uint8)

dilation1=cv2.dilate(image,kernel,iterations=1)
erosion=cv2.erode(image,kernel,iterations=1)
dilation2=cv2.dilate(erosion,kernel,iterations=1)

cv2.imshow("image",image)
cv2.imshow("image-dilation",dilation1)
cv2.imshow("erosion",erosion)
cv2.imshow("erosion-dilation",dilation2)

cv2.waitKey(0)
cv2.destroyAllWindows()