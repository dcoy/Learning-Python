# This is an exercise for learning about 'functions'
# This function will take any word and 'right_justify' it
# so the last letter is at column 70

def right_justify(s):
    # Get length of 's'
    s_rght = 70 - len(s)
    # Shift 's' 65 spaces
    print(s_rght * ' ' + s)

right_justify("David")
