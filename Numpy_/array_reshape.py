# Reshaping M X N array to A X B X C array 
# Condition to do that is M X N should be equal to A X B X C 
# ==> sizes should be equal
import numpy as np
array = np.array([[1, 2, 3, 4], 
                [5, 2, 4, 2], 
                [1, 2, 0, 1]]) 
# above one is 3X4 array lets change our array shape to 1 x 6 x 2
newarr = array.reshape(1,6,2)

# Flatten array 
#destroys array to a single dimension array
flarr = array.flatten()
print(flarr)
