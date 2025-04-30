import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import seaborn as sns
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB

iris = sns.load_dataset('iris')
x= iris.drop(columns = 'species')
y = iris['species']

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.1)
model = GaussianNB()
model.fit(x_train,y_train)
print(model.score(x_test,y_test))
cm = confusion_matrix(y_test, model.predict(x_test))
print(cm)
