import string
import random
def generate_random_string(length, uppercase=False):
    letters = string.ascii_uppercase if uppercase else string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))
random_lowercase_string = generate_random_string(10)
print(random_lowercase_string)
random_uppercase_string = generate_random_string(10, uppercase=True)
print(random_uppercase_string)
