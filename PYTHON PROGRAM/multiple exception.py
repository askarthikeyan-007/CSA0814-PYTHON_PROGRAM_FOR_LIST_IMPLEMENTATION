a = 10
b = 11
try:
  print(a/f)
except TypeError:
  print("TypeError")
except ZeroDivisionError:
  print("divisible by zero")
except NameError:
  print("NameError")
except :
  print("some exception happened")
  print("answer not found")

  
  
