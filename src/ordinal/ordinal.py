#!/usr/bin/env python

"""
This script provides a function to calculate the correct ordinal suffix for a given number.

It also includes a test function to demonstrate the ordinal conversion for a range of numbers.

Functions:
    ordinal(num: int) -> str:
        Returns the given number with its appropriate ordinal suffix.

    run_tests() -> None:
        Runs a series of tests on the ordinal function and prints the results.
"""

from typing import Dict


def ordinal(num: int) -> str:
    """
    Calculate the correct ordinal for a given number.

    This function takes an integer and returns a string with the number followed by its
    correct ordinal suffix (e.g., '1st', '2nd', '3rd', etc.). Special handling is provided
    for numbers ending in 11, 12, and 13, which use 'th' instead of 'st', 'nd', or 'rd'.

    Arguments:
        num (int): The number to be converted to its ordinal form.

    Returns:
        str: The number with its appropriate ordinal suffix.

    Examples:
        >>> ordinal(1)
        '1st'
        >>> ordinal(2)
        '2nd'
        >>> ordinal(3)
        '3rd'
        >>> ordinal(11)
        '11th'
        >>> ordinal(21)
        '21st'
    """
    SUFFIXES: Dict[int, str] = {1: 'st', 2: 'nd', 3: 'rd'}

    if 10 <= num % 100 <= 20:
        suffix: str = 'th'
    else:
        suffix = SUFFIXES.get(num % 10, 'th')

    return f"{num}{suffix}"


def run_tests() -> None:
    """
    Run a series of tests on the ordinal function.

    This function tests the ordinal function with numbers from 1 to 24. It prints each
    number followed by its ordinal suffix to the console.

    Returns:
        None

    Examples:
        >>> run_tests()
        1st
        2nd
        3rd
        4th
        ...
        24th
    """
    for i in range(1, 25):
        print(ordinal(i))


if __name__ == "__main__":
    run_tests()
