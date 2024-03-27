"""This generates a system and makes a map of the system."""

from PIL import Image
import random

import bread.space as space
import bread.generation as generation
from settings import *

###################################################
#####                SETTINGS                 #####
###################################################

### What to show:
show_systems = True
highlight_natual_trade_hubs = True
show_wormholes = True
show_spawn_point = True
show_nebulae = True
show_0_corruption_band = True

### Colors of things: (in RGB form.)
background_color = (0, 0, 0)
system_color = (0, 128, 0)
trade_hub_color = (128, 0, 128)
spawn_point_color = (255, 255, 255)
wormhole_color = (255, 255, 0)

### Highlight colors:
# These are numbers added to the existing color.
nebulae_highlight_color = (0, 0, 64)
corruption_highlight_color = (64, 0, 0)

#######################################################################################################
#######################################################################################################
#######################################################################################################

options = [
    "show_systems",
    "highlight_natual_trade_hubs",
    "show_wormholes",
    "show_spawn_point",
    "show_nebulae",
    "show_0_corruption_band"
]

for option in options:
    if option not in globals():
        globals()[option] = False

def generate_map(width: int, height: int) -> Image.Image:
    im = Image.new('RGB', (width, height))

    map_data = generation.galaxy_bulk(
        galaxy_seed = galaxy_seed,
        top_right = (0, map_size - 1),
        bottom_left = (map_size - 1, 0)
    )
    for key, data in map_data.items():
        x = key[0]
        y = key[1]

        if show_systems:
            grade = data.get("system", False) + data.get("trade_hub", False)

            if grade == 0:
                colors = background_color
            elif grade == 2 and highlight_natual_trade_hubs:
                colors = trade_hub_color
            else:
                colors = system_color
        else:
            colors = background_color

        if show_nebulae:
            if data.get("in_nebula", False):
                colors = (
                    colors[0] + nebulae_highlight_color[0],
                    colors[1] + nebulae_highlight_color[1],
                    colors[2] + nebulae_highlight_color[2]
                )
        
        if show_0_corruption_band:
            if space.get_corruption_chance(x - map_radius, y - map_radius) <= 0:
                colors = (
                    colors[0] + corruption_highlight_color[0],
                    colors[1] + corruption_highlight_color[1],
                    colors[2] + corruption_highlight_color[2]
                )
        
        im.putpixel((x, y), colors)
    
    ### Spawn point.
    if show_spawn_point:
        spawn_x, spawn_y = generation.get_galaxy_spawn(galaxy_seed)
        
        im.putpixel((round(spawn_x), round(spawn_y)), spawn_point_color)

    ### Wormholes.
    if show_wormholes:
        points = []
        full = []

        wormhole_count = random.Random(galaxy_seed).gauss(mu=25, sigma=5)

        if wormhole_count < 1:
            wormhole_count = 1 - wormhole_count
        if wormhole_count > 49:
            wormhole_count = 49 - (wormhole_count - 49)

        wormhole_count = round(wormhole_count)
        print("Generating",wormhole_count,"wormholes.")

        for i in range(wormhole_count):
            point_data = generation.get_wormhole_points(galaxy_seed, points)

            full.append(tuple(point_data))
            for data in point_data:
                im.putpixel(data["location"], wormhole_color)

                points.append(data["location"])
    
    return im

img = generate_map(map_size, map_size)
img.save("gen_galaxy.png")

# Comment this out to disable automatically opening the image once it's created.
img.show()