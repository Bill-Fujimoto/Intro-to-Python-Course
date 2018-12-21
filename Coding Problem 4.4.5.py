#Write a function called get_grade that will read a
#given .cs1301 file and return the student's grade.
#To do this, we would recommend you first pass the
#filename to your previously-written reader() function,
#then use the list that it returns to do your
#calculations. You may assume the file is well-formed.
#
#A student's grade should be 100 times the sum of each
#individual assignment's grade divided by its total,
#multiplied by its weight. So, if the .cs1301 just had
#these two lines:
#
# 1 exam_1 80 100 0.6
# 2 exam_2 30 50 0.4
#
#Then the result would be 72:
#
# (80 / 100) * 0.6 + (30 / 50) * 0.4 = 0.72 * 100 = 72


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
        score=int(list_of_fields[2])
        total=int(list_of_fields[3])
        weight=float(list_of_fields[4])
        result.append((number,assignment,score,total,weight))
    input_file.close()    
    return result

def get_grade(filename):
    list_of_scores = reader(filename)	
    grade=0
    for item in list_of_scores:
        score=item[2]
        total=item[3]
        weight=item[4]
        grade += (score/total)*weight*100
    return grade

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 91.55 

print(get_grade("sample_1.cs1301"))

##### Solution ######

#As recommended, we're going to want to re-use our code from
#4.4.3. So, here it is:
def reader(filename):
    file_reader = open(filename)
    results = []
    
    for line in file_reader:
        parts = line.split(" ")
        line_tuple = (int(parts[0]), parts[1], int(parts[2]), int(parts[3]), float(parts[4]))
        results.append(line_tuple)
    
    file_reader.close()
    return results

#The benefit of this is that it takes care of all of our file-
#handling for us! Now when we start to write our get_grade
#function, we can just call reader() and then do all our
#work on the list, which is easier to use:

def get_grade(filename):
    
    #First, we call reader(), and save the result to a list
    #called gradebook_items:
    
    gradebook_items = reader(filename)
    
    #Next, the total grade is the sum of each individual grade
    #divided by its max and multiplied by its weight. So, we
    #first create our total_grade variable and set it to 0:
    
    total_grade = 0
    
    #Now, we iterate through each gradebook item...
    
    for gradebook_item in gradebook_items:
        
        #To keep things easier to read, we'll first unpack
        #the tuple:
        
        number, name, grade, max_grade, weight = gradebook_item
        
        #Now, we'll add this grade's contribution to
        #total_grade:
        
        total_grade += (grade / max_grade) * weight
    
    #Then at the end, we'll return total_grade times 100:
    
    return total_grade * 100

    #Note that none of the new code written here had anything
    #to do with files: once we loaded our data from a file,
    #we did all our work with the data stored in memory.

print(get_grade("sample_1.cs1301"))









