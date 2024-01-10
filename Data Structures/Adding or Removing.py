
# Adding or removing 
# you have two options, 


# if you want to add at the end of the list use append method
letters = ['a','b','c','d']
letters.append('e')
print(letters)

# explain why i cant use this format of appending 
print(letters.append('e'))

# options two, adding specific postion 
letters.insert(0, "-")
print(letters)

# Removing objects
# we have two options

# Remving at the end of the list, use pop method
# you can also pass at given index
letters.pop(0)
letters.pop()
print(letters)

# when you dont know the index of the object, use remove method
# it takes an argument
letters.remove('-')
print(letters)

# option two del method with items index position
# can also be used to remove a range of items
del letters[0]
print(letters)