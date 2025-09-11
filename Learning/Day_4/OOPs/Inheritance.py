# Inheritance in Python
# Inheritance is a fundamental concept in Object-Oriented Programming (OOP) that allows a class (child class) to inherit attributes and methods from another class (parent class).
# This promotes code reusability and establishes a hierarchical relationship between classes.
# Inheritance is used to create a new class that is a modified version of an existing class. The new class can add new attributes and methods or override existing ones.

# Types of Inheritance:
# 1. Single Inheritance: A child class inherits from a single parent class.
# 2. Multiple Inheritance: A child class inherits from multiple parent classes.
# 3. Multilevel Inheritance: A child class inherits from a parent class, which in turn inherits from another parent class.
# 4. Hierarchical Inheritance: Multiple child classes inherit from a single parent class.
# 5. Hybrid Inheritance: A combination of two or more types of inheritance.

# Self Keyword: refers to the current instance of the class and is used to access variables and methods associated with the current object.
class Student:

    def __init__(self, name, roll, std, gender): 
        self.name = name
        self.roll = roll
        self.std = std
        self.gender = gender
    
    def Personal_info(self):
        print("My Name is ", self.name, ".\nMy roll No. is ", self.roll, ". \nI am in std : ", self.std, ".\nMy Gender is ", self.gender)

class College(Student):

    clgname = "IIT"
    clgcode = "IIT2023"
       
    def read_val(self):
        return self.clgname, self.clgcode

College1 = College("Amogh", "2022B28022004", "4th year", "Male")
print(College1.Personal_info())

# Multilevel Inheritance

class A:
    def feature1(self):
        print("Feature 1 is working")
    
    def feature2(self):
        print("Feature 2 is working")
class B(A):
    def feature3(self):
        print("Feature 3 is working")
    
    def feature4(self):
        print("Feature 4 is working")

class C(B):
    def feature5(self):
        print("Feature 5 is working")
    
    def feature6(self):
        print("Feature 6 is working")
c = C()
c.feature1()
c.feature3()
c.feature5()

# Multiple Inheritance
class A:
    def feature1(self):
        print("Feature 1 is working")
class B:
    def feature2(self):
        print("Feature 2 is working")
class C(A, B):
    def feature3(self):
        print("Feature 3 is working")

c = C()
c.feature1()  
c.feature2()
c.feature3()

# Java Does not support multiple inheritance to avoid ambiguity
# Python supports multiple inheritance

# Hierarchical Inheritance  
class A:
    def Father(self):
        print("Father is working")
class B(A):
    def Mother(self):
        print("Mother is working")
class C(A):
    def Son(self):
        print("Son is working")

c1 = B()
c1.Father()
c1.Mother()

c2 = C()
c2.Father()
c2.Son()
