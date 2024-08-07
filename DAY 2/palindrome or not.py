def is_palindrome(num):
    return str(num) == str(num)[::-1]
num = 12321
if is_palindrome(num):
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a palindrome")
