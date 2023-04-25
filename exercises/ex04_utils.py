"""Implementing algorithms to practice computational thinking."""

__author__ = "730308175"


def all(numbers: list[int], n: int) -> bool:
    """Returns True if all numbers in the list `numbers` are equal to `n`. If the list is empty, returns False."""
    if not numbers:
        return False
    i = 0
    while i < len(numbers):
        if numbers[i] != n:
            return False
        i += 1
    return True


def max(input: list[int]) -> int:
    """Return the maximum value in the input list of integers. Raises a ValueWrror if the input list is empty."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    max_value = input[0]
    i = 1
    while i < len(input):
        if input[i] > max_value:
            max_value = input[i]
        i += 1
    return max_value


def is_equal(x: list[int], y: list[int]) -> int:
    """Take two separate lists and determine if they are equal to each other in the integers present."""
    if x == y:
        return True
    else:
        return False