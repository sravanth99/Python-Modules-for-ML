import numpy as np 
########## save txt and load txt fuctions

x = np.array([[1, 2, 3], 
              [4, 5, 6],
              [7, 8, 9]], np.int32)


np.savetxt('my_file.txt',x)
### we can change the format by passing some keyword args

np.savetxt('test1.txt',x,fmt='%.3f',delimiter=',')
np.savetxt('test2.txt',x,fmt='%04d',delimiter=' *')
############################################################
####  |THe complete syntax of the savetxt fumction 
### savetxt(fname, X, fmt='%.18e', delimiter=' ', newline='\n', header='', footer='', comments='# ')
np.savetxt('test3.txt',x,fmt='%.3f',delimiter=' ',
          header='The array is:',
          footer='Thank you') 

############## Loadtxt to read files 
my_r = np.loadtxt('my_file.txt')
#print(my_r)
t1 = np.loadtxt('test1.txt',delimiter=',') #  we should use the same delimeter 
#which is used at the time of creation
#print(t1)
t2 = np.loadtxt('test3.txt',delimiter=' ',usecols= (0,2))
#print(t2)
################################# Tofile ###############
dt = np.dtype([('time', [('min', int), ('sec', int)]),
               ('temp', float)])
x = np.zeros((1,), dtype=dt)
x['time']['min'] = 10
x['temp'] = 98.25
#print(x)
fh = open("test6.txt", "bw")
x.tofile(fh)
############################# best way to load and save data
from tempfile import TemporaryFile
outfile = TemporaryFile()
x = np.arange(10)
np.save(outfile,x)
outfile.seek(0) # Only needed here to simulate closing & reopening file
p = np.load(outfile)
#print(p)