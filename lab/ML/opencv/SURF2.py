import cv2  
import numpy as np  
  
img = cv2.imread("D:/zw.jpg")  
  
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  
cv2.imshow("gray", gray)  
# surf.hessianThreshold=3000  
surf = cv2.SURF()  
  
kp,res = surf.detectAndCompute(gray,None)  
print res.shape  
  
#img = cv2.drawKeypoints(img,kp,None,(255,0,255),4)  
print(len(kp))  
  
for k in kp:
    cv2.circle(img,(int(k.pt[0]),int(k.pt[1])),1,(0,255,0),-1)  

cv2.namedWindow("SURF")  
cv2.imshow("SURF", img)  
cv2.waitKey(0)  
cv2.destroyAllWindows()