#Let's implement the Fibonacci function we saw in the
#previous video in Python!
#
#Like our Factorial function, our Fibonacci function
#should take as input one parameter, n, an integer. It
#should calculate the nth Fibonacci number. For example,
#fib(7) should give 13 since the 7th number in
#Fibonacci's sequence is 13.

#So, our function definition will basically be the same:

def fib(n):
    #What do we want to do inside the function? Once again,
    #there are really only two cases: either we're looking
    #for the first two Fibonacci numbers, or we're not.
    #What happens if we're looking for the first two? Well,
    #we already know that the 1st and 2nd Fibonacci numbers
    #are both 1, so if n == 1 or n == 2, we can go ahead
    #and return 1.
    
    if n == 1 or n == 2:
        return 1
    
    #What if n doesn't equal 1? For any value for n greater
    #than 2, the result should be the sum of the previous
    #two numbers. The previous Fibonacci number could then
    #be calculated with the same kind of function call,
    #decrementing n by 1 or 2.
    
    else:
        return fib(n - 1) + fib(n - 2)
    
    #If n is greater than 2, then it returns the sum of the
    #previous two fibonacci numbers, as calculated by the
    #same function.

#Now let's test it out! Run this file to see the results.
print("fib(5) is", fib(3))
print("fib(10) is", fib(10))
print()

#Want to see more about how this works? Select the other
#file, FibonacciwithPrints.py, from the drop-down in the
#top left to see a version of this that traces the output.

###############################################################

#As before, our core function below hasn't changed. What
#has changed is that we've added print statements so we can
#see a bit about how the program is running.

def fib(n):
    if n == 1 or n == 2:
        print("Found fib(", n, "): returning 1!", sep = "")
        return 1
    
    #As with the factorial function, we want to print every
    #time we're about to create a new call to Fibonacci,
    #and every time such a call is completed.
    
    else:
        print("Finding fib(", n, "): fib(", n - 1, ") + fib(", n-2, ")", sep = "")
        result =  fib(n - 1) + fib(n - 2)
        print("Found fib(", n, "): ", result, sep = "")
        return result

#Now if we run this, we'll see a lot more output. Feel free
#to change this line to visualize different Fibonacci
#numbers.
print("fib(6) is", fib(6))

#The output here is more complex; you may want to copy it
#into another window to read it.
#
#When fib(5) is first called, it wants to calculate fib(4)
#and fib(3). So, it calls fib(4) first, which demands fib(3)
#and fib(2). So, it calls fib(3), which demands fib(2) and
#fib(1). Those are both the base case, so both return 1.
#So, in the execution order, we see fib(5), then fib(4),
#then fib(3), then fib(2), then fib(1).
#
#Once fib(2) and fib(1) have run, then fib(3) can finish,
#and so the next statement printed is the result of fib(3).
#Once fib(3) is finished, then we can finish fib(4) by
#finding fib(2). fib(2) is again 1, so the next line is
#fib(2).
#
#Once fib(3) and fib(2) have finished, we can finish
#fib(4), so the next statement printed is the result of
#fib(4).
#
#Now that fib(4) is finished, we're all the way back to the
#first call, which wanted fib(4) + fib(3). Now, the rest of
#the execution is evaluating fib(3), which immediately
#demands fib(2) and fib(1). So, the next two lines are the
#results of fib(2) and fib(1). Once those are done, fib(3)
#is finished again.
#
#Now fib(4) and fib(3) are both finished, so the very first
#line can end: fib(4) + fib(3) = 3 + 2 = 5.



