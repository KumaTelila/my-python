import json

data = json.load(open("data.json"))

#function to convert
def translate(word):
    word = word.lower()
    if(word in data):
        return data[word]
    else:
        return "word not found"

word = input("Enter word: ")

print(translate(word))
