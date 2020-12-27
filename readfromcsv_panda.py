import pandas as pd 
import os
time_cols = ['tpep_dropoff_datetime', 'tpep_pickup_datetime']
filepath = os.getcwd()+os.path.sep+'taxi.csv.bz2'

def load_df(file_name):
    return pd.read_csv(file_name, parse_dates=time_cols)

print(load_df(filepath).head())


def iter_df(file_name):
    yield from pd.read_csv(file_name, parse_dates=time_cols, chunksize=100)


for i, df in enumerate(iter_df(filepath)):
    if i > 10:
        break
    print(len(df))