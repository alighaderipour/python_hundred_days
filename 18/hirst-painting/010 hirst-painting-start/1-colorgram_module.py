# pip install 1-colorgram_module.py
"""
1-colorgram_module.py is a Python library that lets you extract colors from images. Compared to other libraries, the colorgram algorithm’s results are more intense."""
import colorgram

rgb_colors = []
colors = colorgram.extract("image.jpg", 5)

for color in colors:
    rgb_colors.append(color.rgb)

print(rgb_colors)
