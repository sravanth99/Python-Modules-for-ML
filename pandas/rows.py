###     we now see the row operation
from data_frame import *
import pandas as pd
row = city_frame.loc[1]
# here we extracted data from row with index as 1
#print(row)
### we can pass a list of indices to extract data from multiple rows 
row_multiple = city_frame.loc[range(2,5)] 
#print(row_multiple)
### now we do boolean masking for our row 
row_bool = city_frame.loc[city_frame.country == 'Spain']
### here we got all rows with country name as Spain
#print(row_bool)
