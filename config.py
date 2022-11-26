import apriltag, cv2


#Camera Options
cameraoptions = {
    "videoid": 0,
    "height": 720,
    "width": 1280,
}


#Apriltag Detection Options
detection_options = apriltag.DetectorOptions(families='tag16h5',
                                 border=1,
                                 nthreads=4,
                                 quad_decimate=1.0,
                                 quad_blur=1.25,
                                 refine_edges=False,
                                 refine_decode=False,
                                 refine_pose=True,
                                 debug=False,
                                 quad_contours=True)