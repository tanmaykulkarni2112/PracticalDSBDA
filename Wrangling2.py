import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
arr = [[1,34],[2,50], [3,20], [4, 70], [5, 89], [6,14], [7, None], [8,100]]
df = pd.DataFrame(arr, columns = ['roll', 'marks'])
df['marks'] = df['marks'].fillna(df['marks'].mean())
sns.displot(data = df, x = 'marks')
q1 = df['marks'].quantile(0.25)
q3 = df['marks'].quantile(0.75)
IQR = q3 -q1
lowerbound = q1 -1.5 * IQR
upperbound = q3 +1.5 * IQR
outlier = ((upperbound < df['marks']) | (lowerbound > df['marks']))
df['marks'] = np.where(outlier, df['marks'].mean(), df['marks'])
