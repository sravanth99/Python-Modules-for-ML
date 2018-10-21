import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
gaussian_value = np.random.normal(size = 10000)
'''
plt.hist(gaussian_value,color = 'red',
        bins=100,density='true',stacked='true',
        edgecolor = 'black',
        cumulative='ture')'''
f = plt.figure()
ax  = f.add_subplot(1,1,1,projection = '3d',facecolor = 'red')
ax.bar([1,2,3,4], [1,4,9,16],color = 'black')
ax.set_title('graph')

plt.show()