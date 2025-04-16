#!/usr/bin/env python3

# Name: Kevin Darling
# Course: CSC500
# Module: 5
# Created Date: 2025-03-29

from statistics import mean

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]
entry_prompt = "\nThis program allows the user to enter in rainfall data for a predetermined number of years, with the average rainfall calculated. Enter 'q' to exit the program.\n "


def get_user_year_number():
    """
    This function prompts the user to enter an Integer value. If the input is not an
    integer, the user will be prompted to reinput a value. The user can enter 'q' at
    any time to exit the program.

    Parameters:
        None

    Returns:
        input_num: An integer entered by the user.
    """
    validate_input = False
    while not validate_input:
        input_num = input(
            "Please insert number of years of data to enter (or 'q' to quit): "
        )
        if input_num.lower() == "q":
            print("Exiting program... Goodbye!")
            exit()
        try:
            input_num = int(input_num)
            print(f"You entered {input_num} years.\n")
            validate_input = True
        except ValueError:
            print("Invalid entry. Please enter an integer.\n")
    return input_num


def get_user_input_float(month):
    """
    This function prompts the user to enter a float amount, or q to exit.

    Parameters:
        month: The current month of data to collect.

    Returns:
        input_float (float): The float value entered by the user.
    """
    validate_input = False
    while not validate_input:
        input_float = input(
            f"Please insert the inches of rainfall float amount for the month {month} (or 'q' to quit): "
        )
        if input_float.lower() == "q":
            print("Exiting program... Goodbye!")
            exit()
        try:
            input_float = float(input_float)
            print(f"You entered the amount: {input_float:.2f}\n")
            validate_input = True
        except ValueError:
            print("Invalid entry. Please enter an float.\n")
    return input_float


def main():
    while True:
        print(entry_prompt)
        years_entered = get_user_year_number()
        years = years_entered
        rainfall = []
        while years > 0:
            for month in months:
                rainfall.append(get_user_input_float(month))
            years -= 1
        print(
            f"You entered {years_entered} years of data with {years_entered * len(months)} months of rainfall entered."
        )
        print(f"Total inches rainfall: {sum(rainfall):.2f}")
        print(f"The average inches rainfall: {mean(rainfall):.2f}")
        if (
            input("\nEnter 'q' to quit or any other input to start over: ").lower()
            == "q"
        ):
            print("Exiting program... Goodbye!")
            break


if __name__ == "__main__":
    main()
