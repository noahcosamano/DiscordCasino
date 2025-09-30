class Card():
    __slots__ = ["value", "suit"]
    
    suit_value = {
        "clubs": 0,
        "diamonds": 1,
        "hearts": 2,
        "spades": 3
    }
    
    def __init__(self, value: int, suit: str):
        self.value = value
        self.suit = suit
        
    def num_value(self):
        if self.value == "A":
            return 14
        elif self.value == "K":
            return 13
        elif self.value == "Q":
            return 12
        elif self.value == "J":
            return 11
        else:
            return int(self.value)
        
    def get_value(self) -> int:
        return self.value
    
    def get_suit(self) -> str:
        return self.suit
    
    def __str__(self) -> str:
        return f"{self.value}{self.suit[0].upper()}"
    
    def __eq__(self, other) -> bool:
        return (
            isinstance(other, Card) and
            self.__num_value() == other.__num_value() and
            self.suit == other.suit
        )
        
    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Card):
            raise TypeError(f"Cannot compare Card type to {other.__class__}")
        
        if Card.suit_value[self.suit] > Card.suit_value[other.suit]:
            return True
        elif Card.suit_value[self.suit] < Card.suit_value[other.suit]:
            return False
        else:
            return self.__num_value() > other.__num_value()
        
    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Card):
            raise TypeError(f"Cannot compare Card type to {other.__class__}")
        
        if Card.suit_value[self.suit] < Card.suit_value[other.suit]:
            return True
        elif Card.suit_value[self.suit] > Card.suit_value[other.suit]:
            return False
        else:
            return self.__num_value() < other.__num_value()
