from abc import ABC, abstractmethod

# create an abstract class Animal using ABC package
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

# subclass Dog
class Dog(Animal):
    def sound(self):
        return "Bark"

# subclass Cat
class Cat(Animal):
    def sound(self):
        return "Meow"
