def sum_odd_even(num):
    odd_sum = 0
    even_sum = 0
    for digit in str(num):
        if int(digit) % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    return odd_sum, even_sum
number = 123456
odd_sum, even_sum = sum_odd_even(number)
print(f"Sum of odd numbers: {odd_sum}")
print(f"Sum of even numbers: {even_sum}")
