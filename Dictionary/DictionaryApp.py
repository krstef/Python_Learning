import json
from difflib import get_close_matches

invalidWord = "The word does not exist. Please doublecheck it."
bestMatch = "Did you mean %s instead? Enter Y if yes, or N if no: "
wrongConfirmation = "Wrong input"
#save json file into local object

data = json.load(open("data.json"))
"""
define function for returning the word
argument is word - input from user
returns word description
"""
def translate_func(w):
    #make it case sensitive - to lower case(because of json)
    w = w.lower()
    try:
        if w in data:
            returnValue = data[w]
        elif w.title() in data:
            returnValue = data[w.title()]
        elif w.upper() in data:
            returnValue = data[w.upper()]
        elif len(get_close_matches(w, data.keys())) > 0:
            inputFromUser = input(bestMatch % get_close_matches(w, data.keys())[0])
            if inputFromUser == "Y":
                returnValue = data[get_close_matches(w, data.keys())[0]]
            elif inputFromUser == "N":
                returnValue = invalidWord
            else:
                returnValue = wrongConfirmation
    except:
        returnValue = invalidWord
    return returnValue
"""    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        return bestMatch % get_close_matches(w, data.keys())[0]
    else:
        return invalidWord
"""
while(1):
    word = input("Please enter your word: ")
    output = translate_func(word)
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)
    print("\n")
