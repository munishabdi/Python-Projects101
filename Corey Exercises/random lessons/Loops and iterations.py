
# Loops and iterations - 
# loop through the iteration and each time num will equal to new value in the list of nums

nums = [1,2,3,4,5]
for num in nums:
    print(num)

# break will terminate the loop completely
for num in nums:
    if num == 3:
        print('found it')
        break
    print(num)
    # we brake out of the loop before the 3 printed out 
    # if the print() function was before the if statement it will printed out the 3

# continue will skip to the next iteration
for num in nums:
    if num == 3:
        print('found it')
        continue
    print(num)
    # when continue, it skips to the next iteration which went to the for loop and didnt meet the condition 
    # then it printed 4 and 5
    # if the condition didnt meet, then controller moves to print the values left 

# loop within a loop
for num in nums:
    for letter in 'abc':
        print(num, letter)

# going through a loop for certain times using the range function
for i in range(10):
    print('value:', i)

# While loops - will keep going until a certain condition is met or we break the condition
# x = 0
# while x < 10:
#     print(x)
#     x += 1
    # when we increment 9 + 1, the condition becomes false, and the loop stops working 

# Infinite loop
x = 0
while True:
    if x == 5:
        break
    print(x)
    x += 1
    # the infinite loop keeps going until x == 5, which will break the statement and stops the iteration of the loop
    