#Recall in Worked Example 5.2.5 that we showed you the code
#for two versions of binary_search: one using recursion, one
#using loops.
#
#In this problem, we want to implement a new version of
#binary_search, called binary_year_search. binary_year_search
#will take in two parameters: a list of instances of Date,
#and a year as an integer. It will return True if any date
#in the list occurred within that year, False if not.
#
#For example, imagine if listOfDates had three instances of
#date: one for January 1st 2016, one for January 1st 2017,
#and one for January 1st 2018. Then:
#
#  binary_year_search(listOfDates, 2016) -> True
#  binary_year_search(listOfDates, 2015) -> False
#
#You should not assume that the list is pre-sorted, but you
#should know that the sort() method works on lists of dates.
#
#Instances of the Date class have three attributes: year,
#month, and day. You can access them directly, you don't
#have to use getters (e.g. myDate.month will access the
#month of myDate).
#
#You may copy the code from Worked Example 5.2.5 and modify
#it instead of starting from scratch.
#
#Don't move this line:
from datetime import date


#Write your code here!
def binary_year_search(searchList, searchTerm):

    #First, the list must be sorted.
    searchList.sort()
    #print(searchTerm in searchList)    
    min = 0
    max = len(searchList) - 1

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
    
        if searchTerm == searchList[currentMiddle].year:
            return True
            
         
        elif searchTerm < searchList[currentMiddle].year:
            max = currentMiddle - 1
            #print(searchList[currentMiddle].year)
             
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

#The lines below will test your code. If it's working
#correctly, they will print True, then False.
listOfDates = [date(2016, 11, 26), date(2014, 11, 29), 
               date(2008, 11, 29), date(2000, 11, 25), 
               date(1999, 11, 27), date(1998, 11, 28), 
               date(1990, 12, 1), date(1989, 12, 2), 
               date(1985, 11, 30)]

print(binary_year_search(listOfDates, 2016))
print(binary_year_search(listOfDates, 2007))


