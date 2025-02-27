import numpy as np
import pandas as pd

dataframe=pd.read_csv('data/Sales Transaction v.4a.csv')
print(dataframe.shape)
#print(dataframe.duplicated().head())
#print(dataframe.duplicated().sum())
df2=dataframe.drop_duplicates(subset=['TransactionNo','Date'],keep='first')
print(df2.shape)
print(df2.head())


