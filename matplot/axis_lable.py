import matplotlib.pyplot as plt
import random

x  = [i for i in range(1,10)]
y = [random.randint(20,45) for _ in range(1,10)]
plt.xlabel('DAY')
plt.ylabel('Temparature')
plt.plot(x,y,color = 'orange',marker = 'o')
plt.show()