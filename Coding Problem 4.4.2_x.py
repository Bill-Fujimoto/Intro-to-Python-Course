def format_checker(filename):
    input_file=open(filename, "r")    
    sum_of_weight=0
    for line in input_file:
        list_of_fields = line.strip().split(" ")
        try:
            int(list_of_fields[0])
            str(list_of_fields[1])
            int(list_of_fields[2])
            int(list_of_fields[3])
            float(list_of_fields[4])
            sum_of_weight += float(list_of_fields[4])
        except:
            return False

    return sum_of_weight == 1 and len(list_of_fields) == 5



#Test your function below. With the original values of these
#files, these should print True, then False:
print(format_checker("sample_1.cs1301"))
print(format_checker("sample_2.cs1301"))
