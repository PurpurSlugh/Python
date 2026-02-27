import random

char1 = ["🕋", "👑", "💎", "🔥", "🍪","🕋"]
mymoney = 1000

cycle = True 
while cycle:
    print(f"\nYou have {mymoney}$")
    if mymoney <= 0:
        print("You lost all the money, GAME OVER.")
        break
        
    print("How much do you want to gamble? 1$, 5$, 25$, 50$ o 100$?")
    try:
        bet = int(input())
    except ValueError:
        print("Select a valid choise!")
        continue

    if bet not in [1, 5, 25, 50, 100] or bet > mymoney:
        print("Invalid choise or negative balance!")
        continue 

    result = [random.choice(char1) for _ in range(3)]
    print(f"Risultato: {' '.join(result)}")


    if len(set(result)) == 1:
        won = bet * 10
        mymoney += won
        print(f"CONGRATULATIONS! You won {won}$!")
    else:
        mymoney -= bet
        print(f"You lost {bet}$.")
    
    if mymoney > 0:
        print("You want to play again? (yes/no)")
        if input().lower() != "yes":
            cycle = False
    else:
        cycle = False
