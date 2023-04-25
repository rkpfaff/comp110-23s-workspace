"""Return a list of words that are shorter than 5 characters."""

__author__ = "730308175"


def short_words(words: list[str]) -> list[str]:
    """Return a list of words that are shorter than five characters."""
    new_list: list[str] = []
    for i in words:
        if len(i) < 5:
            new_list.append(i)
        else:
            print(f'"{i}" is too long.')
    return new_list