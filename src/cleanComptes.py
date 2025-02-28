import pandas as pd
import pandasql as ps
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
