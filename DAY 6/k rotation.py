lst = [1, 2, 3, 4, 5]
k = int(input("Enter the number of positions to rotate: "))
k = k % len(lst)  
rotated_list = lst[-k:] + lst[:-k]
print("Original list:", lst)
print("Rotated list:", rotated_list)