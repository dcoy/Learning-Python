# This file will demonstrate the use of the 'continue' statement. It will show
# the flow based on 'decisions' made by these statements

# Using the 'continue' statement -- used to tell Python to skip the rest of the
# statements and to continue through the next iteration of the loop.

while True:
    s = input('Enter something here: ')
    if s == 'quit':
        print('Quitting...')
        break
    if len(s) < 3:
        print('Too small')
        continue
    print('Input is of sufficient length')
    # Do other processing here...
