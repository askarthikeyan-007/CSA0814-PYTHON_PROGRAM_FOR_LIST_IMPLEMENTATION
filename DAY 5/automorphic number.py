num = int(input("Enter a number: "))
square = num * num
num_str = str(num)
square_str = str(square)
if square_str.endswith(num_str):
    print(f"{num} is an automorphic number.")
else:
    print(f"{num} is not an automorphic number.")
