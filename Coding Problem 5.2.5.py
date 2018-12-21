#Write a function called string_search() that takes two
#parameters, a list of strings, and a string. This function
#should return  a list of all the indices at which the
#string is found within the list.
#
#You may assume that you do not need to search inside the
#items in the list; for examples:
#
#  string_search(["bob", "burgers", "tina", "bob"], "bob")
#      -> [0,3]
#  string_search(["bob", "burgers", "tina", "bob"], "bae")
#      -> []
#  string_search(["bob", "bobby", "bob"])
#      -> [0, 2]
#
#Use a linear search algorithm to achieve this. Do not
#use the list method index.
#
#Recall also that one benefit of Python's general leniency
#with types is that algorithms written for integers easily
#work for strings. In writing string_search(), make sure
#it will work on integers as well -- we'll test it on
#both.

####### from 5.2.5 Coding Exercise 1 ##################
#def linear(str_list, string):
    #string_found = False
    #for i in range(len(str_list)):
        #if string == str_list[i]:
            #string_found = True
            #return i
    #return string_found

#Write your code here!
def string_search(str_list, string):
	index = []
	for i in range(len(str_list)):
		if string == str_list[i]:
			index.append(i)
	return index
    
#Feel free to add code below to test your function. You
#can, for example, copy and print the test cases from
#the instructions.
print(string_search(["bob", "burgers", "tina", "bob"], "bob"))
#    -> [0,3]
print(string_search(["bob", "burgers", "tina", "bob"], "bae"))
#      -> []
print(string_search(["bob",10, "bobby", "bob", 10, 20], 10))
#     -> [0, 2]
