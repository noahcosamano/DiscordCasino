from deck import Deck
from card import Card

player_hand = []
banker_hand = []

deck = Deck()

def verify_bet(bet: str, amount: int) -> tuple[str, int]:
    if bet not in ("player", "banker", "tie"):
        raise ValueError("Bet must be Player, Banker, or Tie")
    
    if amount < 5:
        raise ValueError("Amount must be atleast $5")
    
    return bet.lower(), amount

def check_natural(hand: list[Card]) -> bool:
    sum = 0
    
    for card in hand:
        if card.num_value() > 9:
            sum += 0
        elif card.num_value() == 14:
            sum += 1
        else:
            sum += card.num_value()
        
    if sum > 9:
        sum -= 10
        
    return 7 < sum < 10

def get_total(hand: list[Card]) -> int:
    sum = 0
    
    for card in hand:
        if card.num_value() == 14:
            sum += 1
        elif card.num_value() > 9:
            sum += 0
        else:
            sum += card.num_value()
        
    if sum > 9:
        sum -= 10
        
    return sum  

def check_natural_winner() -> str | None:
    if (check_natural(player_hand) == True) and (check_natural(banker_hand) == False):
        return "player"
    if (check_natural(player_hand) == False) and (check_natural(banker_hand) == True):
        return "banker"
    if (check_natural(player_hand) == True) and (check_natural(banker_hand) == True):
        return "tie"
    if (check_natural(player_hand) == False) and (check_natural(banker_hand) == False):
        return None
    
def check_winner() -> str:
    banker_sum = get_total(banker_hand)
    player_sum = get_total(player_hand)
    
    if player_sum > banker_sum:
        return "player"
    if player_sum < banker_sum:
        return "banker"
    if player_sum == banker_sum:
        return "tie"

def first_draw() -> str | None:
    print("--- first draw ---")
    p1 = deck.draw()
    print(f"player got {p1}")
    player_hand.append(p1)
    
    b1 = deck.draw()
    print(f"banker got {b1}")
    banker_hand.append(b1)
    
    p2 = deck.draw()
    print(f"player got {p2}")
    player_hand.append(p2)
    
    b2 = deck.draw()
    print(f"banker got {b2}")
    banker_hand.append(b2)
    
    print(f"player total: {get_total(player_hand)} | banker total: {get_total(banker_hand)}")

def round_two():
    print("\n--- second draw ---")
    if get_total(player_hand) <= 5:
        p3 = deck.draw()
        print(f"player got {p3}")
        player_hand.append(p3)
        print(f"player total: {get_total(player_hand)}")
        banker_draw_logic(p3.num_value())
    else:
        banker_sum = get_total(banker_hand)
        
        if banker_sum <= 5:
            banker_draw()
            
    print(f"player total: {get_total(player_hand)} | banker total: {get_total(banker_hand)}")

def banker_draw():
    b3 = deck.draw()
    print(f"banker got {b3}")
    banker_hand.append(b3)
    
def banker_draw_logic(num: int):
    banker_sum = get_total(banker_hand)
    
    if banker_sum <= 2:
        banker_draw()
    elif banker_sum == 3 and num != 8:
        banker_draw()
    elif banker_sum == 4 and num in range(2, 8):
        banker_draw()
    elif banker_sum == 5 and num in range(4, 8):
        banker_draw()
    elif banker_sum == 6 and num in range(6, 8):
        banker_draw()
        
def pay(winner: str, bet: str, amount: int) -> int:
    if (winner == bet) and (winner == "player"):
        return amount * 2
    if (winner == bet) and (winner == "banker"):
        return int(amount * 1.95)
    if (winner == bet) and (winner == "tie"):
        return amount * 8
    else:
        return 0
            
def play(bet: str, amount: int) -> int:
    player_hand.clear()
    banker_hand.clear()
    deck.shuffle()
    bet, amount = verify_bet(bet, amount)
    first_draw()
    winner = check_natural_winner()
    if winner:
        print(f"{winner} wins!")
        winnings = pay(winner, bet, amount)
        print(f"+ {winnings}")
        return winnings
    round_two()
    winner = check_winner()
    print(f"{winner} wins!")
    winnings = pay(winner, bet, amount)
    print(f"+ {winnings}")
    return winnings
    
if __name__ == "__main__":
    play("player", 500)