import apriltag, cv2, numpy as np


"""
To Do:
Be able to get closest apriltag to any point on screen, not just center.
Be able to iterate through video devices to get the correct one easily.
Also include a single file version.
Auto calibration.
"""





#Camera Options
cameraoptions = {
    "videoid": 0, #Camera ID on device, anywhere from 0 to 255, 99% chance of it being 0, 1 or 2
    "height": 240, #Try to keep width and height as small as possible, for performance
    "width": 320,
    "optimizedcv2": True, #Change to false if there are any problems
    "debug_text": True,
}


#Apriltag Detection Options
detection_options = apriltag.DetectorOptions(families='tag16h5',
                                 border=1,
                                 nthreads=4,
                                 quad_decimate=1.0,
                                 quad_blur=1.25, # Detection distance/speed tradeoff
                                 refine_edges=True,
                                 refine_decode=True,
                                 refine_pose=True, #Keep as true
                                 debug=False,
                                 quad_contours=True)
