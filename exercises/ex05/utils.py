"""Return a new list only containing the even elements of the input list!"""

__author__ = "730308175"


def only_evens(xs: list[int]): 
    """Take a list of numbers and sort for only even numbers."""
    even_list = []
    for element in xs:
        if element % 2 == 0:
            even_list.append(element)
    return even_list 


def concat(list1: list[int], list2: list[int]):
    """Take two lists and add them together through concantenation."""
    concatenated_list = []
    for idx in list1:
        concatenated_list.append(idx)
    for idx in list2:
        concatenated_list.append(idx)
    return concatenated_list


def sub(a_list: list[int], start: int, end: int):
    """Take a list of integers and two integers for an index and return the specified start index and end index - 1."""
    b_list = []
    for i in range(start, end):
        if i >= 0 and i < len(a_list):
            b_list.append(a_list[i])
    return b_list