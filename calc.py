expr = False

print("Insert the first number: ")
num1 = float(input())

print("Insert the second number: ")
num2 = float(input())

print("You want to add a third number? y (yes), n (no)")
num3yn = input()

num3 = 0 

if num3yn == "y" or num3yn == "Y":
    print("Insert the third number: ")
    num3 = float(input())
elif num3yn == "n" or num3yn == "N":
    print("Third number not added")

while expr == False:
    print("Select which of these expression you want to solve:")
    print("Addition(1) Subtraction(2) Multiplication(3) Division(4)")
    
    option = input()

    if option not in ["1", "2", "3", "4"]:
        print("Select a valid number!")
    
    elif option == "1":
        print("Result:", num1 + num2 + num3)
        expr = True
    
    elif option == "2":
        print("Result:", num1 - num2 - num3)
        expr = True
    
    elif option == "3":
        print("Result:", num1 * num2 * num3)
        expr = True
    
    elif option == "4":
        if num2 == 0 or num3 == 0:
            print("Division by zero is not allowed!")
        else:
            print("Result:", num1 / num2 / num3)
            expr = True