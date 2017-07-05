import numpy as np
import cv2
from find_obj import filter_matches,explore_match
import matplotlib.pyplot as plt

img1 = cv2.imread('D:/11.jpg',0)          # queryImage
img2 = cv2.imread('D:/12.jpg',0) # trainImage

# Initiate SIFT detector
#sift = cv2.SIFT()
sift = cv2.SURF()
# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)

# BFMatcher with default params
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2, k=2)

# Apply ratio test
good = []
for m,n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])

# cv2.drawMatchesKnn expects list of lists as matches.
p1, p2, kp_pairs = filter_matches(kp1, kp2, matches)
vis=explore_match('IMAGE', img1, img2, kp_pairs)  # cv2 shows image
cv2.imwrite("D:\\cat2.jpg", vis)
cv2.waitKey()
cv2.destroyAllWindows()

