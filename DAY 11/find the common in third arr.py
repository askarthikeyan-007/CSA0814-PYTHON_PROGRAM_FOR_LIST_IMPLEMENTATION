def common_elements(arr1, arr2, arr3):
    i = j = k = 0
    common = []
    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        if arr1[i] == arr2[j] == arr3[k]:
            common.append(arr1[i])
            i += 1; j += 1; k += 1
        elif arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr3[k]:
            j += 1
        else:
            k += 1
    return common
arr1 = [1, 5, 10, 20]
arr2 = [5, 10, 15, 20]
arr3 = [10, 20, 30]
print(common_elements(arr1, arr2, arr3))  
