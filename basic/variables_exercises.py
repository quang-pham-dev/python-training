# Sum of 2 numbers
a = 2
b = 3
print(a + b)

# Division with remainder
mod = 10 % 3
print(mod)


# String concatenation
first_name = "Quang"
last_name = "Pham"
full_name = first_name + " " + last_name
print(full_name)  # Output "Quang Pham"

# Repeat string
repeat_string = "Hello! " * 3
print(repeat_string)  # Output "Hello! Hello! Hello! "

# Indexing và slicing String
text = "Python"
print(text[0])  # Output "P"
print(text[-1])  # Output "n"
print(text[1:4])  # Output "yth"

# How many seconds are there in 42 minutes 42 seconds?
# Define the number of minutes and seconds
minutes = 42
seconds = 42

# Convert minutes to seconds
total_seconds = minutes * 60 + seconds

# Output the result
print(f"There are {total_seconds} seconds in 42 minutes 42 seconds.")

# How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile
# Define the distance in kilometers
kilometers = 10

# Conversion factor from kilometers to miles
conversion_factor = 1.61

# Calculate the distance in miles
miles = kilometers / conversion_factor

# Output the result
print(f"There are {miles:.2f} miles in {kilometers} kilometers.")

# If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per
# mile in minutes and seconds)? What is your average speed in miles per hour?
# Given data
kilometers = 10
total_time_seconds = 42 * 60 + 42

# Conversion factors
conversion_factor = 1.61
distance_miles = kilometers / conversion_factor

# Calculate average pace (time per mile)
average_pace_seconds_per_mile = total_time_seconds / distance_miles
minutes_per_mile = int(average_pace_seconds_per_mile // 60)
seconds_per_mile = round(average_pace_seconds_per_mile % 60, 2)

# Calculate average speed (miles per hour)
total_time_hours = total_time_seconds / 3600
average_speed_mph = round(distance_miles / total_time_hours, 2)

# Output results
print(
    f"Average pace: {minutes_per_mile} minutes and {seconds_per_mile} seconds per mile"
)
print(f"Average speed: {average_speed_mph} miles per hour")
