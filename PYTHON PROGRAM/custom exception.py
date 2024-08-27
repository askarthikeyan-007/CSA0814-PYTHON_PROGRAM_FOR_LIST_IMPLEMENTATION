num = 18
try:
  age = 19
  if num<age:
    raise("eligible for voting")
  else:
    print("invalid age exception")
except:
    print("not eligible for voting")
