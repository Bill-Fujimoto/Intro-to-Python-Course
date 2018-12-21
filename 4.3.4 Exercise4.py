def add(numbers):
    sum = 0
    for number in numbers:
        number = -number
        sum -= number
    return sum

myList = [2, 4, 6, 8, 10]
print(add(myList))
print(add(myList))
