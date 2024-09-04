# 2. __init__ is a constructor which allow us to create variables in class.


class Person:
    def __init__(self):
        # 👇 Instance Variables
        self.name = "Quang Pham"
        self.age = 20
        self.location = "USA"

    def user_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Location: {self.location}")


quang_pham = Person()
quang_pham.user_info()
