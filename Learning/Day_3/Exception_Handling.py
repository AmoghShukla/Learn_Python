# Exception Handling in Python
# Exception handling is a way to gracefully handle errors and exceptions that may occur during the execution of a program.
# It allows you to catch and respond to errors without crashing the program.
# The main keywords used in exception handling are try, except, else, and finally.

# Basic Structure of Exception Handling
try:
    a = 10/0
except ZeroDivisionError as e:
    print("Error: Division by zero is not allowed.", e)
except Exception as e:
    print("An error occurred:", e)
else:
    print("No errors occurred. Result is:", a)
finally:
    print("Execution completed.")