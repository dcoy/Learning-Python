# This will demonstrate the usage of the 'references' in data structures.

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
