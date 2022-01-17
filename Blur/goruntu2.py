# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 21:40:47 2022

@author: Erdal
"""
import cv2
import numpy as np

goruntu=cv2.imread("2.jpg")

meanFilter=cv2.blur(goruntu,(3,3))
meanFilter2=cv2.blur(goruntu,(5,5))
meanFilter3=cv2.blur(goruntu,(7,7))

cv2.imshow("Orjinal Resim",goruntu)
cv2.imshow("Degistrilimis Resim 3x3",meanFilter)
cv2.imshow("Degistrilimis Resim 5x5",meanFilter2)
cv2.imshow("Degistrilimis Resim 7x7",meanFilter3)

cv2.waitKey(0)
cv2.destroyAllWindows()
