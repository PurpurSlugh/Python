def hello (name, age):
    print("Hello",name)
    if age >= 18:
        print(name, "you're an adult, you can drink Jägermeister!")
    else:
        print(name, "you're not an adult, you can't drink Jägermeister yet!")
    
print("What's your name?")
name = input()
print("How old are you?")
age = int(input())

hello(name, age)