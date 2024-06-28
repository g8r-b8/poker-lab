class Card:

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.card = self.value+'_'+self.suit
