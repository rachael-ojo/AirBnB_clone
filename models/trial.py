#!/usr/bin/python3

class Listing:
    """
    Represents a listing on Airbnb.

    Attributes:
        id (int): The unique identifier for the listing.
        title (str): The title of the listing.
        description (str): The description of the listing.
        price (float): The price per night for the listing.
        location (str): The location of the listing.
    """

    def __init__(self, id, title, description, price, location):
        """
        Initialize a new listing.

        Args:
            id (int): The unique identifier for the listing.
            title (str): The title of the listing.
            description (str): The description of the listing.
            price (float): The price per night for the listing.
            location (str): The location of the listing.
        """
        self.id = id
        self.title = title
        self.description = description
        self.price = price
        self.location = location

    def __str__(self):
        """
        Return a string representation of the listing.

        Returns:
            str: A string representation of the listing.
        """
        return f"{self.title} - {self.location}"

    def update_price(self, new_price):
        """
        Update the price of the listing.

        Args:
            new_price (float): The new price per night for the listing.
        """
        self.price = new_price
