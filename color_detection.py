import numpy as np
import cv2
cap = cv2.VideoCapture(0) #0-> set up the 1th webcam
while True:
    ret, frame = cap.read() #frame: imageitself, ret-> capture works properly or not
    width = int(cap.get(3)) #3-> width
    height = int(cap.get(4))#4-> height
    #goal BGR ->HSV why? method to detect the color require the hsv image
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #pick lower and upper bound for specific color to display
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue) #return an image with color in the range and other pixels blacked out (->(0,0,0))
    #pixels in the range gets a '1', else it gets '0' in the mask
    #apply the mask to the original image(keep the pixels of the image where the mask covers)
    result = cv2.bitwise_and(frame, frame, mask=mask) #img1, img2, blend them together by the mask
    cv2.imshow("frame", result)
    if cv2.waitKey(1) == ord('q'): #wait 1 millsec -> return ascii key val, press q to break
        break
cap.release() #release camera resource
cv2.destroyAllWindows()
