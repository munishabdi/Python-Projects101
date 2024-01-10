
# Removing duplicates 

def remove_duplicate(*nums):
    unique_nums = []
    for num in nums:
        if num not in unique_nums:
            unique_nums.append(num)
    return unique_nums

sorted_unique_nums = remove_duplicate(1,33,23,7,20,19,23)
print(sorted(sorted_unique_nums, reverse=True))