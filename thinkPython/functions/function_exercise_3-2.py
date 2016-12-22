# This is an exercise for learning about 'functions'

# This function will take any word and 'right_justify' it
# so the last letter is at column 70

def right_justify(s):
    # Get length of 's'
    s_rght = 70 - len(s)
    # Shift 's' 65 spaces
    print(s_rght * ' ' + s)

right_justify("David")

# Time to print some spam

def do_twice(func, arg):
    func(arg)
    func(arg)

def print_twice(arg):
    print(arg)
    print(arg)

def do_four(func, arg):
    do_twice(func, arg)
    do_twice(func, arg)

do_twice(print_twice, 'spam')
print('\n')
do_four(print_twice, 'spam')
