#Let's implement a binary search using a loop! For now,
#our search will just return True if the item is found,
#False if it's not.

#Like our linear search, our binary search needs to
#parameters: a list to search, and an item to search for.

def binary_search(searchList, searchTerm):

    #First, the list must be sorted.
    searchList.sort()

    #Now, each iteration of the loop, we want to narrow
    #down the part of the list to look at. So, we need to
    #keep track of the range we've narrowed down to so
    #far. Initially, that will be the entire list, from
    #the first index to the last.
    
    min = 0
    max = len(searchList) - 1
    
    #Now, we want to loop as long as our range has any
    #numbers left to investigate. As long as there is
    #more than one number between minimum and maximum,
    #we're not done searching.
    
    while min <= max:

        #We want to check the middle item of the
        #current range, which is the average of the
        #current minimum and maximum index. For
        #example, if min was 5 and max was 15, our
        #middle number would be at index 10. We'll
        #use floor division because indices must be
        #integers.
        currentMiddle = (min + max) // 2

        #If the term in the middle is the term we're
        #looking for, we're done!
        if searchList[currentMiddle] == searchTerm:
            return True

        #If not, we want to check if the term we're
        #looking for should come earlier or later.

        #If the term we're looking for is less than
        #the current middle, then search the first
        #half of the list:
        elif searchTerm < searchList[currentMiddle]:
            max = currentMiddle - 1

        #If the term we're looking for is greater
        #than the current middle, search the second
        #half of the list:
        else:
            min = currentMiddle + 1

        #Each iteration of the loop, one of three
        #things happens: the term is found, max
        #shrinks, or min grows. Eventually, either
        #the term will be found, or min will be
        #equal to max.

    #If the search term was found, this line will
    #never be reached because the return statement
    #will end the function. So, if we get this
    #far, then the search term was not found, and
    #we can return False.
    return False

#Let's try it out!
intlist = [12, 64, 23, 3, 57, 19, 1, 17, 51, 62]
print("23 is in intlist:", binary_search(intlist, 23))
print("50 is in intlist:", binary_search(intlist, 50))

#Want to see something else interesting? Because of
#the way Python handles types, this exact same
#function works for any sortable data type. Check
#it out with strings:
strlist = ["David", "Joshua", "Marguerite", "Jackie"]
print("David is in strlist:", binary_search(strlist, "David"))
print("Lucy is in strlist:", binary_search(strlist, "Lucy"))

#Or with dates!
from datetime import date
datelist = [date(1885, 10, 13), date(2014, 11, 29), date(2016, 11, 26)]
print("10/13/1885 is in datelist:", binary_search(datelist, date(1885, 10, 13)))
print("11/28/2015 is in datelist:", binary_search(datelist, date(2015, 11, 28)))


#Now, go see how it works with recursion instead of loops
#in RecursiveBinarySearch.py! Or, print how this works with
#LoopingBinarySearchwithPrints.py.

#######################################################################
#This code is identical to LoopingBinarySearch.py, but
#with print statements throughout. In some places, the
#results of certain operations may be stored before
#being returned, but the functionality is the same.

#Let's implement a binary search using a loop! For now,
#our search will just return True if the item is found,
#False if it's not.

#Like our linear search, our binary search needs to
#parameters: a list to search, and an item to search for.

