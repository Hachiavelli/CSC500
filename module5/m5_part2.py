#!/usr/bin/env python3

# Name: Kevin Darling
# Course: CSC500
# Module: 5
# Created Date: 2025-03-29

entry_prompt = "\nThis program allows the user to enter the number of books purchased this month, and the rewawrd points will be displayed. Enter 'q' to exit the program.\n "


def get_user_input_int():
    """
    This function prompts the user to enter a integer amount, or q to exit.

    Parameters:
        None

    Returns:
        input_int (int): The int value entered by the user.
    """
    validate_input = False
    while not validate_input:
        input_int = input(
            "Please insert the number of books purchased this month (or 'q' to quit): "
        )
        if input_int.lower() == "q":
            print("Exiting program... Goodbye!")
            exit()
        try:
            input_int = int(input_int)
            print(f"You entered the amount: {input_int}\n")
            validate_input = True
        except ValueError:
            print("Invalid entry. Please enter an int.\n")
    return input_int


def calculate_reward_points(books_purchased):
    """
    This function calculates the reward points based on the number of books purchased using a Python switch statement.

    Parameters:
        books_purchased (int): The number of books purchased this month.

    Returns:
        (int) or (str): returns the number points earned or an invalid message.
    """
    if books_purchased >= 0:
        match books_purchased:
            case 0 | 1:
                return 0
            case 2 | 3:
                return 5
            case 4 | 5:
                return 15
            case 6 | 7:
                return 30
            case _ if books_purchased >= 8:
                return 60
    else:
        return "Unable to calculate reward points - Please enter a valid number greater than 0."


def main():
    while True:
        print(entry_prompt)
        print(f"Reward points earned: {calculate_reward_points(get_user_input_int())}")
        if (
            input("\nEnter 'q' to quit or any other input to start over: ").lower()
            == "q"
        ):
            print("Exiting program... Goodbye!")
            break


if __name__ == "__main__":
    main()
