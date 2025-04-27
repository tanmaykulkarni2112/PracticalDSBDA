import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
import seaborn as sns
from sklearn.linear_model import LinearRegression

arr = [[2,22], [4,44], [6,66],[8,88]]
df = pd.DataFrame(arr, columns = ['area', 'price'])
plt.scatter(df.area, df.price)
plt.xlabel('area')
plt.ylabel('price')
model = LinearRegression()
model.fit(df[['area']], df.price)
print(model.score(df[['area']],df.price))
model.predict([[10]])
