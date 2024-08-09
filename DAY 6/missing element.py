import string
sentence = input("Enter a sentence: ")
css = ''.join(e.lower() for e in sentence if e.isalpha())
as = set(string.ascii_lowercase)
ss = set(css)
missing = as - ss
if missing:
    print( ', '.join(sorted(missing)))
else:
    print("The sentence is already a pangram.")