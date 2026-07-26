#This is used to pass default  value to name because if we dont assign some value to name during calling the function it will not run that line of code and give error but when we give default value to name it will automatically give that default value to name and if we give some value to name it overpass that default value and give our assign value to it.
def greet(name = "user"):
    print("Hello" , name)

greet()
greet("Rahul")

def greet(name ="User" , city = "Delhi"):
    print ("Hello!" , name , city )

greet("Rohan" , "Bangalore")