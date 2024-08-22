str1="treele"
str2="home"
str3=""
length=max(len(str1),len(str2))
for i in range(length):
    if i<len(str1):
        str3+=str1[i]
    if i<len(str2):
        str3+=str2[i]
print(str3)
