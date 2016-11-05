# This file will demonstrate the use of the 'if' statement. It will show
# the flow based on 'decisions' made by these statements

# Using the 'if' statement -- 'if' the condition is true, execute the block statements
# 'else' process another block statement(else-block).  'Else' is optional.

# Variable declaration
number = 23
# Accept user input and store it in the variable 'guess'
guess = int(input('Enter an integer: '))

if guess == number:
    # New block starts here
    print('Congrats, you guess it!')
    print('(but you did not win anything.)')
    # New block ends right here
elif guess < number:
    # Start another block
    print('No, it is a bit higher than that')
else:
    print('No, it is a bit lower than that')

print('Good guess though!')
