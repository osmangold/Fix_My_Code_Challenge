#!/usr/bin/env python3
"""Defines a square class."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes a new square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size

    def area(self):
        """Computes the area of the square.

        Returns:
            The area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """Gets the size of the square.

        Returns:
            The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value (int): The new size of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __eq__(self, other):
        """Checks if this square is equal to another square.

        Args:
            other (Square): The other square.

        Returns:
            True if the squares are equal, False otherwise.
        """
        return self.__size == other.__size

    def __lt__(self, other):
        """Checks if this square is less than another square.

        Args:
            other (Square): The other square.

        Returns:
            True if this square is less than the other square, False otherwise.
        """
        return self.__size < other.__size

    def __le__(self, other):
        """Checks if this square is less than or equal to another square.

        Args:
            other (Square): The other square.

        Returns:
            True if this square is less than or equal to the other square, False otherwise.
        """
        return self.__size <= other.__size

    def __gt__(self, other):
        """Checks if this square is greater than another square.

        Args:
            other (Square): The other square.

        Returns:
            True if this square is greater than the other square, False otherwise.
        """
        return self.__size > other.__size

    def __ge__(self, other):
        """Checks if this square is greater than or equal to another square.

        Args:
            other (Square): The other square.

        Returns:
            True if this square is greater than or equal to the other square, False otherwise.
        """
