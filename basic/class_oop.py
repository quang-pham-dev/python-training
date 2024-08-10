# Define a class
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"


# Create an object
my_dog = Dog("Buddy", 5)
print(my_dog.bark())  # Outputs "Buddy says woof!"


# Class attributes and methods
# Define a class with class attributes
class Car:
    wheels = 4  # Class attribute

    def __init__(self, make, model):
        self.make = make  # Instance attribute
        self.model = model  # Instance attribute

    def description(self):
        return f"This car is a {self.make} {self.model} with {Car.wheels} wheels."


# Create objects
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")

print(car1.description())  # Outputs "This car is a Toyota Camry with 4 wheels."
print(car2.description())  # Outputs "This car is a Honda Civic with 4 wheels."


# Inheritance and method overriding
# Define a parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"


# Define a child class
class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow!"


# Create an object of the child class
my_cat = Cat("Whiskers")
print(my_cat.speak())  # Outputs "Whiskers says meow!"


# Encapsulation and private attributes
# Encapsulation example
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        if amount > self.__balance:
            return "Insufficient funds"
        self.__balance -= amount
        return self.__balance

    def get_balance(self):
        return self.__balance


# Create an account object
account = Account("Quang", 100)
account.deposit(50)
print(account.get_balance())  # Outputs 150
