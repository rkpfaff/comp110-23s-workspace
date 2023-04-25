"""This module contains unit tests for the functions defined in utils.py."""

__author__ = "730308175"

from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens1():
    """Test the only_evens function."""
    # Edge case: empty list
    assert only_evens([]) == []


def test_only_evens2():
    """Test the only_evens function."""
    # Use case 1: list of odd numbers
    assert only_evens([1, 3, 5]) == []


def test_only_evens3():
    """Test the only_evens function."""
    # Use case 2: list of even numbers
    assert only_evens([2, 4, 6]) == [2, 4, 6]


def test_only_evens4():
    """Test the only_evens function."""
    # Use case 3: list of mixed numbers
    assert only_evens([1, 2, 3, 4, 5, 6]) == [2, 4, 6]


def test_sub1():
    """Test the sub function."""
    # Edge case 1: empty list
    assert sub([], 0, 0) == []


def test_sub2():
    """Test the sub function."""
    # Edge case 2: start index is negative
    assert sub([1, 2, 3], -2, 2) == [1, 2]


def test_sub3():
    """Test the sub function."""
    # Edge case 3: end index is greater than the length of the list
    assert sub([1, 2, 3], 0, 5) == [1, 2, 3]


def test_sub4():
    """Test the sub function."""
    # Use case 1: start and end indices within the bounds of the list
    assert sub([10, 20, 30, 40], 1, 3) == [20, 30]


def test_sub5():
    """Test the sub function."""
    # Use case 2: start index is greater than or equal to the length of the list
    assert sub([1, 2, 3], 3, 4) == []


def test_sub6():
    """Test the sub function."""
    # Use case 3: end index is at most 0
    assert sub([1, 2, 3], 0, 0) == []


def test_concat1():
    """Test the concat function."""
    # Edge case 1: empty lists
    assert concat([], []) == []


def test_concat2():
    """Test the concat function."""
    # Edge case 2: one list is empty
    assert concat([1, 2, 3], []) == [1, 2, 3]


def test_concat3():
    """Test the concat function."""
    # Edge case 3: another list is empty
    assert concat([], [4, 5, 6]) == [4, 5, 6]


def test_concat4():
    """Test the concat function."""
    # Use case 1: non-empty lists
    assert concat([1, 2], [3, 4]) == [1, 2, 3, 4]


def test_concat5():
    """Test the concat function."""
    # Use case 2: lists with duplicate elements
    assert concat([1, 2, 2], [2, 3, 3]) == [1, 2, 2, 2, 3, 3]


def test_concat6():
    """Test the concat function."""
    # Use case 3: lists with negative elements
    assert concat([-1, -2], [-3, -4]) == [-1, -2, -3, -4]
