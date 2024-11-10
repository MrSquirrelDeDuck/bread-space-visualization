"""This is for settings that files may use."""

# The seed of the galaxy.
# galaxy_seed = "a0cebc902b365f41ce6963cfcf457a21a995c515564c230b409206b61a32b77b"
galaxy_seed = "2e66d9c79fe5779baa2d820cd9af9767c6f9a38772f4a6f2ceb861d85df26801" # Bread Space development seed.

# For things that use it, this is the position in the galaxy to generate.
galaxy_xpos = 203
galaxy_ypos = 89

# Galaxy generation variables.
# These probably shouldn't be changed unless it is to reflect a change in Machine-Mind.
map_size = 256

map_radius = map_size // 2
half_radius = map_radius // 2
map_radius_squared = map_radius ** 2

# This is in `1 in __`, so an 8 means a 1/8 chance.
chance_system = 8 # Chance of any point being a system, assuming it doesn't have a system very close nearby.
chance_trade = 3 # The chance of any generated system having a trading hub by default.