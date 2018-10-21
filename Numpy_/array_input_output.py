import numpy as np
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
##########################################################
# we'll write our data to a csv file
np.savetxt("population_table.csv",
           population_table_unicode,
           fmt="%s;%d;%d;%d",           
           delimiter=";")

#######################Read file
x = np.genfromtxt('population_table.csv',dtype=dt,delimiter=";")

#print(x)
'''There is also a function "loadtxt", 
but it is more difficult to use, 
because it returns the strings as binary string
To overcome this problem, 
we can use loadtxt with a converter function for the first column.
'''
y = np.loadtxt('population_table.csv',dtype=dt,converters={0: lambda _: _.decode('utf-8')},delimiter=";")
#print(y)
