# My shopping list
shoppingList = ['apple', 'banana', 'spinach', 'carrots', 'eggs']

print('I have', len(shoppingList), 'items to purchase.')

print('These items are:', end=' ')
for item in shoppingList:
    print(item, end=' ')

print('\nI also have to buy brown rice!')
shoppingList.append('brown rice')
print('My shopping list is now', shoppingList)

print('\nI will sort my list now')
shoppingList.sort()
print('Shopping list sorted:', shoppingList)

print('\nThe first item I will buy is', shoppingList[0])
oldItem = shoppingList[0]
print('I bought the', oldItem)
print('My shopping list is now', shoppingList)
