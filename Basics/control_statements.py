# if statements in python


age = int(input("enter your age: "))

if age >= 18:
    print("you are eligible to vote")

elif age <= 0:
    print("unable to process your request")

elif age == 17  and age > 18:
    print("you are going to be eligible to vote next year")
    
else:
    print("you are not eligible to vote")