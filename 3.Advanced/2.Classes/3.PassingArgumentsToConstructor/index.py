class Person:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location

    def user_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Location: {self.location}")


quang_pham = Person("Quang Pham", 20, "Da Nang")
quang_pham.user_info()

david = Person("David", 26, "USA")
david.user_info()

alex = Person("alex", 19, "China")
alex.user_info()
