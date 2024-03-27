"""This visualizes the corruption chance throughout the entire galaxy.

The brighter a pixel is, the higher the chance of corruption."""

from PIL import Image

import bread.space as space
from settings import *

im = Image.new('RGBA', (map_size, map_size))

for y in range(map_size):
    for x in range(map_size):
        val = space.get_corruption_chance(x - map_radius, y - map_radius)
        
        color = int(val * 255)

        im.putpixel((x, y), (color, color, color, color))

im.save("corruption.png")

# Comment this out to disable automatically opening the image once it's created.
im.show()