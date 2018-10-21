import numpy as np
import matplotlib.pyplot as plt
X = np.linspace(-2 * np.pi, 2 * np.pi, 70, endpoint=True)
F1 = np.sin(2* X)
F2 = (2*X**5 + 4*X**4 - 4.8*X**3 + 1.2*X**2 + X + 1)*np.exp(-X**2)
# get the current axes, creating them if necessary:
ax = plt.gca()
# making the top and right spine invisible:
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
# moving bottom spine up to y=0 position:
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data',0))
# moving left spine to the right to position x == 0:
ax.xaxis.set_ticks_position('bottom')
ax.spines['left'].set_position(('data',0))
plt.plot(X, F1)
plt.plot(X, F2)
plt.show()