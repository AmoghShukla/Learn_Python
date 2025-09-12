# Abstraction in Python
# Abstraction is one of the fundamental concepts of Object-Oriented Programming (OOP). It refers to the concept of hiding the complex implementation details and showing only the essential features of the object.
# Abstraction helps in reducing programming complexity and effort. It allows the programmer to focus on interactions
# at a higher level without needing to understand all the details of the lower-level implementation.
# In Python, abstraction can be achieved using abstract classes and interfaces. An abstract class is a class that cannot be instantiated and is meant to be subclassed. It can contain abstract methods (methods without implementation) that must be implemented by any subclass.
# Python provides the 'abc' module to define abstract base classes.
# Example of Abstraction using Abstract Base Class

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius
# Creating objects of the subclasses
rectangle = Rectangle(5, 10)
circle = Circle(7)
# Displaying the area and perimeter of the shapes
print("Rectangle Area:", rectangle.area())
print("Rectangle Perimeter:", rectangle.perimeter())
print("Circle Area:", circle.area())
print("Circle Perimeter:", circle.perimeter())