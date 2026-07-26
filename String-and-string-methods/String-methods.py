name = "Aditya  "
#name[0] = "R" # This will give an error because strings are immutable

print(name)
print(len(name)) # This will print the length of the string
print(name.lower()) # This will print the string in lowercase
print(name.upper()) # This will print the string in uppercase
print(name[7]) 
print(name.strip()) # This will remove the leading and trailing whitespace
print(name.replace("Aditya", "Rahul")) # This will replace "Aditya" with "Rahul"
print(name.split()) # This will split the string into a list of words
print(name.isalpha()) # This will check if all characters in the string are alphabetic
print(name.isnumeric()) # This will check if all characters in the string are numeric