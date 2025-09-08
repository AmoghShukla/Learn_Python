# Difference Bewteen Set and Dictionary in Python
# Set is an unordered collection of unique elements, 
# while a dictionary is an unordered collection of key-value pairs.
# Sets are defined using curly braces {} or the set() function,
# whereas dictionaries are defined using curly braces {} with key-value pairs separated by colons.

# a = set()
# b = {}
# print(type(a))
# print(type(b))

x = {'Vaishnavi', 1, 2, 3, 4, 5, 'Mayur'}
x.pop()
print(x)

x.pop()
print(x)

x.pop()
print(x)

x.pop()
print(x)

x.pop()
print(x)

x.pop()
print(x)

x.pop()
print(x)

# Output:
# {1, 2, 3, 4, 5, 'Mayur'}
# {2, 3, 4, 5, 'Mayur'}
# {3, 4, 5, 'Mayur'}
# {4, 5, 'Mayur'}
# {5, 'Mayur'}
# {'Mayur'}
# set()


# Remove and Discard in Sets

# Remove in python is used with sets to remove a specific element from the set.
# If the element is not found, it raises a KeyError.

# Discard in python is used with sets to remove a specific element from the set.
# If the element is not found, it does nothing and does not raise an error.

a = {1, 2, 3, 4, 5}
a.remove(3)
print(a)  # Output: {1, 2, 4, 5}

a.discard(4)
print(a)  # Output: {1, 2, 5}

a.discard(10)  # Does nothing, no error
print(a)  # Output: {1, 2, 5}