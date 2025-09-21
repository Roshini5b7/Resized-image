import os
from PIL import Image

# Input file
input_image = r"C:\Users\roshi\Downloads\rose.jpeg"

# Output folder (new folder for resized images)
output_folder = r"C:\Users\roshi\Downloads\resized_images"

# Desired size
output_size = (800, 400)

# Create output folder if it does not exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Open and resize the image
img = Image.open(input_image)
resized_img = img.resize(output_size)

# Save the resized image
output_path = os.path.join(output_folder, "rose_resized.jpeg")
resized_img.save(output_path)

print(f"Resized image saved at: {output_path}")
