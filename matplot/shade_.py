import numpy as np
import matplotlib.pyplot as plt
X = np.linspace(0,2*np.pi,endpoint= True)
Y = np.sin(X)
plt.plot(X,Y,'red')
####### shading     regions between with fill_between
plt.fill_between(X,0,Y,color = 'black',alpha = 1.)
plt.show()