import os
import math
from PIL import Image
from slice import slice_image
from stitch import stitch_images

def calculate_tile_size(img_width, img_height, min_size=10, max_size=100):
    # Calculate the greatest common divisor (GCD) for the width and height
    gcd_value = math.gcd(img_width, img_height)
    
    # Clamp the GCD within the min_size and max_size range
    tile_size = max(min(gcd_value, max_size), min_size)

    print(f"Calculated tile size (clamped between {min_size} and {max_size}): {tile_size}")
    return tile_size

def process_image(image_path):
    try:
        # Load the image to get its dimensions
        img = Image.open(image_path)
        img_width, img_height = img.size
        
        # Calculate the optimal tile size
        tile_size = calculate_tile_size(img_width, img_height)
        print(f"Using tile size: {tile_size}x{tile_size} pixels")

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
    image_path = 'SpooksImage.jfif'  # Update this with the actual image path
    process_image(image_path)
