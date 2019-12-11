#string variable example

phrase = "akb"
print(phrase)

#concatenation : taking a string and append with other string
print(phrase + " is india ")

#strings with functions

print(phrase.upper())
print(phrase.upper().isupper()) # To check whether the string is in upper case or not

#To find out the length of the string 
print(len(phrase))

#To access a specific character in a string 
phrase = "kiane"
print(phrase[2])
print(phrase.index("k"))

#replace function to replace in a string
phrase = "India country"
print(phrase.replace("country", " is my country "))

#Multiple calculations in python
print(10%3)
print(4 * 3 + 7)
print(4 * (3 + 7))
