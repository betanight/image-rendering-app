from PIL import Image

# Load images
img1 = Image.open('mapimage1.jfif')
img2 = Image.open('mapimage1.jfif')

# Stitch images side by side
total_width = img1.width + img2.width
max_height = max(img1.height, img2.height)

stitched_image = Image.new('RGB', (total_width, max_height))
stitched_image.paste(img1, (0, 0))
stitched_image.paste(img2, (img1.width, 0))

stitched_image.save('stitched_image.png')
