########## linspace to define x
import numpy as np
import matplotlib.pyplot as plt
X = np.linspace(0,2*np.pi,endpoint= True)
Y1 = np.cos(X)
Y2  = np.tan(X)
plt.plot(X,Y1,'ko')
plt.plot(X,Y1)
plt.plot(X,Y2,'b*')
plt.plot(X,Y2)
plt.axis([-0.1,2*np.pi+0.1,-2,2])
plt.show()