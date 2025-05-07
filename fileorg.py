#!/usr/bin/env python3
# TODO: process ziporg.py
#   - Test the unzip functionality
#   - Refactor unzip
#   - Choice to group zips or not
#   - Fix file name cleaning (~, .., double spaces, trimming)
# TODO: webp_to_jpg;
#   - test Pillow with (partially) transparent background
#   - add command line flags for local and specific locations to start from
#   - add subfolder iteration option
#   - add Windows executable or shortcut creator
#   - fix overwriting existing files
# TODO: visual
#   - show current settings in menu
#   - add ASCII art
#   - fix lines and layout
#   - add progress bar function to taktools and implement where cool
# TODO: added functionality
#   - rename zip files in folder
#   - Add prompt flags for options
#   - Add Windows executable
# TODO: Refactoring
#   - Proper refactor
#   - make exit exit everywhere elegantly
#   - Turn into proper package
#   - group print items in taktools.py
#   - move settings option to submenu
#   - make menu selection in this script dynamic
#   - make warning messages for redundant else statements
#   - Proper refactor

# Import packages
from glob import iglob
import os
from PIL import Image
import taktools as tt
import zipfile

# Define functions
def unzip_and_rename(main_folder, char_limit):
    # Set up variables
    ext = ".zip"
    ext_len = len(ext)
    del_char_list = [".", ",", "  "]
    zip_file_list = [file for file in os.listdir(main_folder) if file.endswith(".zip")]

    # Loop through each zip file
    for file_name in zip_file_list:
        # Create a cleaned version of the zip file name
        trunc_name = file_name[:-ext_len]
        # Remove nasty characters
        for del_char in del_char_list:
            while True:
                if del_char in trunc_name:
                    trunc_name = trunc_name.replace(del_char, "")
                else:
                    break
        # Trim the name
        trunc_name = trunc_name.strip()
        # Shorten the name to the max length. - 1 for reuse in file extensions with more characters than ext_len.
        trunc_name = trunc_name[:(char_limit - ext_len - 1)]

        # Create folder to unzip to if it does not exist. Skip if it does.
        new_dir_path = os.path.join(main_folder, trunc_name)
        if os.path.isdir(new_dir_path):
            print(f"WARNING: Folder {new_dir_path} already exists. Unzipping skipped.")
            continue
        else:
            os.makedirs(new_dir_path)

        # Unzip the contents of the zip file to the new folder
        zipfile.ZipFile(file_name).extractall(path=str(new_dir_path))

        # Rename the unzipped files to include the trunc_name
        unzip_files = os.listdir(str(new_dir_path))

        # Find length of longest file name to determine cutoff
        longest_file_name = max(unzip_files, key=len)
        if len(trunc_name + "-" + longest_file_name) > char_limit:
            zip_idx_ext = longest_file_name.rfind(".")
            zip_ext = longest_file_name[zip_idx_ext:]
            cutoff = char_limit - len(zip_ext)
        else:
            cutoff = -1

        # Rename the files
        for unzip_file in unzip_files:
            # Create new file name
            new_unzip_file = trunc_name[:cutoff] + "-" + unzip_file
            # Rename file
            os.rename(os.path.join(str(new_dir_path), str(unzip_file)),
                      os.path.join(str(new_dir_path), new_unzip_file))

        # Move old zip file to a renamed version in new folder
        os.replace(file_name, os.path.join(new_dir_path, trunc_name + ext))

    return


def update_char_limit(current_limit):
    """Updates the character limit after validation .
        Args:
            current_limit (int): The input character limit.
        Returns:
            new_limit (int): The updated and validated character limit.
    """
    while True:
        # Register new path
        new_limit = input(f"The file name character limit is \"{current_limit}\". Please enter the new limit: ")
        # Return limit if it is valid
        try:
            new_limit = int(new_limit)
            print(f"File path character limit changed to \"{new_limit}\".")
            return new_limit
        # Ask to fix the limit if not an int
        except ValueError:
            tt.print_line()
            print("Invalid input. Only integers are allowed. Please try again.")


def update_path(current_path):
    """Updates an OS path after validation .
        Args:
            current_path (str): The input path
        Returns:
            new_path (str): The updated and validated path.
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
            "use_subfolders": False,
            "unzip_into_single_folder": False,
            "file_name_character_limit": 255,}
menu = {"1": "Convert .webp files to .jpg in folder",
        "2": "Unzip and rename with zipfile prefix",
        "exit": "Quit the script",
        "a": "View current settings",
        "b": "Set different working folder path",
        "c": "Set iterating over subfolders",
        "d": "Set file name character limit"}


if __name__ == "__main__":
    while True:
        tt.print_line("=")
        print("Johnny Aschenbecher file organization tool")
        selected_option = tt.select_from_menu(menu)
        if selected_option == "1":
            webp_to_jpg(main_folder=settings["current_path"], use_subfolders=settings["use_subfolders"])
        elif selected_option == "2":
            unzip_and_rename(main_folder=settings["current_path"], char_limit=settings["file_name_character_limit"])
        elif selected_option == "exit":
            tt.quit_script()
        elif selected_option == "a":
            tt.print_dict_items(settings)
        elif selected_option == "b":
            settings["current_path"] = update_path(settings["current_path"])
        elif selected_option == "c":
            settings["use_subfolders"] = not settings["use_subfolders"]
            print(f"use_subfolders is set to {settings['use_subfolders']}")
        elif selected_option == "d":
            settings["file_name_character_limit"] = update_char_limit(settings["file_name_character_limit"])
        else:
            break


    tt.quit_script()
