### Template
import random

class Card:
    def __init__(self, value, suite):
        self.value = value
        self.suite = suite

    def __str__(self):
        return f"{self.value} of {self.suite}"

    def __eq__(self, other):
        """Check if two cards are the same"""
        if self.value == other.value:
            if self.suite == other.suite:
                return True
        return False

class CardSet:
    def __init__(self):
        self.cards = []

    def view(self):
        for card in self.cards:
            print(card)

    def add_cards(self, cards):
        """Add cards to your set"""
        for c in cards:
            self.cards.append(c)
            
class Deck(CardSet):
    def __init__(self):
        """Initialize the 52-card set. Start from 1-11, then Jack, Queen, King, then by suite: clubs, spades, hearts, diamonds"""
        cards = []
        suites = ["clubs", "spades", "hearts", "diamonds"]
        royals = ["Jack", "Queen", "King"]
        for s in suites:
            for i in range(1,11):
                cards.append(Card(i, s))
            for r in royals:
                cards.append(Card(r, s))
        self.cards = cards
            
    def count_cards(self):
        """"Count the number of cards in a deck"""
        print(f"Cards Left: {len(self.cards)}")
    
    def shuffle(self, seed=None):
        """Shuffle your deck using a random seed"""
        random.seed(seed)
        random.shuffle(self.cards)

    def peek(self, number=5):
        """Show the top n cards of the stack. This is analogous to getting the last n cards then reversing it."""
        for c in list(reversed(self.cards[-number:])):
            print(c)
        # should i reverse the order of the list?
            
    def draw(self, cardset, number=5):
        """Transfer the top n cards of the stack to your cardset."""
        cardset.add_cards(list(reversed(self.cards[-number:])))
        del self.cards[-number:]

    def add_cards(self):
        pass

if __name__ == "__main__":
    seed, hand, peek = input().split(",")    

    myDeck = Deck()
    handA = CardSet()
    handB = CardSet()

    myDeck.shuffle(int(seed))

    for x in range(1,3):
        print(f"\nRound {x}:")

        myDeck.draw(handA, int(hand))
        myDeck.draw(handB, int(hand))        

        print("Hand A: ")
        handA.view()
        print("Hand B: ")
        handB.view()  

        myDeck.count_cards()
        if(x == 1):  
            print(f"\n{peek} Cards at the top: ")    
            myDeck.peek(int(peek))
