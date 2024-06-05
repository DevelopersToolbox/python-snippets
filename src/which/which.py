#!/usr/bin/env python

"""
A Python implementation of the UNIX which command.

This script provides functions to expand the system's PATH environment variable and to locate
the executable file for a given command within the system's PATH. It also includes a test
function to demonstrate the functionality.

Functions:
    generate_expanded_path() -> str:
        Generates an expanded version of the system's PATH environment variable.

    which(command: str) -> str:
        Locates the executable file for a given command within the system's PATH.

    run_tests() -> None:
        Runs a series of tests on the which function and prints the results.
"""

import shutil
import os
from typing import List, Optional


def generate_expanded_path() -> str:
    """
    Generate an expanded version of the system's PATH environment variable.

    This function performs the following steps:
        1. Retrieves the current PATH environment variable.
        2. Splits the PATH into individual paths based on the system's path separator.
        3. Expands any paths that start with a tilde (~) to their full user directory paths.
        4. Joins the expanded paths back into a single string using the system's path separator.

    Returns:
        str: The expanded PATH environment variable as a single string.
    """
    # Retrieve the current $PATH
    current_path: str = os.environ.get('PATH', '')

    # Split the $PATH into individual paths
    path_elements: List[str] = current_path.split(os.pathsep)

    # Expand paths that start with ~
    expanded_path_elements: List[str] = [os.path.expanduser(path) for path in path_elements]

    # Join the expanded paths back into a single string
    expanded_path: str = os.pathsep.join(expanded_path_elements)

    return expanded_path


def which(command: str) -> str:
    """
    Locate the executable file for a given command within the system's PATH.

    This function searches for the given command in the expanded system's PATH and returns the
    full path to the executable file if found. If the command is not found, it returns "not installed".

    Arguments:
        command (str): The command to locate.

    Returns:
        str: The full path to the executable file if found, otherwise "not installed".

    Examples:
        >>> which("python")
        '/usr/bin/python'
        >>> which("nonexistentcommand")
        'not installed'
    """
    expanded_search_path: str = generate_expanded_path()
    full_path: Optional[str] = shutil.which(command, path=expanded_search_path)

    if full_path is None:
        return "not installed"
    return full_path


def run_tests() -> None:
    """
    Run a series of tests on the which function.

    This function tests the which function with a list of commands, including some common UNIX commands
    and a non-existent command ('flibble'). It prints the results for each command.

    Examples:
        >>> run_tests()
        touch = /usr/bin/touch
        grep = /usr/bin/grep
        wget = /usr/bin/wget
        flibble = not installed
    """
    required_commands: List[str] = ['touch', 'grep', 'wget', 'flibble']

    for command in required_commands:
        path: str = which(command)
        print(f"{command} = {path}")


if __name__ == '__main__':
    run_tests()
