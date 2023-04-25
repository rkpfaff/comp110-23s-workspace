"""Return a list of integers containing elements of the input list that areoff and have an even index."""


__author__ = "730308175"


def odd_and_even(nums: list[int]) -> list[int]:
    """Return a list of integers containing elements of the input list that areoff and have an even index."""
    new_list: list[str] = []
    for i in range(0, len(nums), 2):
        if nums[i] % 2 != 0:
            new_list.append(nums[i])
    return new_list