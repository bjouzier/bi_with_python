#import missingno as msno
import pandas as pd

#dataframe=pd.read_csv('data/Sales Transaction v.4a.csv')
dataframe=pd.read_csv('data/Comptes_Perso_2023_Cloture.csv'
                     , sep=';', decimal=',')
#print(dataframe.info())
#print(dataframe.isna().head())
#print(dataframe.isna().sum())
#print(type(dataframe.isna().sum()))
#msno.matrix(dataframe)
print(dataframe.dtypes)
#mean_value = dataframe.mean(numeric_only=True) #mean only numeric columns
#print(mean_value)




