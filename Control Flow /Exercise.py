
# Display the even numbers between 1 to 10
# return the count of even numbers we get at the end 

count = 0
for number in range(1,10):
    if number % 2 == 0:
        count += 1
        print(number)

print(f"we have {count} even numbers")