"""
Task 2: Number Guessing Game
Author: Himani Thakur
Description:
    A classic number guessing game. The computer picks a secret random
    number between 1 and 100, and the player guesses until they find it,
    receiving hints ('Too High' or 'Too Low') along with their attempt count.
"""

import random


def check_guess(guess: int, target: int) -> str:
    """
    Compare the player's guess to the target number.
    Returns:
        'Too Low' if guess < target
        'Too High' if guess > target
        'Correct' if guess == target
    """
    if guess < target:
        return "Too Low"
    elif guess > target:
        return "Too High"
    else:
        return "Correct"


def play_game(target: int = None):
    """Run one full session of the guessing game."""
    if target is None:
        target = random.randint(1, 100)

    print("=" * 45)
    print("        WELCOME TO NUMBER GUESSING GAME      ")
    print("=" * 45)
    print("I have chosen a secret number between 1 and 100.")
    print("Can you guess what it is?\n")

    attempts = 0

    while True:
        user_input = input("Enter your guess (1-100) or 'q' to quit: ").strip()

        if user_input.lower() in ("q", "quit", "exit"):
            print(f"You gave up! The secret number was {target}.")
            break

        # Validate that the input is an integer
        try:
            guess = int(user_input)
        except ValueError:
            print("[Invalid Input] Please enter a valid whole number between 1 and 100.")
            continue

        # Validate range
        if guess < 1 or guess > 100:
            print("[Out of Range] Please guess a number strictly between 1 and 100.")
            continue

        attempts += 1
        result = check_guess(guess, target)

        if result == "Correct":
            print(f"\n[CORRECT] Congratulations! You guessed the number {target} correctly!")
            print(f"Total attempts taken: {attempts}")
            break
        elif result == "Too Low":
            print("[TOO LOW] Try a higher number.\n")
        else:
            print("[TOO HIGH] Try a lower number.\n")


def main():
    while True:
        play_game()
        replay = input("\nDo you want to play another round? (y/n): ").strip().lower()
        if replay not in ("y", "yes"):
            print("Thanks for playing! See you next time.")
            break


if __name__ == "__main__":
    main()
