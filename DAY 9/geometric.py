sequence = [2,6,18,54]
a=sequence[1]/sequence[0]
flag=0
for i in range(1,len(sequence)-1):
    if sequence[i+1]/sequence[i]!=a:
        flag=1
        break
if flag==0:
    print("It is a Geometric Progression")
else:
    print("It is not a Geometric Progression")
        
