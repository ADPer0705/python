import random

# Defined a class for the deck of cards 
class Deck:
    def __init__(self):
        # initializing the deck

        self.cards = []

        # listing all the possible combinations
        suits = ["spades", "clubs", "hearts", "diamonds"]
        ranks = [
                {"rank" : "A", "value" : 11},
                {"rank" : "2", "value" : 2},
                {"rank" : "3", "value" : 3},
                {"rank" : "4", "value" : 4},
                {"rank" : "5", "value" : 5},
                {"rank" : "6", "value" : 6},
                {"rank" : "7", "value" : 7},
                {"rank" : "8", "value" : 8},
                {"rank" : "9", "value" : 9},
                {"rank" : "10", "value" : 10},
                {"rank" : "J", "value" : 10},
                {"rank" : "Q", "value" : 10},
                {"rank" : "K", "value" : 10},
            ]

        # Combining the ranks and suits to make the deck
        for suit in suits:
            for rank in ranks:
                self.cards.append([suit, rank])

    #shuffling the deck
    def shuffle(self):
        random.shuffle(self.cards)

    # dealing n number of cards from the deck
    def deal(self, number):
        cards_delt = []
        for i in range(number):
            card = self.cards.pop()
            cards_delt.append(card)
        
        return cards_delt
    

# instantiating a deck
deck1 = Deck()
deck2 = Deck()

deck2.shuffle()
print(deck1.cards)
print(deck2.cards)