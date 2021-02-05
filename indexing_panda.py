import numpy as np 
import pandas as pd 

from pandas import Series, DataFrame

series_obj = Series(np.arange(8),index = ['row 1','row 2','row 3','row 4','row 5','row 6','row 7','row 8',])
print(series_obj)

np.random.seed(25)
DF_obj = DataFrame(np.random.rand(36).reshape((6,6)),
                        index = ['row 1','row 2','row 3','row 4','row 5','row 6'],
                        columns=['Column 1','Column 2','Column 3','Column 4','Column 5','Column 6']
                        )
print(DF_obj)
print(DF_obj.loc[['row 1','row 2'],['Column 1','Column 2']])
print(series_obj['row 3':'row 7'])
print(DF_obj <.2)
print(series_obj[series_obj>6])
series_obj['row 3','row 7'] = 10
print(series_obj)

