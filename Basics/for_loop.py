# for loop is used to iterate over a sequence (such as a list, tuple, string, or range) and execute a block of code for each item in the sequence. It is useful for situations where you want to perform an action on each item in a collection of items.
# repeat a block of code for a specific number of times.

for i in range(5):  # This will repeat the block of code 5 times, with i taking values from 0 to 4.
    print(f"This is iteration number {i}")

# You can also use a for loop to iterate over a list of items:
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")

# you can also use a for loop to iterate over a string:
name = "chaitanya"
for letter in name:
    print(letter)

# you can also use a for loop to iterate over a range of numbers with a specific step:
for i in range(0, 10, 2):  # This will repeat the block of code for i taking values 0, 2, 4, 6, and 8.
    print(i)

for i in range(0, 10):  # This will repeat the block of code for i taking values 0, 2, 4, 6, and 8.
    print(i)

# you can also use a for loop to iterate over a list of items and their corresponding indices using the enumerate() function:
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")