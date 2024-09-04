# Abstraction is the process of hiding the implementation details of a class and showing only the necessary information to the user.
# It is a fundamental concept in object-oriented programming (OOP) that helps in managing complexity by focusing on essential features and ignoring unnecessary details.

# Abstraction allows us to create more modular and reusable code. It helps in reducing complexity and makes the code more understandable and maintainable.

# In Python, abstraction can be achieved using abstract classes and interfaces.


# Abstract Class
# An abstract class is a class that cannot be instantiated directly.
# It is designed to be subclassed, and it can contain both abstract and concrete methods.

# Abstract methods are declared but have no implementation. Subclasses must provide an implementation for these methods.

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass  # Abstract method to be implemented by subclasses


class Dog(Animal):
    # If we don't implement the abstract method, we will get an error
    # TypeError: Can't instantiate abstract class Dog without an implementation for abstract method 'make_sound'
    def make_sound(self):
        return "Woof!"


class Cat(Animal):
    def make_sound(self):
        return "Meow!"


# Usage
dog_instance = Dog()
cat_instance = Cat()

print(dog_instance.make_sound())  # Output: Woof!
print(cat_instance.make_sound())  # Output: Meow!

# In this example, the Animal class is an abstract class that defines an abstract method make_sound.
# The Dog class is a subclass of Animal and provides an implementation for the make_sound method.
