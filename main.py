#External Libraries
import apriltag, cv2, time

#Local Files
from config import detection_options
from utils import log

#Setup for Detections
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
detector = apriltag.Detector(detection_options)



while True:
    log("Apriltag detection has begun...", "[INFO]")
    ret, image = cap.read()
    if not ret:
        break
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_wid = image.shape[1]
    image_hgt = image.shape[0]
    results = detector.detect(img)
    key = cv2.waitKey(1)
    if key == 27:  # ESC
        break

    #Iterates over detected apriltags
    for result in results:

        (side_a, side_b, side_c, side_d) = result.corners #Gets Corners
        (center_x, center_y)= (int(result.center[0]), int(result.center[1])) #Get Center
        family = result.tag_family.decode("utf-8") #Gets Tag Family

        #Gets sides from corner data
        side_b = (int(side_b[0]), int(side_b[1]))
        side_c = (int(side_c[0]), int(side_c[1]))
        side_d = (int(side_d[0]), int(side_d[1]))
        side_a = (int(side_a[0]), int(side_a[1]))

        #Draws over the corners and center of apriltags 
        cv2.circle(image, (center_x, center_y), 2, (255,255,0), -1)
        cv2.line(image, side_a, side_b, (0,100,0), 2)
        cv2.line(image, side_b, side_c, (0,100,0), 2)
        cv2.line(image, side_c, side_d, (0,100,0), 2)
        cv2.line(image, side_d, side_a, (0,100,0), 2)
        id_ = str(f"ID: {result.tag_id}")
        #Draws tag type if resolution is sufficient

        cv2.putText(image, id_, (center_x - 20, center_y + 30),
        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 125, 255), 2, cv2.LINE_AA)

        log(f"Family: {family}, ID: {result.tag_id} Center_X: {center_x}, Center_Y: {center_y}")

    cv2.imshow("Apriltags Output", image)
cap.release()
cv.destroyAllWindows()