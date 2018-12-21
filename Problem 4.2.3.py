phrase = "HULK MAD"
phrase = phrase.lower()
phrase = phrase.title()
cutPhrase = phrase[:5]
newPhrase = "x"
for char in phrase[5:]:
    if char == "m":
        newPhrase = cutPhrase + "Hungry"
    elif char == "a":
        newPhrase = cutPhrase + "Angry"
    elif char == "d":
        newPhrase = cutPhrase + "Smash"
    print(newPhrase)

#Problem 4.2.3 4 of 4
phrase = "HULK MAD"
phrase = phrase.lower()
phrase = phrase.title()
cutPhrase = phrase[:5]
newPhrase = ""

for char in phrase[5:]:
    if char == "m":
        newPhrase = cutPhrase + "Hungry"
    elif char == "a":
        newPhrase = cutPhrase + "Angry"
    elif char == "d":
        newPhrase = cutPhrase + "Smash"
    print(newPhrase)
