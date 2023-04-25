"""Create a function that returns True if the int exists as a value in the dictionary, and False otherwise."""


__author__ = "730308175"


def value_exists(xs:dict[str,int], x: int) -> bool:
    """Create a function that returns True if the int exists as a value in the dictionary, and False otherwise."""
    for key in xs:
        if x == xs[key]:
            return True
    return False