# tuple() is a built-in function in Python that creates a tuple from an iterable. A tuple is an immutable sequence type, meaning that once it is created, its elements cannot be changed.
# Example of using tuple() to create a tuple from a list
# immutable and faster to access than lists, but cannot be modified after creation.

fruits = ("apple", "banana", "cherry", "apple")
print(fruits)  # Output: ('apple', 'banana', 'cherry', 'apple')
# Accessing tuple items
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana
print(fruits[2])  # Output: cherry
print(fruits[3])  # Output: apple
# Tuples are immutable, so we cannot modify their items
# fruits[1] = "orange"  # This will raise a TypeError
# However, we can create a new tuple by concatenating existing tuples
new_fruits = fruits + ("grape",)  # Adding "grape" to the tuple
print(new_fruits)  # Output: ('apple', 'banana', 'cherry', 'apple', 'grape')
# Length of the tuple
print(len(fruits))  # Output: 4
for fruit in fruits:
    print(fruit, end=' ')  # Output: apple banana cherry apple (each on a new line)     
    