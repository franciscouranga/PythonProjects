import json
from random import randint
import string

'''
1. find world
2. count attempts
3. compare results with string
'''

#choose a random Word
def get_rndm_word(m):
    dict = json.load(open("data.json"))
    x = 1
    while x == 1:
        x = 0
        i = randint(0, len(dict.keys()))
        word = list(dict.keys())[i].lower()
        counter = 0
        for letter in word:
            if letter in string.punctuation or letter == " ":
                x = 1
        if len(word) > m:
            x = 1
    return word

#Get word
while True:
    #word = get_rndm_word(randint(4,10))
    word = input("Escribir aca la palabra: ").lower()
    break
    '''
    print(word)
    if input("Press r to choose word") == "r":
        break
    '''

for i in range(20):
    print('\n')
#Initial message
print("Hello, welcome to hangman" + '\n' + "-------------------------" + '\n' + "You have 10 attempts to find the word.")

#Function that prints the hangman
def hangman(i):
    '''
    _______
        O_|
       /|\
       / \
    '''
    if i < 10: print("_________")
    if i < 9:
        if i <= 8 and i > 4: print("    O   ")
        if i == 4: print("  \ O ")
        if i == 3: print("  \ O / ")
        if i == 2: print("  \ O / | ")
        if i == 1: print("  \ O /_| ")
        if i == 0: print("    O_| ")
    if i < 8:
        if i != 0: print("    | ")
        if i == 0: print("   /|\ ")
    if i < 7:
        if i  == 6: print("   /  ")
        else: print("   / \ ")

#Determine number of _
guesses = ""
for letter in word:
    guesses += "-"
print("Word:  " + guesses)

#Parameters
attempts = 10
allguesses = ""

x = "y"
while x == "y":
    guess = input("Guess: ").lower()
    if len(guess) == 1 and guess in string.ascii_lowercase and guess not in allguesses:
        allguesses += guess
        allguesses += " "
        if guess in word:
            standby = guesses
            guesses = ""
            counter = 0
            for letter in word:
                if letter == guess:
                    guesses += letter
                else:
                    guesses += standby[counter]
                counter += 1
            print("Word: " + guesses + "        " + "Attempts left: " + str(attempts) + "       " + "Letters submitted: "+ allguesses)
        else:
            attempts -= 1
            print("Word: " + guesses + "        " + "Attempts left: " + str(attempts) + "       " + "Letters submitted: "+ allguesses)
            hangman(attempts)
    elif guess in allguesses: print("Letter allready guessed")
    else: print("Invalid guess")
    if guesses == word:
        print("You win!")
        x = "n"
    if attempts == 0:
        print("You lose! The word was", word)
        x = "n"
    print("")
