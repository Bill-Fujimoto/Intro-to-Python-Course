#Last exercise, you wrote a function called
#one_dimensional_booleans that performed some reasoning
#over a one-dimensional list of boolean values. Now,
#let's extend that.
#
#Imagine you have a two-dimensional list of booleans,
#like this one:
#[[True, True, True], [True, False, True], [False, False, False]]
#
#Notice the two sets of brackets: this is a list of lists.
#We'll call the big list the superlist and each smaller
#list a sublist.
#
#Write a function called two_dimensional_booleans that
#does the same thing as one_dimensonal_booleans. It should
#look at each sublist in the superlist, test it for the
#given operator, and then return a list of the results.
#
#For example, if the list above was called a_superlist,
#then we'd see these results:
#
# two_dimensional_booleans(a_superlist, True) -> [True, False, False]
# two_dimensional_booleans(a_superlist, False) -> [True, True, False]
#
#When use_and is True, then only the first sublist gets
#a value of True. When use_and is False, then the first
#and second sublists get values of True in the final
#list.
#
#Hint: This problem can be extremely difficult or
#extremely simple. Try to use your answer or our
#code from the sample answer in the previous problem --
#it can make your work a lot easier! You may even want
#to use multiple functions.


#Write your function here!
def two_dimensional_booleans(super_list, use_and):
    results=[]
    for a_list in super_list:
        if not use_and:
            results.append(True in a_list)
        else:
            results.append(not False in a_list)
    return results

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#[True, False, False]
#[True, True, False]
bool_superlist = [[True, True, True], [True, False, True], [False, False, False]]
print(two_dimensional_booleans(bool_superlist, True))
print(two_dimensional_booleans(bool_superlist, False))

###################

def one_dimensional_booleans(bool_list, use_and):
    
    #There are a lot of different ways you could do this.
    #You could, for example, loop over each item in the
    #list and update a running result based on the new
    #value.
    #
    #Let's try it a simpler way, though. If use_and was
    #False, then our logic is pretty simple: we just
    #return whether 'True' is anywhere in the list:
    
    if not use_and:
        return True in bool_list
    
    #If use_and was True, our logic is just a little bit
    #more complicated. First, we want to find our whether
    #False is in the list. If it is, then we want to
    #return False; if it's not (meaning all the values
    #are True), then we want to return True. So, we want
    #to return the *opposite* of False in bool_list. We
    #can do that with the not operator:
    
    else:
        return not False in bool_list
    
    #Note that we could actually compress these four lines
    #down into only one, but it makes the logic a little
    #harder to follow:
    #
    #return (use_and and True in bool_list) or (not use_and and not False in bool_list)



print(one_dimensional_booleans([True, True, True], True))
print(one_dimensional_booleans([True, False, True], True))
print(one_dimensional_booleans([True, False, True], False))
print(one_dimensional_booleans([False, False, False], False))

