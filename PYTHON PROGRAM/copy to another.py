import shutil
source_file= 'same.txt'
destination_file = 'destination.txt'
shutil.copy(source_file,destination_file)
with open('destination.txt','r')as file:
  content = file.read()
  print(content)
