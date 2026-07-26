x = 78 #global variables

def show_value():
    global x # this syntax is used to make the global variables inside the function
    x = 79
    print(x)

show_value()
print(x)
show_value()