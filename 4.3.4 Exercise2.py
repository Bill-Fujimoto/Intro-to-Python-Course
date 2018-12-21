myList = [[3, 4, 5],
         [4, 5, 6],
         [5, 6, 7]]

def mystery(a2DList):
   result = []
   for alist in a2DList:
       value = 0
       for item in alist:
           value += item
       value *= 2
       result.append(value)
   return result

print(mystery(myList))
