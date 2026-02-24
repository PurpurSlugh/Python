import random

cycle = True
while cycle == True:
    print("Set the range for the random number:")
    print("Enter the lower bound: ")
    a = int(input())
    print("Enter the upper bound: ")
    b = int(input())
    if a >= b:
        print("Invalid range! The first number must be smaller than the second.")
        cycle = True
    else:
        cycle = False
     
x = random.randint(a, b)

counter = 0
cycle1 = True
while cycle1 == True:
    print("Guess the generated number: ")
    c = int(input())
    if c > x:
        print("Too high! The number you entered is greater than the generated number.")
        counter = counter + 1
    elif c < x:
        print("Too low! The number you entered is smaller than the generated number.")
        counter = counter + 1
    elif c == x:
        print(f"Congratulations! You guessed the random number in {counter + 1} attempts!")
        cycle1 = False 