"""Creating unit tests for invert, favorite_color, and count functions."""

__author__ = "730308175"


import pytest
from dictionary import invert, favorite_color, count


def test_invert_edge_case() -> None:
    """Test with empty dictionary."""
    assert invert({}) == {}


def test_invert_use_case1() -> None:
    """Test with dictionary of one key-value pair."""
    assert invert({'a': 'z'}) == {'z': 'a'}


def test_invert_use_case2() -> None:
    """Test with dictionary of multiple key-value pairs."""
    assert invert({'a': 'z', 'b': 'y', 'c': 'x'}) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_use_case3() -> None:
    """Test with duplicate values in the input dictionary."""
    with pytest.raises(KeyError):
        my_dictionary = {'a': 'z', 'b': 'z'}
        invert(my_dictionary)


def test_favorite_color_edge_case() -> None:
    """Test with empty dictionary."""
    with pytest.raises(ValueError):
        favorite_color({})


def test_favorite_color_use_case1() -> None:
    """Test with dictionary of one key-value pair."""
    assert favorite_color({'a': 'red'}) == 'red'


def test_favorite_color_use_case2() -> None:
    """Test with dictionary of multiple key-value pairs."""
    assert favorite_color({'a': 'red', 'b': 'blue', 'c': 'red'}) == 'red'


def test_favorite_color_use_case3() -> None:
    """Test with tie for most popular color."""
    assert favorite_color({'a': 'red', 'b': 'blue', 'c': 'blue'}) == 'blue'


def test_count_edge_case() -> None:
    """Test with empty list."""
    assert count([]) == {}


def test_count_use_case1() -> None:
    """Test with list of one item."""
    assert count(['apple']) == {'apple': 1}


def test_count_use_case2() -> None:
    """Test with list of multiple items."""
    assert count(['apple', 'banana', 'apple', 'orange', 'banana', 'pear']) == {'apple': 2, 'banana': 2, 'orange': 1, 'pear': 1}


def test_count_use_case3() -> None:
    """Test with list containing repeated items."""
    assert count(['apple', 'apple', 'apple']) == {'apple': 3}
