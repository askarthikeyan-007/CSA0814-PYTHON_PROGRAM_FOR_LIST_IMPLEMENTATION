#import numpy by install pip install numpy
import numpy as np
mat=[[0,3,0,0],
    [4,0,0,6],
    [2,0,7,6],
    [5,8,9,3]]
mat=np.array(mat)
print(np.sum(np.max(mat,axis=1)))
