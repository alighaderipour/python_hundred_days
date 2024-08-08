fruits = ["apple", "banana", "cherry"]
colors = ["red", "yellow", "pink"]

# Using zip to combine the two lists
zipped = zip(fruits, colors)
print(type(zipped))
# Converting the zip object to a list to display the pairs
result = list(zipped)
print(result)  # Output: [('apple', 'red'), ('banana', 'yellow'), ('cherry', 'pink')]


names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
countries = ["USA", "UK", "Canada"]

# Zipping three lists together
zipped2 = zip(names, ages, countries)

# Converting to a list
result2 = list(zipped2)
print(result2)
# Output: [('Alice', 25, 'USA'), ('Bob', 30, 'UK'), ('Charlie', 35, 'Canada')]


names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

# Using zip with enumerate to get index and values
for index, (name, age) in enumerate(zip(names, ages)):
    print(f"{index}: {name} is {age} years old.")
