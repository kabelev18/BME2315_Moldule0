# This is your first coding assignment for Computational BME.
# As discussed in class, feel free to use AI tools to help you complete this assignment, but remember to cite them.
# I encourage you to try the problems yourself first and only use AI tools when you are stuck to benefit your learning. 

# Name: Katia Abelev
# AI Contribution: ChatGPT was used to troubleshoot and fix errors in my pseudocode and regular code in each problem.

# %% ###########################################################
# Problem 1: Practice writing pseudocode

# Write pseudocode that will input a integer N and output the sum of the first N numbers in the fibonacci sequence.
# Fibonacci sequence starts: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
# Example: If N = 5, the output should be 0 + 1 + 1 + 2 + 3 = 7

""" # you can use three double-quotes to write multi-line comments
Input integer N
Set sum = 0
Set first = 0
Set second = 1

Repeat N times:
    Add first to sum
    Set next = first + second
    Set first = second
    Set second = next

Output sum
"""

# %% ###########################################################
# Problem 2: Comment your code
# Comments are very helpful for others (especially when pair-coding!) and yourself to understand your code! Add comments to the following code, which will run but produces the wrong output. Once you comment the code, you should be able to identify the error and fix it (the correct total that should be printed is 12).
N = 6

a = 0 # set a to the first fibonacci number
b = 1 # set b to the second fibonacci number
count = 0
total = 0

while count < N:
    total = total + a # total = total + a, need to start with adding a first

    next_value = a + b #calculates the next fibonacci number
    a = b # set a to the value of b, b becomes the new a
    b = next_value #next fibonacci number becomes the new b

    count = count + 1 #increases the count by 1 to keep track of how many fibonacci numbers have been added

print(total) #prints the total sum of the first N fibonacci numbers

# %% ###########################################################
# Problem 3: Using common Python libraries
# What is the standard deviation of the first 10 numbers in the fibonacci sequence? Use the numpy library to calculate the standard deviation.

import numpy as np

fib_first10 = [0,1,1,2,3,5,8,13,21,34]
standard_deviation = np.std(fib_first10)
print(standard_deviation)

# %% ###########################################################
# Problem 4: Don't repeat yourself by writing functions
# Write a function that takes an integer N as input and returns the sum of the first N numbers in the fibonacci sequence.
# Then use this function to calculate the sums for N = 5, 10, 15, 20, 25, and 30 and print them as a list.

def sum_fib(N):
    a = 0
    b = 1
    total = 0
    for i in range(N):
        total += a
        next_value = a + b
        a = b
        b = next_value
    return total

all_sums = []
for N in [5,10,15,20,25,30]:
    all_sums.append(sum_fib(N))

print(all_sums)

# %% ###########################################################
# Problem 5: Read your error messages
# Run the following code block to see what the error messages are. Then, for each error:
# 1. Identify what type of error it is (SyntaxError, NameError, TypeError, etc.)
# 2. Add a comment to the line that is throwing the error explaining what the error is
# 3. Fix the error so that the code runs correctly

# You will only see one error at a time when you run the code. After fixing one error, run the code again to see the next error. Your final code should work correctly and will have comments where the original errors were.


def find_fib_above_limit(limit):
    """# The function inputs an integer called "limit" and finds the first number that goes above "limit" in the fibonacci sequence. It returns the index of that number.
    :param limit: limit of fibonacci sequence
    :type limit: integer
    :return: index of the first number above limit
    :rtype: integer
    """
    a = 0 #These (a and b) need to be integers not strings
    b = 1
    index = 0 #added to initialize "index" variable

    while a <= limit: #TypeError: '<=' not supported between instances of 'str' and 'int', the variables a and b should be integers not strings
        next_value = a + b
        a = b
        b = next_value
        index += 1 #UnboundLocalError: can't access local variable "index" where it is not associated with a value, need to initialize index prior to while loop in order to use it
    return index


result = find_fib_above_limit(50)
print("The index of the first number above your limit is: ", result)
# %% ###########################################################
# Problem 6: Test your code
# The following function will run but will output the wrong answer sometimes. Add test cases to verify that the function works correctly for a variety of inputs. If you find any inputs that produce incorrect outputs, fix the function. The function, when working properly, should return the sum of all odd Fibonacci numbers less than or equal to the input "limit".


def sum_odd_fib(limit): #starts out giving even numbers instead of odd, changed this to odd
    a, b = 0, 1
    total = 0
    while b <= limit:
        if b % 2 == 1:#This line checked if the Fibonacci number is even, changed it to check for odd
            total += b #This used to just change the number to the input, changed it to add it to the total
        a, b = b, a + b
    return total

# test cases
print(sum_odd_fib(10))
print(sum_odd_fib(6))
print(sum_odd_fib(20))
print(sum_odd_fib(45))
print(sum_odd_fib(100))
# %%
