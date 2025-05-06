#!/usr/bin/env python3
# Collection of functions
# TODO: Add folder iteration function
# TODO: Turn into proper package
# TODO: webp_to_jpg;
#   - fix webp file removal if package does not work + comments (better package?)
#   - add command line flags for local and specific locations to start from
#   - add subfolder iteration
#   - add Windows executable or shortcut creator

# Import packages
import os
import sys
# WARNING: if Python is installed in a folder containing spaces like "Program Files" dwebp does not work
from webptools import dwebp

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


def select_from_menu(menu_dict, selection_text):
    """Select a value from a dictionary through an input menu.
        Args:
            menu_dict (dict): A dictionary containing menu items
            selection_text (str): A string describing the menu items
        Returns:
            selection (str): A key value for the input dictionary
    """
    print_line()
    for item in menu_dict:
        print(f"({item}) {menu_dict[item]}")

    while True:
        print_line()
        selection = input(f"Please select {selection_text} by typing the value in brackets (or \"exit\" to quit): ")
        if selection == "exit":
            quit_script()
        elif selection not in menu_dict:
            print_line()
            print("Incorrect input. Please select a value from the list or type \"exit\"")
        else:
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
    """Rewrites all .webp files in a folder to .jpg.
        Args:
            image_folder (str): The folder containing the .webp files. Defaults to script location
        Returns: None
    """
    # WARNING: if the dwebp package does not work, images will simply be removed
    webp_list = [file for file in os.listdir(image_folder) if file.endswith(".webp")]
    for webp_image in webp_list:
        input_image = os.path.join(image_folder, webp_image)
        output_image = os.path.join(image_folder, webp_image[:-5] + ".jpg")
        dwebp(input_image=input_image, output_image=output_image, option="-o")  # logging="-v")
        os.remove(input_image)

    return


# Define global variables

# Main script
if __name__ == "__main__":
    print_line("=")
    print("Ciao bella, ciao")
    print_line("=")
    sys.exit()
