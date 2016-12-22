# This will demonstrate the usage of the 'str' methods.

name = 'David'

if name.startswith('Da'):
    print('This name starts with "Da"')

if 'a' in name:
    print('This name contains an "a"')

# Find returns -1 if used to locate the positon
# of a given substring in a string
if name.find('vid') != -1:
    print('This name contains "vid" in it')

delimiter = '_*_'
countryList = ['United States', 'Ireland', 'Nigeria', 'Mexico']
print(delimiter.join(countryList))
