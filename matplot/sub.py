import matplotlib.pyplot as plt

python_course_green = "green"
plt.figure(figsize=(6, 4))
plt.subplot(221,facecolor = 'green') # equivalent to: plt.subplot(2, 2, 1)
plt.text(0.5, # x coordinate, 0 leftmost positioned, 1 rightmost
         0.5, # y coordinate, 0 topmost positioned, 1 bottommost
         'subplot(2,2,1)', # the text which will be printed
         horizontalalignment='center', # shortcut 'ha' 
         verticalalignment='center', # shortcut 'va'
         fontsize=20, # can be named 'font' as well
         alpha=.5 # float (0.0 transparent through 1.0 opaque)
         ,color  = 'black'
         )
plt.subplot(224,facecolor = 'red')
plt.xticks(())# to get rid of x and y ticks
plt.yticks(())
plt.text(0.5, 0.5, 
         'subplot(2,2,4)', 
         ha='center', va='center',
         fontsize=20, 
         color="y")
plt.subplot(223,facecolor = 'yellow')
plt.xticks(())# to get rid of x and y ticks
plt.yticks(())
plt.text(0.5, 0.5, 
         'subplot(2,2,3)', 
         ha='center', va='center',
         fontsize=20, 
         color="y")


plt.show()