import numpy as np
from numpy.random import random
import pandas as pd
from pandas import Series, DataFrame
import os

import matplotlib.pyplot as plt
from matplotlib import rcParams

x = range(1,10)
y = [1,2,3,4,0,4,3,2,1]

plt.plot(x,y)

inputfile = os.getcwd()+os.path.sep+"mtcars.csv"
cars = pd.read_csv(inputfile)
cars.columns = ["car_names","mpg","cyl","disp","hp","drat","wt","qsec","vs","am","gear","carb"]
mpg = cars['mpg']
mpg.plot()

df = cars[["cyl","disp","hp"]]
df.plot()

plt.bar(x,y)

mpg.plot(kind="bar")

mpg.plot(kind="barh")

p = [1,2,3,4,0.5]
plt.pie(p)
plt.show()

plt.pie(p)
plt.savefig('save_chart.png')
plt.show()