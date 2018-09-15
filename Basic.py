#author@SwapnilPanwala
import cv2
import numpy as np

#reading an image
img = cv2.imread("C:\\Users\\Swapnil Panwala\\Desktop\\Proj\\Self_Driving_Bot\\lane dection\\M1\\lines.png")

#Converting a RGB image to GRAY
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Perform Canny Edge Detection
edges=cv2.Canny(gray, 75, 150)

#The Standard Hough Transform
#lines = cv2.HoughLines(edges, 1, np.pi/180, 50)
#The Probabilistic Hough Line Transform. This is a more efficient implementation as it takes random points.
#maxLineGap is used to fill gaps between lines
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 30, maxLineGap=250)

#To check the hough line points
#print(lines)

#Draw lines
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1,y1), (x2,y2), (0,255,0), 3)

#Displays an image in the specified window.
cv2.imshow("image",img)

#Waits for a pressed key.Delay in milliseconds. 0 is the special value that means “forever”.
cv2.waitKey(0)

#Destroys all of the HighGUI windows.
cv2.destroyAllWindows()
