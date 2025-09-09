# Args in Python
# Args (short for arguments) allow you to pass a variable number of non-keyword arguments to a function.
# Args are useful when you want to create functions that can handle an arbitrary number of inputs.
# They are defined using an asterisk (*) before the parameter name in the function definition.
# It is a positional argument meaning the order of arguments matters.

def sum_total(*args):
    total = 0
    for i in args:
        total += i
    return total
print(sum_total(1, 2, 3))  # Output: 6
print(sum_total(5, 10, 15, 20))  # Output: 50


def greet(*name):
    for i in name:
        print(f"Hello, {i}!")

greet('Amogh', 'Mayur', 'Aditya')