from PIL import Image
import os

def slice_image(image_path, tile_size, output_dir):
    try:
        # Load the image
        img = Image.open(image_path)
        img_width, img_height = img.size
        
        # Print image dimensions for debugging
        print(f"Image dimensions: width={img_width}, height={img_height}")

        # Calculate the number of tiles needed
        x_tiles = img_width // tile_size
        y_tiles = img_height // tile_size

        # Print the number of tiles
        print(f"Number of tiles: x_tiles={x_tiles}, y_tiles={y_tiles}")

        # Ensure output directory exists
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        # Slice the image into tiles
        for i in range(x_tiles):
            for j in range(y_tiles):
                # Define the box to extract
                left = i * tile_size
                upper = j * tile_size
                right = left + tile_size
                lower = upper + tile_size
                
                # Crop the image
                tile = img.crop((left, upper, right, lower))
                
                # Save the tile
                tile.save(os.path.join(output_dir, f'tile_{i}_{j}.png'))
        
        print(f"Image sliced into {x_tiles * y_tiles} tiles, saved in '{output_dir}'.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
