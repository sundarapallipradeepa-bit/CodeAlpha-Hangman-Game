"""
Project: Hangman Game
Internship: CodeAlpha Python Programming Internship
Description: A simple command-line Hangman game where the computer
             randomly picks a word and the user tries to guess it
             one letter at a time before running out of attempts.
"""

import random  # Used to randomly pick a word from our word list


def choose_word(word_list):
    """
    Randomly selects and returns one word from the given list of words.
    """
    return random.choice(word_list)


def display_word(word, guessed_letters):
    """
    Builds and returns the current state of the word to display.
    - Shows the letter if it has already been guessed correctly.
    - Shows an underscore "_" if the letter has not been guessed yet.
    """
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def get_valid_guess(guessed_letters):
    """
    Asks the user to enter a single letter.
    Keeps asking until a valid, new letter is entered.
    A valid guess must be:
    - A single alphabet character
    - Not already guessed before
    """
    while True:
        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter (a-z).")
        elif guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
        else:
            return guess


def play_hangman():
    """
    Main function that runs the Hangman game.
    Handles the game loop, tracking guesses, wins, and losses.
    """

    # Predefined list of 5 words for the game
    word_list = ["python", "hangman", "internship", "keyboard", "developer"]

    # Randomly select the word to be guessed
    secret_word = choose_word(word_list)

    # Maximum number of wrong guesses allowed
    max_attempts = 6
    wrong_attempts = 0

    # Set to store all letters the player has guessed (correct or wrong)
    guessed_letters = set()

    print("=" * 50)
    print("Welcome to HANGMAN!")
    print(f"The word has {len(secret_word)} letters.")
    print(f"You have {max_attempts} wrong guesses allowed.")
    print("=" * 50)

    # Main game loop - continues until win or max wrong attempts reached
    while wrong_attempts < max_attempts:

        # Show current word progress (letters guessed + underscores)
        print("\nWord: " + display_word(secret_word, guessed_letters))

        # Show letters guessed so far, sorted alphabetically for clarity
        if guessed_letters:
            print("Guessed letters: " + ", ".join(sorted(guessed_letters)))

        print(f"Wrong guesses remaining: {max_attempts - wrong_attempts}")

        # Get a valid letter guess from the user
        guess = get_valid_guess(guessed_letters)
        guessed_letters.add(guess)

        # Check if the guessed letter is in the secret word
        if guess in secret_word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            wrong_attempts += 1
            print(f"Sorry, '{guess}' is not in the word.")

        # Check win condition: every letter in the word has been guessed
        if all(letter in guessed_letters for letter in secret_word):
            print("\n" + "=" * 50)
            print(f"CONGRATULATIONS! You guessed the word: '{secret_word}'")
            print("=" * 50)
            return  # End the game - player wins

    # If loop ends without returning, the player has lost
    print("\n" + "=" * 50)
    print("GAME OVER! You ran out of attempts.")
    print(f"The correct word was: '{secret_word}'")
    print("=" * 50)


# Entry point of the program
if __name__ == "__main__":
    play_hangman()
