#Q.1  Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up

# dictionary = {
#     "नमस्ते": "Hello",
#     "धन्यवाद": "Thank you",
#     "कृपया": "Please",
#     "माफ़ कीजिए": "Sorry",
#     "हाँ": "Yes",
#     "नहीं": "No",
# }

# print("Welcome to the Hindi-English Dictionary!\n")

# for hindi, english in dictionary.items():
#     print(f"{hindi} : {english}")

# Write a program to input eight numbers from the user and display all the unique numbers
# (once)

# numbers = set()

# numbers.add(int(input("Enters the 1st number: " ))),
# numbers.add(int(input("Enters the 2nd number: " ))),
# numbers.add(int(input("Enters the 3rd number: " ))),
# numbers.add(int(input("Enters the 4th number: " ))),
# numbers.add(int(input("Enters the 5th number: " ))),
# numbers.add(int(input("Enters the 6th number: " ))),
# numbers.add(int(input("Enters the 7th number: " ))),
# numbers.add(int(input("Enters the 8th number: " )))

# print(numbers)

# What will be the length of following set s

# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20') # length of s after these operations

# length = len(s)
# print(length)

#  Create an empty dictionary. Allow 4 friends to enter their favorite language as value and
# use key as their names. Assume that the names are unique.

fav_lang = {}

name = input("Enter your first friend's name: ") 
language = input("Enter their favourite language: ")
fav_lang[name] = language

name = input("Enter your second friend's name: ") 
language = input("Enter their favourite language: ")
fav_lang[name] = language

name = input("Enter your third friend's name: ") 
language = input("Enter their favourite language: ")
fav_lang[name] = language

name = input("Enter your fourth friend's name: ") 
language = input("Enter their favourite language: ")
fav_lang[name] = language

name = input("Enter your fifth friend's name: ") 
language = input("Enter their favourite language: ")
fav_lang[name] = language

print(fav_lang)

