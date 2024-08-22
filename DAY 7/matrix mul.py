import numpy as np


matrix1 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

matrix2 = np.array([
    [9, 10, 11],
    [12, 13, 14],
    [15, 16, 17]
])


result = np.dot(matrix1, matrix2)


print(result)
