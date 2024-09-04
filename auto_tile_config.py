import os
import math
from PIL import Image
from slice import slice_image
from stitch import stitch_images

def calculate_tile_size(img_width, img_height):
    # Calculate the greatest common divisor (GCD) for the width and height
    return math.gcd(img_width, img_height)

def process_image(image_path):
    try:
        # Load the image to get its dimensions
        img = Image.open(image_path)
        img_width, img_height = img.size
        
        # Calculate the optimal tile size
        tile_size = calculate_tile_size(img_width, img_height)
        print(f"Calculated tile size: {tile_size}x{tile_size} pixels")

        # Determine the number of tiles along each axis
        x_tiles = img_width // tile_size
        y_tiles = img_height // tile_size

        # Define output directory for sliced tiles
        output_dir = 'output_tiles'

        # Slice the image into smaller tiles
        slice_image(image_path, tile_size, output_dir)

        # Define the path for the stitched output image
        output_image_path = 'stitched_image.png'

        # Stitch the tiles back together to recreate the original image
        stitch_images(output_dir, tile_size, x_tiles, y_tiles, output_image_path)

        print(f"Processing complete. Stitched image saved as '{output_image_path}'.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Specify the image path here
    image_path = 'forgotten_realms.jpeg'  # Update this with the actual image path
    process_image(image_path)
