import pandas as pd
df=pd.read_csv('data/Comptes_Perso_2023_Cloture.csv', sep=';', decimal=',')
# le format est obligatoire parceque par défut il interprète MDY
# le dt.normalize permet que l'heure soit toujorus 00:00:00, on ne gange 
# pas de place mais ergonomiquement la date s'affiché sans l'heure
df['Date']=pd.to_datetime(df['Date'], format='%d/%m/%Y').dt.normalize()
df['Montant']=df['Montant'].replace({' ': '', '€': '', ',': '.'}, regex=True)
df['Montant']=df['Montant'].astype(float)
df['SsCpte']=df['SsCpte'].astype(str).str.zfill(2)
#convert_dytpes permet de convertir les colonnes en types de données
# les plus appropriés
df=df.convert_dtypes()
#On ajoute une colonne pour l'exercice, cela permettra d'avoir un clé unique Ex+Doc
df['Ex']=df['Date'].dt.year
print(df.info())
print(df.head())