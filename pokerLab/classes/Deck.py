from Card import Card

import random

class Deck:

    def __init__(self):
        self.cards = self.new_deck()
        random.shuffle(self.cards)

    def new_deck(self):
        values = [str(e) for e in range(1,10)] + ['J','Q','K','A']
        suits = ['club', 'spade', 'diamond', 'heart']
        deck = []
        for suit in suits:
            for value in values:
                deck.append(Card(value, suit))
        return deck

    def pop(self):
        return self.cards.pop()
