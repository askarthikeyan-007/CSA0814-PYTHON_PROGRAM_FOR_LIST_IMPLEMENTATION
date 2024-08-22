s = "(}" 
stack = []  
pairs = {')': '(', '}': '{', ']': '['}

is_valid = True  

for char in s:
    if char in pairs.values():  
        stack.append(char)
    elif char in pairs:  
        if stack and stack[-1] == pairs[char]:
            stack.pop()
        else:
            is_valid = False
            break

if stack:  
    is_valid = False

print(is_valid)
