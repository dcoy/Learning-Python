# This will demonstrate the usage of the 'slice' operator.

# How this works: first, we are using indexes to get individuals items in a sequence.
# This is also called the 'subscription operation'.  Index can also be a negative number,
# which will calculate from the end of the sequence. Slice is used by specifying the name
# of the sequence, followed by an optional pair of numbers seperated by a colon.  The numbers
# are option, but the colon is required.  [firstNum:lastNum] firstNum refers to the start of
# of the index is the position which slicing will occur and lastNum is where the slice stops.

shoppingList = ['apple', 'banana', 'spinach', 'carrots', 'eggs']

name = 'David'

# Indexing or 'Subscription' operation #
print('Item 0 is', shoppingList[0])
print('Item 1 is', shoppingList[1])
print('Item 2 is', shoppingList[2])
print('Item 3 is', shoppingList[3])
print('Item -1 is', shoppingList[-1])
print('Item -2 is', shoppingList[-2])
print('Item -3 is', shoppingList[-3])
print('Character 0 is', name[0])

# Slicing on a list #
print('Item 1 to 3 is', shoppingList[1:3])
print('Item 2 to end is', shoppingList[2:])
print('Item 1 to -1 is', shoppingList[1:-1])
print('Item start to end is', shoppingList[:])

# Slicing on a string #
print('characters 1 to 3 is', name[1:3])
print('characters 2 to end is', name[2:])
print('characters 1 to -1 is', name[1:-1])
print('characters start to end is', name[:])

# Slice with a third identifier, step #
print('every 2 characters from 1 to 5 is', name[1:5:2])
print('every 3 characters is', name[::3])
