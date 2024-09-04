# open()
# The open() function is used to open a file and return a corresponding file object. It is a built-in function that takes two arguments: the file (path) and the (mode) in which to open the file (e.g., read mode, write mode, append mode, etc.).
# close()
# Close function is used to close a file.
# With Statement
# "with" statement is also use to open a file, but when we open a file with "with" statement there is no need to close the file explicitly.
# File Modes
# r 👉: Read mode. Opens a file for reading only. The file pointer is placed at the beginning of the file.
# w 👉: Write mode. Opens a file for writing only. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.
# a 👉: Append mode. Opens a file for appending data. The file pointer is at the end of the file if the file exists. If the file does not exist, it creates a new file for writing.
# b 👉: Binary mode. Opens the file in binary mode, which is used for non-text files (e.g., images, videos).
# + 👉: Read and Write mode. Opens a file for both reading and writing.

# ⚠️ Use terminal ⚠️

# users_info = open("users.txt", mode="r")  # 👈 hover your mouse over this function
# users_info = open("users.txt", r)
# users_info = open("users.txt")
# print(users_info)

# File Info
# print(users_info.name)
# print(users_info.mode)
# print(users_info.readable())  # Boolean
# print(users_info.closed)  # Boolean

# -------------------------------
import os

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists

# In addition you can specify if the file should be handled as binary or text mode

# "t" - Text - Default value. Text mode

# "b" - Binary - Binary mode (e.g. images)

file_path = os.path.join("3.Advanced", "4.FilesFolderHandling", "example.txt")
# With Statement
with open(file_path, "r") as example:
    content = example.read()
    print(content)  # Outputs the content of the file
