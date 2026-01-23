# f-string is nothing but you could use variable along with some text by using f-string
# always mention the variable in curly braces{variable_name} along with the text

first_name = "chaitanya"        # Here "chaitanya" can be called as string because it is mentioned within quotations

print(first_name)

# By using f-string

print(f" my name is {first_name}")

# for Integers
age = 25
print(f"My age is {age} years")

# for Floating point numbers
height = 5.9
print(f"my height is  {height} feet")

# for Boolean
x = None
print(bool(x))

# Returns False as x is an empty sequence
x = 0.0
print(bool(x))

# Returns False as x is an empty mapping
x = {}
print(bool(x))

# Returns True as x is a non empty string
x = 'GeeksforGeeks'
print(bool(x))

is_student = True
if  is_student:
    print("Yes, I am a student")
else:
    print("No, I am not a student")
