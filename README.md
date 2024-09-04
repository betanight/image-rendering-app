# Image Rendering Tool

**Image Rendering Tool** is a utility designed to manage large images by slicing them into smaller tiles and then stitching those tiles back together. This tool is particularly useful for creating detailed maps or processing large images in applications like tabletop role-playing games (TTRPGs) or other map-based games.

## Features

- **Image Slicing**: Breaks down large images into smaller, equally-sized tiles, enabling detailed analysis and manipulation of individual segments.
- **Image Stitching**: Reassembles the tiles to recreate the original image or a composite image, ensuring accurate reconstruction from segmented parts.
- **Flexible Tile Sizes**: Allows users to specify tile sizes that evenly divide the dimensions of the original image, facilitating consistent slicing and reassembly.

## How It Works

1. **Slicing**: The tool slices a large image into smaller tiles based on a specified tile size. The tiles are saved in an output directory with names indicating their position in the grid.

2. **Stitching**: The tool reconstructs the original image from the saved tiles by arranging them in the correct order, ensuring that the final stitched image accurately represents the original.

## Usage

To use the tool, provide the image path, specify the desired tile size, and set an output directory for the resulting tiles. For stitching, supply the output directory containing the tiles and the tile size used during slicing.

## Project Setup

1. **Install Dependencies**: Ensure that the required Python Imaging Library (PIL) is installed. Use the following command:

    ```bash
    pip install pillow
    ```

2. **Run the Functions**: Update the parameters for slicing and stitching as needed, and execute the functions to process your images.
