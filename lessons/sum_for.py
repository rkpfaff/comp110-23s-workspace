"""Replacing while loop with for...in loop"""

def sum(xs: list[float]) -> float:
    """return sum of all elements in xs"""
    sum_total: float = 0.0
    for element in xs:
        sum_total += element
    return sum_total
