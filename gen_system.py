"""This generates a map of the entire galaxy."""

from PIL import Image
import math

import bread.generation as generation

from settings import *

###################################################
#####                SETTINGS                 #####
###################################################

### What to show:
show_planets = True
show_asteroid_belt = True
show_wormhole = True

### Colors:
wormhole_color = (255, 255, 0)
asteroid_color = (128, 128, 128)

star_colors = {
    "star1": (128, 255, 255),
    "star2": (255, 128, 255),
    "star3": (255, 255, 128),
    "black_hole": (5, 5, 5)
}

planet_colors = {
    "bread": (252, 229, 205),
    
    "croissant": (249, 203, 156),
    "flatbread": (249, 203, 156),
    "stuffed_flatbread": (249, 203, 156),
    "french_bread": (249, 203, 156),
    "sandwich": (249, 203, 156),

    "bagel": (246, 178, 107),
    "doughnut": (246, 178, 107),
    "waffle": (246, 178, 107),

    "Bpawn": (183, 183, 183),
    "Bknight": (183, 183, 183),
    "Bbishop": (183, 183, 183),
    "Brook": (183, 183, 183),
    "Buqeen": (183, 183, 183),
    "Bking": (183, 183, 183),

    "Wpawn": (224, 224, 224),
    "Wknight": (224, 224, 224),
    "Wbishop": (224, 224, 224),
    "Wrook": (224, 224, 224),
    "Wqueen": (224, 224, 224),
    "Wking": (224, 224, 224),

    "gem_red": (234, 153, 153),
    "gem_blue": (159, 197, 232),
    "gem_purple": (180, 167, 214),
    "gem_green": (182, 215, 168),
    "gem_gold": (255, 242, 204),

    "anarchy_chess": (224, 104, 104)
}

# The weights for different types of stars appearing.
star_weights = {
    "star1": 50,
    "star2": 22,
    "star3": 22,
    "black_hole": 6
}

# Weights for planet categories.
planet_weights = {
    "normal_bread": 20,
    "special_bread": 20,
    "rare_bread": 50,
    "piece_black": 55,
    "piece_white": 45,
    "gem_red": 20,
    "bem_blue": 48,
    "gem_purple": 24,
    "gem_green": 12,
    "gem_gold": 6,
    "anarchy_chess": 3
}

# The options for each planet category.
planet_options = {
    "normal_bread": ["bread"],
    "special_bread": ["croissant", "flatbread", "stuffed_flatbread", "french_bread", "sandwich"],
    "rare_bread": ["bagel", "doughnut", "waffle"],
    "piece_black": ["bpawn", "bpawn", "bpawn", "bpawn", "bpawn", "bpawn", "bpawn", "bpawn", "bknight", "bknight", "bbishop", "bbishop", "brook", "brook", "bqueen", "bking"],
    "piece_white": ["wpawn", "wpawn", "wpawn", "wpawn", "wpawn", "wpawn", "wpawn", "wpawn", "wknight", "wknight", "wbishop", "wbishop", "wrook", "wrook", "wqueen", "wking"],
    "gem_red": ["gem_red"],
    "bem_blue": ["gem_blue"],
    "gem_purple": ["gem_purple"],
    "gem_green": ["gem_green"],
    "gem_gold": ["gem_gold"],
    "anarchy_chess": ["anarchy_chess"]
}

###################################################################################################################
########## IMAGE GENERATION

options = [
    "show_planets",
    "show_asteroid_belt",
    "show_wormhole"
]

for option in options:
    if option not in globals():
        globals()[option] = False

system_data = generation.generate_system(
    galaxy_seed = galaxy_seed,
    galaxy_xpos = galaxy_xpos,
    galaxy_ypos = galaxy_ypos
)

if system_data is None:
    raise ValueError("Galaxy location listed in settings.py is not a system.")

radius = system_data["radius"]
size = radius * 2

if size % 2 == 0:
    size += 1 # Make sure the size is odd.

im = Image.new('RGB', (size, size))

im.putpixel((radius, radius), star_colors[system_data["star_type"]])

if show_asteroid_belt:
    if system_data["asteroid_belt"]:
        for a in range(3600):
            x = round(math.cos(math.radians(a / 10)) * system_data["asteroid_belt_distance"])
            y = round(math.sin(math.radians(a / 10)) * system_data["asteroid_belt_distance"])

            im.putpixel((x + radius, y + radius), asteroid_color)
    
if show_planets:
    for data in system_data.get("planets", []):
        x = round(math.cos(math.radians(data.get("angle"))) * data["distance"])
        y = round(math.sin(math.radians(data.get("angle"))) * data["distance"])

        im.putpixel((x + radius, y + radius), planet_colors[data["type"].name])

if show_wormhole:
    if system_data["wormhole"]["exists"]:
        im.putpixel(
            (
                system_data["wormhole"]["xpos"] + radius,
                system_data["wormhole"]["ypos"] + radius
            ),
            wormhole_color
        )


im.save("gen_system.png")

# Comment this out to disable automatically opening the image once it's created.
im.show()
