import itertools
rows = int(input("Enter the number of rows: "))
a, b = 0, 1
fib_gen = itertools.count(start=a)
for i in range(1, rows + 1):
    for _ in range(i):
        print(a, end=" ")
        a, b = b, a + b
    print()