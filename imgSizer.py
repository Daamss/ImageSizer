import os
from PIL import Image, ImageFilter
import threading
import webbrowser

# Get the input image
input_image = input("Enter the name of the input image: ")

# Get the desired output size
output_width = int(input("Enter the desired width: "))
output_height = int(input("Enter the desired height: "))

# Create a function to resize the image
def resize_image(img):
    img_resized = img.resize((output_width, output_height), resample=Image.Resampling.LANCZOS)
    return img_resized

# Create a function to sharpen the image
def sharpen_image(img):
    img = img.filter(ImageFilter.SHARPEN)
    return img

# Open the image
img = Image.open(input_image)

# Get the name of the output image
output_image = os.path.splitext(input_image)[0] + "_resized" + os.path.splitext(input_image)[1]

# Resize the image
img_resized = resize_image(img)

# Sharpen the image
img_resized = sharpen_image(img_resized)

# Save the resized image
img_resized.save(output_image)

# Open the resized image
webbrowser.open(output_image)

print("Image resized successfully!")