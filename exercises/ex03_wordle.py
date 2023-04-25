"""This program implements a main function that contains Wordle's game loop"""

__author__ = "730308175"

def contains_char(string: str, char: str) -> bool:
    """
    This function takes in two strings and returns True if the second string is found at any index of the first string, and False otherwise.

    :param string: The string being searched through for the second parameter
    :param char: The character being searched for
    :return: True if char is found in string, False otherwise
    """
    assert len(char) == 1 
    if char in string:
        return True
    else:
        return False

def emojified(guess: str, secret: str) -> str:
    """
    Given two strings of equal length, the function returns a string of emoji whose color codifies the same as implemented in EX02.
    Yellow box emoji is used for matching characters in the same position in the guess and secret string. 
    White box emoji is used for matching characters in different positions in the guess and secret string.

    :param guess: A string containing the guess
    :param secret: A string containing the secret to be guessed
    :return: A string of emoji representing the similarity between the guess and the secret
    """
    WHITE_BOX_EMOJI: str = "\U00002B1C"
    GREEN_BOX_EMOJI: str = "\U0001F7E9"
    YELLOW_BOX_EMOJI: str = "\U0001F7E8"
    assert len(guess) == len(secret)
    emoji_str = ""
    i: int =0
    #for i in range(len(guess)):
    while i < len(guess):
        if guess[i] == secret[i]:
            emoji_str += GREEN_BOX_EMOJI
        elif contains_char(secret, guess[i]):
            emoji_str += YELLOW_BOX_EMOJI
        else:
            emoji_str += WHITE_BOX_EMOJI
        i += 1
    return emoji_str

def input_guess(expected_length: int) -> str:
    """
    Prompts the user to input a guess and continues prompting until they provide a guess of the expected length.

    :param expected_length: An integer representing the expected length of the guess.
    :return: A string representing the user's guess of the expected length.
    """
    guess = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        print(f"That wasn't {expected_length} chars!")
        guess = input("Try again: ")
    return guess

def main() -> None:
    """The entrypoint of the program and main game loop."""
    num_turns = 6
    turn = 1
    secret = "codes"
    while turn <= num_turns:
        print(f"=== Turn {turn}/{num_turns} ===")
        guess = input_guess(len(secret))
        result = emojified(guess, secret)
        print(result)
        if guess == secret:
            print(f"You won in {turn}/{num_turns} turns!")
            return
        turn += 1
    print(f"X/6 - Sorry, try again tomorrow!")     

if __name__ == "__main__":
    main()