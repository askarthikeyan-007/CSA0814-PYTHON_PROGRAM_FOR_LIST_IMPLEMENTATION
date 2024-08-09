import string
sentence = input("Enter a sentence: ")
css = ''.join(e.lower() for e in sentence if e.isalpha())
as = set(string.ascii_lowercase)
ss = set(css)
pangram = as.issubset(ss)
print(pangram)
