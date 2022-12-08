# Homework 7: OOP - The 4 Pillars

# ABSTRACTION
# Import Abstract Base Classes module
from abc import ABC, abstractmethod


# Define abstract class GeometricShape
class GeometricShape(ABC):
    # fields
    PI = 3.14

    # methods
    @abstractmethod
    def area(self):
        pass

    def describe(self):
        print("Most likely, I have corners.")

    """ OR
    @classmethod
    def decribe(cls):
        print("Most likely, I have corners.")
    """


# INHERITANCE
class Square(GeometricShape, ABC):
    # constructor with private side
    def __init__(self, side):
        self.__side = side

# ENCAPSULATION

    @property
    def side(self):
        return self.__side

    # Getter method
    @side.getter
    def side(self):
        print(f'Getting side: {self.__side}')
        return self.__side

    # Setter method
    @side.setter
    def side(self, new_side):
        self.__side = new_side
        print(f'Setting side to {self.__side}')

    # Deleter method
    @side.deleter
    def side(self):
        self.__side = None
        print('Side deleted')

    def area(self):
        print(f'The area is {self.__side ** 2}')
        return self.__side ** 2


class Circle(GeometricShape, ABC):
    # constructor
    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    # Getter method
    @radius.getter
    def radius(self):
        print(f'Getting radius: {self.__radius}')
        return self.__radius

    # Setter method
    @radius.setter
    def radius(self, new_radius):
        self.__radius = new_radius
        print(f'Setting radius to {self.__radius}')

    # Deleter method
    @radius.deleter
    def radius(self):
        self.__radius = 0
        print('Radius deleted')

    def area(self):
        print(f'The area is {round((self.PI * self.__radius) ** 2, 2)}')
        return round((self.PI * self.__radius) ** 2, 2)

# POLIMORFISM
    def describe(self):
        print("I don't have corners")


square = Square(2)
square.describe()
square.area()
square.side
square.side = 7
square.side
del square.side

print("-------------------")

circle = Circle(3)
circle.describe()
circle.radius
circle.area()
circle.radius = 4
circle.radius
circle.area()
del circle.radius
circle.radius
