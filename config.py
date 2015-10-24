# -*- coding: utf-8 -*-
"""
    Config file for HWP
    ~~~~~~~~~~~~~~~~~~~

    "ANGLE" – angle of amino-acids step.
    Set it in radians. Use numpy «pi»
    By default angle is 5pi/9 (100 degrees)

    "NODES_IN_WHEEL" — integer number.
    How many times acid can fit in projection.
    By default - 18.

    "BEGIN_POSITION" — position of first amino-acid.
    By default - pi/2

    "DIRECTION" – clockwise: -1, else 1
"""
import numpy as np

ANGLE = np.pi * 5 / 9 # 100 degrees
NODES_IN_WHEEL = 18 # for 100 degrees ti's 18, yah
BEGIN_POSITION = np.pi / 2
DIRECTION = -1
