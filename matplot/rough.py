import  matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
X = np.arange(1,30)
Y  = [np.sin(x) for x in X]
plt.figure(facecolor='black')
plt.subplot()
plt.plot(X,Y,'or',Y,X,'og')
plt.show()