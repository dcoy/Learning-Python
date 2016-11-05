# This file will demonstrate the use of the 'break' statement. It will show
# the flow based on 'decisions' made by these statements

# Using the 'break' statement -- 'break' is used to stop the execution of a looping
# statement, even if is hasn't become 'False' or the iteration hasn't completed.
# If used to break out of a 'for' or 'while' loop, the corresponding 'else' block
# is not executed.

while True:
    s = input('Enter anything here: ')
    if s == 'quit':
        break
    print('Length of string is', len(s))
print('This loop is finished')
