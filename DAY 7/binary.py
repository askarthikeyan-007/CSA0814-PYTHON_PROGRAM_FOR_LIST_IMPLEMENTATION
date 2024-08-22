binary1 = "1010"
binary2 = "1101"


num1 = int(binary1, 2)
num2 = int(binary2, 2)


sum = num1 + num2


binary_sum = bin(sum)[2:]

print( binary_sum)
