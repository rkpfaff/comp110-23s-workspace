"""Replacing while loop with for...in loop with range"""

def sum(xs: list[float]) -> float:
    """return sum of all elements in xs"""
    sum_total: float = 0.0
    for idx in range(len(xs)):
        sum_total += xs[idx]
    return sum_total