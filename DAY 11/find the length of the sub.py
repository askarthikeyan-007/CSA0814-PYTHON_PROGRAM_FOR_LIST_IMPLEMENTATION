def length_of_lis(nums):
    from bisect import bisect_left
    lis = []
    for num in nums:
        pos = bisect_left(lis, num)
        if pos == len(lis):
            lis.append(num)
        else:
            lis[pos] = num
    return len(lis)
print(length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]))  
