#Tymoteusz Maj
#Github: Xeraoo

import random

words = ["apple", "banana", "orange", "grape", "kiwi"]

def guess_word_game():
    while True:
        # Randomly choose a word from the list
        secret_word = random.choice(words)
        guessed_letters = []
        attempts = len(secret_word) * 2
        while attempts > 0:
            display_word = ""
            for letter in secret_word:
                if letter in guessed_letters:
                    display_word += letter
                else:
                    display_word += "_"
            print("Current word:", display_word)

            guess = input("Guess a letter: ").lower()

            # Input validation loop
            while not guess.isalpha() or len(guess) != 1 or guess in guessed_letters:
                print("Please enter a single letter that you haven't guessed before.")
                guess = input("Guess a letter: ").lower()

            if guess in secret_word:
                print("Correct guess!")
                guessed_letters.append(guess)
            else:
                print("Incorrect guess!")
                attempts -= 1

            if all(letter in guessed_letters for letter in secret_word):
                print("Congratulations! You guessed the word:", secret_word)
                break

            if attempts == 0:
                print("Sorry, you ran out of attempts. The word was:", secret_word)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        while play_again not in ["yes", "no"]:
            print("Please enter 'yes' or 'no'.")
            play_again = input("Do you want to play again? (yes/no): ").lower()

        if play_again == "no":
            print("Thanks for playing!")
            break

# Call the game function
guess_word_game()
