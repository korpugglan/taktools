#!/usr/bin/env python3
# Script to batch process and organize zip files
# TODO: Use folder in which the script is run as default
# TODO: Add command line flags for local and specific locations to start from
# TODO: Add subfolder iteration
# TODO: Add Windows executable
# TODO: Add webp to jpg feature
# TODO: Find better package to work with Program Files Python installation
# TODO: Proper refactor


# Import packages
import os
import sys


# Define functions
def change_current_start_dir_path():
    while True:
        print_line()
        input_path = input(f"Please enter the new path: ")
        if input_path == "exit":
            quit_script()
        new_path = os.fspath(input_path)
        if os.path.isdir(new_path):
            print(f"Path changed to \"{new_path}\"")
            return new_path
        else:
            print_line()
            print("Invalid input. Path is not an accessible directory. Please try again or type \"exit\"")


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
        selection = input(f"Please select {selection_text} by typing the value in brackets: ")
        if selection == "exit":
            quit_script()
        elif selection not in menu_dict:
            print_line()
            print("Invalid input. Please select a value from the list or type \"exit\"")
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


# Define global variables
current_path = os.path.abspath(os.path.dirname(__file__))
feat_dict = {"1": f"Set different start directory path (currently: \"{current_path}\")",
             "2": "Unzip and unpack into separate folders",
             "3": "Rename zip files",
             "4": "Unzip and rename into single folder",
             "5": "Convert .webp files to .jpg in folder and subfolders"}


# Main script
if __name__ == "__main__":
    # Welcome text
    print_line("=")
    print("Welcome to ZIPORG")
    print("Entering the phrase \"exit\" always quits the script")

    # Feature select
    feat_select = select_from_menu(feat_dict, "a feature")
    if feat_select == "1":
        current_path = change_current_start_dir_path()
        feat_dict["1"] = f"Set different start directory path (currently: \"{current_path}\")"

    feat_select = select_from_menu(feat_dict, "a feature")

    # print(f"{feat_select} selected. This means \"{feat_dict[feat_select]}\"")

    quit_script()
