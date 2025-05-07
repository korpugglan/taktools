#!/usr/bin/env python3
# TODO: rename taktools and recreate a taktools with only common base functions
# TODO: group scripts into this one
# TODO: todo's in taktools.py
# TODO: add flags for menu options + settings overwrite
# TODO: show current settings in menu
# TODO: add ASCII art
# TODO: make exit exit everywhere elegantly
# TODO: Add file name cleaning (~, .., double spaces, trimming)
# TODO: Add subdirectory iteration
# TODO: Add Windows executable
# TODO: Add webp to jpg feature
# TODO: Find better package to work with Program Files Python installation
# TODO: Proper refactor
# TODO: Add folder iteration function
# TODO: Turn into proper package
# TODO: webp_to_jpg;
#   - test Pillow with (partially) transparent background
#   - add command line flags for local and specific locations to start from
#   - add subfolder iteration option
#   - add Windows executable or shortcut creator
# TODO: fix lines and layout
# TODO: group print items
# TODO: move settings option to submenu
# TODO: make menu selection in this script dynamic
# TODO: make warning messages for redundant else statements
# TODO: add progress bar function to taktools and implement where cool
# TODO: webp_to_jpg fix overwriting existing files

# Import packages
import os
import taktools as tt

# Define functions

# Define global variables
settings = {"current_path": os.path.abspath(os.path.dirname(__file__)),
            "use_subfolders": False,}
menu = {"1": "Convert .webp files to .jpg in folder",
        "exit": "Quit the script",
        "a": "View current settings",
        "b": "Set different working folder path",
        "c": "Set iterating over subfolders",}

# feat_dict = {
#              "2": "Unzip and unpack into separate directories",
#              "3": "Rename zip files",
#              "4": "Unzip and rename into single directory",
#              "5": "Convert .webp files to .jpg in directory and subdirectories"}

if __name__ == "__main__":
    while True:
        tt.print_line("=")
        print("Johnny Aschenbecher file organization tool")
        selected_option = tt.select_from_menu(menu)
        if selected_option == "1":
            tt.webp_to_jpg(main_folder=settings["current_path"], use_subfolders=settings["use_subfolders"])
        elif selected_option == "exit":
            tt.quit_script()
        elif selected_option == "a":
            tt.print_dict_items(settings)
        elif selected_option == "b":
            settings["current_path"] = tt.update_path(settings["current_path"])
        elif selected_option == "c":
            settings["use_subfolders"] = not settings["use_subfolders"]
            print(f"use_subfolders is set to {settings['use_subfolders']}")
        else:
            break


        # elif feat_select == "2":
        #     unpack_zip_files_separately(current_path)


    tt.quit_script()
