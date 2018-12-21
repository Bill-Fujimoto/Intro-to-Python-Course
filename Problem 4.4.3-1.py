def saveUserProfile(firstName, lastName, age, height, country):
    filename = lastName + firstName + ".txt"
    outputFile = open(filename, "w")
    print(lastName, file = outputFile)
    print(firstName, file = outputFile)
    print(country, file = outputFile)
    print(height, file = outputFile)
    print(age, file = outputFile)
    outputFile.close()

saveUserProfile("David", "Joyner", 30, 1.8, "USA")


def loadUserProfile(filename):
    inputFile = open(filename, "r")
    #for line in inputFile:
    #   print(line)
    lastName = inputFile.readline()
    firstName = inputFile.readline()
    country = inputFile.readline()
    #height = inputFile.readline()
    #age = inputFile.readline()
    height = float(inputFile.readline())
    age = int(inputFile.readline())
    print(height, age) 
    return (firstName, lastName, age, height, country)
    
user=loadUserProfile("JoynerDavid.txt")
print(user)
