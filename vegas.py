"""
assignment: Lab 7
file: vegas.py
author: Ryan Nowak

simulates a card game a given number of times and prints the stats
for all games
"""

import random as rand
from cs_queue import make_empty_queue, enqueue, dequeue
from cs_stack import *


def init_deck(deck_size):
    """
    creates a queue of integers from 1 to the size of the deck
    :param deck_size: integer, number of elements in queue
    :return: queue of integers
    """
    deck = make_empty_queue()
    for i in range(1, deck_size+1):
        enqueue(deck, i)
    return deck


def random_draw(deck):
    """
    cycles through the given queue and picks a random element
    :param deck: queue of integers
    :return: randomly chosen element from queue
    """
    for i in range(rand.randint(0, deck.size)):
        card = dequeue(deck)
        enqueue(deck, card)

    card = dequeue(deck)
    return card


def play_game(deck):
    """
    simulates the card game with the given deck
    :param deck: queue of integers
    :return: number of elements in victory stack
    """
    discard1 = make_empty_stack()
    discard2 = make_empty_stack()
    victory = make_empty_stack()
    for i in range(deck.size):
        card = random_draw(deck)
        if is_empty(victory) and card == 1:
            push(victory, card)
        elif not is_empty(victory) and top(victory) == card-1:
            push(victory, card)
        elif is_empty(discard1):
            push(discard1, card)
        elif is_empty(discard2):
            push(discard2, card)
        elif top(discard1) > top(discard2):
            push(discard1, card)
        elif top(discard1) < top(discard2):
            push(discard2, card)

        while True:
            if is_empty(discard1) and is_empty(discard2):
                break
            elif is_empty(victory):
                if not is_empty(discard1) and top(discard1) == 1:
                    push(victory, pop(discard1))
                elif not is_empty(discard2) and top(discard2) == 1:
                    push(victory, pop(discard2))
                else:
                    break
            elif not is_empty(discard1) and top(discard1) == top(victory)+1:
                push(victory, pop(discard1))
            elif not is_empty(discard2) and top(discard2) == top(victory)+1:
                push(victory, pop(discard2))
            else:
                break

    if is_empty(victory):
        return 0
    else:
        return size(victory)


def play_all_games(deck_size, num_of_games):
    """
    plays the game the given number of times and prints the stats
    of all the games
    :param deck_size: integer, number of elements to be in queue
    :param num_of_games: integer, how many times to simulate the card game
    :return: None
    """
    avg_cards = 0.0
    max_cards = 0
    min_cards = deck_size
    for i in range(num_of_games):
        deck = init_deck(deck_size)
        num_victory_cards = play_game(deck)
        avg_cards += num_victory_cards
        if num_victory_cards > max_cards:
            max_cards = num_victory_cards
        if num_victory_cards < min_cards:
            min_cards = num_victory_cards

    avg_cards /= num_of_games
    print('Average number of cards on victory pile:', avg_cards)
    print('Maximum number of cards on victory pile:', max_cards)
    print('Minimum number of cards on victory pile:', min_cards)


def main():
    """
    gets the deck size and number of games to be played from the user
    then calls the function play_all_games to simulate all of the games
    """
    deck_size = int(input('Enter deck size: '))
    num_of_games = int(input('Enter number of games: '))
    play_all_games(deck_size, num_of_games)


if __name__ == '__main__':
    main()
