from card import Card
import random

class Deck():
    def __init__(self):
        self.cards = []
        self.drawn_cards = []
        
        values = range(1, 14)
        suits = ["spades", "hearts", "diamonds", "clubs"]
        for suit in suits:
            for value in values:
                match value:
                    case 1:
                        value = "A"
                    case 11: 
                        value = "J"
                    case 12:
                        value = "Q"
                    case 13: 
                        value = "K"
                        
                self.cards.append(Card(value, suit))
                
    def __str__(self) -> str:
        cards = []
        for card in self.cards:
            cards.append(card.__str__())
            
        return " ".join(cards)
    
    def __len__(self) -> int:
        return len(self.cards)
    
    def shuffle(self):
        self.cards += self.drawn_cards
        random.shuffle(self.cards)
    
    def order(self):
        self.cards.sort()
        
    def draw(self) -> Card:
        card = self.cards.pop()
        self.drawn_cards.append(card)
        return card
