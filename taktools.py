#!/usr/bin/env python3
# Collection of functions
# TODO: Add folder iteration function
# TODO: Turn into proper package

# Import packages
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


# Define global variables

# Main script
if __name__ == "__main__":
    print_line("=")
    print("Ciao bella, ciao")
    print_line("=")
    sys.exit()
