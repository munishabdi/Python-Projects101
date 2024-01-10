
# Lists, tuples, and sets
# Lists and tuples allows us to work with sequencial data
# sets are unordered collections with values and no duplicates 

courses = ['math', 'biology', 'chemistry', 'history']
courses2 = ['education', 'traning']
print(courses)
print(len(courses))

# checking the index
print(courses[0]) # returns history
print(courses[-1]) # returns the last value 

# slicing index or grabing a range of values
print(courses[0:2]) # third item will not be included 

# List method - allows us to modify the list items

# adding item end of the list
courses.append('art')
print(courses)

# adding item in specific location
# inset method takes two argument (index, value)
courses.insert(2, 'compsci')
print(courses)

# adding list with another list with extend method
courses.extend(courses2)
print(courses)

# removing values
courses.remove('math')
print(courses)
# pop method - by default this will remove that last value
# pop method can return the popped value by reassiging a variable to it
popped = courses.pop()
print(popped)
print(courses)

# sorting a list
courses.sort()
print(courses)

# how to sort a list without altering the original list
print(sorted(courses))

# for loop with index 
for index, item in enumerate(courses, start=1):
    print(index, item)

# Comma seperated values using joint method
comma_seperated = ", ".join(courses)
print(comma_seperated)