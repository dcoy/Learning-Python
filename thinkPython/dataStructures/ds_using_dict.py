# This will demonstrate the usage of the 'dictionary' data structure.
# 'ab' is short for address book

ab = {
    'David': 'name@example.com',
    'Name2': 'name2@example.org',
    'Name3': 'name3@example.net',
    'Name4': 'name4@example.xyz'
}

print("David's address is", ab['David'])

# Delete a key-value pair
del ab['Name3']

print('\nThere are {} contacts in the address book\n'.format(len(ab)))

for name, address in ab.items():
    print('Contact {} at {}'.format(name, address))

# Adding a key-value pair
ab['Name5'] = 'name5@example.biz'

if 'Name5' in ab:
    print("\nName5's address is", ab['Name5'])
