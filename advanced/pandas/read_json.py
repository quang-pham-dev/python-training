# Read JSON
# Big data sets are often stored, or extracted as JSON.
# JSON is plain text, but has the format of an object, and is well known in the world of programming,
# including Pandas.
import os
import pandas as pd

try:
    file_path = os.path.join("advanced", "pandas", "data.json")
    df = pd.read_json(file_path)
    # print(df.to_string())
    # Print the last 5 rows of the DataFrame:
    # Print the first 5 rows of the DataFrame:
    print(df.head())
    print(df.tail()) 
    # Get a quick overview by printing the first 10 rows of the DataFrame:
    print(df.head(10))
    # Print information about the data:
    print(df.info()) 
except FileNotFoundError:
    print("File not found.")
except pd.errors.ParserError:
    print("Error parsing JSON file.")
except Exception as e:
    print("An error occurred:", str(e))

# Explanation:
# - The code is wrapped in a try-except block to handle any potential exceptions that may occur during execution.
# - The FileNotFoundError exception is caught if the specified file is not found.
# - The pd.errors.ParserError exception is caught if there is an error parsing the JSON file.
# - The general Exception class is used to catch any other unexpected exceptions.
# - If any exception is caught, an appropriate error message is printed.


# Assuming the Python dictionary is already defined
my_dict = {
    "Name": ["John", "Alice", "Bob"],
    "Age": [25, 30, 35],
    "City": ["New York", "London", "Paris"],
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(my_dict)

# Print the DataFrame
print(df)
