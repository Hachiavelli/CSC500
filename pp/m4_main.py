#!/usr/bin/env python3

# Name: Kevin Darling
# Course: CSC500
# Module: 4
# Created Date: 2025-04-08

import ItemToPurchase

entry_prompt = "\nThis program allows the user to enter two items, including the item name, item price, and item quantity, with entry validation and purchase summary printed to the console. Enter 'q' to exit the program.\n "


def main():
    while True:
        print(entry_prompt)
        items_to_purchase = [
            ItemToPurchase.build_item(item_num + 1) for item_num in range(2)
        ]
        print("Purchase Summary & Total Cost:")
        [item.print_item_cost() for item in items_to_purchase]
        print(
            f"Total Cost: ${sum([item.item_total_cost for item in items_to_purchase])}"
        )
        if (
            input("\nEnter 'q' to quit or any other input to start over: ").lower()
            == "q"
        ):
            print("Exiting program... Goodbye!")
            break


if __name__ == "__main__":
    main()
