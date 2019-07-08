"""
Python is a strongly-typed language under the hood, which means 
that the types of values matter, especially when we're trying
to perform operations on them. 

Note that if you try running the following code without making any
changes, you'll get a TypeError saying you can't perform an operation
on a string and an integer.
"""

x = 5
y = "7"

# Write a print statement that combines x + y into the integer value 12

# YOUR CODE HERE

x = 6
y = 6

sum = (x) + (y)

print('The sum of {0} and {1} is {2}'.format(x, y, sum))

# Write a print statement that combines x + y into the string value 57

# YOUR CODE HERE

x = "5"
y = "7"

sum = (x) + (y)

print('The sum of strings {0} and {1} is {2}'.format(x, y, sum))