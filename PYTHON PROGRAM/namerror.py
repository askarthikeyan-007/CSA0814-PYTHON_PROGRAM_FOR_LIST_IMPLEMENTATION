a = 5
b =10
try:
  print(a/c)
  print(a**b)
except TypeError:
  print("type error")
except ZeroDivisionError:
  print("divided by zero")
except Exception as e:
  print(e)
except:
  print("some exception occured")
  print("welcome")
