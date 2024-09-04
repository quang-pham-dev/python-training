# write()
# The write() method is used to write data to a file. It is called on a file object that has been opened in write or append mode. The write() method takes a single argument, which is the string of data to be written to the file.
# writelines()
# The writelines() method is used to write a list of lines to a file. Each item in the list should be a string representing a line of text. The writelines() method does not add line separators (like \n) between the lines, so you'll need to include them in the strings if you want them to be present in the file.

# -----------------------
import os

content_file = os.path.join("3.Advanced", "4.FilesFolderHandling", "write.txt")

# write()
content = open(content_file, "w")

# If the file is already created it'll append this data,
# -- If not so it will first create that file then write this data to it.

content.write("I'm writing this text to my file using python.")
content.close()

# -----------------------
friends_file = os.path.join("3.Advanced", "4.FilesFolderHandling", "friend.txt")
# writelines()
content = open(friends_file, "w")

friends = ["Quang\n", "David\n", "Xuan\n", "Huy\n"]
content.writelines(friends)
content.close()
