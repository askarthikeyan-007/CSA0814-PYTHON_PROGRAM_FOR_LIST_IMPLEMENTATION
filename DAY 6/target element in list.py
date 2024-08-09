lst = [2, 4, 3, 7, 5, 1]
target = 8
pairs = []
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] + lst[j] == target:
            pairs.append((lst[i], lst[j]))
print("Pairs that sum up to",target,"is",pairs)
