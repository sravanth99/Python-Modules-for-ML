###### in this we'll deal with missing data
# isnull and  notnull methods
import pandas as pd
my_cities = ["London", "Paris", "Zurich", "Berlin", 
             "Stuttgart", "Hamburg"]
cities = {"London":   8615246, 
          "Berlin":   3562166, 
          "Madrid":   3165235, 
          "Rome":     2874038, 
          "Paris":    2273305, 
          "Vienna":   1805681, 
          "Bucharest":1803425, 
          "Hamburg":  1760433,
          "Budapest": 1754000,
          "Warsaw":   1740119,
          "Barcelona":1602386,
          "Munich":   1493900,
          "Milan":    1350680}

S = pd.Series(cities,index = my_cities)
#print(S.isnull())
#print(S.notnull())
##################### we'll use dropna method 
#To drop all nan or null values from our series
S_drop = S.dropna()

#print(S)
#print(S_drop)

#############################################
# filling missing data by fillna method
# first argument takes value to fill in it can be anything 
S_fill = S.fillna('I filled data')

#print(S_fill)
# we can convert float to int by using astype method
S_fill_int = S.fillna(0).astype(int)
#print(S_fill_int)
# To fill different values to differnt indices 
# we should pass dictionary to fillna method
fill_dict = {'Zurich':'I filled data for zurich','Stuttgart':'Done with stgt'}
S_fill_data = S.fillna(fill_dict).astype(str)
#print(S_fill_data)
