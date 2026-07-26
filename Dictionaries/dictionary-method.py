students = {
    "Name" : "Aditya",
    "City" : "Bangalore",
    "Age" : 22,
    "Company" : "Google"
}

students.pop("Age") 
print(students)

students["Salary"] = 500000
print(students)
# students.popitem() # This will remove the last item added to the dictionary, which is "Salary" in this case
# print(students)

#other syntax used to remove an item from the dictionary is del keyword
# del students["Company"]
# print(students)

# students.clear() # This will remove all the items from the dictionary
# print(students)

print(students.keys()) # This will return a view object that contains the keys of the dictionary.
print(students.values()) # This will return a view object that contains the values of the dictionary.


