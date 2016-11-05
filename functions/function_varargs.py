# This will demonstrate a function that can take any number of
# parameters.  This is achieved using stars or asterisks.
# How this works: when declaring a 'starred' parameter such as *numbers,
# all positional arguments from there until the end are collected as
# a tuple names 'numbers'.
# When declaring a double-starred parameter such as **phonebook, then
# all keyword arguments from there until the end are collected
# as a dictionary called 'phonebook'.

def total(a=5, *numbers, **phonebook):
    print('a', a)

    # iterate through all the items in tuple
    for single_item in numbers:
        print('single_item', single_item)

    # iterate through all the items in a dictionary
    for first_part, second_part in phonebook.items():
        print(first_part,second_part)

print(total(10,1,2,3,Jack=1123,John=2231,David=1560))
