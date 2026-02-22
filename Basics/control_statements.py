# if statements in python


age = int(input("enter your age: "))

# Implementing bool() function to check the truth value of a variable
has_ticket = True
if has_ticket:
    print("you can enter")
else: 
    print(" you cannot enter: ")

if age >= 18:
    print("you are eligible to vote")

elif age <= 0:
    print("unable to process your request")

elif age == 17  and age > 18:
    print("you are going to be eligible to vote next year")
    
else:
    print("you are not eligible to vote")