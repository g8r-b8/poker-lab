from Deck import Deck
from Player import Player

class Table:

    def __init__(self, players):
        self.players = {i:player for i, player in enumerate(players)}
        self.deck = Deck()

    def new_game(self):
        self.deck = Deck()
        self.deal_cards()
        breakpoint()

    def deal_cards(self):
        for i, player in self.players.items():
            player.recieve_card(self.deck.pop())
        for i, player in self.players.items():
            player.recieve_card(self.deck.pop())

if __name__ == "__main__":
    players = [
        Player('Joe', 100),
        Player('Jerry', 100),
        Player('Alfert', 100),
        Player('Barry', 100),
     ]
    table = Table(players)
    table.new_game()
