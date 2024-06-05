#!/usr/bin/env python

"""
This script contains functions to convert a given number of seconds into a human-friendly format.

It also includes a test function to demonstrate the conversion for various inputs.

Functions:
    human_duration(secs: int) -> str:
        Converts a number of seconds into a human-friendly string format representing
        days, hours, minutes, and seconds.

    run_tests() -> None:
        Runs a series of tests on the human_duration function and prints the results.
"""

from typing import List


def human_duration(secs: int) -> str:
    """
    Convert the number of seconds into a human-friendly string format.

    This function takes an integer representing a duration in seconds and converts it
    into a string that expresses the duration in terms of days, hours, minutes, and seconds.
    For example, 12345 seconds would be converted to '3 hours, 25 minutes & 45 seconds'.

    Parameters:
        secs (int): The number of seconds to convert. Should be a non-negative integer.

    Returns:
        str: A string representing the duration in a human-friendly format. If the input is
             less than 0, returns 'unknown'. If the input is 0, returns 'None'.

    Examples:
        >>> human_duration(12345)
        '3 hours, 25 minutes & 45 seconds'
        >>> human_duration(0)
        'None'
        >>> human_duration(-5)
        'unknown'
    """
    days: int = 0
    hours: int = 0
    minutes: int = 0

    if secs < 0:
        return 'unknown'

    if secs == 0:
        return 'None'

    parts: List = []

    days, secs = divmod(secs, 86400)
    if days:
        parts.append(f'{days} day{"s" if days != 1 else ""}')

    hours, secs = divmod(secs, 3600)
    if hours:
        parts.append(f'{hours} hour{"s" if hours != 1 else ""}')

    minutes, secs = divmod(secs, 60)
    if minutes:
        parts.append(f'{minutes} minute{"s" if minutes != 1 else ""}')

    if secs or not parts:
        parts.append(f'{secs} second{"s" if secs != 1 else ""}')

    # Combine parts with commas and an "and" before the last part if necessary
    if len(parts) > 1:
        result: str = ', '.join(parts[:-1]) + ' & ' + parts[-1]
    else:
        result = parts[0]

    return result


def run_tests() -> None:
    """
    Run a series of tests on the human_duration function.

    This function tests the human_duration function with a variety of inputs, including
    edge cases like negative numbers and zero. It prints the results of each test to the
    console.

    The tests include:
        - A negative number of seconds (-1)
        - Zero seconds (0)
        - Small numbers of seconds (1, 12, 123)
        - Larger numbers of seconds (1234, 12345, 123456)
        - Very large numbers of seconds (1234567, 12345678, 123456789, 1234567890)

    Returns:
        None

    Examples:
        >>> run_tests()
        Test 1: -1 converts to: unknown
        Test 2: 0 converts to: None
        Test 3: 1 converts to: 1 second
        Test 4: 12 converts to: 12 seconds
        Test 5: 123 converts to: 2 minutes & 3 seconds
        Test 6: 1234 converts to: 20 minutes & 34 seconds
        Test 7: 12345 converts to: 3 hours, 25 minutes & 45 seconds
        Test 8: 123456 converts to: 1 day, 10 hours, 17 minutes & 36 seconds
        Test 9: 1234567 converts to: 14 days, 6 hours, 56 minutes & 7 seconds
        Test 10: 12345678 converts to: 142 days, 21 hours, 21 minutes & 18 seconds
        Test 11: 123456789 converts to: 1428 days, 21 hours, 33 minutes & 9 seconds
        Test 12: 1234567890 converts to: 14288 days, 23 hours, 31 minutes & 30 seconds
    """
    tests: List[int] = [-1, 0, 1, 12, 123, 1234, 12345, 123456, 1234567, 12345678, 123456789, 1234567890]

    for count, test in enumerate(tests, start=1):
        try:
            print(f'Test {count}: {test} converts to: {human_duration(test)}')
        except ValueError as e:
            print(f'ValueError for test {count} with input {test}: {e}')


if __name__ == '__main__':
    run_tests()
