# Challenge 1: Creating Sets
# Using curly braces {}: Create a set of your favorite hobbies.
# Using the set() function: Create a set from a list containing duplicate elements (e.g., set([1, 1, 2, 3]) will remove duplicates).
my_hobbies = {
    "football",
    "basketball",
    "tennis",
    "swimming",
}
print(my_hobbies)
my_hobbies2 = set(
    ["football", "basketball", "tennis", "football", "basketball", "tennis", "swimming"]
)
print(my_hobbies2)

# Challenge 2: Set Membership and Checking for Uniqueness
# Create a set of numbers.
# Check if a specific number is present in the set using the in operator.
# Try adding a duplicate element to the set and observe that it's not included (sets cannot have duplicates).
number_set = {1, 2, 3, 4, 5}

# Check if a specific number is present in the set using the in operator.
print(3 in number_set)  # True
print(6 in number_set)  # False

# Try adding a duplicate element to the set and observe that it's not included (sets cannot have duplicates).
number_set.add(3)
print(number_set)  # Still {1, 2, 3, 4, 5}

# Add a new number to demonstrate that non-duplicates are added
number_set.add(6)
print(number_set)  # Now {1, 2, 3, 4, 5, 6}

# Challenge 3: Set Operations: Union, Intersection, Difference
# Create two sets: one representing movies you've watched and another representing your friend's watched movies.
# Use the following set operations to find:
# Union: The movies watched by either you or your friend.
# Intersection: The movies you both have watched.
# Difference: The movies you've watched that your friend hasn't and vice versa (use appropriate methods like union(), intersection(), and difference()).

# Create two sets representing movies watched
my_movies = {"Inception", "The Dark Knight", "Interstellar", "Tenet"}
friend_movies = {"Inception", "The Dark Knight", "The Matrix", "Pulp Fiction"}

# Union: Movies watched by either you or your friend
all_movies = my_movies.union(friend_movies)
print("All movies watched:", all_movies)

# Intersection: Movies you both have watched
common_movies = my_movies.intersection(friend_movies)
print("Movies watched by both:", common_movies)

# Difference: Movies you've watched that your friend hasn't
my_unique_movies = my_movies.difference(friend_movies)
print("Movies only I've watched:", my_unique_movies)

# Difference: Movies your friend has watched that you haven't
friend_unique_movies = friend_movies.difference(my_movies)
print("Movies only my friend has watched:", friend_unique_movies)

# Alternative syntax using operators (|, &, -)
print("\nAlternative syntax:")
print("All movies:", my_movies | friend_movies)
print("Common movies:", my_movies & friend_movies)
print("My unique movies:", my_movies - friend_movies)
print("Friend's unique movies:", friend_movies - my_movies)
print(
    "Intersection: Movies you both have watched", my_movies.intersection(friend_movies)
)


# Challenge 4: Adding and Removing Elements from Sets
# Create a set of fruits.
# Add a new fruit to the set using the add() method.
# Remove a specific fruit from the set using the remove() method.
# (Optional) Try removing an element that's not in the set using discard() (which won't cause an error).

# Create a set of fruits
fruits = {"apple", "banana", "cherry"}

# Add a new fruit to the set using the add() method
fruits.add("orange")
print("Fruits after adding orange:", fruits)

# Remove a specific fruit from the set using the remove() method
fruits.remove("banana")
print("Fruits after removing banana:", fruits)

# Remove a fruit that's not in the set using discard() (which won't cause an error)
fruits.discard("grape")
print("Fruits after discarding grape:", fruits)
