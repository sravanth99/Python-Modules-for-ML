import pandas as pd
import matplotlib.pyplot as plt

#### Let's deal with datastructures 
#Series and
#DataFrame
#series is 1d data structure usaed by pandas
# returns index and actual data when we pass a list to it
arr = pd.Series([1,22,33,556,89,10,87],dtype= 'float')
#print(arr)
#We can directly access the index and the values of our Series S:#
#print(arr.index)
#print(arr.values)
fruits = ['apple','mango','guava','pomogranite','orange']
price = [20,15,5,20,10]
S  = pd.Series(price,index= fruits)
plt.figure(facecolor='green')
plt.subplot()
#plt.axis('off')
plt.xticks([])
plt.yticks([])
plt.plot(fruits ,price,'or')
plt.show()
#4704474536