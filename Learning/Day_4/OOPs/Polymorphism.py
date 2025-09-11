# Polymorphism in Python
# Polymorphism is a core concept in Object-Oriented Programming (OOP) that allows methods to do different things based on the object it is acting upon, even though they share the same name.
# This means that a single function or method can work in different ways depending on the context,
# such as the type of object it is called on or the number and types of arguments passed to it.
# Polymorphism is used to increase the flexibility and reusability of code, allowing for more dynamic and adaptable programs.
# In OOPs the same method, operators, or functions behave differently depending on the object and Datatype.

# Types of Polymorphism:
# 1. Compile-time Polymorphism (Static Polymorphism): This type of polymhism is achieved through method overloading and operator overloading. The method to be invoked is determined at compile time based on the method signature (name and parameters).
# 2. Run-time Polymorphism (Dynamic Polymorphism): This type of polymhism is achieved through method overriding. The method to be invoked is determined at runtime based on the object type.
# Method Overloading: Method overloading is a feature that allows a class to have multiple methods
# with the same name but different parameters (different type or number of parameters). Python does not support method overloading directly, but it can be achieved using default arguments or variable-length arguments.

# Python Does not Support Overloading Because it is a Dynamically Typed Language and it does not check the type of arguments at compile time.
# It will Directly take the last defined method if we define multiple methods with the same name.
# For Example:
class A:
    def add(self, a, b):
        return a + b
    
    def add(self, a, b, c=5): # This will override the previous add method
        return a + b + c
obj = A()
print(obj.add(2, 3)) # This will call the second add method and output