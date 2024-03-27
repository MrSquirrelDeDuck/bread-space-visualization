import math

from settings import *

def get_corruption_chance(
        xpos: int,
        ypos: int,
    ) -> float:
    """Returns the chance of a loaf becoming corrupted for any point in the galaxy. Between 0 and 1."""
    dist = math.hypot(xpos, ypos)

    # The band where the chance is 0 is between 80 and 87.774.
    if 80 <= dist <= 87.774:
        return 0.0

    return ((dist ** 2.15703654359 / 1000) + 118 * math.e ** (-0.232232152965 * (dist / 22.5) ** 2) - 19) / 100