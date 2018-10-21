import matplotlib.pyplot as plt
X = [1,2,3,4,5,6,7,8,9]
Y = [2,3,4,7,1,9,20,2,5]
fig = plt.figure()
ax1 = fig.add_axes([0.1,0.1,0.8,0.8])# left, bottom, width, height :::: This is for main axis
ax2 = fig.add_axes([0.3,0.4,0.2,0.4])# left, bottom, width, height :::: This is for main axis
### main fig
ax1.plot(X,Y,'green')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_title('main_graph')
ax1.grid(linewidth = 0.5 ,color = 'red',alpha = 0.6,linestyle = 'dashed')
##inserted
ax2.plot(X,Y,'red')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_title('inserted_graph')
plt.grid(linewidth = 0.5 ,color = 'black',alpha = 0.6,linestyle = 'dashed')
plt.show(fig)

