import random

print("Insert the number of rolls for the dice: ")
dice = int(input())
tails = 0
heads = 0

for i in range(dice):
    x = random.randint(1, 2)
    if (x == 1):
        print("Heads")
        heads = heads +1
    else:
        print("Tails")
        tails = tails +1

print("Heads = ",heads / dice * 100, "%")
print("Tails = ",tails / dice * 100, "%")