def binary_search(searchList, searchTerm):

    #First, the list must be sorted.
    searchList.sort()

    #Now, each iteration of the loop, we want to narrow
    #down the part of the list to look at. So, we need to
    #keep track of the range we've narrowed down to so
    #far. Initially, that will be the entire list, from
    #the first index to the last.
    
    min = 0
    max = len(searchList) - 1
    
    #Now, we want to loop as long as our range has any
    #numbers left to investigate. As long as there is
    #more than one number between minimum and maximum,
    #we're not done searching.
    
    while min <= max:
        print("Searching for", searchTerm, "in", searchList[min:max+1])
        
        #We want to check the middle item of the
        #current range, which is the average of the
        #current minimum and maximum index. For
        #example, if min was 5 and max was 15, our
        #middle number would be at index 5. We'll
        #use floor division because indices must be
        #integers.
        currentMiddle = (min + max) // 2

        #If the term in the middle is the term we're
        #looking for, we're done!
        if searchList[currentMiddle] == searchTerm:
            print(searchTerm, "==", searchList[currentMiddle], "-- search term found!")
            return True

        #If not, we want to check if the term we're
        #looking for should come earlier or later.

        #If the term we're looking for is less than
        #the current middle, then search the first
        #half of the list:
        elif searchTerm < searchList[currentMiddle]:
            print(searchTerm, "<", searchList[currentMiddle], "-- repeating for left side.")
            max = currentMiddle - 1

        #If the term we're looking for is greater
        #than the current middle, search the second
        #half of the list:
        else:
            print(searchTerm, ">", searchList[currentMiddle], "-- repeating for right side.")
            min = currentMiddle + 1

        #Each iteration of the loop, one of three
        #things happens: the term is found, max
        #shrinks, or min grows. Eventually, either
        #the term will be found, or min will be
        #equal to max.

    #If the search term was found, this line will
    #never be reached because the return statement
    #will end the function. So, if we get this
    #far, then the search term was not found, and
    #we can return False.
    print(searchTerm, "never found.")
    return False

#Let's try it out!
intlist = [12, 64, 23, 3, 57, 19, 1, 17, 51, 62]
print("23 is in intlist:", binary_search(intlist, 23))
print("50 is in intlist:", binary_search(intlist, 50))

#Want to see something else interesting? Because of
#the way Python handles types, this exact same
#function works for any sortable data type. Check
#it out with strings:
strlist = ["David", "Joshua", "Marguerite", "Jackie"]
print("David is in strlist:", binary_search(strlist, "David"))
print("Lucy is in strlist:", binary_search(strlist, "Lucy"))

#Or with dates!
from datetime import date
datelist = [date(1885, 10, 13), date(2014, 11, 29), date(2016, 11, 26)]
print("10/13/1885 is in datelist:", binary_search(datelist, date(1885, 10, 13)))
print("11/28/2015 is in datelist:", binary_search(datelist, date(2015, 11, 28)))


#Now, go see how it works with recursion instead of loops
#in RecursiveBinarySearch.py!

################################################################
#Let's implement a binary search using recursion! For now,
#our search will just return True if the item is found,
#False if it's not.

#Like our linear search, our binary search needs to
#parameters: a list to search, and an item to search for.

def binary_search(searchList, searchTerm):

    #First, the list must be sorted.
    searchList.sort()

    #With each recursive call to binary_search, the size
    #of the list will be cut in half, rounding down. If
    #the search term is not found, then eventually an
    #empty list will be passed into binary_search. So,
    #if searchList is empty, we know that the search
    #term was not found, and we can return False. This
    #is the base case for the recursive binary_search.

    if len(searchList) == 0:
        return False

    #If there are still items in the list, then we want
    #to find if searchTerm is greater than, less than,
    #or equal to the middle term in the list. For that,
    #we need the index of the middle term.

    middle = len(searchList) // 2

    #First, the easy case: if it's the middle term, we
    #found it! Return True.
    if searchList[middle] == searchTerm:
        return True

    #If the search term is less than the middle term,
    #then repeat the search on the left half of the
    #list.
    elif searchTerm < searchList[middle]:
        return binary_search(searchList[:middle], searchTerm)

    #If the search term is greater than the middle
    #term, then repeat the search on the right half
    #of the list.
    else:
        return binary_search(searchList[middle + 1:], searchTerm)

    #As long as there are items to be searched, binary_search
    #will keep getting called on smaller and smaller lists,
    #until eventually the item is found or the list of possible
    #places it could be found is empty.


