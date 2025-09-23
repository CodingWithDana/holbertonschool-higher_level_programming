from abc import ABC, abstractmethod
# create an abstract class Animal using ABC package
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

# create two subclasses: Dog & Cat
class Dog(Animal):
    super().sound("Bark")
    
class Cat(Animal):
    super().sound("Meow")
