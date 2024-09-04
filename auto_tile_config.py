import json
import os
from PIL import Image
import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def optimal_tile_size(width, height):
    return gcd(width, height)

def load_config():
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
    return config

def update_slice_and_stitch():
    config = load_config()
    image_path = config.get("image_path", "image1.png")
    output_dir = config.get("output_directory", "output_tiles")

    # Load the image to determine dimensions
    img = Image.open(image_path)
    img_width, img_height = img.size

    # Calculate the optimal tile size using GCD
    tile_size = optimal_tile_size(img_width, img_height)

    # Now, pass these parameters to your slice.py and
