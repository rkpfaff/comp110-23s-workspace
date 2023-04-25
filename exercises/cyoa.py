"""Design an open-ended program with specific requirements but can use my own imagination to design and implement!"""

__author__ = "730308175"


import random

MOUSY_EMOJI: str = "\U0001F401"
CASTLE_EMOJI: str = "\U0001f3f0"
points: int = 0
player: str = ""


def greet() -> None:
    """Greet the player and ask for their name."""
    global player
    print("Welcome to the adventure game!")
    player = input("What is your name? ")
    print(f"Good luck on your adventure, {player}!")
    

def main() -> None:
    """Main function of the adventure game."""
    global points
    global player
    greet()
    print("You set off on your adventure...")
    while True:
        print("What will you do next?")
        choice: str = input("1. Explore\n2. Take the challenge\n3. End adventure\n")
        if choice == "1":
            explore()
        elif choice == "2":
            points = challenge(points)
        elif choice == "3":
            print(f"Thanks for playing, {player}! You earned a total of {points} adventure points!")
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")
    

def explore() -> None:
    """Exploring the path either to the right or the left will yield different choices!"""
    global points
    
    print(f"{player}, you find yourself in a mysterious forest. You see a path to the left and a path to the right.")
    choice: str = input("Which path will you take? (left/right) ")
    if choice == "left":
        print("You come across a group of friendly fairies who grant you 5 adventure points!")
        points += 5
        print(f"After walking for what seemed like hours, {player} stumbled upon a fork in the road where you came across a prophetic {MOUSY_EMOJI}.")
        print(f"One path led towards the {CASTLE_EMOJI}, while the other path led towards the unknown.")
        print(f"The {MOUSY_EMOJI} advised {player} decided to take the path towards the {CASTLE_EMOJI}.")

    elif choice == "right":
        print("You encounter a ferocious dragon who attacks you, but you manage to defeat it and earn 10 adventure points!")
        points += 10
        print(f"After walking for what seemed like hours, {player} stumbled upon a {MOUSY_EMOJI} at the cave entrance.")
        print(f"{player} decided to explore the cave.")
    else:
        print("Invalid choice. You wander around and find nothing of interest.")
    print(f"Your adventure points: {points}")


def challenge(points: int) -> int:
    """See if the player can pass the challenging riddle in front of him/her/them!"""
    print(f"{player}, you come across a mysterious old man who challenges you to a riddle. Answer correctly to earn more adventure points!")
    answer = input("What is always in front of you but can't be seen? ")
    if answer.lower() == "the future":
        print("Correct! The old man grants you 10 adventure points!")
        points += 10
    else:
        deduction = random.randint(1, 5)
        print(f"Incorrect. You lose {deduction} adventure points.")
        points -= deduction
    return points
    

if __name__ == "__main__":
    main()