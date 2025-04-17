#!/usr/bin/env python3

# Name: Kevin Darling
# Course: CSC500
# Module: 7
# Created Date: 2025-04-16

entry_prompt = "\nThis program allows the user to enter a course value, and the course information will be returned. Enter 'q' to exit the program.\n "

room_dict = {
    "CSC101": 3004,
    "CSC102": 4501,
    "CSC103": 6755,
    "NET110": 1244,
    "COM241": 1411,
}

instructor_dict = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee",
}

course_time_dict = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m.",
}


def get_user_input_string():
    """
    This function prompts the user to enter a string, or q to exit.

    Parameters:
        None

    Returns:
        input_str (str): The str value entered by the user.
    """
    validate_input = False
    while not validate_input:
        input_str = input("Please insert the course value (or 'q' to quit): ")
        if input_str.lower() == "q":
            print("Exiting program... Goodbye!")
            exit()
        try:
            input_str = str(input_str)
            print(f"You entered the course: {input_str}\n")
            validate_input = True
        except ValueError:
            print("Invalid entry. Please enter a course value.\n")
    return input_str


def get_results(lookup_value):
    """
    This function takes passed lookup_value and finds matches for the result in the dictionaries, printing results to the console.

    Parameters:
        lookup_value (str): The user-entered value to lookup.

    Returns:
        None
    """
    dicts = [room_dict, instructor_dict, course_time_dict]
    lookup_value_tuple = {
        lookup_value: [
            (key, value)
            for dictionary in dicts
            for key, value in dictionary.items()
            if key == lookup_value
        ]
    }
    if not lookup_value_tuple[lookup_value]:
        print("No matches found.")
        return
    output_labels = ["Room", "Instructor", "Course Time"]
    for i, label in enumerate(output_labels):
        if i < len(lookup_value_tuple[lookup_value]):
            print(f"{label}: {lookup_value_tuple[lookup_value][i][1]}")


def main():
    while True:
        print(entry_prompt)
        get_results(get_user_input_string().upper())
        if (
            input("\nEnter 'q' to quit or any other input to start over: ").lower()
            == "q"
        ):
            print("Exiting program... Goodbye!")
            exit()


if __name__ == "__main__":
    main()
