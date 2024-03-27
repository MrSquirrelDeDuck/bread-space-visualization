"""This is for settings that files may use."""

# The seed of the galaxy.
galaxy_seed = "7b1b11fed8bae4a69168d53b1ab9ae5e5c68f327ab6073392de83457f3ec0a24"

# For things that use it, this is the position in the galaxy to generate.
galaxy_xpos = 203
galaxy_ypos = 89

# Galaxy generation variables.
# These probably shouldn't be changed unless it is to reflect a change in Machine-Mind.
map_size = 256

map_radius = map_size // 2
map_radius_squared = map_radius ** 2

# This is in `1 in __`, so an 8 means a 1/8 chance.
chance_system = 8 # Chance of any point being a system, assuming it doesn't have a system very close nearby.
chance_trade = 3 # The chance of any generated system having a trading hub by default.