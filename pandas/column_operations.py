import pandas as pd
from data_frame import *
##############################
## Sum and Cummulative Sum  ##
##############################
# we can do sum for all columns or for particular columns
#########################################################
Sum_all = city_frame.sum()
#print(Sum_all)
############ now we'll do sum for particular column
Sum_pop = city_frame['population'].sum()
#print(Sum_pop)
########### to calculate cummulative sum we'll use cumsum method #######
Cum_sum_pop = city_frame['population'].cumsum()
#print(Cum_sum_pop)
##################################################################################
######## Assigning new values to columns #########################################
##################################################################################
city_frame['population'] = Cum_sum_pop
#print(city_frame)
################################################################
#### accessing columns #####################################
#############################################################
### Method 1
'''city_frame['population']'''
######## Method 2
'''city_frame.population'''
####################################################
############### Sorting dataframe ##################
####################################################
# we can sort dataframe withrespect any value like columnm
####################################################

sort_city = city_frame.sort_values(by = 'population',ascending = False)
#print(sort_city)
## adding columns by insert method####
### we can insert column at specified loaction
## arguments taken by insert method #  
# insert(self, loc, column, value, allow_duplicates=False)`
## allo_duplictes is set false by default
# if allow_dup's is set to true it don't raise exception even if col already in dataframe
# ########################################################################## 
### it only checks for column name not values # #############################
# ########################################################################### 
city_frame.insert(1,'new',city_frame.population,allow_duplicates = False)
#print(city_frame)


 

