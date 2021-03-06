from PIL import Image
import pyheif
from pathlib import Path
import os

# Get directory for images folder
images_folder = Path("images/")

# List of image objects
images = []

# Image new size
# size = width, height
# Feel free to change the numerators and denominators to suit your needs
img_new_size = 3024//6, 4032//6

# Iterate over images in /images folder
# Resize the image and then add it to the images list
for image_file in sorted(os.listdir(images_folder)):
    if image_file.endswith(".HEIC"):
        print('processing', image_file)
        heif_file = pyheif.read(images_folder/image_file)

        image = Image.frombytes(
            heif_file.mode, 
            heif_file.size, 
            heif_file.data,
            "raw",
            heif_file.mode,
            heif_file.stride,
            )

        image.thumbnail(img_new_size)
        images.append(image)

for count, element in enumerate(images):
    if count == 0: # Start with first image only; append the rest
        if len(images) == 1: # If only one image
            element.save('image.pdf', 'PDF')
        else: # Else, there are multiple images
            element.save('images.pdf', save_all=True, append_images=images[1:])
    else:
        break

print('PDF is now ready')