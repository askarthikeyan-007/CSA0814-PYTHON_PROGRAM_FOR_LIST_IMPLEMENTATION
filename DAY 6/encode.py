message = "Hello World"
shift = 3
encoded_message = ""
for char in message:
    if char.isalpha():
        start = ord('A') if char.isupper() else ord('a')
        shifted = (ord(char) - start + shift) % 26
        encoded_char = chr(start + shifted)
        encoded_message += encoded_char
    else:
        encoded_message += char
print(f"Original message: {message}")
print(f"Encoded message: {encoded_message}")