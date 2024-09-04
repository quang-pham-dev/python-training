# To create a class, use the keyword class:
class FirstClass:
    x = 5


# Create Object
# Now we can use the class named FirstClass to create objects:
p1 = FirstClass()
print(f"Object p1: {p1.x}")


# Create a class named Person, use the __init__() function to assign values for name and age:
# Note: The __init__() function is called automatically every time the class is being used to create a new object.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("Quang", 34)

print(p1.name)
print(p1.age)


# The __str__() Function
# The __str__() function controls what should be returned when the class object is represented as a string.
# If the __str__() function is not set, the string representation of the object is returned:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"


p1 = Person("Quang", 34)

print(p1)

# Object Methods
# Objects can also contain methods. Methods in objects are functions that belong to the object.
# Let us create a method in the Person clas


class Person:
    def __init__(user_info, name, age):  # constructor
        user_info.name = name
        user_info.age = age

    def intro(self):
        print("Hello my name is " + self.name)


p1 = Person("Quang", 34)
p1.age = 35
p1.name = "Kaka"
p1.intro()


# Delete Objects
# You can delete objects by using the del keyword:
class Person:
    def __init__(user_info, name, age):  # constructor
        user_info.name = name
        user_info.age = age

    def intro(self):
        print("Hello my name is " + self.name)


p1 = Person("David", 34)
del p1.age
p1.intro()


# Inheritance
class Person:
    def __init__(user_info, name, age):  # constructor
        user_info.name = name
        user_info.age = age

    def intro(self):
        print("Hello my name is " + self.name, f"I'm {self.age} years old")


p1 = Person("David", 34)
p1.intro()


class Student(Person):
    pass


x = Student("Quang", 22)
x.intro()


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def intro(self):
        print(self.firstname, self.lastname)


class Student(Person):
    # Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)


x = Student("Quang", "Pham")
x.intro()


# Use the super() Function
# Python also has a super() function that will make the child class inherit all the methods and properties from its parent:
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def intro(self):
        print("My name is " + self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname, year):
        # By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.
        super().__init__(fname, lname)
        self.graduation_year = year


x = Student("Quang", "Pham", 2024)
x.intro()
print(f"and I graduated in : {x.graduation_year}")


# Add Methods
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def intro(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduation_year = year

    # Add Methods
    def congrats(self):
        print(
            "Congratulation to",
            self.firstname,
            self.lastname,
            "on graduating in",
            self.graduation_year,
        )


x = Student("Quang", "Pham", 2014)
x.congrats()
