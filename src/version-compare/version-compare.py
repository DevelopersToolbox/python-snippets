#!/usr/bin/env python

"""
A Python script to compare version numbers.

This script provides a function to compare two version strings and a test function to verify the comparison logic.

Functions:
    version_compare(version1: str, version2: str) -> int:
        Compares two version strings and returns an integer indicating their order.

    run_tests() -> None:
        Runs a series of tests on the version_compare function and prints the results.
"""

import re

from typing import Any, List


def version_compare(version1: str, version2: str) -> int:
    """
    Compare two version strings.

    This function compares two version strings by normalizing them and comparing each numeric component.
    It returns:
        - a negative integer if version1 < version2
        - zero if version1 == version2
        - a positive integer if version1 > version2

    Parameters:
        version1 (str): The first version string to compare.
        version2 (str): The second version string to compare.

    Returns:
        int: The comparison result.

    Examples:
        >>> version_compare("1", "1")
        0
        >>> version_compare("2.1", "2.2")
        -1
        >>> version_compare("3.0.4.10", "3.0.4.2")
        1
    """
    def normalize(v: str) -> List[int]:
        return [int(x) for x in re.sub(r'(\.0+)*$', '', v).split(".")]

    # Custom comparison function
    def cmp(a, b) -> Any:
        return (a > b) - (a < b)

    return cmp(normalize(version1), normalize(version2))


def run_tests() -> None:
    """
    Run a series of tests on the version_compare function.

    This function tests the version_compare function with various pairs of version strings.
    It includes tests that are expected to pass and one test that is expected to fail, demonstrating
    the correctness and robustness of the comparison logic.

    Returns:
        None

    Examples:
        >>> run_tests()
        It failed as expected
    """
    assert version_compare("1", "1") == 0                   # nosec: B101
    assert version_compare("2.1", "2.2") < 0                # nosec: B101
    assert version_compare("3.0.4.10", "3.0.4.2") > 0       # nosec: B101
    assert version_compare("4.08", "4.08.01") < 0           # nosec: B101
    assert version_compare("3.2.1.9.8144", "3.2") > 0       # nosec: B101
    assert version_compare("3.2", "3.2.1.9.8144") < 0       # nosec: B101
    assert version_compare("1.2", "2.1") < 0                # nosec: B101
    assert version_compare("2.1", "1.2") > 0                # nosec: B101
    assert version_compare("5.6.7", "5.6.7") == 0           # nosec: B101
    assert version_compare("1.01.1", "1.1.1") == 0          # nosec: B101
    assert version_compare("1.1.1", "1.01.1") == 0          # nosec: B101
    assert version_compare("1", "1.0") == 0                 # nosec: B101
    assert version_compare("1.0", "1") == 0                 # nosec: B101
    assert version_compare("1.0", "1.0.1") < 0              # nosec: B101
    assert version_compare("1.0.1", "1.0") > 0              # nosec: B101
    assert version_compare("1.0.2.0", "1.0.2") == 0         # nosec: B101

    # The following should fail
    try:
        assert version_compare("1.0.1", "1.0") < 0          # nosec: B101
    except AssertionError:
        print("It failed as expected")


if __name__ == '__main__':
    run_tests()
