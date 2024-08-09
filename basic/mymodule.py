def say_hello(name):
    return f"Hello, {name}!"


def say_goodbye(name):
    return f"Good bye, {name}!"
  
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"


api_key = "your_api_key_here"
api_url = "https://api.example.com"
timeout = 30


def get_full_api_url(endpoint):
    return f"{api_url}/{endpoint}"

