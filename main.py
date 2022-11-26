#!/usr/bin/env python

import apriltag, cv2, numpy as np, time
from datetime import datetime

#Local Files
from config import detection_options, cameraoptions
###################################################


def log(message, level="[INFO]"):
    now = datetime.now()
    formatted_time = now.strftime("%H:%M:%S, %d/%m/%Y")
    print(f"{level}: {message}  |{formatted_time}")

def main():

    # Sets all the parameters for detection and vision
    cap = cv2.VideoCapture(cameraoptions["videoid"])
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, cameraoptions["width"])
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, cameraoptions["height"])
    detector = apriltag.Detector(detection_options)

    scan = True
    ids = [] # Holds all of the detected tags' IDs
    centers = [] # Holds all of the detected tags' centers
    closest_center = (np.int16(0), np.int16(0)) #x,y of the closest tag to  the center
    closest_id = (np.int16(0), np.int16(0)) #ID of closest tag to the center

    log("Apriltag detection has begun...", "[INFO]")

    while scan:
        # Get camera input
        ret, image = cap.read()
        if not ret:
            break
        key = cv2.waitKey(1)
        if key == 27: 
            scan = False
        (image_h, image_w) = image.shape[:2] #Gets height and width of camera image
        screen_center = np.array((image_w//2, image_h//2)) #Cam Center
        img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #Converts to black and white

        scan_results = detector.detect(img)
        for result in scan_results:
    
            (corner_a, corner_b, corner_c, corner_d) = result.corners #Get Corners
            (center_x, center_y)= (np.int16(result.center[0]), np.int16(result.center[1]))#Get Center
            family = result.tag_family.decode("utf-8") #Get Tag Family

            if len(centers) < len(scan_results): #Append current tag's center to list 
                centers.append((center_x, center_y))
                ids.append(result.tag_id) 

            #Gets sides from corner data
            side_b = (np.int16(corner_b[0]), np.int16(corner_b[1]))
            side_c = (np.int16(corner_c[0]), np.int16(corner_c[1]))
            side_d = (np.int16(corner_d[0]), np.int16(corner_d[1]))
            side_a = (np.int16(corner_a[0]), np.int16(corner_a[1]))

            #Drawing operations
            cv2.circle(image, screen_center, 3, (0, 0, 0), -1) #Screen's center
            cv2.circle(image, (center_x, center_y), 2, (255,255,0), -1) #Crosshair
            cv2.circle(image, closest_center, 5, (255,255, 255), -1) #Closest tag's center
            cv2.line(image, side_a, side_b, (0,100,0), 2) #Side
            cv2.line(image, side_b, side_c, (0,100,0), 2) #Side
            cv2.line(image, side_c, side_d, (0,100,0), 2) #Side
            cv2.line(image, side_d, side_a, (0,100,0), 2) #Side

            #Draws the ID of the apriltag onto it
            cv2.putText(image, str(f"ID: {result.tag_id}"), (center_x - 20, center_y + 30),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 125, 255), 2, cv2.LINE_AA)

            log(f"Family: {family}, ID: {result.tag_id} Center_X: {center_x}, Center_Y: {center_y} Centermost: {closest_center} ID:{closest_id}")

        #Gets nearest tag to center using np.linalg.norm
        if len(centers) == len(scan_results) and len(scan_results) != 0:
            distances = np.linalg.norm(centers-screen_center, axis=1)
            closest_center, closest_id = centers[np.argmin(distances)], ids[np.argmin(distances)]
            centers = []
            ids = []
        elif len(scan_results) == 0:
            closest_center, closest_id = (0, 0), 0
        cv2.imshow("Apriltags Output", image)

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
