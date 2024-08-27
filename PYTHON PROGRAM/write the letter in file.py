try:
  with open('same.txt','w')as file:
    content = file.write('unreal is the best game developing software')
    print(content)
except exception as e:
  print(e)
