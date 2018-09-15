#author@SwapnilPanwala
import cv2
import numpy as np 

#Reading a vedio
vedio = cv2.VideoCapture("C:\\Users\\Swapnil Panwala\\Desktop\\Proj\\Self_Driving_Bot\\lane dection\\M1\\road_car_view.mp4")

#Processing the vedio frame by frame
while True:
    #Reading the frame. ret returs true or false. If its false than vedio has finished.
    ret, orj_frame = vedio.read()

    #To run the vedio for infinte time
    if not ret:
        #Loading the vedio again
        vedio = cv2.VideoCapture("C:\\Users\\Swapnil Panwala\\Desktop\\Proj\\Self_Driving_Bot\\lane dection\\M1\\road_car_view.mp4")
        continue
    
    #Using Gaussian Blur for higher accuracy
    frame = cv2.GaussianBlur(orj_frame, (5,5), 0)

    #Converting RGB colorspace to HSV(Hue(H), Saturation(S) and Value(V)) colorspace for extracting a colored object
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #Creating a range of color that need to be detected
    low_yellow = np.array([18, 94, 140])
    up_yellow = np.array([48, 255, 255])
    #Selection only those colors that fall in the specified range
    mask = cv2.inRange(hsv, low_yellow, up_yellow)

    #Detection of egdes
    edges=cv2.Canny(mask, 75, 150)

    #Detection of lines
    lines=cv2.HoughLinesP(edges, 1, np.pi/180, 50, maxLineGap=50)

    #Ploting the lines on each frame
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(frame, (x1, y1), (x2,y2), (0,255,0), 5)

    
    cv2.imshow("frame",frame)
    cv2.imshow("edges",edges)
    key=cv2.waitKey(25)
    if(key==27):
        break
#Calling the Destructor
vedio.release()
cv2.destroyAllWindows()