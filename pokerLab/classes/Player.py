class Player:

    def __init__(self, user, bank):
        self.user = user
        self.bank = bank
        self.cards = []
    
    def recieve_card(self, card):
        self.cards.append(card)
        if len(self.cards) > 2:
            raise ValueError('Player recieved more than 2 cards.')
