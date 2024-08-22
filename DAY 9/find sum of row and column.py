import numpy as np
mat=[[1,2,3],
    [4,5,6],
    [7,8,9]]
mat=np.array(mat)
print(np.sum(np.sum(mat,axis=1)))
print(np.sum(np.sum(mat,axis=0)))
print(np.sum(np.diagonal(mat)))
