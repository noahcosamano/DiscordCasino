import baccarat_logic as bl

def banker_test() -> str:
    bankroll = 10000
    money_per_play = 100
    plays = int(bankroll / money_per_play)
    
    for _ in range(plays + 1):
        bankroll -= money_per_play
        bankroll += bl.play("banker", money_per_play)
        
    return (f"Starting Bankroll: {10000} | Bankroll after {plays} runs of ${money_per_play} on banker: {bankroll}")
    
def player_test() -> str:
    bankroll = 10000
    money_per_play = 100
    plays = int(bankroll / money_per_play)
    
    for _ in range(plays + 1):
        bankroll -= money_per_play
        bankroll += bl.play("player", money_per_play)
        
    return (f"Starting Bankroll: {10000} | Bankroll after {plays} runs of ${money_per_play} on player: {bankroll}")
    
def tie_test() -> str:
    bankroll = 10000
    money_per_play = 100
    plays = int(bankroll / money_per_play)
    
    for _ in range(plays + 1):
        bankroll -= money_per_play
        bankroll += bl.play("player", money_per_play)
        
    return (f"Starting Bankroll: {10000} | Bankroll after {plays} runs of ${money_per_play} on a tie: {bankroll}")

def main():
    banker_results = banker_test()
    player_results = player_test()
    tie_results = tie_test()
    
    print(banker_results)
    print(player_results)
    print(tie_results)

if __name__ == "__main__":
    main()
    