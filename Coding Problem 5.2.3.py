#Recall in the lesson on sorts that we had you complete the
#Bubble and Selection sort, and we showed you Merge sort.
#We didn't show any of insertion sort, and I bet you can
#guess why.
#
#Implement insertion sort below.
#
#Name your function 'insertion'. insertion should take as
#input a list, and return as output a sorted list. Note that
#even though technically a sorting method does not have to
#return the sorted list, yours should.
#
#If you're stuck on where to start, or having trouble
#visualizing or understanding how exactly insertion sort
#works, check out this website - https://visualgo.net/sorting
#It provides a visual representation of all of the sorting
#algorithms as well as pseudocode you can base your own code
#off of.


#Write your code here!
def insertion(mylist):
	
	for i in range(1,len(mylist)): #unsorted element
		for j in range(i,0,-1):
			if mylist[j] < mylist[j-1]:
				temp = mylist[j]
				mylist[j] = mylist[j-1]
				mylist[j-1] = temp
	return mylist

#The code below will test your function. If your function
#works, it will print: [1, 2, 3, 4, 5].
print(insertion([5, 1, 3, 2, 4, 9, 7, 8, 6]))

##### Pseudo Code from https://visualgo.net/sorting ######

#mark first element as sorted
#for each unsorted element X
  #'extract' the element X
  #for j = lastSortedIndex down to 0
    #if current element j > X
      #move sorted element to the right by 1
    #break loop and insert X here
