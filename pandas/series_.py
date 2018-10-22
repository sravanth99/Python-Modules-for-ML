import pandas as pd
import numpy as np
fruits = ['peaches', 'oranges', 'cherries', 'pears']
S = pd.Series([1, 33, 52, 10], index=fruits)
#print((S + 3)* 4)
#print(S['peaches'])
S1 = S.apply(np.log)
#print(S1)
#filter with booleans
#print(S[S < 50])