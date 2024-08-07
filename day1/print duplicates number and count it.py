my_list = [1, 2, 2, 3, 4, 4, 4]
duplicates = {item for item in my_list if my_list.count(item) > 1}
print({item: my_list.count(item) for item in duplicates})
