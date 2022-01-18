# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 13:05:57 2022

@author: eozbademci
"""
import cv2
import numpy as np

goruntu=cv2.imread("2.jpg")

medianFilter3=cv2.medianBlur(goruntu,3)
medianFilter5=cv2.medianBlur(goruntu,5)
medianFilter7=cv2.medianBlur(goruntu,7)


cv2.imshow("Orjinal Resim",goruntu)
cv2.imshow("MedianBlur3",medianFilter3)
cv2.imshow("MedianBlur5",medianFilter5)
cv2.imshow("MedianBlur7",medianFilter7)

cv2.waitKey(0)
cv2.destroyAllWindows()
