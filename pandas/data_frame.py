# ' A DataFrame has both a row and a column index.'
#Like a spreadsheet or Excel sheet, 
# a DataFrame object contains an ordered collection of columns.
#  Each column consists of a unique data typye, 
# but different columns can have different types, 
# e.g. the first column may consist of integers, 
# while the second one consists of boolean values and so on.
import pandas as pd
#A DataFrame can be seen as a concatenation of Series, 
# each Series having the same index, i.e. the index of the DataFrame.
N = [0,1,2,3]
result1 = pd.Series([2479.984, 2998.01, 3496.893, 3119.5], index=N)
result2 = pd.Series([1203.45, 3476.62, 3007.83, 3619.5], index=N)
result3 = pd.Series([39812.412, 3981.16, 3457.19, 1963.0], index=N)
main = pd.concat([result1,result2,result3])
#print(main)
#lets deal with axis by default it is set to 0
main = pd.concat([result1,result2,result3],axis=1)
#print(main)
# let's give name to columns
col = ['zero','one','two']
main.columns = col
#print(main)
### dataframe from dict
#### A DataFrame has a row and column index; 
# it's like a dict of Series with a common index.
cities = {"name": ["London", "Berlin", "Madrid", "Rome", 
                   "Paris", "Vienna", "Bucharest", "Hamburg", 
                   "Budapest", "Warsaw", "Barcelona", 
                   "Munich", "Milan"],
          "population": [8615246, 3562166, 3165235, 2874038,
                         2273305, 1805681, 1803425, 1760433,
                         1754000, 1740119, 1602386, 1493900,
                         1350680],
          "country": ["England", "Germany", "Spain", "Italy",
                      "France", "Austria", "Romania", 
                      "Germany", "Hungary", "Poland", "Spain",
                      "Germany", "Italy"]}
city_frame = pd.DataFrame(cities)
#print(city_frame)




