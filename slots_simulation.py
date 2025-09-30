import slots_logic as sl

def main():
    bankroll = 10000
    money_per_spin = 10
    spins = int(bankroll / money_per_spin)
    
    for _ in range(spins + 1):
        bankroll -= money_per_spin
        bankroll += sl.spin(money_per_spin)
        
    print(f"Starting Bankroll: {10000} | Bankroll after {spins} spins of ${money_per_spin}: {bankroll}")

if __name__ == "__main__":
    main()
    