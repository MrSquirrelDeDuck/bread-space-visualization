"""This generates the nebula positions and renders an image of them."""

from PIL import Image

import bread.generation as generation
from settings import *

###################################################
#####                SETTINGS                 #####
###################################################

### Colors of things: (in RGB form.)
background_color = (0, 0, 0)
nebula_color = (0, 0, 255)

#######################################################################################################
#######################################################################################################
#######################################################################################################

im = Image.new('RGB', (map_size, map_size), color=background_color)

data = generation.generate_nebulae(galaxy_seed=galaxy_seed)
for y in range(map_size):
    for x in range(map_size):
        if generation.in_nebula(
            nebulae_info = data,
            x = x - map_radius,
            y = y - map_radius
        ):
            im.putpixel((x, y), nebula_color)

im.save("nebulae.png")
im.show()