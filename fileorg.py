#!/usr/bin/env python3
# TODO: process ziporg.py
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

# Define functions
def unzip_and_rename(main_folder):




    # max_zip_file_name_len = 64
    # del_char_list = ["~", ".", ",", "!", "@", "#", "$"]
    #
    # zip_file_list = [file for file in os.listdir(start_dir) if file.endswith(".zip")]
    # for zip_file_name in zip_file_list:
    #     new_zip_file_name = zip_file_name[:-len(".zip")]
    #     for del_char in del_char_list:
    #         new_zip_file_name = new_zip_file_name.replace(del_char, "")
    #     while True:
    #         if "  " in new_zip_file_name:
    #             new_zip_file_name = new_zip_file_name.replace("  ", "")
    #         else:
    #             break
    #     new_zip_file_name = new_zip_file_name.strip()
    #     new_zip_file_name = new_zip_file_name[:max_zip_file_name_len] + ".zip"
    #     os.rename(os.path.join(start_dir, zip_file_name),
    #               os.path.join(start_dir, new_zip_file_name))
    #     zip_file_name = new_zip_file_name
    #
    #     full_zip_file_path = os.path.join(start_dir, zip_file_name)
    #     zip_dir_name = zip_file_name[:-4]
    #
    #     full_zip_dir_path = os.path.join(start_dir, zip_dir_name)
    #     while True:
    #         if os.path.isdir(full_zip_dir_path):
    #             copy_dir_text = "-COPY"
    #             print(f"WARNING! Directory \"{full_zip_dir_path}\" exists. "
    #                   f"Adding \"{copy_dir_text}\" to directory name")
    #             full_zip_dir_path = os.path.join(start_dir, zip_dir_name + copy_dir_text)
    #         else:
    #             break
    #     os.mkdir(full_zip_dir_path)
    #
    #     zipfile.ZipFile(full_zip_file_path).extractall(path=full_zip_dir_path)
    #
    #     unpacked_file_list = os.listdir(full_zip_dir_path)
    #     for unpacked_file_name in unpacked_file_list:
    #         os.rename(os.path.join(full_zip_dir_path, unpacked_file_name),
    #                   os.path.join(full_zip_dir_path, zip_dir_name + "-" + unpacked_file_name))
    #
    #     os.replace(full_zip_file_path, os.path.join(full_zip_dir_path, zip_file_name))




    return


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
            "use_subfolders": False,
            "unzip_into_single_folder": False,}
menu = {"1": "Convert .webp files to .jpg in folder",
        "2": "Unzip and rename with zipfile prefix",
        "exit": "Quit the script",
        "a": "View current settings",
        "b": "Set different working folder path",
        "c": "Set iterating over subfolders",}


if __name__ == "__main__":
    while True:
        tt.print_line("=")
        print("Johnny Aschenbecher file organization tool")
        selected_option = tt.select_from_menu(menu)
        if selected_option == "1":
            webp_to_jpg(main_folder=settings["current_path"], use_subfolders=settings["use_subfolders"])
        elif selected_option == "2":
            unzip_and_rename(main_folder=settings["current_path"])
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


    tt.quit_script()
