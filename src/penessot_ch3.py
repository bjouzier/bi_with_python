import numpy as np
import pandas as pd

pd.set_option('display.max_columns', 10)
#dataframe=pd.read_csv('data/Sales Transaction v.4a.csv')
dataframe=pd.read_csv('data/Comptes_Perso_2023_Cloture.csv'
                      , sep=';', decimal=',')
#print(dataframe.head().transpose())
#print(type(dataframe.head()))
#print(dataframe.head()[['ProductName','Price']])
#print(dataframe.iloc[1:19,[1,4,5]])

#loc admet un filtre comme argument
#le second indice de loc est la liste des colonnes attendues, ici
#on utilise l'attribut columns pour els avoir toutes
#équivalent de select * from dataframe where Cpte <> 'BIL'
print(dataframe.loc[dataframe['Cpte'] != 'BIL',dataframe.columns].head())
#identique à
print(dataframe.loc[dataframe['Cpte'] != 'BIL'].head())
# si on veut un select date,doc,montant where dataframe where Cpte <> 'BIL'
print(dataframe.loc[dataframe['Cpte'] != 'BIL',['Date','Doc','Montant']].head())
#autre syntaxe pour le filtre
print(dataframe[dataframe['Cpte'] != 'BIL']
               [['Date','Doc','Montant','Cpte']].head())
# Avec numpy (plus performant si on a beaucoup de données)
myFilter = np.where((dataframe['Cpte'] != 'BIL') & (dataframe['SsCpte'] == 2))

print(dataframe.loc[myFilter].head())    