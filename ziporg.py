#!/usr/bin/env python3
# Script to batch process and organize zip files
# TODO: Add file name cleaning (~, .., double spaces, trimming)
# TODO: Add subdirectory iteration
# TODO: Add Windows executable
# TODO: Add webp to jpg feature
# TODO: Find better package to work with Program Files Python installation
# TODO: Proper refactor


# Import packages
import os
import sys
import zipfile


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


def unpack_zip_files_separately(start_dir):
    max_zip_file_name_len = 64
    del_char_list = ["~", ".", ",", "!", "@", "#", "$"]

    zip_file_list = [file for file in os.listdir(start_dir) if file.endswith(".zip")]
    for zip_file_name in zip_file_list:
        new_zip_file_name = zip_file_name[:-len(".zip")]
        for del_char in del_char_list:
            new_zip_file_name = new_zip_file_name.replace(del_char, "")
        while True:
            if "  " in new_zip_file_name:
                new_zip_file_name = new_zip_file_name.replace("  ", "")
            else:
                break
        new_zip_file_name = new_zip_file_name.strip()
        new_zip_file_name = new_zip_file_name[:max_zip_file_name_len] + ".zip"
        os.rename(os.path.join(start_dir, zip_file_name),
                  os.path.join(start_dir, new_zip_file_name))
        zip_file_name = new_zip_file_name

        full_zip_file_path = os.path.join(start_dir, zip_file_name)
        zip_dir_name = zip_file_name[:-4]

        full_zip_dir_path = os.path.join(start_dir, zip_dir_name)
        while True:
            if os.path.isdir(full_zip_dir_path):
                copy_dir_text = "-COPY"
                print(f"WARNING! Directory \"{full_zip_dir_path}\" exists. "
                      f"Adding \"{copy_dir_text}\" to directory name")
                full_zip_dir_path = os.path.join(start_dir, zip_dir_name + copy_dir_text)
            else:
                break
        os.mkdir(full_zip_dir_path)

        zipfile.ZipFile(full_zip_file_path).extractall(path=full_zip_dir_path)

        unpacked_file_list = os.listdir(full_zip_dir_path)
        for unpacked_file_name in unpacked_file_list:
            os.rename(os.path.join(full_zip_dir_path, unpacked_file_name),
                      os.path.join(full_zip_dir_path, zip_dir_name + "-" + unpacked_file_name))

        os.replace(full_zip_file_path, os.path.join(full_zip_dir_path, zip_file_name))

    return


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
             "2": "Unzip and unpack into separate directories",
             "3": "Rename zip files",
             "4": "Unzip and rename into single directory",
             "5": "Convert .webp files to .jpg in directory and subdirectories"}


# Main script
if __name__ == "__main__":
    # Welcome text
    print_line("=")
    print("Welcome to ZIPORG")
    print("Entering the phrase \"exit\" always quits the script")

    # Feature select
    while True:
        feat_select = select_from_menu(feat_dict, "a feature")
        if feat_select == "1":
            current_path = change_current_start_dir_path()
            feat_dict["1"] = f"Set different start directory path (currently: \"{current_path}\")"
        elif feat_select == "2":
            unpack_zip_files_separately(current_path)
        else:
            print(f"Option {feat_select} selected: {feat_dict[feat_select]}")
