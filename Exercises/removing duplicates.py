
# Removing duplicate numbers
 # The logic ensures that only the first occurrence of 
# each unique element is added to unique_nums.


def remove_duplicate(nums):
    unique_nums = []
    for num in nums:
        if num not in unique_nums:
            unique_nums.append(num)
    
    return unique_nums

nums = [1,22,33,28,8,12,22]
unique_items = remove_duplicate(nums)
print(unique_items)