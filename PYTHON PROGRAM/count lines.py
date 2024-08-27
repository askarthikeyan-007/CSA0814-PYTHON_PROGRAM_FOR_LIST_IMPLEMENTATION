def count_lines(sentence):
  return sentence.count('\n')+1 if sentence else 0
input_sentence = '\n this is python code.\n this is 2nd python code.\n this is 3rd python code'
print(count_lines(input_sentence))
