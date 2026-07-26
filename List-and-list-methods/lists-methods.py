items = ["Apple", "Banana", "Cherry"]

print(items)
items[1] = "Blueberry"
print(items)

print(len(items))

# Adding new items to the list at the end using append() method because lists are mutable
items.append("guava")
print(items)

# Adding new items to the list at a specific index using insert() method
items.insert(1, "oranges")
print(items)

# Removing items from the list using remove() method from its first occurance
items.remove("Apple")
print(items)

#items.extend is used to add multiple items to the list at the end and it is different from append() method because append() adds a single item to the list and extend() adds multiple items to the list at the end
items.extend(["Grapes", "Mangoes"])
print(items)

3# Removing items from the list using pop() method from its index and if we dont specify the index it will remove the last item from the list
items.pop(1)
print(items)

#items.clear() #clear() method is used to remove all the items from the list and it will return an empty list
print(items)

#items.index() method is used to find the index of the first occurrence of the specified item in the list and it will return the index of the item if it is found in the list and if it is not found it will raise a ValueError
print(items.index("Cherry"))

#items.count() method is used to count the number of occurrences of the specified item in the list and it will return the count of the item if it is found in the list and if it is not found it will return 0
print(items.count("Banana"))

#items.sort() method is used to sort the items in the list in ascending order and it will sort the items in place and it will return None
numbers = [22,33,44,56,76,45,27,98]
numbers.sort()
print(numbers)

numbers.sort(reverse=True) 
#sort() method can also be used to sort the items in descending order by passing reverse=True as an argument
print(numbers)

 #in operator is used to check if the specified item is present in the list or not and it will return True if the item is found in the list and if it is not found it will return False
print(27 in numbers)
