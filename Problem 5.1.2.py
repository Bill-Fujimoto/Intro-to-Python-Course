def main():
    counter = Counter()
    print(id(counter.count))
    print()
    
    num = 0
    for x in range(0, 100):
        incrementor(counter, num)
        #print(id(counter.count))
    return (counter.count, num)
    
def incrementor(c, num):
    #print(id(c.count))
    c.count = c.count + 1
    #print(id(c.count))
    num = num + 1

class Counter:
    def __init__(self):
        self.count = 0

aTuple = main()
print(aTuple)
#print(id(counter))

