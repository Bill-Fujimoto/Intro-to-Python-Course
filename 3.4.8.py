def average_word_length(my_string):
    letter_count=0
    word_count=0
    try:
        for char in my_string:
            if not char in [" ",",","!","?","."]:
                letter_count +=1
        if letter_count > 0:
            if len(my_string) <=2:
                word_count = 1
            else:
                for i in range(0,len(my_string)):
                    if i <= len(my_string)-2:
                        if not my_string[i] in [" ",",","!","?","."] and my_string[i+1] in [" ",",","!","?","."]:
                            word_count += 1
                    elif i == len(my_string)-1:
                        if not my_string[i] in [" ",",","!","?","."]:
                            word_count += 1  		
            return letter_count/word_count
        else:
            return "No words"
    except:
        return "Not a string"
#When your function works, the following code should
#output:
#2.0
#3.0
#4.0
#Not a string
#No words

print(average_word_length("Hi!"))
print(average_word_length("Hi, Lucy!"))
print(average_word_length("   What  big spaces  you  have "))
print(average_word_length(True))
print(average_word_length("?!?!?! ... !"))

