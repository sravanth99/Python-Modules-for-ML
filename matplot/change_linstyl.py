import numpy as np
import matplotlib.pyplot as plt
X = np.linspace(0,2*np.pi,endpoint= True)
F1 = 3 * np.sin(X)
F2 = np.sin(2*X)
F3 = 0.3 * np.sin(X)
F4 = np.cos(X)
plt.plot(X,F1,'o','red')
plt.plot(X,F2,'--','thickblack')
plt.plot(X,F3,'grey')
plt.plot(X,F4,'magenta','*')
plt.show()