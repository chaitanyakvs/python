# Logical operatores: and, or, not
# or = At least once condition is True
# and  = All conditions must be true
# not = Inverts the truth value value of the condition( True becomes False and False becomes True)

temp = 30
is_raining =  False

if temp > 30 or temp < 0 or is_raining:     # If any of the conditions is true, the weather is bad
    print("The weather is bad")
else: 
    print(" The weather is gooid")