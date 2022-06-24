from random import randint

def diceroll():
    i = randint(1,6)
    return i;

hola = [0,0,0,0,0]
x = "y"
while x == "y":
    i = diceroll()
    print(i)
    x = input("Press y to roll again: ")
