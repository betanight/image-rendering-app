from PIL import Image
import os

def slice(image_path, tile_size, output_dir):
    try:
        # Load the image
        img = Image.open(image_path)
        img_width, img_height = img.size
        
        # Print image dimensions for debugging
        print(f"Image dimensions: width={img_width}, height={img_height}")

        # Adjust tile size if necessary
        if tile_size > img_width or tile_size > img_height:
            print(f"Adjusting tile size from {tile_size} to the smaller dimension of the image.")
            tile_size = min(img_width, img_height)
        
        # Calculate the number of tiles needed
        x_tiles = (img_width + tile_size - 1) // tile_size
        y_tiles = (img_height + tile_size - 1) // tile_size

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
                right = min(left + tile_size, img_width)
                lower = min(upper + tile_size, img_height)
                
                # Crop the image
                tile = img.crop((left, upper, right, lower))
                
                # Save the tile
                tile.save(os.path.join(output_dir, f'tile_{i}_{j}.png'))
        
        print(f"Image sliced into {x_tiles * y_tiles} tiles, saved in '{output_dir}'.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Parameters
image_path = 'mapimage1.jfif'  # Path to the original image
tile_size = 100  # Adjusted size of each tile (e.g., 100x100 pixels)
output_dir = 'output_tiles'  # Directory to save the tiles

# Run the slicing function
slice(image_path, tile_size, output_dir)
