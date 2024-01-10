
# Accessing items

letters = ['a','b','c','d']
print(letters[0]) # returns first item
print(letters[-1]) # returns first item at the end of the list

# modifying
letters[0] = 'A'
print(letters)

# slicing List
print(letters[0:3]) 
# returns a new list with the first three item in the orginal list

print(letters[:]) 
# this returns all the item in the orginal list

print(letters[:])
# give back a copy of the original list

numbers = list(range(20))
print(numbers[::2])
# returns every other element in the list 

print(numbers[::-1])
# returns the original list but in reverse order
