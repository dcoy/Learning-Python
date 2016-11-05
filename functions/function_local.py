# This will demonstrate a function variables within the local scope.

# Global variable declaration
x = 50

def func(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)

func(x)
print('x is still', x)
