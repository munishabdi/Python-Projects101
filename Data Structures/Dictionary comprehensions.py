
# Dictionary Comprehensions

values = []
for x in range(5):
    values.append(x * 2)
print(values)
# whenever we have a pattern like this, we can use map or list comprehensions
# Dictionary comprehensions
dic = {x: x * 2 for x in range(5)}
# here we can use x as key, and x *2 as values
print(dic)