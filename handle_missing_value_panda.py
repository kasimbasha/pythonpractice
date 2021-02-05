import pandas as pd
import numpy as np
from pandas import Series, DataFrame

missing = np.nan
seris_obj = Series(['row 1','row 2',missing,'row 3','row 4','row 5','row 6',missing,'row 8'])
print(seris_obj)
print(seris_obj.isnull)
np.random.seed(25)
DF_obj = DataFrame(np.random.rand(36).reshape((6,6)))
print(DF_obj)
DF_obj.loc[3:5,0] = missing
DF_obj.loc[1:4,5] = missing
print(DF_obj)
fillna_DR = DF_obj.fillna(0)
print(fillna_DR)
fillna_DR = DF_obj.fillna({0:0.1,5:1.35})
print(fillna_DR)

#print (
'''
*******
remove duplicate
*****
'''
#)

DF_obj2 = DataFrame({'Column 1':[1,1,1,2,2,2,3,3,3],
'Column 2':['a','a','a','b','b','b','c','c','c'],
'Column 3':['A','A','A','B','B','B',"C","C","C"]})
print(DF_obj2)
print(DF_obj2.duplicated())
print(DF_obj2.drop_duplicates())
print(DF_obj2)

'''
*******
Concatination and transfermation
*****
'''
DF_obj3 = pd.DataFrame(np.arange(36).reshape(6,6))
print(DF_obj3)
DF_obj4 = pd.DataFrame(np.arange(15).reshape(5,3))
print(DF_obj4)
print(pd.concat([DF_obj3,DF_obj4],axis=1))
print(pd.concat([DF_obj3,DF_obj4]))
''' Drop columns'''
print(DF_obj3.drop([0,2]))
print(DF_obj3.drop([0,2],axis=1))
''' Adding '''
seris_obj1 = Series(np.arange(6))
seris_obj1.name = 'added_coloumn'
var_DF = DataFrame.join(DF_obj3,seris_obj1)
print(var_DF)

''''
Grouping and aggregation
'''''

