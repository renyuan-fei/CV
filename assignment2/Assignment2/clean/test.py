# Numpy is the main package for scientific computing with Python.
import numpy as np
import cv2

# Matplotlib is a useful plotting library for python
import matplotlib.pyplot as plt
# This code is to make matplotlib figures appear inline in the
# notebook rather than in a new window.

plt.rcParams['figure.figsize'] = (10.0, 8.0) # set default size of plots, can be changed
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['image.cmap'] = 'gray'


def draw_outline (ref, query, model):
    """
        Draw outline of reference image in the query image.
        This is just an example to show the steps involved.
        You can modify to suit your needs.
        Inputs:
            ref: reference image
            query: query image
            model: estimated transformation from query to reference image
    """
    h, w = ref.shape[:2]
    pts = np.float32 ([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape (-1, 1, 2)
    dst = cv2.perspectiveTransform (pts, model)

    img = query.copy ()
    img = cv2.polylines (img, [np.int32 (dst)], True, 255, 3, cv2.LINE_AA)
    plt.imshow (img, 'gray'), plt.show ()


def draw_inliers (img1, img2, kp1, kp2, matches, matchesMask):
    """
        Draw inlier between images
        img1 / img2: reference/query  img
        kp1 / kp2: their keypoints
        matches : list of (good) matches after ratio test
        matchesMask: Inlier mask returned in cv2.findHomography()
    """
    matchesMask = matchesMask.ravel ().tolist ()
    draw_params = dict (
        matchColor=(0, 255, 0),  # draw matches in green color
        singlePointColor=None,
        matchesMask=matchesMask,  # draw only inliers
        flags=2
        )
    img3 = cv2.drawMatches (img1, kp1, img2, kp2, matches, None, **draw_params)
    plt.imshow (img3, 'gray'), plt.show ()

# ----------------------------------------------------------------------------------------------------------------------
