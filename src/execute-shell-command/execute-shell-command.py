#!/usr/bin/env python

"""
A Python script for executing shell commands and returning the outputs and exit status.

This script defines a function to execute shell commands and a simple test function to
demonstrate its usage.

Classes:
    ExecutionResult: A named tuple to store the status, stdout, and stderr of a shell command execution.

Functions:
    execute_shell_command(cmd: List[str]) -> ExecutionResult: Executes a shell command and returns the results.
    run_tests() -> None: Runs a test to check the 'ls -l' command.
"""

import os

from subprocess import Popen, PIPE  # nosec: B404
from typing import Any, NamedTuple, List


class ExecutionResult(NamedTuple):
    """
    A named tuple to store the result of executing a shell command.

    Attributes:
        status (int): The exit status of the executed command.
        stdout (str): The standard output produced by the command.
        stderr (str): The standard error output produced by the command.
    """

    status: int
    stdout: str
    stderr: str


def execute_shell_command(cmd: List[str]) -> ExecutionResult:
    """
    Execute a shell command and returns the status, stdout, and stderr.

    Arguments:
        cmd (List[str]): The shell command to execute as a list of arguments.

    Returns:
        ExecutionResult: A named tuple containing the status, stdout, and stderr.

    Example:
        >>> result = execute_shell_command(['ls', '-l'])
        >>> print(result.status)
        >>> print(result.stdout)
        >>> print(result.stderr)
    """
    with Popen(cmd, stdout=PIPE, stderr=PIPE, cwd=os.getcwd()) as process:  # nosec: B603
        stdout_raw, stderr_raw = process.communicate()
        status: int | Any = process.returncode

    stdout: str = stdout_raw.decode('utf-8').rstrip()
    stderr: str = stderr_raw.decode('utf-8').rstrip()

    return ExecutionResult(status, stdout, stderr)


def run_tests() -> None:
    """
    Run a test to check if the 'ls -l' command works as required.

    This function demonstrates the usage of the execute_shell_command function.
    It executes the 'ls -l' command and prints the status, stdout, and stderr.

    Example:
        >>> run_tests()
        Status: 0
        Stdout: total 0
        -rw-r--r--  1 user  staff  0 Jan 1 00:00 file1
        -rw-r--r--  1 user  staff  0 Jan 1 00:00 file2
        Stderr:
    """
    results: ExecutionResult = execute_shell_command(['ls', '-l'])

    print(f'Status: {results.status}')
    print(f'Stdout: {results.stdout}')
    print(f'Stderr: {results.stderr}')


if __name__ == '__main__':
    run_tests()
