# Functions in Python
# Functions are reusable blocks of code that perform a specific task.
# They are defined using the def keyword, followed by the function name and parentheses.

# def greet(name):
#     print(f"Hello, {name}!")

# greet('Amogh')

# # 1) Factorial

# def factoria(num):
#     if num == 0 or num == 1:
#         return 1
#     else:
#         return num * factoria(num-1)
    
    
# n = int(input("Find factorial of: "))
# print(factoria(n)) 

# # q) How to Access a global variable inside a function

# x = 10  # Global variable
# def print_global():
#     a = x 
#     a -= 5
#     print(a)  # Accessing the global variable
# print(x)
# print_global()  # Output: 5
# print(x)  # Output: 5

# # Note: If you want to modify a global variable inside a function, you need to use the global keyword.

# # Default Arguments
# def greet(name="Guest"):
#     print(f"Hello, {name}!")
# greet()  # Output: Hello, Guest!
# greet("Alice")  # Output: Hello, Alice!

# Pallindrome Number
def is_palindrome(num):
    return str(num) == str(num)[::-1]
n = input("Enter an input to check if it's a palindrome: ")
print(is_palindrome(n))








def check_palindrome(n):
    return list(str(n)) == list(str(n)[::-1]) # String because we can reverse a string using slicing [::-1] but we cannot reverse an integer