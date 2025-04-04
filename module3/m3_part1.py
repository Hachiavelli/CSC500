#!/usr/bin/env python3

# Name: Kevin Darling
# Course: CSC500
# Module: 3
# Created Date: 2025-03-26

sales_tax = 0.07
gratuity = 0.18
entry_prompt = "\nThis program allows the user to enter a bill amount, and the total will be calculated with a 7% sales tax and 18% gratuity. Enter 'q' to exit the program.\n "


def get_user_input_float():
    """
    This function prompts the user to enter a float amount, or q to exit.

    Parameters:
        None

    Returns:
        input_float (float): The float value entered by the user.
    """
    validate_input = False
    while not validate_input:
        input_float = input("Please insert the bill amount (or 'q' to quit): ")
        if input_float.lower() == "q":
            print("Exiting program... Goodbye!")
            exit()
        try:
            input_float = float(input_float)
            print(f"You entered the amount: ${input_float:.2f}\n")
            validate_input = True
        except ValueError:
            print("Invalid entry. Please enter an float.\n")
    return input_float


def calculate_bill_total(user_float=None):
    """
    This function calculates the total bill amount after sales tax and gratuity.

    Parameters:
        user_float (float): Float amount used as the base for calculations.

    Returns:
        None
    """
    calculated_sales_tax = user_float * sales_tax
    print(f"Sales Tax = ${calculated_sales_tax:.2f} @ {(sales_tax * 100):.2f}%")
    calculated_gratuity = user_float * gratuity
    print(f"Gratuity = ${calculated_gratuity:.2f} @ {(gratuity * 100):.2f}%")
    print(
        f"Total amount owed = ${(user_float + calculated_sales_tax + calculated_gratuity):.2f}"
    )


def main():
    while True:
        print(entry_prompt)
        calculate_bill_total(get_user_input_float())
        if (
            input("\nEnter 'q' to quit or any other input to start over: ").lower()
            == "q"
        ):
            print("Exiting program... Goodbye!")
            break


if __name__ == "__main__":
    main()