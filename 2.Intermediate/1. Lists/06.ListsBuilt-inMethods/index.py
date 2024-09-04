# Lists Built-In Methods
# append(x)
# Adds element at the end of the list.
# extend(iterable)
# Extends the list by appending elements from the iterable.
# insert(i, x)
# Inserts element x at the specified position i.
# remove(x)
# Removes the first occurrence of element x.
# pop([i])
# Removes and returns the element at the specified position i. If no index is provided, it removes and returns the last element.
# count(x)
# Returns the number of occurrences of element x in the list.
# sort(key=None, reverse=False)
# Sorts the elements of the list in ascending order. The key and reverse parameters are optional.
# reverse()
# Reverses the elements of the list in place.
# copy()
# Returns a shallow copy of the list.

# append
my_list = [1, 2, 3]
my_list.append(4)

# extend
my_list = [1, 2, 3]
my_list.extend([4, 5, 6])

# insert
my_list = [1, 2, 3]
my_list.insert(1, 4)

# remove
my_list = [1, 2, 3, 2]
my_list.remove(2)

# pop
my_list = [1, 2, 3]
popped_element = my_list.pop(1)

# count
my_list = [1, 2, 3, 2]
count_of_2 = my_list.count(2)

# sort
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
my_list.sort()

# reverse
my_list = [1, 2, 3]
my_list.reverse()

# copy
original_list = [1, 2, 3]
copied_list = original_list.copy()
