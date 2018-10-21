import numpy as np
import matplotlib.pyplot as plt
 
 
# get the current axes, creating them if necessary:
ax = plt.gca()
# set the locations and labels of the xticks
plt.xticks( np.arange(4), 
           ('Berlin', 'London', 'Hamburg', 'Toronto') )
plt.yticks([0,0.5,1.,1.5]) # #   customising y ticks 
 
plt.show('green')