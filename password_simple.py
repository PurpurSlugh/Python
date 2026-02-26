import random
import string

char1 = ["!", ",", ".", ";", "/", "@", "#", "$", "%", "^", "&", "*"]
i = random.randint(10, 20)

password = ""

for _ in range(i):
    password += random.choice(string.ascii_letters)
    password += random.choice(char1)

print(password)