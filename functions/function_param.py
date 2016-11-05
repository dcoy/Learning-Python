# This will demonstrate a function that accepts parameters.
# Parameters are values that you supply to the function so the function
# can do something utilizing those values.  Parameters are specified within
# the parenthesis in the function definition, separated by commas.  When
# calling the function, simply supply the values in the same way.

# Variable declaration
x = 3
y = 4

def print_max(a, b):
    if a > b:
        print(a, 'is maximum')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is maximum')

# directly pass literal values
print_max(5, 10)
# pass defined variables as arguments
print_max(x, y)
