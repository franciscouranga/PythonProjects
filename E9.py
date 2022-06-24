import random

print("Guess the number from 1 to 10. Press \'e\' to exit")

num = random.randint(1, 10)
c = 0
while True:
    while True:
        user = input("Guess the number: ")
        if user == "e":
            print("You have not found the number.")
            exit()
        try:
            user = int(user)
            break
        except ValueError:
            print("That is not a valid integer.")
    if num == user:
        print("You guessed correctly, the number was {}. The number of guesses was {}".format(user, c+1))
        break
    elif num < user: print("The number is smaller than your guess.")
    else: print("The number is higher than your guess.")
    c += 1
