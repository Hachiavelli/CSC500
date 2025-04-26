#!/usr/bin/env python3

# Name: Kevin Darling
# Course: CSC500
# Module: 6
# Created Date: 2025-04-26

import udf_utils
import ShoppingCart
import ItemToPurchase


def print_menu(shopping_cart):
    """
    This function acts as the main menu for the application.

    Parameters:
        shopping_cart (class object): The shopping cart object to reference.

    Returns:
        None
    """
    menu_options = {
        "a": "Add item to cart",
        "r": "Remove item from cart",
        "c": "Change item quantity",
        "i": "Output items' descriptions",
        "o": "Output shopping cart",
        "q": "Quit",
    }

    while True:
        print("\n\n*** Shopping Cart Menu ***")
        [print(f"    {k} - {v}") for k, v in menu_options.items()]
        menu_selection = udf_utils.get_user_input_string(label="menu option")
        if menu_selection == "q":
            print("Exiting program... Goodbye!")
            break
        elif menu_selection == "a":
            print("\n*** Add Item To Cart ***")
            shopping_cart.add_item(ItemToPurchase.build_item(1))
            print("Item added to cart.")

        elif menu_selection == "r":
            print("\n*** Remove Item From Cart ***")
            item_name = udf_utils.get_user_input_string(label="item name to remove")
            if shopping_cart.remove_item(item_name):
                print(f"{item_name} removed.")

        elif menu_selection == "c":
            print("\n*** Change Item Quantity ***")
            item_name = udf_utils.get_user_input_string(label="item name to change")
            item_quantity = udf_utils.get_user_input_int(label="the new item quantity")
            new_item = ItemToPurchase.ItemToPurchase(
                item_name=item_name,
                item_price=0,
                item_quantity=item_quantity,
                item_description="",
                item_total_cost=0,
            )
            shopping_cart.modify_item(new_item)

        elif menu_selection == "i":
            print("\n*** Output Items' Descriptions ***")
            shopping_cart.print_descriptions()
        elif menu_selection == "o":
            print("\n*** Output Shopping Cart ***")
            shopping_cart.print_total()
        else:
            print("Invalid selection. Please try again (or 'q' to quit).")


def main():
    cart = ShoppingCart.build_cart()
    print_menu(cart)


if __name__ == "__main__":
    main()
