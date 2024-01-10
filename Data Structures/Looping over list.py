
# Looping over a list

# if you want to get the index of list items use enumerate function
# enumerate is iterable, in each iteration it give us a new tuple item 

letters = ['a','b','c','d']
for letter in enumerate(letters):
    print(letter)

# if we're getting a tuple of two items we can unpack them 
# first item is index, second item is the item of that index
    
letters = ['a','b','c','d']
for index, letter in enumerate(letters):
    print(index, letter)

mytuple = ('e', 'f', 'g')
for index, item in enumerate(mytuple):
    print(index, item)