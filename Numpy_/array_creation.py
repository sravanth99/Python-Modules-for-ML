#There are several ways to create arrays

import numpy as np
# Creating array from list with type float
array_list = np.array([[1,2,3],
                 [2,4,6]],dtype='float')

# Creating array from tuple
array_tuple = np.array(((1,2,3),
                 (2,4,6)),dtype='float')

# we can use both at once ==> we can use tuple and list together 
# Creating a 5X4 array with all zeros 
#by default all values are floats
array_0 = np.zeros((5,4))
#print(array_0)

# Creating a constant value array of complex type
array_comp = np.full((4,4),7,dtype='complex')


# Create an array with random values 
array_random = np.random.random((4,3))

# Create a sequence of integers  
# from x to y with steps of z 
# arange takes 4 arguments (start,stop,step,dtype)
array_seq_int = np.arange(1,7,2,dtype= None)
#print(array_seq_int)

# Create a sequence of 10 evenly spaced values in range x to y
#linspace takes 6 arguments(start,stop,num=50,endpoint=True,retstep=False,dtype=None)
#values filled inthe  keyargs are bydefault we can change them according to our need
array_seq = np.linspace(1,9,10,retstep=True)
#print(array_seq)
'''
a scalar is a zero dimensional array
'''
x = np.array(7)
#print(x,np.ndim(x))

'''
There is another interesting way to create an array with Ones or with Zeros, 
if it has to have the same shape as another existing array 'a'

'''

p = np.array([1,2,3,4,5,6,67,8,9,8,20,78])
new = np.ones_like(p)
new_1 = np.zeros_like(p)
#print(new,new_1)
'''
using empty function
it creates array of arbitrary values in desired dimension
'''
new_E = np.empty((4,4))
#print(new_E)
#################################
'''
identity array
'''
######## identity function
id_arr = np.identity(8)
#print(id_arr)
###########eye function
'''
eye returns an ndarray of shape (N,M). 
All elements of this array are equal to zero,
 except for the 'k'-th diagonal, 
whose values are equal to one.
'''
eye_arr = np.eye(4,5, k =0,dtype='float')
#print(eye_arr)