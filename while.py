# This file will demonstrate the use of the 'while' statement. It will show
# the flow based on 'decisions' made by these statements

# Using the 'while' statement -- while the condition is true, execute the block statements
# 'else' process another block statement.  'Else' is optional.

# Variable declaration
number = 23
running = True

while running:
    guess = int(input('Enter an integer: '))

    if guess == number:
        print('Congratulations, you guess it!')
        # while loop will stop
        running = False
    elif guess < number:
        print('No, it is a bit higher')
    else:
        print('No, it is a bit lower')

else:
    print('This "loop" is finished!')

print('Done')
