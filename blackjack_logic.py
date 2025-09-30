from deck import Deck
from card import Card

player_hand = []
dealer_hand = []

deck = Deck()

def verify_bet(bet: int) -> bool:
    return bet >= 5

def initialize() -> str | None:
    p1 = deck.draw()
    print(f"Player got {p1}")
    player_hand.append(p1)
    
    d1 = deck.draw()
    print("Dealer card unknown")
    dealer_hand.append(d1)
    
    p2 = deck.draw()
    print(f"Player got {p2}")
    player_hand.append(p2)
    
    d2 = deck.draw()
    print(f"Dealer card {d2}")
    dealer_hand.append(d2)
    
    if check_blackjack(dealer_hand) == True and check_blackjack(player_hand) == False:
        print("Dealer Blackjack")
        return "dealer"
    
    if check_blackjack(dealer_hand) == False and check_blackjack(player_hand) == True:
        print("Player Blackjack")
        return "player blackjack"
    
    if check_blackjack(dealer_hand) == True and check_blackjack(player_hand) == True:
        print("Player and Dealer Blackjack")
        return "push"
    
    player_total = get_total(player_hand)

    print(f"Player Total: {player_total}")
    print(f"Dealer Total: ? + {dealer_hand[1].num_value()}")
    
    
def get_total(hand: list[Card]) -> int:
    total = 0
    
    for card in hand:
        value = card.num_value()
        if value == 14:
            value = 11
        elif value > 10:
            value = 10
        total += value
        
    if total > 21:
        total -= 10
        
    return total

def check_blackjack(hand: list[Card]) -> bool:
    total = 0
    
    total = get_total(hand)
        
    if total == 21:
        return True
    return False

def payout(result: str, bet: int) -> int:
    if result == "dealer":
        return 0
    
    if result == "player blackjack":
        return bet * 2.5
    
    if result == "player":
        return bet * 2
    
    if result == "push":
        return bet
    
def play(bet: int):
    deck.shuffle()
    if verify_bet(bet) == False:
        print("Bet must be at least $5")
        
    winner = initialize()
    if winner:
        winnings = payout(winner, bet)
        print(f"+ {winnings}")
        
if __name__ == "__main__":
    play(500)