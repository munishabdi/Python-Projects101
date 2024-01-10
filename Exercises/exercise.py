
# Create a program that find the most repeated character in the text
from pprint import pprint

sentence = "This is a common interview question"

char_frequency = {}  # will store the value frequency of each character
for char in sentence:
    if char in char_frequency:
        # if statement check if there is key in the char_frequency dictionary
        char_frequency[char] += 1
        # if there is a key already, then its incremented
    else:
        char_frequency[char] = 1
        # if there is no character in the dictionary
        # a new key-value pair is created and set to 1

# pprint(char_frequency)
# this will provide all characters and their repeated times
# but we want to sort the item in the list and get the most repeated item

print(sorted(char_frequency.items()))
# use the .items method to convert the list of characters into list of tuples
# then we can sort the list in ascending or descending order

sorted_char = sorted(char_frequency.items(), key=lambda kv:kv[1], reverse=True)
print(sorted_char[0])