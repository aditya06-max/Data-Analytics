def show_value():
    x = 34 #local variables, this variable is own property of the function which cannot be chahnge by global variables.
    print(x)
show_value()

x = 78 #global variables

show_value()