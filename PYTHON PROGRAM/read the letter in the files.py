try:
  with open('same.txt','r')as file:
    content = file.read()
    print(content)
except exception as e:
    print(e)
