name = input("What's your name: ")
work = input("Where  do you works:")
live = input("Where do you live: ")

# i want to print the following sentence: Aditya works at Amazon and lives in Gurgaon

print(name + " works at " + work + " And lives in " + live)

#Alternate way to write same thing using f , this method is more efficient and less hastle to use 

print(f"{name} works at {work} and lives in {live}")