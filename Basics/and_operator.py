# logical operator "and" is used to combine two conditions. Both conditions must be true for the overall condition to be true.
# logical operator "not" is used to invert the truth value of a condition. If a condition is true, using "not" will make it false, and if a condition is false, using "not" will make it true.
temp = 27
is_sunny =  True

if temp == 28 and is_sunny: 
    print("It is hot outside and It is sunny")

elif temp <= 0 and is_sunny:
    print("It is cold outside and It is not sunny")

elif 28 > temp > 0 and is_sunny:
    print("It is warm outside and It is sunny")

elif temp >= 35 and not is_sunny:
    print("It is extremely hot outside and It is cloudy")
