import cv2
import math
import numpy as np

################################################################################

print 'Load Image'

img1 = cv2.imread('D:/11.jpg') #query image
img2 = cv2.imread('D:/12.jpg') #train image

rows, cols, channels = img1.shape

img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

imgGray1 = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
imgGray2 = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)
################################################################################

print 'SURF Feature Detection'

# initialize ORB object with default values
surf = cv2.SURF(1000)

# find keypoints
keypoint1, descriptor1 = surf.detectAndCompute(imgGray1, None)
keypoint2, descriptor2 = surf.detectAndCompute(imgGray2, None)

bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)  
matches = bf.match(descriptor1, descriptor2)  

def drawMatches(img1, kp1, img2, kp2, matches):


    rows1 = img1.shape[0]
    cols1 = img1.shape[1]
    rows2 = img2.shape[0]
    cols2 = img2.shape[1]

    out = np.zeros((max([rows1,rows2]),cols1+cols2,3), dtype='uint8')

    # Place the first image to the left
    out[:rows1,:cols1] = np.dstack([img1])

    # Place the next image to the right of it
    out[:rows2,cols1:] = np.dstack([img2])

    # For each pair of points we have between both images
    # draw circles, then connect a line between them
    for mat in matches:

        # Get the matching keypoints for each of the images
        img1_idx = mat.queryIdx
        img2_idx = mat.trainIdx

        # x - columns
        # y - rows
        (x1,y1) = kp1[img1_idx].pt
        (x2,y2) = kp2[img2_idx].pt

        # Draw a small circle at both co-ordinates
        # radius 4
        # colour blue
        # thickness = 1
        cv2.circle(out, (int(x1),int(y1)), 4, (255, 0, 0), 1)   
        cv2.circle(out, (int(x2)+cols1,int(y2)), 4, (255, 0, 0), 1)

        # Draw a line in between the two points
        # thickness = 1
        # colour blue
        cv2.line(out, (int(x1),int(y1)), (int(x2)+cols1,int(y2)), (255, 0, 0), 1)


    # Show the image


    # Also return the image if you'd like a copy
    return out
# combine two images into one
view = drawMatches(img1, keypoint1,img2, keypoint2, matches[:100])
cv2.imshow('Matched Features', view)
cv2.waitKey(0)
cv2.destroyWindow('Matched Features') 
#img3 = cv2.drawMatchesKnn(img1,keypoint1,img2,keypoint2,matches[:10], flags=2)
################################################################################

print 'Goodbye!'