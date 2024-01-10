
# Solve this problem
from pprint import pprint
sentence = 'This is a common interview questions'

# dictionary to find character as keys 
# repetition for the values

char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
    


# dictionaries, like sets are unordered collection which cant be sorted
# the problem is that we cant sort this list since its a dictionary
# so we need to convert the list into a tuple list

char_frequency_sorted = sorted(char_frequency.items(), key= lambda kv:kv[1], reverse=True)
print(char_frequency_sorted[0])
# sorted function - takes an iterable which is char_frequency.items()
# sorted function - by default doesnt know how to sort tuple
# .items() method taks all the key-value pairs as tuples
# use reverse=True to make it descending order
# the first character in the list is the most repeated character with 5 repetition

