#!/usr/bin/env python3

# Name: Kevin Darling
# Course: CSC500
# Module: 6
# Created Date: 2025-04-08
# Updated Date: 2025-04-26


def get_user_input_int(label=""):
    """
    This function prompts the user to enter an integer amount, or q to exit.

    Parameters:
        label (str): A dynamic label for the print statement.

    Returns:
        input_int (int): The int value entered by the user.
    """
    while True:
        user_input = input(f"Please insert {label} (or 'q' to quit): ").strip()
        if user_input.lower() == "q":
            print("Exiting program... Goodbye!")
            exit()
        try:
            return int(user_input)
        except ValueError:
            print("Invalid entry. Please enter a valid integer.\n")


def get_user_input_string(label=""):
    """
    This function prompts the user to enter a string, or q to exit.

    Parameters:
        label (str): A dynamic label for the print statement.

    Returns:
        input_str (str): The str value entered by the user.
    """
    input_str = input(f"Please insert {label} (or 'q' to quit): ")
    if input_str.lower() == "q":
        print("Exiting program... Goodbye!")
        exit()
    return input_str
