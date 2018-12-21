def string_type(string):
    if "\n" in string:
        return "page"
    elif len(string.split(" ")) > 2 and string.count(".") > 1:
        return "paragraph"
    elif len(string)>=3 and len(string.split(" ")) > 1 and (string.count(".")==1 or string.count("!")==1):
        return "sentence"
    elif len(string)>1 and not " " in string:
        return "word"   
    elif len(string)==1:
        return "character"
    else:
        return "" 
        
#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#empty
#character
#word
#sentence
#paragraph
#page
print(string_type(""))
print(string_type("!"))
print(string_type("CS1301."))
print(string_type("This is too many cases!"))
print(string_type("There's way too many ostriches. Why are there so many ostriches. The brochure said there'd only be a few ostriches."))
print(string_type("Paragraphs need to have multiple sentences. It's true.\nHowever, two is enough. Yes, two sentences can make a paragraph."))
