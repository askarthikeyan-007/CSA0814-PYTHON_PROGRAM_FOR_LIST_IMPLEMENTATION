numbers = [1, -2, 3, -4, 5, -6]
positive_count = sum(1 for num in numbers if num > 0)
negative_count = sum(1 for num in numbers if num < 0)
print(f"Positive numbers: {positive_count}, Negative numbers: {negative_count}")
