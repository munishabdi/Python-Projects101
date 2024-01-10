
# Lists - are collection of items which are mutable, ordered sequence

letters = ['a','b','c','d']
mylist = [0] * 5
# print(mylist)
# * repeats the item on the list

combined = mylist + letters
print(combined)

x = list(range(20))
print(x)
y = list('Hello World')
print(y)
# each character in the original string is an item list

print(len(y))
# length using len() function
