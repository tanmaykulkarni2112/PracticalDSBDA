import pandas as pd
import numpy as np
arr = [[10,True, "Male"],[20,True, "Male"],[30,True, "Male"],[11,False, "Female"], [None, True, None]]
df = pd.DataFrame(arr, columns = ['Age', 'Pass', 'Gender'])
print(df['Age'].mean())
print(df['Age'].median())
print(df['Age'].mode()[0])
print(df.isnull())
df['Age'] = df['Age'].fillna(df.Age.mean())
df['Gender'] = df['Gender'].fillna(df['Gender'].mode()[0])
fdf = df[df['Gender'] == 'Female'] ##
fdf = fdf.drop('Pass', axis = 'columns')
fdf['Gender']= fdf['Gender'].map({'Male' : 1, 'Female' : 0}) ##
fdf['Gender'].dtype
df['Gender'].shape
