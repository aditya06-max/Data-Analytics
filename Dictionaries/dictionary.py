students = {
    "Name" : "Aditya",
    "City" : "Bangalore",
    "Age" : 22,
    "Company" : "Google"
}

print(students)
print(students["Name"])
#print(students["Cityyy"]) # This will give an error because there is no key named "Cityyy" in the dictionary
print(students.get("Cityyy"))# This will not give an error, it will return None because there is no key named "Cityyy" in the dictionary

students["City"] = "Mumbai"  # This will update the value of the key "City"
print(students)