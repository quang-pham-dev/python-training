# Method Over Riding
# Method overriding happens when a child class has a method with the same name as a method in its parent class.
# The child class can then give its own version of the method, which is used instead of the parent's version when
# the method is called on an instance of the child class. This lets the child class customize how the method works
# to fit its needs.
class Animal:
    def make_sound(self):
        print("Generic animal sound")


class Dog(Animal):
    def make_sound(self):
        print("Woof!")


class Cat(Animal):
    def make_sound(self):
        print("Meow")


dog = Dog()
cat = Cat()

# Calling the overridden method
dog.make_sound()  # Woof!
cat.make_sound()  # Meow
