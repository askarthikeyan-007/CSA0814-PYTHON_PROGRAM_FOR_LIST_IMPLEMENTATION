str1 = "paper"
str2 = "title"
isomorphic = len(str1) == len(str2) and len(set(str1)) == len(set(str2)) == len(set(zip(str1, str2)))
print(isomorphic)str1 = "abca"
str2 = "zbxz"
isomorphic = len(str1) == len(str2) and len(set(str1)) == len(set(str2)) == len(set(zip(str1, str2)))
print(isomorphic)

str1 = "foo"
str2 = "bar"
isomorphic = len(str1) == len(str2) and len(set(str1)) == len(set(str2)) == len(set(zip(str1, str2)))
print(isomorphic)
