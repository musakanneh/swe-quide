#!/usr/bin/python3
"""Blind Auction Game"""

from art import logo
from os import system

print(logo)


def clear_console():
    """Clears the console for new inputs"""
    _ = system('clear')


def find_highest_bidder(bidding_record):
    """Calculates and displays final result"""
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print("The winner is {} with a bid of {}".format(winner, highest_bid))


bids = {}
bidding_finished = True

while bidding_finished:
    user_name = input("What is your name? ")
    bid_price = int(input("What is your bid price? $"))
    bids[user_name] = bid_price

    should_continue = input(
        "Are there any other bidder? yes or no: ").lower()
    if should_continue == "no":
        bidding_finished = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear_console()
    else:
        raise ValueError("Unknown input. Sorry")


if __name__ == '__main__':
    find_highest_bidder(bids)
