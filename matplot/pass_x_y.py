# we can pass our x and y values to the plot
import matplotlib.pyplot as plt
x = [ i for i in range(800,1000)]
y = [ i**-1 for  i in range(800,1000) ]
plt.plot(x,y,color = 'r',marker = '_')
plt.show()