#coding=utf-8  
import cv2  
import numpy as np    

img = cv2.imread("F:/1.jpg", 0)  
gray_lap7 = cv2.Laplacian(img,cv2.CV_16S,ksize = 3)
gray_lap3 = cv2.Laplacian(gray_lap7,cv2.CV_16S,ksize = 3)  
dst = cv2.convertScaleAbs(gray_lap3)  
cv2.imshow('laplacian',dst)  
cv2.waitKey(0)  
cv2.destroyAllWindows()  
