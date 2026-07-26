a = "Aditya is good" 

# file = open("Aditya.txt", "w") # open is function which takes two arguements first one is file name and second one is file mode, the mode in which we want to open this file.
# #This is the way to write a file.
# file.write(a)

file = open("robot.txt", "r")
# content = file.read()
content = file.readlines()
print(content)
file.close