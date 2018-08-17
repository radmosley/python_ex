import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show (self):
        print('{} of {}'.format(self.suit, self.value))

class Deck:
    def __init__(self):
        self.cards = []
        self.build()
    
    def build(self):
        suit = ['spade ', 'club', 'diamond', 'heart']
        for s in suit:
            for v in range(1,14):
                self.cards.append(Card(s, v))

    def show(self):
        for c in self.cards:
            c.show()
    
    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def draw(self):
        return self.cards.pop()


deck = Deck()
# card_1 = Card()
# card_1.show()
# deck.show()
# deck.shuffle()
deck.show()

# card = deck.draw()
# card.show()