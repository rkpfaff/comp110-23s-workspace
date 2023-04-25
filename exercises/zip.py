"""Function Dictionaries Writing Practice."""

__author__ = "730308175"

def zip(x: list[str], y:list[str]) -> dict[str,int]:
    if len(x) != len(y) or len(x) == 0 or len(y) == 0:
        return {}
    result = {}
    for i in range(len(x)):
        result[x[i]] = y[i]
    return result 