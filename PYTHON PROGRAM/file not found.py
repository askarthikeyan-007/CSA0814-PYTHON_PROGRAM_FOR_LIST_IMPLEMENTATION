try:
  with open('same.txt','r')as file:
    content = file.read()
    print(content)
except Exception as e:
    print(e)
    
