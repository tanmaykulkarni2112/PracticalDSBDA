import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

iris = sns.load_dataset('iris')
x = iris.drop(columns = 'species')
y = iris['species']
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.2)

model = LogisticRegression()
model.fit(x_train,y_train)
print(model.score(x_test, y_test))
cm = confusion_matrix(y_test, model.predict(x_test))
cm
