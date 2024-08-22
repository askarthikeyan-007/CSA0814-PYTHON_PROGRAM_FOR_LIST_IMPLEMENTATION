n=3
n1=5
a=[]
for i in range(1,500):
    if i%n==0 or i%n1==0:
        a.append(i)
c=sum(a)
print("sum of multiply of 3 and 5:",c)
