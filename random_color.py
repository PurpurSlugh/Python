from numpy import random
mylist = ["Red", "Yellow", "Orange","Green","Blue"]
randomcol = random.choice(mylist)
print("Select a color from: Red , Yellow , Orange , Green or Blue")
color = str(input())
if color == randomcol:
   print("You selected the correct color!")
   print("Congratulations!")
else:
    print("You selected the WRONG color!")
    print("Now I'll delete your OS!")
    