# This will demonstrate the usage of the 'set' data structure.

names = set(['David','Alex', 'Brian', 'Eric'])

print('David' in names)
print('John') in names

namesC = names.copy()
namesC.add('Mason')

print(namesC.issuperset(names))

names.remove('Alex')

print(names & namesC) # OR names.intersection(namesC)
