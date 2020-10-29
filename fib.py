"""

>>> fib(6)
8

>>> fib(2)
1

>>> fib(7)
13

>>> fib(10)
55

>>> fib(9)
34

>>> fib(17) # bigger number!!
1597

>>> fib(14) # bigger number!!
377

>>> fib(27) #a huge number!!!
196418


Step 1. For the first couple of numbers in the Fibonacci sequence, check if the number (n) is 1 or 2 first.
Step 2. If n is equal to 1 or 2, then the code will return the number 1 as the sum of the first numbers
        of that sequence equals 1.
Step 3. If it is more than 2, then n must be applied for this equation for the sequence : fib(n-1)+fib(n-2)
Step 4. Once the equation for the Fibonacci sequence is set up underneath the else statement, return the equation
        so the answers will be verfied within the test suites above.

"""

from math import *
# make Python look in the right place for logic.py, or complain if it doesn't
try:
    import sys
    sys.path.append('/home/courses/python')
    from logic import *
except:
    print("Can't find logic.py; if this happens in the CS teaching lab, tell your instructor")
    print("   If you are using a different computer, add logic.py to your project")
    print("   (You can download logic.py from http://www.cs.haverford.edu/resources/software/logic.py)")
    sys.exit(1)

def fib(n: int):
    precondition: n >= 1
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
    #postcondition: The result of the Fibonacci Sequence fib(n: int) is the sum of the previous two numbers in the sequence.




#############################################################################################
# The following gets the DocTest system to check test cases in the documentation comments.  #
# In most Haverford CS course, you won't need to modify the stuff below.                    #
#############################################################################################

if __name__ == "__main__":
    import doctest
    result = doctest.testmod()
    if result[0] == 0:
        print(("Congratulations! You have passed all "+str(result[1])+" tests"))
    else:
        print("Rats!")


