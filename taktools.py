#!/usr/bin/env python3
# Collection of common functions

# Import packages
import os
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


def print_dict_items(menu_dict):
    """Print all the items in an input menu.
        Args:
            menu_dict (dict): A dictionary containing menu items
        Returns: None
    """
    print_line("-")
    # Print all the menu items
    for item in menu_dict:
        print(f"({item}) {menu_dict[item]}")
    print_line("-")
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
    print_dict_items(menu_dict)
    # Ask to select and return selection if valid
    while True:
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


# Main script
if __name__ == "__main__":
    quit_script()
