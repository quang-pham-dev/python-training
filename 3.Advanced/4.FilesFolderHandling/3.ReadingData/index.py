# read()
# The read() method in Python is used to read a specified number of bytes from a file.
# If no argument is provided, it will attempt to read the entire file. When the end of the file is reached,
# read() returns an empty string.

import os
file_path = os.path.join("3.Advanced", "4.FilesFolderHandling", "data.txt")

# 1. We're reading the data so we can provide 'r' mode
# 2. The file should be existed
# 3. You can also omit the "r" mode because it's the default mode
# users = open(file_path, "r")

# ----------------------
# Reading All Data
users = open(file_path)
users_content = users.read()
print(users_content)
# ----------------------

# ----------------------
# Reading just a chunk of data
users = open(file_path)
users_content = users.read(5)
print(users_content)

# ----------------------
# Read Only Single Line
content = open(file_path)
print(content.readline())
