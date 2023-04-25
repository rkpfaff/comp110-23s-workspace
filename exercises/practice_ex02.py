import random

def generate_word():
    """Generates a random 6-letter word."""
    words = ["python", "photos", "oneten", "apple", "orange", "banana"]
    return random.choice(words)

def compare_words(guess, secret_word):
    """Compares the guess and the secret word and returns the number of correct letters."""
    correct_count = 0
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            correct_count += 1
    return correct_count

def play_game():
    secret_word = generate_word()
    print("Welcome to One-Shot Wordle!")
    print("Can you guess the secret 6-letter word?")
    print("Enter your guess below:")
    guess = input("> ")
    while len(guess) != 6:
        print("Your guess must be exactly 6 letters long. Try again:")
        guess = input("> ")
    correct_count = compare_words(guess, secret_word)
    while correct_count != 6:
        result = ""
        for i in range(6):
            if guess[i] == secret_word[i]:
                result += "🟩"
            elif guess[i] in secret_word:
                result += "🟨"
            else:
                result += "⬜"
        print(result)
        print("Not quite. Play again soon!")
        guess = input("> ")
        while len(guess) != 6:
            print("Your guess must be exactly 6 letters long. Try again:")
            guess = input("> ")
        correct_count = compare_words(guess, secret_word)
    print("🟩🟩🟩🟩🟩🟩")
    print("Woo! You got it!")

if __name__ == "__main__":
    play_game()
    
    


rando: str = "hello"
i: int = 0
while i < len(rando):
    print(rando[i])
    i += 1