from PIL import Image
import os

def stitch_images(output_dir, tile_size, x_tiles, y_tiles, output_image_path):
    try:
        # Determine the dimensions of the stitched image
        img_width = x_tiles * tile_size
        img_height = y_tiles * tile_size
        
        # Create a new blank image with the appropriate size
        stitched_img = Image.new('RGB', (img_width, img_height))
        
        # Loop through each tile and paste it to recreate the original image
        for i in range(x_tiles):
            for j in range(y_tiles):
                # Construct the filename for the tile
                tile_filename = os.path.join(output_dir, f'tile_{i}_{j}.png')
                
                # Open the tile image
                tile_img = Image.open(tile_filename)
                
                # Calculate the position to paste the tile into the stitched image
                left = i * tile_size
                upper = j * tile_size
                
                # Paste the tile into the stitched image
                stitched_img.paste(tile_img, (left, upper))
        
        # Save the stitched image
        stitched_img.save(output_image_path)
        print(f"Image successfully stitched and saved to '{output_image_path}'.")
    
    except Exception as e:
        print(f"An error occurred: {e}")