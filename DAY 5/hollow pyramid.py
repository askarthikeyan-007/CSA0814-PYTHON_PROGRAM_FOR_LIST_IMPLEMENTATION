rows = int(input("Enter the number of rows: "))
for i in range(rows):
    print(" " * (rows - i - 1), end="")
  
    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i or i == rows - 1:
            print("*", end="")
        else:
            print(" ", end="")
       print()
