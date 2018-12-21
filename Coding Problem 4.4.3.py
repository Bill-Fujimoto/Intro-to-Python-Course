#Write a function called "reader" that reads in a ".cs1301" 
#file described in the previous problem. The function should 
#return a list of tuples representing the lines in the file like so:
#
#[(line_1_number, line_1_assignment_name, line_1_grade, line_1_total, line_1_weight), 
#(line_2_number, line_2_assignment_name, line_2_grade, line_2_total, line_2_weight)]
#
#All items should be of type int except for the name (string) 
#and the weight (float). You can assume the file will be in the 
#proper format -- in a real program, you would use your code
#from the previous problem to check for formatting before
#trying to call the function below.
#
#Hint: Although you could use readlines() to read in all
#the lines at once, they would all be strings, not a list.
#You still need to go line-by-line and convert each string
#to a list.


#Write your function here!
def reader(filename):
    input_file=open(filename, "r")
    result=[]    
    for line in input_file.readlines(): #"input_file.readlines()" is equivalent to simply "input_file";
		#which returns a list of strings, one string for each line in the file.
        #print(line)
        list_of_fields = line.strip().split(" ")
        #int() and float() strip off line feed and spaces.  No need for .strip() in line 5.
        number=int(list_of_fields[0])
        assignment=str(list_of_fields[1])
        grade=int(list_of_fields[2])
        total=int(list_of_fields[3])
        weight=float(list_of_fields[4])

        result.append((number,assignment,grade,total,weight))
    input_file.close()    
    return result


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 
#[(1, 'assignment_1', 85, 100, 0.25), (2, 'test_1', 90, 100, 0.25), (3, 'exam_1', 95, 100, 0.5)]
print(reader("sample.cs1301"))

######Solution#####

#This problem is deceptive: it looks really, really hard,
#and your solution might be long and complex. However,
#because we can assume that the file is well-formed, it's
#actually somewhat straightforward to solve -- it just
#doesn't feel that way.

def reader(filename):
    
    #First, we open the file:
    
	file_reader = open(filename)
    
    #Next, we'll create an empty list. We'll fill this
    #list with our results as we read them in.
    
	results = []
    
    #Now, we want to iterate through each line in the
    #file...
    
	for line in file_reader:
        
        #And split based on the space character:
        
		parts = line.split(" ")
        
        #Now parts is a list of 5 items. This problem
        #guarantees it will be well-formed, so we can
        #assume that our int and float conversions will
        #work. We could do them one-by-one, but we can
        #also do them all at once:
        
        line_tuple = (int(parts[0]), parts[1], int(parts[2]), int(parts[3]), float(parts[4]))
        
        #Then, we add it to our list of results:
        
        results.append(line_tuple)
        
        #And now we're done with what we need to do
        #for each line! All we have to do is split it,
        #convert it, tuple it, and add it to the list.
        
	
    #Then, at the end, we close the file...
    
    file_reader.close()
    
    #And return the list!
    
	return results



print(reader("sample.cs1301"))






