# This will demonstrate the use of document strings, or DocStrings, for short.
# Using docstrings will help document the program better and makes it easier
# to understand.

def print_max(x, y):
    '''Prints the maximum of two numbers.

    The two values must be integers.'''
    # convert to integers, if possible
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')

print(print_max.__doc__)
print_max(3,5)
