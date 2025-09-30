import random

symbol_odds = {
    "cherry": range(1, 21),
    "lemon": range(21, 41),
    "orange": range(41, 56),
    "watermelon": range(56, 71),
    "grape": range(71, 81),
    "bell": range(81, 91),
    "star": range(91, 96),
    "diamond": range(96, 101)
}

payout = {
    ("cherry",): 1,
    ("cherry", "cherry"): 2,
    ("cherry", "cherry", "cherry"): 4,
    ("lemon", "lemon", "lemon"): 5,
    ("orange", "orange", "orange"): 10,
    ("watermelon", "watermelon", "watermelon"): 15,
    ("grape", "grape", "grape"): 20,
    ("bell", "bell", "bell"): 30,
    ("star", "star", "star"): 50,
    ("diamond", "diamond", "diamond"): 100
}

def get_slots(buy_in: int) -> int:
    slots = []
    
    if buy_in < 1:
        raise ValueError("Amount must be atleast $1")
    
    for _ in range(3):
        number = random.randint(1, 100)
        
        for symbol, odds in symbol_odds.items():
            if number in (odds):
                slots.append(symbol)
                
    return slots

def pay(buy_in: int, slots: list[str]) -> int:
    slots_tuple = tuple(slots)

    if slots_tuple in payout:
        return buy_in * payout[slots_tuple]
    
    if slots.count("cherry") == 2:
        return buy_in * payout[("cherry", "cherry")]
    elif slots.count("cherry") == 1:
        return buy_in * payout[("cherry",)]
    
    return 0

def spin(buy_in: int):
    slots = get_slots(buy_in)
    difference = pay(buy_in, slots)
    
    return difference
    
if __name__ == "__main__":
    print(spin(0.5))