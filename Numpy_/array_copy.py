import numpy as np
###########
'''
Array copying
'''
x = np.array([[42,22,12],[44,53,66]], order='C')
y = x.copy()
x[0,0] = 1001
#print(x)
#print(y)

