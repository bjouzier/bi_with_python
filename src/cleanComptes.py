import pandas as pd
import pandasql as ps
#import numpy as np
from decimal import Decimal

df = pd.read_csv('data/Comptes_Perso_2023_Cloture.csv', sep=';', decimal=',')
# le format est obligatoire parceque par défut il interprète MDY
# le dt.normalize permet que l'heure soit toujorus 00:00:00, on ne gange 
# pas de place mais ergonomiquement la date s'affiché sans l'heure
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y').dt.normalize()
df['Montant'] = df['Montant'].replace({' ': '', '€': '', ',': '.'}, regex=True)
df['Montant'] = df['Montant'].astype(float)
df['SsCpte'] = df['SsCpte'].astype(str).str.zfill(2)
# convert_dtypes permet de convertir les colonnes en types de données
# les plus appropriés
df = df.convert_dtypes()
# On ajoute une colonne pour l'exercice, cela permettra d'avoir un clé unique Ex+Doc
df['Ex'] = df['Date'].dt.year

#Filtrer pour ne pas prendre les lignes de report à nouveau
# ~ est le not en python
# on ne peut pas écrire df[n not df['Description'].str.contains('Report à nouveau',na=False)]
# car le not est appliqué à la liste des lignes et non à chaque ligne
# na=False permet de ne pas tenir compte des valeurs nulles
# on ne peut pas utiliser le not dans le contains, il faut utiliser ~
print(df.head())
df = df[~df['Description'].str.contains('Report à nouveau',na=False)]
print(df.head())


"""
Dans l'instruction ci-dessous assigne créé une nouvelle colonne. Lambda est 
une fonction anonyme, un callable acceptée par assign.
l'argument de lambda est df, le dataframe lui-même.
"""
df=df.assign(DebitCredit=lambda df:
             df.Montant .case_when([
                    (df.Montant >= 0, 'D'),
                    (df.Montant < 0, 'C')
             ])
             
    )
"""
Autres synaxes possibles :
df['DebitCredit'] = df['Montant'].apply(lambda x: 'D' if x >= 0 else 'C')   

# Use case_when to create the DebitCredit column
df['DebitCredit'] = df['Montant'].case_when(
    [
        (df['Montant'] >= 0, 'D'),
        (df['Montant'] < 0, 'C')
    ],
)
"""
print(df.info())
print(df.head())
#On change montant en Decimal pour éviter les pb de float en e+xx
"""
Ci-dessous on utilise pandasql pour faire un group by.
En arrière-fonds pandasql lance un moteur local SQLLite, ce qui est moins
performan que pandas mais plus lisible.
Le type Decimal ne peut pas être mis avant calcul parceque pandasql fait un insert
dans une table sqlLite et le format décimal n'est pas reconnu : le insert échoue.
"""
df_grouped = ps.sqldf(('Select Cpte,SSCpte,sum(Montant)/12 as MontantMensuel,count(*) as nbLines '
                        'from df group by Cpte,SsCpte order by Cpte')
                        , locals())  # `locals()` is used to pass the DataFrame to the SQL query
df_grouped['MontantMensuel']=df_grouped['MontantMensuel'].apply((lambda x: round(Decimal(x),2)))
print(df_grouped.info())
print(df_grouped.head())
df_grouped2=df.groupby(['Cpte','SsCpte'])[['Montant']].sum()
df_grouped2 = df_grouped2.reset_index() # pour avoir les colonnes Cpte et SsCpte
#cela sort les colonnes de l'index, qui est recréé comme in undex de base 0,1,2,3...
print(df_grouped2.info())
print(df_grouped2.head())

#Recherche de valeurs aberrantes du montant
data=df['Montant'].transform(abs) # on prend la valeur absolue
Q1 = data.quantile(0.25)
Q3 = data.quantile(0.75)
IQR = Q3 - Q1
limit_sup = Q3 + 1.5 * IQR
#Q3np = np.percentile(data, 25) marche aussi
print("Q1 : ",Q1)
print("Q3 : ",Q3)
print("IQR : ",IQR)
print("limit_sup",limit_sup)
filtered_data = data[(data < Q1 - 1.5 * IQR) | (data > Q3 + 1.5 * IQR)]

