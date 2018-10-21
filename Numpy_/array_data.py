import numpy as np
'''
The elements of the list 'lst' are turned into i16 types 
to create the two-dimensional array A
'''
i = np.dtype(np.int32)

arr = np.empty((4,4),i)
#print(arr)
#print(i)
##########################################################################################
######           STRUCTURED ARRAYS                                                  ######
###########################################################################################
'''
We Now create a structured array with the 'density' column.

'''
dt = np.dtype([('density',np.int32)])
struc_arr = np.array([[1,2],[2,3],[4,5],[6,7],[89,9]],dtype=dt)
#print(struc_arr)
#print(struc_arr['density'])
'''
Now we will add the country name(string), 
the area(int) and the population number(int) to our data type:
'''
dt = np.dtype([('Country','S20'),('density','i4'),('Area','i4'),('Population','i4')])
population_table = np.array([
    ('Netherlands', 393, 41526, 16928800),
    ('Belgium', 337, 30510, 11007020),
    ('United Kingdom', 256, 243610, 62262000),
    ('Germany', 233, 357021, 81799600),
    ('Liechtenstein', 205, 160, 32842),
    ('Italy', 192, 301230, 59715625),
    ('Switzerland', 177, 41290, 7301994),
    ('Luxembourg', 173, 2586, 512000),
    ('France', 111, 547030, 63601002),
    ('Austria', 97, 83858, 8169929),
    ('Greece', 81, 131940, 11606813),
    ('Ireland', 65, 70280, 4581269),
    ('Sweden', 20, 449964, 9515744),
    ('Finland', 16, 338424, 5410233),
    ('Norway', 13, 385252, 5033675)],
    dtype=dt)
'''
we'll get corresponding data by entering name assigned to that particular data
'''
###country names
#print(population_table['Country'])
#print(population_table['density'])
#print(population_table['Area'])
#print(population_table['Population'])

### lets plot these values
'''
import matplotlib.pyplot as plt
plt.plot(population_table['Area'])
plt.show()
'''
############## UNICODE STRINGS ##############################
'''
To get unicode strings we exchange 'S20' with the definition "('country', np.unicode, 20)"
'''
dt = np.dtype([('Country',np.unicode,20),('density','i4'),('Area','i4'),('Population','i4')])
population_table_unicode = np.array([
    ('Netherlands', 393, 41526, 16928800),
    ('Belgium', 337, 30510, 11007020),
    ('United Kingdom', 256, 243610, 62262000),
    ('Germany', 233, 357021, 81799600),
    ('Liechtenstein', 205, 160, 32842),
    ('Italy', 192, 301230, 59715625),
    ('Switzerland', 177, 41290, 7301994),
    ('Luxembourg', 173, 2586, 512000),
    ('France', 111, 547030, 63601002),
    ('Austria', 97, 83858, 8169929),
    ('Greece', 81, 131940, 11606813),
    ('Ireland', 65, 70280, 4581269),
    ('Sweden', 20, 449964, 9515744),
    ('Finland', 16, 338424, 5410233),
    ('Norway', 13, 385252, 5033675)],
    dtype=dt)

#print(population_table_unicode['Country']) # text mode with unicoding
#print(population_table['Country']) # it is in binary mode without unicoding
