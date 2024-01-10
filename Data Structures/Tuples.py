
# Tuples -> is unordered, unchangable, collection of objects
# we can modify tuples, add and remove item in tuple list
# Tuples are immutable, can't change them 

point = (1,2,3)
# we can define tuples without parenthesis
# add comma if you're defining one item
print(type(point))

# tuple concatenation
mytuple = 10,20,30
print(mytuple + point)

# multuplication to repeat 
print(mytuple * 3)

# convert a list to tuple
mylist = tuple([30,40])
print(mylist)

# we can get item index in tuple
print(point[0])

# range of items 
print(mytuple[0:2])

# unpack tuple
x,y,z = mytuple
print(x,y,z)

# use 'in' operator to check existance of an item
if 20 in mytuple:
    print("Yes it exists")

