#################################
## LET'S PLAY WITH COLUMNS ######
#################################
import pandas as pd
import numpy as np
from data_frame import *
# we just imported data_frame to avoid extra effort
#print(city_frame)
#  We can retreive column names as a list
p = city_frame.columns.values
#print(p)
############ we can change index names by passing a list
custom_index = ["first", "second", "third", "fourth",
            "fifth", "sixth", "seventh", "eigth",
            "ninth", "tenth", "eleventh", "twelvth",
            "thirteenth"]

city_custom = pd.DataFrame(cities, index= custom_index)
#print(city_custom)
### Fixing order for columns
city_order1 = pd.DataFrame(cities,columns=['population',
                                           'name','country'])
#print(city_order)
city_order2 = pd.DataFrame(cities,columns=['name','population',
                                           'country'])
#print(city_order2)
########## change names with rename method
city_frame.rename(columns = {"country":'REGION', "population":'TOTAL'},inplace = True)
#print(city_frame)
########################################################
####  we can turn column into index by set_index method#
########################################################
city_new1 = city_order1.set_index('name')
#print(city_new1)
######### inplace  set to true ###############
city_frame.set_index('name',inplace = True)
###########################################################################################
# if inplace is true the original data frame itself will be converted to                 ##
# new data frame otherwise it returns new data frame,                                    ##
#  which we store in new variable                                                        # #
############################################################################################
                                                                                         
#print(city_frame)