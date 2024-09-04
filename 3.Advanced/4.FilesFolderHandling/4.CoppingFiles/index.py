import os

friends_file = os.path.join("3.Advanced", "4.FilesFolderHandling", "friend.txt")
write_file = os.path.join("3.Advanced", "4.FilesFolderHandling", "write.txt")


write = open(write_file, "w")
friends = open(friends_file, "r")

# 1. Read the data
content = friends.read()

# 2. Write to "write_file" file
write.write(content)
write.close()
