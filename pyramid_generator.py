import os
from PIL import Image

def create_image_pyramid(image_path, output_dir, min_size=10, scale_factor=2, max_levels=10):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    img = Image.open(image_path)
    width, height = img.size

    level = 0
    while level < max_levels and min(width, height) >= min_size:
        new_width = width
        new_height = height

        # Use Image.LANCZOS for resizing
        resized_img = img.resize((new_width, new_height), Image.LANCZOS)
        resized_img.save(os.path.join(output_dir, f'pyramid_level_{level}.png'))
        print(f"Level {level}: {new_width}x{new_height}")

        width //= scale_factor
        height //= scale_factor
        level += 1

    print(f"Image pyramid created up to level {max_levels}.")

if __name__ == "__main__":
    # Specify the image path here
    image_path = 'stitched_image.png'  # Ensure this path is correct
    output_dir = 'pyramid_images'
    create_image_pyramid(image_path, output_dir)
