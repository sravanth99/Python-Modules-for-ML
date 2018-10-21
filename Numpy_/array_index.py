# indexing in numpy
import numpy as np
arr = np.array([(-1, 2, 0, 4), 
                (4, -0.5, 6, 0), 
                [2.6, 0, 7, 8], 
                [3, -7, 4, 2.0]]) 

# slicing an array
#Array with first 2 rows and alternatecolumns(0 and 2)
#first argument is for rows and and arg is for columns 
sliced_arr = arr[:2,::2]
s = arr[:3]
y = arr[:,2::1]
x = arr[:,2::1][:2]
#print(x)
'''
slicing creates a original view of actual array elements so if we cheange
Them the original one will be effected
'''
list_ = [sliced_arr,s,y,x]
# checking whether sliced ones have same memory location 
truth_ness = [np.may_share_memory(i,arr) for i  in list_ ]
#print(truth_ness)

# Integer array indexing example 
# it takes two lists one consits of rowindex and second consists col index
int_arr = arr[[1,2,3,0],[2,3,0,1]] #1D array of elements at the indices (1,2), (2,3),(3,0),(0,1)

# boolean array indexing example 
cond =  arr > 1 #cond is a boolean array
#bool_arr is a 1D array of elements from arr which are greater than 1
bool_arr = arr[cond]
