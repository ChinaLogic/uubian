import cv2
img = cv2.imread('D:/zw.jpg')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  
dst = cv2.convertScaleAbs(gray)
#cv2.imshow('dst',dst)
#cv2.imshow('dst',dst)


s = cv2.SURF(20)
keypoints = s.detect(gray)
for k in keypoints:
    cv2.circle(img,(int(k.pt[0]),int(k.pt[1])),1,(0,255,0),-1)
cv2.imshow('SURF_features',img)
cv2.waitKey()
cv2.destroyAllWindows()