import json
from difflib import get_close_matches

def translate(word):
    dict = json.load(open("data.json"))
    ''' Otra opcion
    with open('C:/Users/urang/desktop/FRAN/Python/prueba.json') as f:
        dict = json.load(f)
    '''
    if word in dict:
        return dict[word]
    elif word.title() in dict:
        return dict[word.title()]
    elif word.upper() in dict:
        return dict[word.upper()]
    else:
        similarword = get_close_matches(word, dict.keys(), n=3)
        for count in range(len(similarword)):
            response = input("Did you mean? " + similarword[count] + " (y/n) ")
            if response == "y":
                out = translate(similarword[count])
                return out
        return "WNF"



y = "y"
while y == "y":
    word = input("What word do you want to look up? ").lower()
    listwithdef = translate(word)
    if listwithdef == "WNF":
        print("Word was not found")
    else:
        counter = 0
        for item in listwithdef:
            counter += 1
            print(str(counter) + ". " + item)
    y = input("Do you want to look up another word? (y/n) ")
