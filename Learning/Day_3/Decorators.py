# # Decorators in Python
# # Decorators are a way to modify or enhance the behavior of functions or methods.
# # They are often used for logging, access control, caching, and more.

# # Why use Decorators?
# # Code Reusability
# # Separation of Concerns
# # Enhanced Readability

# # Every Decorator function has only one argument that is the function to be decorated.
# # Every Decorator has only one wrapper function that wraps the original function.
# # The wrapper function can take any number of arguments and keyword arguments.

# # def my_decorator(func):6
# #     def wrapper(*args, **kwargs): # Wrapper function
# #         print("Something is happening before the function is called.")
# #         func(*args, **kwargs)
# #         print("Something is happening after the function is called.")
# #     return wrapper

# # def say_hello():
# #     print("Hello!")
# # say_hello()  # Output: Something is happening before the function is called. Hello! Something is happening after the function is called.

# # @my_decorator
# # def say_something(something):
# #     print(something)
# # say_something("Max is Midget")

# # Single Wrapper function example
# def my_d(a):
#     def wrapper():
#         print("Past")
#         a()
#         print("Future")
#     return wrapper

# @my_d
# def ab():
#     print("Present")
# ab()


# # Two Wrapper function example
# def decorator1(func):
#     def wrapper1():
#         print("Decorator 1 - Before")
#         func()
#         print("Decorator 1 - After")
#     return wrapper1

# def decorator2(func):
#     def wrapper2():
#         print("Decorator 2 - Before")
#         func()
#         print("Decorator 2 - After")
#     return wrapper2

# @decorator1
# @decorator2
# def my_function():
#     print("Hello, World!")
# my_function()


# # Three Wrapper Function
# def decorator1(func):
#     def wrapper1():
#         print("W1")
#         func()
#         print("W2")
#     return wrapper1

# def decorator2(func):
#     def wrapper2():
#         print("X1")
#         func()
#         print("X2")
#     return wrapper2

# def decorator3(func):
#     def wrapper3():
#         print("Y1")
#         func()
#         print("Y2")
#     return wrapper3

# @decorator1
# @decorator2
# @decorator3
# def say_name():
#     print("Hii Amogh")
# say_name()


# # Convert a Lowercase string to Uppercase using Decorators
# def uppercase_decorator(func):
#     def wrapper():
#         original_string = func()
#         uppercased = original_string.upper()
#         return uppercased
#     return wrapper

# @uppercase_decorator
# def low_ans():
#     return "max is gay"
# print(low_ans())



# # Addition of two numbers by using decorators
# def decorator(func):
#     def wrapper(num1, num2):
#         c = num1 + num2
#         return 'Addition of ' + str(num1) + " And " + str(num2) + " is " + str(c)
#     return wrapper

# @decorator
# def calc(a, b):
#     return a, b
# a = int(input("Num1 : "))
# b = int(input("Num2 : "))
# print(calc(a, b))



# # Square of a number using decorators
# def decorator(func):
#     def wrapper(num):
#         sq = num*num
#         return 'Square of ' + str(num) + " is " + str(sq)
#     return wrapper

# @decorator
# def calc(a):
#     return a
# a = int(input("Num1 : "))
# print(calc(a))


# # Factorial of a number using decorators
# def fact(func):
#     def wrapper(num):
#         if num == 0 or num == 1:
#             return 1
#         else:
#             return num * wrapper(num-1)
#     return wrapper

# @fact
# def calc(n):
#     return n
# n = int(input("Find factorial of: "))
# print(calc(n))



# Create a Login Authentication System using decorators
database = {}

def Auth(func):
    def wrapper(username, password):
        db1 = database.get('Username')
        db2 = database.get('Password')
        if username == db1 and password == db2:
            return "Congratulations! You are logged in."
        else:
            return "Wrong Username/Password"
    return wrapper


print("Welcome to Login Page")
val = int(input("1) Login\n2) SignUp\nChoose an option: "))

@Auth
def Credentials(user, password):
    return "Login Authentication Successful"

def set_Credentials(user, password):
        database['Username'] = user
        database['Password'] = password
        return "Credentials Set Successfully"

if val == 1:

    user = input("Enter Your Username to Login : ")
    password = input("Enter Your Password to Login : ")
    print(Credentials(user, password))
    

elif val == 2:

    cred1 = input("Enter Your Username : ")
    cred2 = input("Enter Your Password : ")
    print(set_Credentials(cred1, cred2))

    print("\n--- Now Login with your new credentials ---")
    user = input("Enter Your Username to Login : ")
    password = input("Enter Your Password to Login : ")
    print(Credentials(user, password))

else:
    print("Wrong Input Detected")

