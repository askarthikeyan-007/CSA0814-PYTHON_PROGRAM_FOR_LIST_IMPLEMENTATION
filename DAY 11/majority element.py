def majority_element(nums):
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
        return candidate if nums.count(candidate) > len(nums) // 2 else None
array = [3, 2, 3]
result = majority_element(array)
print(result) 
