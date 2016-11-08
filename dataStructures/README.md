## Data Structures

Data structures are *structures* that hold some type of *data* together.  In short, they store a collection of related data.

There are four built-in data structures in Python -- list, tuple, dictionary, and set.

#### List

A *list* is a data structure that holds an ordered collection of items and you can store a *sequence* of items in a list.  The list items should be enclosed in square brackets, `[]`.  This will specify to Python that a list is being created.  Lists are a *mutable* data type, meaning they can be altered by adding, deleting, or modifying the contents of the list.  Run `help(list)` to display all properties of the *list* data type.

#### Tuple

Tuples are used to hold together multiple objects.  Tuples are similar to lists, but not as extensive as lists are.  Tuples are *immutable*, meaning they cannot be modified.  Tuples are defined by specifying items separated by commas within an option pair of parentheses, `()`. Run `help(tuple)` to display all properties of the tuple data type.

#### Dictionary

A *dictionary* is similar to an address-book where contacts are listed by their name and associated with an address, phone number, etc.  The *keys* are the names of the individuals/businesses and the *values* are the details associated with those individuals/businesses.  

Keys can only be immutable objects(like strings), however, values can be immutable and mutable objects(strings and integers).  Key-value pairs are specified in a dictionary in this manner: `dict = {key1: value1, key2: value2}`.  Key-value pairs in a dictionary are not ordered in any specific manner.  If the intention is to have a specific order, the data must be sorted prior to adding them to a dictionary.  Run `help(dict)` to display all properties of the dictionary data type.

#### Sequence

Lists, tuples and strings are examples of sequences.  The major feature of sequences are *membership tests*, the `in` and `not in` expressions, and *indexing operations*, which allows you to fetch a particular item in the sequence directly.

The three types of sequences also have a *slicing* operation which will allow us to retrieve part of the sequence.  Run `help(slice)` to display all properties of the slice operation.

#### Set

A *set* is an unordered collection of simple objects.  These are used when an object within a collection is more important than the order or amount it occurs.  By using sets, membership tests can be run, regardless if it's a subset of another set.  Run `help(set)` to display all properties of the set data structure.

#### References

When an object is created and assigned to a variable, the variable is only referring to the object and doesn't represent it.  This is called *binding* the name to the object.  There's a subtle effect due to references that need to known.

#### Strings

Strings are objects that have methods that can check part of a string as well as strip spaces out of the string.  They're all objects of the class `str`.  Run `help(str)` to display all methods of the string data type.
