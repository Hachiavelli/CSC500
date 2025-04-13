#!/usr/bin/env python3

# Name: Kevin Darling
# Course: CSC500
# Module: 4
# Created Date: 2025-04-08


def get_user_input_int(label=""):
    """
    This function prompts the user to enter an integer amount, or q to exit.

    Parameters:
        label (str): A dynamic label for the print statement.

    Returns:
        input_int (int): The int value entered by the user.
    """
    validate_input = False
    while not validate_input:
        input_int = input(f"Please insert {label} (or 'q' to quit): ")
        if input_int.lower() == "q":
            print("Exiting program... Goodbye!")
            exit()
        try:
            if not isinstance(input_int, int):
                validate_input = True
        except ValueError:
            print("Invalid entry. Please enter a valid integer.\n")
    return int(input_int)


def get_user_input_string(label=""):
    """
    This function prompts the user to enter a string, or q to exit.

    Parameters:
        label (str): A dynamic label for the print statement.

    Returns:
        input_str (str): The str value entered by the user.
    """
    validate_input = False
    while not validate_input:
        input_str = input(f"Please insert {label} (or 'q' to quit): ")
        if input_str.lower() == "q":
            print("Exiting program... Goodbye!")
            exit()
        validate_input = True
    return input_str
