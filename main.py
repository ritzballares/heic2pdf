from PIL import Image
import pyheif
from pathlib import Path
import os

# Get directory for images folder
images_folder = Path("images/")

# List of image objects
images = []

# Iterate over images in /images folder
# Add the image to images list
for image_file in os.listdir(images_folder):
    if image_file.endswith(".HEIC"):
        heif_file = pyheif.read(images_folder/image_file)

        image = Image.frombytes(
            heif_file.mode, 
            heif_file.size, 
            heif_file.data,
            "raw",
            heif_file.mode,
            heif_file.stride,
            )

        images.append(image)

for count, element in enumerate(images):
    if count == 0: # Start with first image only; append the rest
        if len(images) == 1: # If only one image
            element.save('image.pdf', 'PDF')
        else: # Else, there are multiple images
            element.save('images.pdf', save_all=True, append_images=images)
    else:
        break