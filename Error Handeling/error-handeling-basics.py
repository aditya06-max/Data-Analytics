print("initializing....")

a = int(input("Enter a:-  \n"))
b = int(input("Enter b:- \n"))

try:
    print("The value of a/b is :" , a/b)
except Exception as e:
    print("Some error occured! - " , e)

print("Thank you")