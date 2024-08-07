def remove_duplicates(arr):
    return list(set(arr))
original_array = [1, 2, 2, 3, 4, 4, 5]
array_without_duplicates = remove_duplicates(original_array)
print(array_without_duplicates)
