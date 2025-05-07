#!/usr/bin/env python3
# Collection of functions
# TODO: Add folder iteration function
# TODO: Turn into proper package
# TODO: webp_to_jpg;
#   - test Pillow with (partially) transparent background
#   - add command line flags for local and specific locations to start from
#   - add subfolder iteration option
#   - add Windows executable or shortcut creator

# Import packages
import os
from PIL import Image
import sys


# Define functions
def print_line(print_chars="-", repetition=100):
    """Prints an amount of strings in a row.
        Args:
            print_chars (str): The string to print repeatedly.
            repetition (int): The amount of times the string is printed.
        Returns:
            None
    """
    print(print_chars * repetition)
    return


def print_menu_selection(menu_key, menu_value):
    """Prints a message about menu choice selection.
        Args:
            menu_key (str): The menu selection key.
            menu_value (str): The menu selection value.
        Returns: None
    """
    print_line("-")
    print(f"Option \"({menu_key}): {menu_value}\" selected.")
    return


def select_from_menu(menu_dict, selection_text="your option"):
    """Select a value from a dictionary through an input menu.
        Args:
            menu_dict (dict): A dictionary containing menu items
            selection_text (str): A string describing the menu items
        Returns:
            selection (str): A key value for the input dictionary
    """
    print_line("=")
    for item in menu_dict:
        print(f"({item}) {menu_dict[item]}")

    while True:
        print_line("=")
        selection = input(f"Please select {selection_text} by typing the value in brackets (\"exit\" to quit): ")
        if selection == "exit":
            quit_script()
        elif selection not in menu_dict:
            print_line()
            print("Incorrect input. Please select a value from the list or type \"exit\"")
        else:
            print_menu_selection(selection, menu_dict[selection])
            return selection


def quit_script():
    """Prints a message and quits the script.
        Args: None
        Returns: None
    """
    print_line("=")
    print("Ciao bella, ciao")
    print_line("=")
    sys.exit()


def webp_to_jpg(image_folder=os.path.dirname(os.path.abspath(__file__))):
    """Converts all .webp files in a folder to .jpg.
        Args:
            image_folder (str): The folder containing the .webp files. Defaults to script location.
        Returns: None
    """
    print(f"Converting all .webp files in {image_folder} to .jpg.")
    webp_list = [file for file in os.listdir(image_folder) if file.endswith(".webp")]
    for webp_image in webp_list:
        # Set file paths for input and output
        input_file_path = os.path.join(image_folder, webp_image)
        output_file_path = os.path.join(image_folder, webp_image[:-5] + ".jpg")

        # Load .webp file and write as .jpg
        input_image = Image.open(input_file_path)
        input_image = input_image.convert("RGB")
        input_image.save(output_file_path, format="JPEG")

        # Remove input image
        os.remove(input_file_path)

    print(f"Operation completed successfully.")
    return


# Main script
if __name__ == "__main__":
    quit_script()
