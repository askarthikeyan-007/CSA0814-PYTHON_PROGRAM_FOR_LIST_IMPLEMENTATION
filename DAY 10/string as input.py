def insert_symbols(s):
    return ''.join(c + ('^' if c in 'aeiou' else '@') for c in s)

input_string = "hello"
output_string = insert_symbols(input_string)
print(output_string) 
