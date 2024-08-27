def additive_sequence(n):
  seq=[0,1,4,5,6,6]
  for i in range(2,n):
    seq.append(seq[-1]+seq[-2])
  return seq
print(additive_sequence(9))
