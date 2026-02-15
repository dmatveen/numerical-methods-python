import numpy as np
import matplotlib.pyplot as plt
import math
import logging
from typing import Callable, Optional, Tuple
import enum
import math

EPS=.00001
MAX_ITER=1000
X_MIN=-3
X_MAX=3
X_STEP=.01
MIN_STEP=.00000001
TINY_VALUE=1E-10
TAU=(math.sqrt(5)-1)/2

class IntegrationType(enum.Enum):
    rectangle_left=1
    rectangle_right=2
    rectangle_mid=3
    trapezoid=4
    parabolic=5

    def __str__(self):
        names = {
            1: "Левые прямоугольники",
            2: "Правые прямоугольники",
            3: "Средние прямоугольники",
            4: "Трапеции",
            5: "Параболы"
        }
        return names[self.value]