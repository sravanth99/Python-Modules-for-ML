import pandas as pd
# the actual meaning of csv is comma seperated values
## similarly the meaning of dsv is delimeter  seperated values 
#Pandas offers two ways to read in CSV or DSV files to be precise:
#  1. DataFrame.from_csv
#  2. read_csv
## in general we'll use read_csv more often
exchange_rates = pd.read_csv("dollar_euro.txt",
                             sep="\t")
# here tabspace is the seperator so we used '\t'
# print(exchange_rates)
exchange_rates1 = pd.read_csv("dollar_euro.txt",
                             sep="\t",
                             header = 0,
                             index_col= 0,
                             names = ['new','Average','Min','Max','No_of_days'],
                             )
# to skip first line we'll header
# header key word takes int and is used to extract the data 
# from a particular row till end 
# index_col is used  set desired column as index to our dataframe

print(exchange_rates1)
