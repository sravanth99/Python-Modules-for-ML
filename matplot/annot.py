import numpy as np
import matplotlib.pyplot as plt
X = np.linspace(-2 * np.pi, 3 * np.pi, 70, endpoint=True)
F1 = np.sin(X)
F2 = 3 * np.sin(X)
ax = plt.gca()
plt.xticks( [-6.28, -3.14, 3.14, 6.28],
        [r'$-2\pi$', r'$-\pi$', r'$+\pi$', r'$+2\pi$'])
plt.yticks([-3, -1, 0, +1, 3])
x = 3 * np.pi / 4
plt.scatter([x,],[3 * np.sin(x),], 50, color ='red')
plt.annotate(r'$(3\sin(\frac{3\pi}{4}),\frac{3}{\sqrt{2}})$',
         xy=(x, 3 * np.sin(x)), 
         xycoords='data',
         xytext=(+20, +20), 
         textcoords='offset points', 
         fontsize=15,
         arrowprops=dict(facecolor='green'))
plt.plot(X, F1, label="$sin(x)$")
plt.plot(X, F2, label="$3 sin(x)$")
plt.legend(loc='upper left')
plt.show()