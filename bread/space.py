import math

from settings import *

def get_corruption_chance(
        xpos: int,
        ypos: int,
    ) -> float:
    """Returns the chance of a loaf becoming corrupted for any point in the galaxy. Between 0 and 1.
    
    Subtract the map radius from a regular coordinate for this."""
    dist = math.hypot(xpos, ypos)

    # The band where the chance is 0 is between 80 and 87.
    if 80 <= dist <= 87:
        return 0.0
    
    # f\left(x\right)=\left\{x\le2:99,2\le x\le80:\left(\frac{\cos\left(\left(x-2\right)\frac{\pi}{78}\right)}{2}+0.5\right)99,80<x<87:0,87\le x\le241.81799:\left(\frac{\cos\left(\frac{\left(x-87\right)\pi}{154.8179858682464038403596020291203352621852869144970764695290884}\right)}{-2}+0.5\right)99,x>241.81799:99\right\}
    # Where `x` is the distance to (0, 0)
    # lmao

    # It's a piecewise function, so `if` statements are used.
    if dist <= 2:
        chance = 99
    elif dist <= 80:
        chance = (math.cos((dist - 2) * (math.pi / 78)) / 2 + 0.5) * 99
    elif dist <= 87:
        chance = 0
    elif dist <= 241.81799:
        chance = (math.cos(((dist - 87) * math.pi) / 154.8179858682464038403596020291203352621852869144970764695290884) / -2 + 0.5) * 99
    else:
        chance = 99

    return chance / 100