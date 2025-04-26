#!/usr/bin/env python3

# Name: Kevin Darling
# Course: CSC500
# Module: 6
# Created Date: 2025-04-26

import udf_utils
import ItemToPurchase as ItemToPurchaseClass


def build_cart():
    """
    This function works with the udf_util input functions to manage and handle building new instances of carts.

    Parameters:
        None

    Returns:
        new_cart: Newly created instance of ShoppingCart.
    """
    customer_name = udf_utils.get_user_input_string(label="the customer name")
    current_date = udf_utils.get_user_input_string(
        label="today's date in the following format (Month Day, Year) - February 1, 2020: "
    )
    new_cart = ShoppingCart(customer_name, current_date)
    print(f"New cart created for {customer_name} on {current_date}!\n")
    return new_cart


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        """Init function with default constructors"""
        self._customer_name = customer_name
        self._current_date = current_date
        self._cart_items = []

    @property
    def customer_name(self):
        """Getter function"""
        return self._customer_name

    @property
    def current_date(self):
        """Getter function"""
        return self._current_date

    @property
    def cart_items(self):
        """Getter function"""
        return self._cart_items

    @customer_name.setter
    def customer_name(self, value):
        """Setter function"""
        if not isinstance(value, str):
            raise ValueError("Customer name must be a string.")
        self._customer_name = value

    @current_date.setter
    def current_date(self, value):
        """Setter function"""
        if not isinstance(value, str):
            raise ValueError("Current date must be a string.")
        self._current_date = value

    @cart_items.setter
    def cart_items(self, value):
        """Setter function"""
        if not isinstance(value, list):
            raise ValueError("Cart items must be a list.")
        self._cart_items = value

    def add_item(self, ItemToPurchase=None):
        """
        This function adds an object from the ItemToPurchase class to the cart.

        Parameters:
            ItemToPurchase (class object): Item to add to cart.

        Returns:
            None.
        """
        if ItemToPurchase is None:
            ItemToPurchase = ItemToPurchaseClass.ItemToPurchase()
        self.cart_items.append(ItemToPurchase)

    def remove_item(self, item_name=None):
        """
        This function removes an ItemToPurchase object with a matching item_name from the cart.

        Parameters:
            item_name (string): Item name to search and remove.

        Returns:
            None.
        """
        if item_name is not None:
            initial_length = len(self.cart_items)
            self.cart_items = [
                item for item in self.cart_items if item.item_name != item_name
            ]

            if len(self.cart_items) < initial_length:
                print(f"Item {item_name} removed from cart.")
            else:
                print("Nothing removed.")

    def modify_item(self, modified_item):
        """
        This function modifies an ItemToPurchase object's quantity and updates the total cost.

        Parameters:
            modified_item (class object): A new ItemToPurchase object.

        Returns:
            None
        """
        for item in self.cart_items:
            if item.item_name == modified_item.item_name:
                if modified_item.item_quantity > 0:
                    item.item_quantity = modified_item.item_quantity
                    print(
                        f"Item {item.item_name} quantity modified successfully. New quantity: {item.item_quantity}"
                    )
                    item.calculate_item_total_cost()
                    print(
                        f"Total cost for {item.item_name} updated to reflect new quantity. New total: ${item.item_total_cost}"
                    )
                    return
        print(f"Item {modified_item.item_name} not found in cart.")
        return

    def get_num_items_in_cart(self):
        """
        This function gets the total number of items in the cart from all item objects.

        Parameters:
            cart (class object): The cart class object.

        Returns:
            None
        """
        total = 0
        for item in self.cart_items:
            total += item.item_quantity
        return total

    def get_cost_of_cart(self):
        """
        This function calculates the total cost of all items and all quantities in the cart.

        Parameters:
            cart (class object): The cart class object.

        Returns:
            None
        """
        total_cost = 0.0
        for item in self.cart_items:
            total_cost += item.item_price * item.item_quantity
        return total_cost

    def print_total(self):
        """
        This function prints the total cost of items in the cart, or the required empty verbiage if applicable.

        Parameters:
            cart (class object): The cart class object.

        Returns:
            None
        """
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
            return
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}\n")
        for item in self.cart_items:
            item.print_item_cost()
        print(f"\nTotal: ${self.get_cost_of_cart()}")

    def print_descriptions(self):
        """
        This function prints the item descriptions for all items in the cart.

        Parameters:
            cart (class object): The cart class object.

        Returns:
            None
        """
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}\n")
        print("Item Descriptions")
        for item in self.cart_items:
            item.print_item_description()
