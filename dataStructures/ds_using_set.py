# This will demonstrate the usage of the 'set' data structure.

names = set(['David','Alex', 'Brian', 'Eric'])

print("\nprint('David' in names)")
print('David' in names)

print("\nprint('John') in names")
print('John') in names

namesC = names.copy()
namesC.add('Mason')
print("\nnamesC.issuperset(names)")
namesC.issuperset(names)

print("\nnames.remove('Alex')")
names.remove('Alex')

print("\nnames & namesC")
print(names & namesC) # OR names.intersection(namesC)
