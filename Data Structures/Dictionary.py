
# Dictionary - a collection of key-value pairs

point = {"x": 1, "y": 2}
newdic = dict(name= 'munasar', role= 'engineer')
# the second format is prefered with cleaner syntax

print(type(newdic))

# getting the values associated
print(point['x'])
print(newdic['name'])

# change the keys
point['x'] = 20
print(point)

# adding new key
# point['z'] = 40
# print(point)

# getting the key with .get method
print(point.get('y'))

# iterating over a dictionary
point = {"x": 1, "y": 2}
for key in point:
    print(key, point[key])
    # getting the key and associated values 

# second option to iterate over a dictionary using .items
for x in point.items():
    print(x)
# in each iteration, we get a tuple of two items, key and values
# so we can unpacking or extract it 
for key, value in point.items():
    print(key, value)