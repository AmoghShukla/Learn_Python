# Dictionary in Python
# A dictionary is an unordered collection of key-value pairs.
# Dictionaries are mutable, meaning they can be changed after creation.
# They are defined using curly braces {} with key-value pairs separated by colons.

my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
print(my_dict)

# Accessing values in a dictionary using keys
print(my_dict['name'])  # Output: Alice

# Adding a new key-value pair to the dictionary
my_dict['job'] = 'Engineer'

# Change the age value
my_dict['age'] = 26

# Find the Number of key-value pairs in the dictionary
print(len(my_dict))  # Output: 4

# Print only keys
print(my_dict.keys())  # Output: dict_keys(['name', 'age', 'city', 'job'])

# Print only values
print(my_dict.values())  # Output: dict_values(['Alice', 26, 'New York', 'Engineer'])

print(my_dict)  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York', 'job': 'Engineer'}

# Merge two Dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict1.update(dict2)
print(dict1)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Nested Dictionary
# A dictionary can contain another dictionary as a value.

nested_dict = {
    'person1': {'name': 'John', 'age': 30},
    'person2': {'name': 'Jane', 'age': 25}
}
print(nested_dict['person1']['name'])  # Output: John