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

def create_image_pyramid(image_path, output_dir, min_size=256, scale_factor=2):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    img = Image.open(image_path)
    width, height = img.size

    level = 0
    while min(width, height) >= min_size:
        new_width = width
        new_height = height

        resized_img = img.resize((new_width, new_height), Image.ANTIALIAS)
        resized_img.save(os.path.join(output_dir, f'pyramid_level_{level}.png'))
        print(f"Level {level}: {new_width}x{new_height}")

        width //= scale_factor
        height //= scale_factor
        level += 1

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

        # Generate image pyramid
        create_image_pyramid(image_path, 'pyramid_images')

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Specify the image path here
    image_path = 'forgotten_realms.jpeg'  # Update this with the actual image path
    process_image(image_path)
