# set{} is mutable and unordered collection of unique elements. It is used to store multiple items in a single variable. Sets are defined using curly braces {} or the
# NO duplicate elements allowed in sets. Best for membership testing and eliminating duplicate entries.
fruits = {"apple", "banana", "cherry", "apple"}
print(fruits)  # Output: {'apple', 'banana', 'cherry'} (duplicate "apple" is removed)
# Adding a item to the set
fruits.add("grape")
print(fruits)  # Output: {'apple', 'banana', 'cherry', 'grape'}
# Removing an item from the set
fruits.remove("cherry")
print(fruits)  # Output: {'apple', 'banana', 'grape'}   
fruits.pop()  # Removes and returns an arbitrary item from the set
print(fruits)  # Output: {'banana', 'grape'} (the remaining items

if "apple" in fruits:
    print("Apple was found")
else:
    print("Apple was not found")  # Output: Apple was not found

fruits = {"apple", "banana", "cherry", "apple"}

fruit = input("enter the fruit name: ")
if fruit in fruits:
    print(f"{fruit} was found")
else:
    print(f"{fruit} was not found")