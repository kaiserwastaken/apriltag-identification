# Dependencies
Install using: `pip install -r requirements.txt`






# Documentation

### Configuration

This configuration file defines two dictionaries, cameraoptions and detection_options, which contain settings for a camera and for AprilTag detection, respectively.

The cameraoptions dictionary has four keys:

    videoid: an integer value that represents the camera ID on the device. This can range from 0 to 255, but is most likely to be 0, 1, or 2.
    height: an integer value that specifies the height of the video frames captured by the camera. This should be kept as small as possible for performance reasons.
    width: an integer value that specifies the width of the video frames captured by the camera. This should be kept as small as possible for performance reasons.
    optimizedcv2: a boolean value that specifies whether to use optimized OpenCV 2 functions. This should be set to True, but can be changed to False if there are any problems.
    debug_text: a boolean value that specifies whether to display debug text on the video frames. This can be set to True or False.

The detection_options dictionary is an instance of the DetectorOptions class from the apriltag module. It has several keys:

    families: a string that specifies the tag family to use for detection. In this case, it is set to tag16h5, which is one of the available AprilTag families.
    border: an integer value that specifies the border size of the tag.
    nthreads: an integer value that specifies the number of threads to use for detection.
    quad_decimate: a floating-point value that specifies the decimation factor for the quadrature filter.
    quad_blur: a floating-point value that specifies the sigma value for the quadrature filter's Gaussian blur. This value is a tradeoff between detection distance and speed.
    refine_edges: a boolean value that specifies whether to use edge refinement. 
    refine_decode: a boolean value that specifies whether to use decoding refinement. 
    refine_pose: a boolean value that specifies whether to use pose refinement.
    debug: a boolean value that specifies whether to display debugging information.
    quad_contours: a boolean value that specifies whether to use quad contours.

### Main Loop

This code imports several modules and defines a function, main(), which uses the AprilTag library to detect AprilTags in video frames from a camera. The main() function has several steps:

    1 - It initializes a VideoCapture object from the cv2 module, using the videoid and width/height values from the cameraoptions dictionary. It also creates an instance of the Detector class from the apriltag module, using the detection_options dictionary.
    2 - It sets a boolean variable, scan, to True and initializes empty lists for detected tag IDs and centers, as well as a tuple for the closest tag to the center of the screen.
    3 - It enters a loop that continues as long as scan is True. In each iteration of the loop, it captures a frame from the camera, checks for the ESC key press, and converts the frame to grayscale.
    4 - It detects AprilTags in the grayscale frame using the detector object and saves the results to a variable, scan_results. If the debug_text option is enabled, it displays the number of detected tags and the ID of the closest tag to the center of the screen on the frame.
    5 - For each detected tag, it gets the tag's corners, center, and family and draws a crosshair, rectangle, and ID on the frame. It also updates the closest tag to the center of the screen, if necessary.
    6 - If the ESC key was pressed, it sets scan to False and exits the loop.

    The main() function also includes a log() function, which is used to print messages to the console with timestamps. This can be useful for debugging or tracking the progress of the detection.

### Stabilized Version

This code is similar to the previous example, but it also uses the VidStab class from the vidstab module to stabilize the camera frames before detecting AprilTags.

The main() function has several additional steps at the beginning:

    1 - It creates an instance of the VidStab class and initializes a VideoCapture object, detector object, and cv2 optimization settings in the same way as the previous example.
    2 - It enters a loop that continues as long as scan is True. In each iteration of the loop, it captures a frame from the camera, checks for the ESC key press, and converts the frame to grayscale.
    3 - It passes the frame to the stabilize_frame() method of the stabilizer object to stabilize the frame. If the stabilized frame is None, it exits the loop.
    4 - It detects AprilTags in the grayscale frame using the detector object and saves the results to a variable, scan_results. If the debug_text option is enabled, it displays the number of detected tags and the ID of the closest tag to the center of the screen on the frame.
    5 - For each detected tag, it gets the tag's corners, center, and family and draws a crosshair, rectangle, and ID on the frame. It also updates the closest tag to the center of the screen, if necessary.
    6 - It displays the stabilized frame using the cv2.imshow() function from the cv2 module and waits for a specified amount of time using the cv2.waitKey() function.
    7 - If the ESC key was pressed, it sets scan to False and exits the loop.

    The rest of the code is the same as the previous example, including the log() function. This version of the code uses video stabilization to reduce the effects of camera motion on the detection of AprilTags.
