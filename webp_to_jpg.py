#!/usr/bin/env python3
# Convert webp images to jpg
# WARNING: THE DWEBP PACKAGE DOES NOT WORK IF PYTHON IS INSTALLED IN A FOLDER CONTAINING A SPACE LIKE "PROGRAM FILES"
# THE IMAGES WILL SIMPLY BE REMOVED
# TODO: Use folder in which the script is run as default
# TODO: Add command line flags for local and specific locations to start from
# TODO: Add subfolder iteration
# TODO: Find better package to work with Program Files Python installation
# TODO: Add Windows executable

# Import packages
import os
from webptools import dwebp

# Define global variables
# image_folder = "C:\\Users\\korpu\\OneDrive\\Skrivbord\\Korpugglan\\Images\\Funny\\to_ship"
image_folder = "C:/Users/korpu/OneDrive/Skrivbord/Korpugglan/Images/Funny/to_ship"


if __name__ == "__main__":
    webp_list = [file for file in os.listdir(image_folder) if file.endswith(".webp")]
    for image in webp_list:
        input_image = os.path.join(image_folder, image)
        output_image = os.path.join(image_folder, image[:-5] + ".jpg")
        dwebp(input_image=input_image, output_image=output_image, option="-o")  # logging="-v")
        os.remove(input_image)
