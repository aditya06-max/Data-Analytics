try:
    x = int(input("Enter a number: "))
    y = 10/x
except ValueError:
    print("Enter a valid number ")
except ZeroDivisionError:
    print("division byb zero is not allowed")

finally: #This block will always run no matter what error is comming
    print("it will always run")