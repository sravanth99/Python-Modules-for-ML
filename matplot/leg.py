import numpy as np
import matplotlib.pyplot as plt

plt.plot(np.log([x for x in range(1,10)]),'ob',label = 'sine')
plt.plot(np.log10([x for x in range(1,10)]),'or',label = 'cosine')
plt.legend(loc = 'best')
plt.show()