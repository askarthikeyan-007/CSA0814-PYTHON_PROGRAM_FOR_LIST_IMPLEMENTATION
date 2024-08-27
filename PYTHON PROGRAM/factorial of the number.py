num = 10;
factorial = 1;
if num < 0:
  print("error")
elif num == 0:
  print("the number of factorial is 1 or 0 ")
else:
  for i in range (1,num+1):
    factorial = factorial*i
print("the factorial of the num is" ,factorial)
  
