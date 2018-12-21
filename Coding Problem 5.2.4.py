#Recall in 5.2.4 Worked Example 1, we gave you the code for
#merge_sort. You may copy that code into this problem and
#modify it. Change it such that instead of sorting from
#lowest to highest, it sorts from highest to lowest.
#
#Name your function merge_sort(). For example, if you call
#merge_sort([5, 3, 1, 2, 4]), you would get [5, 4, 3, 2, 1].
#
#Do not use Python's sort or reverse methods to complete
#this.


#Write your code below!
def merge_sort(mylist):
    
    #Then, what does it do? mergesort should recursively
    #run mergesort on the left and right sides of mylist until
    #it's given a list only one item. So, if mylist has only
    #one item, we should just return that one-item list.
    
    if len(mylist) <= 1:
        return mylist
    
    #Otherwise, we should call mergesort separately on the
    #left and right sides. Since each successive call to
    #mergesort sends half as many items, we're guaranteed
    #to eventually send it a list with only one item, at
    #which point we'll stop calling mergesort again.
    else:

        #Floor division on the length of the list will
        #find us the index of the middle value.
        midpoint = len(mylist) // 2

        #mylist[:midpoint] will get the left side of the
        #list based on list slicing syntax. So, we want
        #to sort the left side of the list alone and
        #assign the result to the new smaller list left.
        left = merge_sort(mylist[:midpoint])

        #And same for the right side.
        right = merge_sort(mylist[midpoint:])

        #So, left and right now hold sorted lists of
        #each half of the original list. They might
        #each have only one item, or they could each
        #have several items.

        #Now we want to compare the first items in each
        #list one-by-one, adding the smaller to our new
        #result list until one list is completely empty.

        newlist = []
        while len(left) and len(right) > 0:

            #If the first number in left is larger, add
            #it to the new list and remove it from left
            if left[0] > right[0]:
                newlist.append(left[0])
                del left[0]

            #Otherwise, add the first number from right
            #to the new list and remove it from right
            else:
                newlist.append(right[0])
                del right[0]

        #When the while loop above is done, it means
        #one of the two lists is empty. Because both
        #lists were sorted, we can now add the remainder
        #of each list to the new list. The empty list
        #will have no items to add, and the non-empty
        #list will add its items in order.

        newlist.extend(left)
        newlist.extend(right)

        #newlist is now the sorted version of mylist! So,
        #we can return it. If this was a recursive call
        #to mergesort, then this sends a sorted half-
        #list up the ladder. If this was the original
        #call, then this is the final sorted list.

        return newlist


#The code below will test your function. If it works, this
#will print [5, 3, 1, -1, -3, -5].
print(merge_sort([1, 3, -1, -3, -5, 5]))


