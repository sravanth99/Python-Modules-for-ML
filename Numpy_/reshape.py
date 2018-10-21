import numpy as np
A = np.array([[3, 4, 5],
              [1, 9, 0],
              [4, 6, 8]],order='F')
B = np.array([[8, 6, 4],
              [0, 86, 0],
              [41, 62, 83]],order='F')
s = np.dstack((A, B))

p = np.tile(A,reps=(2,2))
print(p)