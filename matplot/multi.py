import matplotlib.pyplot as plt
import random
from mpl_toolkits.mplot3d import Axes3D
x = list(range(1,11))
y1 = [random.randint(30,35) for _ in range(1,11) ]
y2 = [random.randint(10,30) for _ in range(1,11)]
f = plt.figure()
p = f.add_subplot(1,1,1,projection = '3d')
p.plot(x,y1,'ob',
x,y2,'or')


plt.show()

