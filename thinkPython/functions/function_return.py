# This will demonstrate the return statement to break out of a function.
# Optionally, you can return a value from the function.

def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'The numbers are equal.'
    else:
        return y

print(maximum(2,3))
print(maximum(3,2))
print(maximum(10,10))
