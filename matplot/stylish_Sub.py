import matplotlib.pyplot as plt
import numpy as np


def g(t):
    return np.log10(t)
fig = plt.figure(figsize=(4,4),facecolor= 'red',edgecolor='yellow')
x  = list(range(10))
sub1 = fig.add_subplot(221,facecolor = 'pink',alpha = 1.)

sub1.set_title('Sub1',color = 'white',size = 16) # setting title to the plot
'''sub1.text(0.5,0.5,
          'SUB 1',
          va = 'center',
          ha = 'center',
          alpha = .8,
          color = 'black'
          ,fontsize = 20)'''

sub1.plot(x,g(x))
#### we'll zoom in sub1 by setting x and y ticks
sub3 = fig.add_subplot(222,facecolor = 'pink',alpha = 1.)
sub3.set_xticks([0,0.3,0.6,0.9,1.2]) 

sub3.set_yticks([-0.25,-0.1,0.5]) 
x = np.arange(0,1.5,0.2)
sub3.plot(x,g(x))

sub2 = fig.add_subplot(224,facecolor = 'pink',alpha = 1.)
sub2.set_xticks([]) 
sub2.set_yticks([]) 
sub2.text(0.5,0.5,
          'SUB 2',
          va = 'center',
          ha = 'center',
          alpha = .8,
          color = 'black'
          ,fontsize = 20)
fig.tight_layout() #   looks good!!! imagines as if all grids are filled
plt.show()