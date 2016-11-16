# This exercise will draw a 4x4 grid with '+' and '-'
# like so:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +

# Print twice first
def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_beam():
    print('|')
