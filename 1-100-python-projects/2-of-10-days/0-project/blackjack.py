#!/usr/bin/python3
"""Blackjack Game"""

from art import logo
import random


def del_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Returns score from the list of cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    """Compares player scores and declare a winner"""
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Loose, opponent has a blackjack"
    elif user_score == 0:
        return "Win with a blackjack"
    elif user_score > 21:
        return "You went over. You lose :("
    elif computer_score > 21:
        return "opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"


def play_game():
    """Hadles the blackjack game"""
    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(del_card())
        computer_cards.append(del_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print("Your card: {}, current score {}".format(user_cards, user_score))
        print("Computer's first card: {}".format(computer_cards[0]))

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input(
                "Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_should_deal == 'y':
                user_cards.append(del_card())
            else:
                is_game_over = True
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(del_card())
        computer_score = calculate_score(computer_cards)

    print("\nYour final hand: {}, final score: {}".format(user_cards, user_score))
    print("Computer's final hand: {}, final score: {}\n".format(
        computer_cards, computer_score))
    print(compare(user_score, computer_score))


if __name__ == '__main__':
    while input("Do you want to the play the blackjack game? 'y' for yes, 'n' for no") == "y":
        play_game()
