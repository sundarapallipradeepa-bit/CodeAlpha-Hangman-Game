hangman.py
"""
Project: Hangman Game
Internship: CodeAlpha Python Programming Internship
Description: A simple command-line Hangman game where the computer
             randomly picks a word and the user tries to guess it
             one letter at a time before running out of attempts.
"""

import random


def choose_word(word_list):
    return random.choice(word_list)


def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def get_valid_guess(guessed_letters):
    while True:
        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter (a-z).")
        elif guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
        else:
            return guess


def play_hangman():
    word_list = ["python", "hangman", "internship", "keyboard", "developer"]

    secret_word = choose_word(word_list)

    max_attempts = 6
    wrong_attempts = 0
    guessed_letters = set()

    print("=" * 50)
    print("Welcome to HANGMAN!")
    print(f"The word has {len(secret_word)} letters.")
    print(f"You have {max_attempts} wrong guesses allowed.")
    print("=" * 50)

    while wrong_attempts < max_attempts:

        print("\nWord: " + display_word(secret_word, guessed_letters))

        if guessed_letters:
            print("Guessed letters: " + ", ".join(sorted(guessed_letters)))

        print(f"Wrong guesses remaining: {max_attempts - wrong_attempts}")

        guess = get_valid_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in secret_word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            wrong_attempts += 1
            print(f"Sorry, '{guess}' is not in the word.")

        if all(letter in guessed_letters for letter in secret_word):
            print("\n" + "=" * 50)
            print(f"CONGRATULATIONS! You guessed the word: '{secret_word}'")
            print("=" * 50)
            return

    print("\n" + "=" * 50)
    print("GAME OVER! You ran out of attempts.")
    print(f"The correct word was: '{secret_word}'")
    print("=" * 50)


if __name__ == "__main__":
    play_hangman()
