# kwargs in Python
# Kwargs (short for keyword arguments) allow you to pass a variable number of keyword arguments to a function.
# They are useful when you want to create functions that can handle an arbitrary number of named inputs
# They are defined using two asterisks (**) before the parameter name in the function definition.
# It is a keyword argument meaning the order of arguments does not matter.
# The arguments are passed as a dictionary where the keys are the argument names and the values are the argument values.

def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")
print(display_info(name="Amogh", age=21, city="Pune", profession='Student', message="Hello World!"))


