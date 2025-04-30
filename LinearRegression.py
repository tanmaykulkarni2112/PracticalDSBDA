import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
import seaborn as sns
from sklearn.linear_model import LinearRegression

# when reading from dataset x = iris['sepal_length'].values.reshape(-1,1)

arr = [[2,22], [4,44], [6,66],[8,88]]
df = pd.DataFrame(arr, columns = ['area', 'price'])
plt.scatter(df.area, df.price)
plt.xlabel('area')
plt.ylabel('price')
model = LinearRegression()
model.fit(df[['area']], df.price)
print(model.score(df[['area']],df.price))
model.predict([[10]])

# -----------------
iris = sns.load_dataset('iris')
x= iris['sepal_length'].values.reshape(-1,1)
y = iris['sepal_width']

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.1)
model = LinearRegression()
model.fit(x_train,y_train)
model.score(x_test,y_test)
mse = mean_squared_error(y_test, model.predict(x_test))
print(mse)
