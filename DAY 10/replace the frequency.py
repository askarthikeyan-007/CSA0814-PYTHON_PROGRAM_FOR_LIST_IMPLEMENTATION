def replace_by_frequency(s):
    from collections import Counter
    freq = Counter(s)
    return ''.join(chr(96 + freq[c]) for c in s)
result = replace_by_frequency("hello")
print(result)  
