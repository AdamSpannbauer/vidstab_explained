"""Functions to help generate example shaky video"""

import cv2
import numpy as np


def rand_shape(lo, hi, n_points=4):
    """Create random polygon vertices in bounded range

    :param lo: lower bound for vertex value (inclusive)
    :param hi: upper bound for vertex value (exclusive)
    :param n_points: number of vertices to generate

    :return: numpy array of vertices that can be easily plotted by cv2.fillConvexPoly

    >>> print(rand_shape(0, 5))
    array([[[3, 4],
            [2, 4],
            [4, 1],
            [2, 2]]], dtype=int32)
    """
    pts = np.random.randint(lo, hi, size=n_points * 2, dtype='int32')
    return pts.reshape((1, n_points, 2))


def circle_poly_corners(img, pts):
    """Draw circles around each vertex in a numpy array

    :param img: 3d numpy array (opencv image) to draw circles on
    :param pts: numpy array of points to draw circles at.  expects same structure as cv2.fillConvexPoly

    :return: None; img is modified in place

    >>> img = np.ones((100, 100, 3), dtype='uint8')
    >>> pts = rand_shape(0, 5)
    >>> circle_poly_corners(img, pts)
    """
    for pt in pts[0]:
        cv2.circle(img, tuple(pt), 3, (0, 255, 0), 1)