#Let's try it out!
intlist = [12, 64, 23, 3, 57, 19, 1, 17, 51, 62]
print("23 is in intlist:", binary_search(intlist, 23))
print("50 is in intlist:", binary_search(intlist, 50))

#Want to see something else interesting? Because of
#the way Python handles types, this exact same
#function works for any sortable data type. Check
#it out with strings:
strlist = ["David", "Joshua", "Marguerite", "Jackie"]
print("David is in strlist:", binary_search(strlist, "David"))
print("Lucy is in strlist:", binary_search(strlist, "Lucy"))

#Or with dates!
from datetime import date
datelist = [date(1885, 10, 13), date(2014, 11, 29), date(2016, 11, 26)]
print("10/13/1885 is in datelist:", binary_search(datelist, date(1885, 10, 13)))
print("11/28/2015 is in datelist:", binary_search(datelist, date(2015, 11, 28)))


#Now, go see how it works with loops instead of recursion
#in LoopingBinarySearch.py! Or, print how this works with
#RecursiveBinarySearchwithPrints.py.

#########################################################################
#This code is identical to RecursiveBinarySearch.py, but
#with print statements throughout. In some places, the
#results of certain operations may be stored before
#being returned, but the functionality is the same.

#Let's implement a binary search using recursion! For now,
#our search will just return True if the item is found,
#False if it's not.

#Like our linear search, our binary search needs to
#parameters: a list to search, and an item to search for.

def binary_search(searchList, searchTerm):

    #First, the list must be sorted.
    searchList.sort()

    #With each recursive call to binary_search, the size
    #of the list will be cut in half, rounding down. If
    #the search term is not found, then eventually an
    #empty list will be passed into binary_search. So,
    #if searchList is empty, we know that the search
    #term was not found, and we can return False. This
    #is the base case for the recursive binary_search.

    if len(searchList) == 0:
        print(searchTerm, "never found.")
        return False

    #If there are still items in the list, then we want
    #to find if searchTerm is greater than, less than,
    #or equal to the middle term in the list. For that,
    #we need the index of the middle term.

    middle = len(searchList) // 2

    #First, the easy case: if it's the middle term, we
    #found it! Return True.
    if searchList[middle] == searchTerm:
        print(searchTerm, "==", searchList[middle], "-- search term found!")
        return True

    #If the search term is less than the middle term,
    #then repeat the search on the left half of the
    #list.
    elif searchTerm < searchList[middle]:
        print(searchTerm, "<", searchList[middle], "-- repeating for left side.")
        return binary_search(searchList[:middle], searchTerm)

    #If the search term is greater than the middle
    #term, then repeat the search on the right half
    #of the list.
    else:
        print(searchTerm, ">", searchList[middle], "-- repeating for right side.")
        return binary_search(searchList[middle + 1:], searchTerm)

    #As long as there are items to be searched, binary_search
    #will keep getting called on smaller and smaller lists,
    #until eventually the item is found or the list of possible
    #places it could be found is empty.


#Let's try it out!
intlist = [12, 64, 23, 3, 57, 19, 1, 17, 51, 62]
print("23 is in intlist:", binary_search(intlist, 23))
print("50 is in intlist:", binary_search(intlist, 50))

#Want to see something else interesting? Because of
#the way Python handles types, this exact same
#function works for any sortable data type. Check
#it out with strings:
strlist = ["David", "Joshua", "Marguerite", "Jackie"]
print("David is in strlist:", binary_search(strlist, "David"))
print("Lucy is in strlist:", binary_search(strlist, "Lucy"))

#Or with dates!
from datetime import date
datelist = [date(1885, 10, 13), date(2014, 11, 29), date(2016, 11, 26)]
print("10/13/1885 is in datelist:", binary_search(datelist, date(1885, 10, 13)))
print("11/28/2015 is in datelist:", binary_search(datelist, date(2015, 11, 28)))


#Now, go see how it works with loops instead of recursion
#in LoopingBinarySearch.py!





