age = int(input("Enter your age: "))

#this is ternary operator , this is called on eline conditionals this execute if-else condition in on line
status = "Adult" if age>=18 else "Minor"

#if we want that code should not be executed on if statement it should be executed only for else statement then this is the syntax to do this 

if age >= 18:
    pass
else: 
    print("You are minor")
