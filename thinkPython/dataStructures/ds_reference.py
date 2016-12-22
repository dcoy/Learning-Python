# This will demonstrate the usage of the 'references' in data structures.
# How this works:  if you want to make a copy, you will need to 'slice' the list
# and cannot simply assign it to a new variable.  This creates a reference by which
# the new variable will reference the original variable and return the same
# objects that the origina variable references.  Example below:

print('Variable Assignment')
shoppingList = ['apple', 'banana', 'spinach', 'carrots', 'eggs']
# creating another name pointing to the same object
newShoppingList = shoppingList

# Bought the apple, so let's remove it
del shoppingList[0]

print('shoppingList is', shoppingList)
print('newShoppingList is', newShoppingList)
# this prints the same items in the list as 'apple' was removed

print('Copying by making a full slice')
# Making the copy with a full slice
newShoppingList = shoppingList[:]
# Removing the first item in the list
del newShoppingList[0]

print('shoppingList is', shoppingList)
print('newShoppingList is', newShoppingList)
