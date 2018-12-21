#Write a function called course_info that takes as input a
#list of tuples. Each tuple contains two items: the first
#item in each tuple is a student's name as a string, and the
#second item in each tuple is that student's age as an
#integer.
#
#The function should return a dictionary with two keys.
#The key "students" should have as its value a list of all
#the students (in other words, a list made from the first
#value of each tuple), in the original order in which they
#appeared in the list. The key "avg_age" should have as its
#value a float representing the average age of all the
#students in the list (in other words, the average of all
#the second items in the tuples).
#
#For example:
#
#  course_info([("Jackie", 20), ("Marguerite", 21)])
#  -> {"students": ['Jackie', 'Marguerite'], "avg_age": 20.5}
#
#Hint: Concentrate first on building the list of students
#and calculating the average age. Save creating the
#dictionary for last.


#Write your function here!
def course_info(tuple_list):
	sum_ages=0.0
	student_dict={}
	student_list=[]
	for tuple_ in tuple_list:
		student_list.append(tuple_[0])
		sum_ages+=tuple_[1]
		
	student_dict["students"]=student_list	
	student_dict["avg_age"]=sum_ages/len(tuple_list)
    #OR done this way:
	#student_dict={"students":student_list,"avg_age":sum_ages/len(tuple_list)}
	return student_dict

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print (although the order of the keys may vary):
print(course_info([("Jackie", 20), ("Marguerite", 21)]))
