arr = list(map(int, input("Enter array elements: ").split()))
seen = set()
repeated = None
for num in arr:
    if num in seen:
        repeated = num
        break
    seen.add(num)
print(f"Repeated element: {repeated}")
