#In Factorial.py, we provide a recursive Factorial function
#in Python. Now, let's see a version of it that makes it
#a little more clear what's going on.

#Notice that the core code of this file is no different from
#Factorial.py, but there are print statements throughout to
#let us see what the program is doing. We store the results
#of n * factorial(n - 1) in the variable result so that we
#can print it before returning.

def factorial(n):
    if n == 1:
        print("Base case reached!")
        return 1
    
    else:
        #print(n)
        print("Finding ", n, " * ", n-1, "!", sep = "")
        result = n * factorial(n - 1)
        #print(n)
        print(n, " * ", n-1, "! = ", result, sep = "")
        return result
    
#Now let's run it again! You can change this line to see
#how different calculations change the output.
print("5! is", factorial(5))


#Notice in the output how the execution climbs down the
#ladder from the original value of n to 1, then climbs
#back up the latter from 1 to n.


