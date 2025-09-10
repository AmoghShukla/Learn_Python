# Decorators in Python
# Decorators are a way to modify or enhance the behavior of functions or methods.
# They are often used for logging, access control, caching, and more.

# Why use Decorators?
# Code Reusability
# Separation of Concerns
# Enhanced Readability

# Every Decorator function has only one argument that is the function to be decorated.
# Every Decorator has only one wrapper function that wraps the original function.
# The wrapper function can take any number of arguments and keyword arguments.

def my_decorator(func):
    def wrapper(*args, **kwargs): # Wrapper function
        print("Something is happening before the function is called.")
        func(*args, **kwargs)
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")
say_hello()  # Output: Something is happening before the function is called. Hello! Something is happening after the function is called.

