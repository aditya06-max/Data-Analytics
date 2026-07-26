a = "\nAditya is also good"
# file = open("robot.txt" , "a")
# file.write(a)
# file.close

with open("robot.txt", "a") as f:
    f.write(a)
