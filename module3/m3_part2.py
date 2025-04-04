#!/usr/bin/env python3

# Name: Kevin Darling
# Course: CSC500
# Module: 3
# Created Date: 2025-03-26

from datetime import date, datetime, timedelta

entry_prompt = "\nThis program allows the user to enter the current time, as well as how many hours to wait for the alarm, and the program will calculate the alarm trigger time. Enter 'q' to exit the program.\n "


def get_user_time():
    """
    This function prompts the user to enter a time amount, or q to exit.

    Parameters:
        None

    Returns:
        [hour, minute] (list): A list of the hour and minute values entered by the user.
    """
    validate_input = False
    while not validate_input:
        user_input = input(
            "Enter the current time in 24-hour clock format - HH:MM (or 'q' to quit): "
        )
        if user_input.lower() == "q":
            print("Exiting program... Goodbye!")
            exit()
        try:
            hour, minute = map(int, user_input.split(":"))
            if 0 <= hour < 24 and 0 <= minute < 60:
                user_datetime = datetime.combine(
                    date.today(), datetime.strptime(user_input, "%H:%M").time()
                )
                print(f"You entered the time: {user_datetime}\n")
                validate_input = True
                return [hour, minute]
        except ValueError:
            print("Invalid entry. Please enter an float.\n")


def get_hours_to_wait():
    """
    This function prompts the user to enter a number of hours to wait, or q to exit.

    Parameters:
        None

    Returns:
        hours_to_wait (int): User entered integer value.
    """
    validate_input = False
    while not validate_input:
        input_num = input(
            "Please insert the number of hours to wait (or 'q' to quit): "
        )
        if input_num.lower() == "q":
            print("Exiting program... Goodbye!")
            exit()
        try:
            input_num = int(input_num)
            print(f"You entered the number: {input_num}\n")
            validate_input = True
        except ValueError:
            print("Invalid entry. Please enter an integer.\n")
    return input_num


def calculate_alarm_time(hour_and_minutes=[], delay=0):
    """
    This function calculates the time difference between the hours_and_minutes values and the delay value.

    Parameters:
        hour_and_minutes (list): A list with the first value being the hour, and the second minutes.
        delay (int): The number of hours to delay.

    Returns:
        None
    """
    start = datetime.now().replace(
        hour=hour_and_minutes[0], minute=hour_and_minutes[1], second=0, microsecond=0
    )
    print(f"Alarm will go off at: {start + timedelta(hours=delay)}")


def main():
    while True:
        print(entry_prompt)
        user_time = get_user_time()
        hours_to_wait = get_hours_to_wait()
        calculate_alarm_time(user_time, hours_to_wait)
        if (
            input("\nEnter 'q' to quit or any other input to start over: ").lower()
            == "q"
        ):
            print("Exiting program... Goodbye!")
            break


if __name__ == "__main__":
    main()
