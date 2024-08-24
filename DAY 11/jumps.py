def min_jumps(arr):
    if len(arr) <= 1:
        return 0
    jumps, current_end, farthest = 0, 0, 0
    for i in range(len(arr) - 1):
        farthest = max(farthest, i + arr[i])
        if i == current_end:
            jumps += 1
            current_end = farthest
    return jumps
arr = [2, 3, 1, 1, 4]
print(min_jumps(arr))
