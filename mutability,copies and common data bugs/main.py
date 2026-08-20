# a = [1,2,3,4,5,65,76,87,98,99,100]
# b = a

# b.append(10
# print(a)1)
# b[2] = 99
# print(a)    #in this way changes is also made in a because we only told memory that b = a, and in memeory both are indicating at same location.

#now if we want to make 'b' a copy of 'a' and wamt to make changes in 'b' such that there is no changes n 'a' then we use copy functions for that.

a = [23, 56, 65, 78, 95]

b = a.copy()  #in this way changes will not aplly to 'a' it only apllies to 'b'.

b[4] = 24
print(a)
print(b)

def add_item(items):
    items.append(10)

data = [1,2,3,4]
add_item(data)

print(data)

#expalinations
# Before function call

# data

# ↓

# [1,2,3,4]

# Function

# def add_item(items):

# At this point

# items

# ↓

# Nothing

# Then

# add_item(data)

# Python automatically performs

# items = data

# Now

# data ───┐
#          │
#          ▼
#      [1,2,3,4]
#          ▲
#          │
# items ───┘

# Now both variables refer to the same list.

# Then

# items.append(10)

# Since both variables point to the same list,

# the list becomes

# data ───┐
#          │
#          ▼
#  [1,2,3,4,10]
#          ▲
#          │
# items ───┘

# Function ends.

# items disappears.

# data

# ↓

# [1,2,3,4,10]