def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_composite_numbers(start, end):
    composite_numbers = []
    for num in range(start, end + 1):
        if not is_prime(num):
            composite_numbers.append(num)
    return composite_numbers

start_num = 10
end_num = 30
composite_nums = generate_composite_numbers(start_num, end_num)
print(composite_nums)
