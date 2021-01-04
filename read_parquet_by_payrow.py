import os
import pyarrow.parquet as pq 
filepath = os.getcwd()+os.path.sep+'taxi.parquet'
table = pq.read_table()
df = table.to_pandas()
print(df.dtypes)
print(df.head())