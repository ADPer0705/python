import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank["rank"] + " of " + self.suit


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
        if (len(self.cards)) > 1:
            random.shuffle(self.cards)

    # dealing n number of cards from the deck
    def deal(self, number):
        cards_delt = []
        for i in range(number):
            if (len(self.cards)) > 0:
                card = self.cards.pop()
                cards_delt.append(card)
        
        return cards_delt
    
card1 = Card("hearts", {"rank" : "Q", "value" : 10},)
print(card1)