"""Using while loops to construct a wordle!"""

__author__ = "730308175"

SECRET: str = "python"
guess: str = str(input('What is your 6-letter guess? '))
playing: bool = True

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while playing:
    if len(guess) == 6:
        playing = False
    else:
        guess = str(input(f'{"That was not 6 letters! Try again: "}'))  
emoji = "" 
letter_checker: int = 0    
while letter_checker < len(SECRET):
    if guess[letter_checker] == SECRET[letter_checker]:
        emoji += GREEN_BOX
    else:
        partial: bool = False
        character_checker: int = 0
        while partial is False and character_checker < len(SECRET):
            if guess[letter_checker] == SECRET[character_checker]:
                partial = True
            else:
                character_checker += 1
        if partial is True:
            emoji += YELLOW_BOX
        else:
            emoji += WHITE_BOX
    letter_checker += 1
print(emoji)
if guess == SECRET:
    print("Woo! You got it! ")
else:
    print("Not quite. Play again soon! ") 