# File handling is an important part of any web application.
# Python has several functions for creating, reading, updating, and deleting files.
# File Handling
# The key function for working with files in Python is the open() function.
# The open() function takes two parameters; filename, and mode.
# There are four different methods (modes) for opening a file:

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists

# In addition you can specify if the file should be handled as binary or text mode

# "t" - Text - Default value. Text mode

# "b" - Binary - Binary mode (e.g. images)

# Working with Files
# Open a file and read its contents
with open("basic/example.txt", "r") as file:
    # with open("basic/example.txt", "rt") as file:
    content = file.read()
    print(content)  # Outputs the content of the file

# Writing to a file
# Open a file and write data to it
with open("basic/output.txt", "w") as file:
    file.write("Hello, Python!\n")
    file.write("This is a new line.")

# Append to an existing file
with open("basic/output.txt", "a") as file:
    file.write("\nThis line is appended.")

# Reading a file line by line
# Read file line by line using a loop
with open("basic/example.txt", "r") as file:
    for line in file:
        print(line.strip())  # Outputs each line without extra newline characters

# Working with CSV files
import csv

# Reading from a CSV file
with open("basic/data.csv", "r") as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)  # Outputs each row as a list

# Writing to a CSV file
with open("basic/output.csv", "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Quang", 30, "Da nang"])

# Check if File exist:
import os
if os.path.exists("basic/xxx.txt"):
  os.remove("basic/xxx.txt")
else:
  print("The file does not exist")