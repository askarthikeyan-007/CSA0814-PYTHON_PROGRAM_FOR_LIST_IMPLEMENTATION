lst = [1, 2, 3, 4, 3, 3, 5]
tar = 3
pos = []
for i in lst:
    if lst[i] == tar:
        pos.append(i)

print("first position:",pos[0])
print("last position:",pos[-1])
