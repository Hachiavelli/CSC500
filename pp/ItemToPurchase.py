#!/usr/bin/env python3

# Name: Kevin Darling
# Course: CSC500
# Module: 4
# Created Date: 2025-04-08

import udf_utils


def build_item(num=0):
    """
    This function works with the udf_util input functions to manage and handle building new instances of items.

    Parameters:
        num (int): The number of items to created.

    Returns:
        new_item: Newly created instance of ItemToPurchase.
    """
    print(f"Building Item #{num}:")
    new_item = ItemToPurchase()
    new_item.item_name = udf_utils.get_user_input_string(label="the item name")
    new_item.item_price = udf_utils.get_user_input_int(label="the item price")
    new_item.item_quantity = udf_utils.get_user_input_int(label="the item quantity")
    new_item.calculate_item_total_cost()
    print("Item built!\n")
    return new_item


class ItemToPurchase:
    def __init__(
        self, item_name="none", item_price=0, item_quantity=0, item_total_cost=0
    ):
        """Init function with default constructors"""
        self._item_name = item_name
        self._item_price = int(item_price)
        self._item_quantity = int(item_quantity)
        self._item_total_cost = int(item_total_cost)

    @property
    def item_name(self):
        """Getter function"""
        return self._item_name

    @property
    def item_price(self):
        """Getter function"""
        return self._item_price

    @property
    def item_quantity(self):
        """Getter function"""
        return self._item_quantity

    @property
    def item_total_cost(self):
        """Getter function"""
        return self._item_total_cost

    @item_name.setter
    def item_name(self, value):
        """Setter function"""
        if not isinstance(value, str):
            raise ValueError("Item name must be a string.")
        self._item_name = value

    @item_price.setter
    def item_price(self, value):
        """Setter function"""
        if not isinstance(value, int) or value < 0:
            raise ValueError("Item price must be a non-negative number.")
        self._item_price = value

    @item_quantity.setter
    def item_quantity(self, value):
        """Setter function"""
        if not isinstance(value, int) or value < 0:
            raise ValueError("Item quantity must be a non-negative integer.")
        self._item_quantity = value

    @item_total_cost.setter
    def item_total_cost(self, value):
        """Setter function"""
        if not isinstance(value, int) or value < 0:
            raise ValueError("Item total cost must be a non-negative integer.")
        self._item_total_cost = value

    def calculate_item_total_cost(self):
        """
        This function handles the automatic setting of the total cost attribute.

        Parameters:
            self (class object): Class object instance.

        Returns:
            self.item_total_cost (int): The integer value or 0.
        """
        try:
            self.item_total_cost = self.item_price * self.item_quantity
            return self.item_total_cost
        except (TypeError, AttributeError) as e:
            print(f"Error calculating total: {e}")
            return 0

    def print_item_cost(self):
        """
        This function prints the item details in the required format per assignment.

        Parameters:
            self (class object): Class object instance.

        Returns:
            self.item_total_cost (int): The integer value or 0.
        """
        print(
            f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_total_cost}"
        )
