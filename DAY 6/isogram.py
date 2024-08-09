def is_isogram(number):
    return len(set(str(number))) == len(str(number))
number = 12345
if is_isogram(number):
    print(f"{number} is an isogram.")
else:
    print(f"{number} is not an isogram.")
