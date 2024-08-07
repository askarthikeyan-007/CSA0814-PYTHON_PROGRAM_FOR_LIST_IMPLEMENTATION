sentence = "welcome to sse"
result = '.'.join([word[0].upper()+'.'*(len(word)-1) for word in sentence.split()])
print(result)