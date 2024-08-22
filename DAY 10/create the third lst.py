def merge_lists(list1, list2):
    return [a + b for a, b in zip(list1, list2)] + list1[len(list2):] + list2[len(list1):]
list1 = [1, 2, 3]
list2 = ['a', 'b']
result = merge_lists(list1, list2)
print(result)
