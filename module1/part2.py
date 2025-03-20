#!/usr/bin/env python3

# Name: Kevin Darling
# Course: CSC500
# Module: 1
# Created Date: 2025-03-16

import udf_util

entry_prompt = "\nThis program allows you to enter 2 numbers, with the multiplication and division of the numbers calculated as the program output. Enter 'q' at any time to exit the program.\n"

def get_results(x=0, y=0):
    """
    This function takes two inputs Integers and prints the multiplication and division results.
    If y is 0, division will not occur (unable to divide by 0).
    
    Parameters:
        x (int): The first Integers
        y (int): The second Integers
    
    Returns:
        None
    """
    print(f"The multiplication of {x} and {y} is: {x * y}")
    if y != 0:
        print(f"The division of {x} and {y} (with a precision of 2) is: {x / y:.2f}")
    else:
        print("Unable to produce division result - The second number entered was {y} (unable to divide by {y}).")

def main():
    while True:
        print(entry_prompt)
        get_results(*udf_util.get_user_input_numbers())
        if input("\nEnter 'q' to quit or any other input to start over: ").lower() == 'q':
            print("Exiting program... Goodbye!")
            break

if __name__ == "__main__":
    main()