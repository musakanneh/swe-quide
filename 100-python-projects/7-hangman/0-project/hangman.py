#!/usr/bin/python3
"""The Hangman Game"""

import random
from hangman_words import word_list
from hangman_art import stages, logo


def hangman():
    """Hangman game"""
    print(logo)

    chosen_word = random.choice(word_list)
    print("The solution is: {}".format(chosen_word))
    display = []
    lives = 6

    for _ in chosen_word:
        display += "_"

    end_of_game = False

    while not end_of_game:
        guess = input("Guess a letter: ").lower()

        for position in range((len(chosen_word))):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
        print(display)

        if guess not in chosen_word:
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose!")

        if "_" not in display:
            end_of_game = True
            print("You win!")

        print(stages[lives])


if __name__ == '__main__':
    hangman()
