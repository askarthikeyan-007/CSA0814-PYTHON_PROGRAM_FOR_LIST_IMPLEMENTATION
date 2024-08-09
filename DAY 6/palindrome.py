string = "noonlight"
length = len(string)
result = []
for i in range(length):
    for j in range(i + 1, length + 1):
        substring = string[i:j]
        if substring == substring[::-1]:  
            result.append(substring)
print("Palindromic substrings:", result)