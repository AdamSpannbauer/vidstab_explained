"""Script to generate a shaky video of arbitrary shapes for example video stabilization"""

# TODO: save created video

import cv2
import numpy as np
from shaky_helpers import rand_shape, circle_poly_corners

# ensure reproducible results
np.random.seed(42)
# control length of video created
N_FRAMES = 100


# generate gray canvas for drawing
base_frame = np.ones((400, 400, 3), dtype='uint8') * 150

# create 2 random shapes in corners of canvas
shape_1 = rand_shape(50, 190)
shape_2 = rand_shape(200, 350)

# iterate through all frames
for _ in range(N_FRAMES):
    frame_i = base_frame.copy()

    # translate shapes to imitate camera movement
    shape_drift = np.random.randint(-5, 5)
    shape_1 += shape_drift
    shape_2 += shape_drift

    # draw shapes
    cv2.fillConvexPoly(frame_i, shape_1, (0, 0, 255))
    cv2.fillConvexPoly(frame_i, shape_2, (255, 0, 0))

    # copy frame to draw key points on it
    kp_frame = frame_i.copy()
    circle_poly_corners(kp_frame, shape_1)
    circle_poly_corners(kp_frame, shape_2)

    # show frames side by side
    display_frame = np.hstack((frame_i, kp_frame))

    # display canvas to screen
    cv2.imshow('shapes', display_frame)
    cv2.waitKey(10)
