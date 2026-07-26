items = {"Apple", "Banana", "Mangoes", "Grapes"}
print(items)

items.add("Pineapple")  #adds an item to the set
print(items)

items.update(["Watermelon", "Strawberry", ]) #adds multiple items to the set
print(items)

#sets doesnt ensure the order of adding of values in sets it only insures that no duplicate values are there in the sets 

items.remove("Grapes")
print(items)

#items.remove("Guava") #this will give error because this item is not present in the set
items.discard("Guava") #this will not give error because this item is not present in the set
print(items)

# a= items.pop() #this will remove a random item from the set and return it
# print(items)
# print(a)

# items.clear() #this will remove all the items from the set
# print(items)

print(len(items))
