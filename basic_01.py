# import opencv
import cv2
#import numpy
import numpy as np
#import pyzbar
from pyzbar.pyzbar import decode

# read the image using opencv
# img = cv2.imread("image_01.png")

# capture video using opencv
cap = cv2.VideoCapture(0)

#infinite loop
while True:
    success, img = cap.read()

    if not success:
        break

     # print(decode(img))

    for code in decode(img):
        decoded_data = (code.data.decode("utf-8"))

        rect_pts = code.rect

        if decoded_data:
            pts = np.array([code.polygon],np.int32)
            cv2.polylines(img,[pts],True,(255,0,0),3)
            cv2.putText(img,str(decoded_data),(rect_pts[0],rect_pts[1]),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

    cv2.imshow("image",img) 

    #show the image
    cv2.imshow("image",img) 

    #wait until esc key is present - 0
    # wait until 1 ms
    cv2.waitKey(1)

#release the captured frames
cap.release()

#destroy all the windows
# cv2.destroyAllWindows()
