"""Creating a dictionary within a directory."""

__author__ = "730308175"


import pytest


def invert(x: dict[str, str]) -> dict[str, str]:
    """Given a dictionary of [str, str], invert should return a dict[str, str] that inverts the keys and the values."""
    inverted_dict: dict[str, str] = {}
    for key, value in x.items():
        if value in inverted_dict:
            raise KeyError("Duplicate value found when inverting the dictionary!")
        inverted_dict[value] = key
    return inverted_dict


def test_invert_with_duplicate_values() -> None:
    """This is a test for the invert function to check if the KeyError is being raised."""
    my_dictionary: dict[str, str] = {'kris': 'jordan', 'michael': 'jordan'}
    with pytest.raises(KeyError):
        invert(my_dictionary)


def favorite_color(names_colors: dict[str, str]) -> str:
    """Given a dictionary of [str,str], favorite_color should return a str which is the color that appears most frequently."""
    colors_count: dict[str, int] = {}
    for color in names_colors.values():
        if color in colors_count:
            colors_count[color] += 1
        else:
            colors_count[color] = 1
    
    sorted_colors: list[tuple[str, int]] = []
    for color, count in colors_count.items():
        sorted_colors.append((color, count))
    
    for i in range(len(sorted_colors)):
        for j in range(i + 1, len(sorted_colors)):
            if sorted_colors[j][1] > sorted_colors[i][1] or (sorted_colors[j][1] == sorted_colors[i][1] and list(names_colors.values()).index(sorted_colors[j][0]) < list(names_colors.values()).index(sorted_colors[i][0])):
                sorted_colors[i], sorted_colors[j] = sorted_colors[j], sorted_colors[i]
    
    return sorted_colors[0][0]


def count(xs: list[str]) -> dict[str, int]:
    """Given a list[str], this function will produce a dict[str, int] where each key is a unique value in the given list and each value associated is the count of the number of times that value appeared in the input list."""
    result: dict[str, int] = {}
    for item in xs:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result