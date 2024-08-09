import math  # built-in
import mymodule


def main():
    x = 16
    print(f"Square root of {x} is {math.sqrt(x)}")
    print(f"Factorial of {x} is {math.factorial(x)}")
    y = 10
    z = 5
    print("==================================")
    print(f"{y} + {z} = {mymodule.add(y, z)}")
    print(f"{y} - {z} = {mymodule.subtract(y, z)}")
    print(f"{y} * {z} = {mymodule.multiply(y, z)}")
    print(f"{y} / {z} = {mymodule.divide(y, z)}")
    print("==================================")

    print(f"API Key: {mymodule.api_key}")
    print(f"Full API URL: {mymodule.get_full_api_url('users')}")


if __name__ == "__main__":
    main()
