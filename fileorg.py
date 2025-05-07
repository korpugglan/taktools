#!/usr/bin/env python3
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
from glob import iglob
import os
from PIL import Image
import taktools as tt

# Define functions
def update_path(current_path):
    """Updates an OS path after validation .
        Args:
            current_path (str): The input path
        Returns:
            new_path (str): The updated and validated path
    """
    while True:
        # Register new path
        new_path_str = input(f"The current path is \"{current_path}\". Please enter the new path: ")
        new_path = os.fspath(new_path_str)
        # Return path if it is valid
        if os.path.isdir(new_path):
            print(f"Path changed to \"{new_path}\"")
            return new_path
        # Ask to fix the path if invalid
        else:
            tt.print_line()
            # TODO: add tips about OS specific writing methods
            print("Invalid input. Path is not an accessible directory. Please try again.\n"
                  "Tip: Based on your OS you may need to use /, \\ or \\\\.\n"
                  "Tip: Make sure you have access to the path.\n")


def webp_to_jpg(main_folder, use_subfolders=False):
    """Converts all .webp files in a folder to .jpg with the option to also include all subfolders.
        Args:
            main_folder (str): The folder containing the .webp files.
            use_subfolders (bool): Whether to iterate over subfolders too. Defaults to False.
        Returns: None
    """
    folder_list = []
    if not use_subfolders:
        folder_list = [main_folder]
    elif use_subfolders:
        main_folder_glob = str(main_folder) + "/**/*"
        folder_list = [f for f in iglob(main_folder_glob, recursive=True) if os.path.isdir(f)]
        folder_list.insert(0, main_folder)
    else:
        print(f"WTF: use_subfolders is set to {use_subfolders}")

    for folder in folder_list:
        webp_to_jpg_single_folder(folder)

    print(f"Operation completed successfully.")
    return


def webp_to_jpg_single_folder(image_folder):
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

    return


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
            webp_to_jpg(main_folder=settings["current_path"], use_subfolders=settings["use_subfolders"])
        elif selected_option == "exit":
            tt.quit_script()
        elif selected_option == "a":
            tt.print_dict_items(settings)
        elif selected_option == "b":
            settings["current_path"] = update_path(settings["current_path"])
        elif selected_option == "c":
            settings["use_subfolders"] = not settings["use_subfolders"]
            print(f"use_subfolders is set to {settings['use_subfolders']}")
        else:
            break


        # elif feat_select == "2":
        #     unpack_zip_files_separately(current_path)


    tt.quit_script()
