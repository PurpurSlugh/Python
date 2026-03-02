import random

suits = {
    "hearts": "♥",
    "diamonds": "♦",
    "clubs": "♣",
    "spades": "♠"
}

values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

deck = [(value, suit) for suit in suits for value in values]

print("=== GUESS THE CARD ===")
print("Try to guess the random card!")
print("Format: Value Suit")
print("Example: J spades")
print()

# Player guess
user_input = input("Enter your guess: ").strip().lower().split()

if len(user_input) != 2:
    print("Invalid format. Please restart and use: Value Suit")
else:
    guessed_value = user_input[0].upper()
    guessed_suit = user_input[1]


    random_card = random.choice(deck)
    random_value, random_suit = random_card

    print("\nThe card was:")
    print(f"{random_value} {suits[random_suit]}")

    if guessed_value == random_value and guessed_suit == random_suit:
        print("🎉 Congratulations! You guessed correctly!")
    else:
        print("❌ Sorry, wrong guess. Try again!")