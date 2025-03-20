#!/usr/bin/env python3

# Name: Kevin Darling
# Course: CSC500
# Module: 1
# Created Date: 2025-03-16

import udf_util

entry_prompt = "\nThis program allows the user to enter 2 numbers, with the addition and subtraction of the numbers calculated as the program output. Enter 'q' at any time to exit the program.\n "

def get_results(x=0, y=0):
    """
    This function takes two input Integers and prints the addition and subtraction results.
    
    Parameters:
        x (int): The first Integers
        y (int): The second Integers
    
    Returns:
        None
    """
    print(f"The addition of {x} and {y} is: {x + y}")
    print(f"The subtraction of {x} and {y} is: {x - y}")

def main():
    while True:
        print(entry_prompt)
        get_results(*udf_util.get_user_input_numbers())
        if input("\nEnter 'q' to quit or any other input to start over: ").lower() == 'q':
            print("Exiting program... Goodbye!")
            break

if __name__ == "__main__":
    main()