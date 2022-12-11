import cv2, numpy as np
from config import cameraoptions

cap = cv2.VideoCapture(cameraoptions["videoid"])
cap.set(cv2.CAP_PROP_FRAME_WIDTH, cameraoptions["width"])
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, cameraoptions["height"])
cv2.setUseOptimized(cameraoptions["optimizedcv2"])
scan = True
while scan:
        # Get camera input
        ret, img = cap.read()
        if not ret:
            break
        key = cv2.waitKey(1)
        if key == 27: 
            scan = False
        img = cv2.cvtColor(np.float32(img), cv2.COLOR_RGB2GRAY)
        ret,thresh1 = cv2.threshold(img,120,255,cv2.THRESH_BINARY)
        ret,thresh2 = cv2.threshold(img,120,255,cv2.THRESH_BINARY_INV)



        cv2.imshow("AA", thresh1)
cap.release()
cv2.destroyAllWindows()
        # Get camera output