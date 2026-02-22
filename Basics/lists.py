# list in python is a collection of items which is ordered and changeable. It allows duplicate members.
# List[] is used to create a list in python. It can contain items of different data types.

fruits = ["apple", "banana", "cherry", "apple"]  # List of fruits with duplicate "apple"
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'apple']
# Accessing list items
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana
print(fruits[2])  # Output: cherry
print(fruits[3])  # Output: apple
# Modifying list items
fruits[1] = "orange"  # Changing "banana" to "orange"
print(fruits)  # Output: ['apple', 'orange', 'cherry', 'apple']
# Adding items to the list
fruits.append("grape")  # Adding "grape" to the end of the list
print(fruits)  # Output: ['apple', 'orange', 'cherry', 'apple', 'grape']
# Removing items from the list
fruits.remove("apple")  # Removing the first occurrence of "apple"
print(fruits)  # Output: ['orange', 'cherry', 'apple', 'grape']
fruits.pop(1)  # Removing the item at index 1 ("cherry")
print(fruits)  # Output: ['orange', 'apple', 'grape']
# Length of the list
print(len(fruits))  # Output: 3
fruits.clear()  # Removing all items from the list
print(fruits)  # Output: []
