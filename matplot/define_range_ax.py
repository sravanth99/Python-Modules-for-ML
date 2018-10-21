import matplotlib.pyplot as plt
import random
x = list(range(1,11))
y1 = [random.randint(30,35) for _ in range(1,11) ]
y2 = [random.randint(10,30) for _ in range(1,11)]
plt.plot(x,y1,'-b', 
        x,y2,'ok')
#print(plt.axis())######### checking the range of axes
# setting axes values for the following values
xmin , xmax, ymin, ymax = 0, 11, 0, 50
plt.axis([xmin,xmax,ymin,ymax])
#print(plt.axis())


plt.show()

