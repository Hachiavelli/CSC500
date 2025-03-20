#!/usr/bin/env python3

# Name: Kevin Darling
# Course: CSC500
# Module: 1
# Created Date: 2025-03-16

def get_user_input_numbers(num=2):
    """
    This function prompts the user to enter two Integer values, one at a time.
    If the input is not an integer, the user will be prompted to reinput a value.
    The user can enter 'q' at any time to exit the program.
    
    Parameters:
        num (int): Variable allowing any number of values to be input. Default is 2.
    
    Returns:
        list: A list of Integers input by the user.
    """
    num_list = [0] * num
    for i in range(num):
        validate_input = False
        while not validate_input:
            input_num = input(f"Please insert number {i + 1} (or 'q' to quit): ")
            if input_num.lower() == "q":
                print("Exiting program... Goodbye!")
                exit()
            try:
                input_num = int(input_num)
                print(f"You entered the number: {input_num}\n")
                validate_input = True
            except ValueError:
                print("Invalid entry. Please enter an integer.\n")
        num_list[i] = input_num
    return num_list
