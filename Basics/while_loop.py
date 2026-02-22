# while loop is used to execute a block of code repeatedly as long as a given condition is true. The loop will continue to run until the condition becomes false. It is useful for situations where you want to repeat an action multiple times, but you don't know in advance how many times it will be needed.
# As long as condition is true.

name = input("enter  you r name:")

while name == "":
    name = input("enter  your name:")

age = int(input("enter your age: "))

while age < 0:
    print("age cannot be less than zero")
    age = int(input("enter a valid age: "))

print(f"hello{name}!")
print(f" your age is {age} years old")