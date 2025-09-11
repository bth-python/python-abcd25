import random
import os


def clear():
    # Works on Mac/Linux/Windows
    os.system("cls" if os.name == "nt" else "clear")


def game():
    clear()
    print("🎲 Welcome to GUESS THE NUMBER 🎲")
    print("I'm thinking of a number between 1 and 100...")

    number = random.randint(1, 100)
    tries = 0

    while True:
        guess = input("Enter your guess: ")

        if not guess.isdigit():
            print("🚫 Please enter a number!")
            continue

        guess = int(guess)
        tries += 1

        if guess < number:
            print("📉 Too low!")
        elif guess > number:
            print("📈 Too high!")
        else:
            print(f"🎉 Correct! The number was {number}. You guessed it in {tries} tries!")
            break

    again = input("Play again? (y/n): ").lower()
    if again == "y":
        game()
    else:
        print("👋 Thanks for playing!")


if __name__ == "__main__":
    game()
