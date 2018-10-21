######### importing numpy
import numpy as np

#######basic array characteristics
array = np.array([[1,2,0],    # Creating array object
         [3,4,1],
         (1,2,3)])

#print(array)
'''
# Printing type of arr object 
print(type(array))
# Printing array dimensions (axes) 
print(array.ndim)
# Printing shape of array 
print(array.shape)
# Printing size (total number of elements) of array 
print(array.size)
# Printing type of elements in array 
print(array.dtype)
'''

###lests form a dict to specify characteristics of array
my_dict = dict(array_type=type(array),
               dimension = array.ndim,
               shape_of_array= array.shape,
               size = array.size,
               type_of_elements=array.dtype)
#print(my_dict)
'''
let's plot some values'''
import matplotlib.pyplot as plt
plt.plot(array)
plt.show()
###############################
'''
indices are taken as x coordinates &
values are taken as y coordinates
'''