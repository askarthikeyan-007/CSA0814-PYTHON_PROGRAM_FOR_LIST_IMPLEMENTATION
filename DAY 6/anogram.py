str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
css1 = ''.join(str1.lower().split())
css2 = ''.join(str2.lower().split())
ana= sorted(css) == sorted(css)
if ana:
    print("it is anagrams.')
else:
    print("it is not anagrams.')
