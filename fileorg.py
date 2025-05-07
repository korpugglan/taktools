#!/usr/bin/env python3
# TODO: update folder setting functionality to use the stuff from ziporg
# TODO: folder iteration setting option
# TODO: group scripts into this one
# TODO: todo's in taktools.py
# TODO: add flags for menu options + settings overwrite
# TODO: show current settings in menu
# TODO: add ASCII art

# Import packages
import os
import taktools as tt


# Define functions

# Define global variables
current_path = os.path.abspath(os.path.dirname(__file__))
feat_dict = {"1": "Convert .webp files to .jpg in directory and subdirectories",
             "exit": "Quit the script",
             "a": f"Set different working folder path (currently: \"{current_path}\")"}

# feat_dict = {"1": f"Set different start directory path (currently: \"{current_path}\")",
#              "2": "Unzip and unpack into separate directories",
#              "3": "Rename zip files",
#              "4": "Unzip and rename into single directory",
#              "5": "Convert .webp files to .jpg in directory and subdirectories"}

if __name__ == "__main__":
    tt.print_line("=")
    print("Welcome to the Johnny Aschenbecher file organization tool")
    while True:
        selected_option = tt.select_from_menu(feat_dict)
        if selected_option == "1":
            tt.webp_to_jpg(image_folder=current_path)
        elif selected_option == "a":
            current_path = input(f"Please enter the full folder path: ")
            print(f"Folder path has been set to {current_path}.")
        else:
            break

        # if selected_option == "1":
        #     current_path = change_current_start_dir_path()
        #     feat_dict["1"] = f"Set different start directory path (currently: \"{current_path}\")"
        # elif feat_select == "2":
        #     unpack_zip_files_separately(current_path)
        # else:
        #     print(f"Option {feat_select} selected: {feat_dict[feat_select]}")

    tt.quit_script()
