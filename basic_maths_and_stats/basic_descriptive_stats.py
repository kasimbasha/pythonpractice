import os
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import scipy
from scipy import stats

inputfile = os.getcwd()+os.path.sep+"mtcars.csv"
cars = pd.read_csv(inputfile)
cars.columns = ["car_names","mpg","cyl","disp","hp","drat","wt","qsec","vs","am","gear","carb"]
print(cars.sum())
print(cars.sum(axis=1))
print(cars.median())

mpg = cars['mpg']