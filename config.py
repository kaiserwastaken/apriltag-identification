import apriltag

#Apriltag Detection Options
detection_options = apriltag.DetectorOptions(families='tag16h5',
                                 border=1,
                                 nthreads=4,
                                 quad_decimate=1.0,
                                 quad_blur=0.0,
                                 refine_edges=False,
                                 refine_decode=True,
                                 refine_pose=True,
                                 debug=False,
                                 quad_contours=True)