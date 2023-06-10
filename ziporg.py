#!/usr/bin/env python3
# Script to batch process and organize zip files
# TODO: Add settings to update
# TODO: Add webp to jpg feature

# Import packages
import sys
import taktools as tt


# Define global variables
feat_dict = {"1": "Rename zip files",
             "2": "Unzip and rename into single folder",
             "3": "Unzip and unpack into separate folders"}

# Main script
if __name__ == "__main__":
    # Welcome text
    tt.print_line("=")
    print("Welcome to ZIPORG")
    print("Entering the phrase \"exit\" always quits the script")

    # Feature select
    feat_select = tt.select_from_menu(feat_dict, "feature")
    print(f"{feat_select} selected. This means \"{feat_dict[feat_select]}\"")

    tt.quit_script()
