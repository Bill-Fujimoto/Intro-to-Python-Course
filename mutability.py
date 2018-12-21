def bar(a_list):
    print("a_list is:",a_list)
    print("a_list id is:", id(a_list))
    
    b_list = a_list + [1]
    print("a_list is:",a_list)
    print("b_list is:",b_list)
    print("b_list id is:", id(b_list))
    
    b_list[3][0] = 0
    print("b_list is:",b_list)
    print("b_list id is:", id(b_list))

#Create a new list.
new_list = [1,2,3,[4,5,6]]
print("New list is:",new_list)
print("New list id is:", id(new_list))

#Call bar on new_list
bar(new_list)
print("New list is:", new_list)
print("New list id is:", id(new_list))
