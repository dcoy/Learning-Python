# This file will demonstrate the use of the 'for' statement. It will show
# the flow based on 'decisions' made by these statements

# Using the 'for...in' statement -- this statement iterates over a sequence of
# objects.  'Else' is optional here.

for i in range(1, 5):
    # will print each number from 1 - 4
    print(i)
else:
    print('The for loop is over!\n')

for j in list(range(9)):
    # Adding list to range will result in 0-8
    print(j)
else:
    print('This list-loop is done')
