import pandas as pd

# Specify the delimiter explicitly
"""
data = pd.read_csv('./data/Comptes_Perso_2023_Cloture.xlsm'
                  , usecols=["Date","Doc","Description","Montant","Cpte","Ss-Cpte","Dest"]
                  , dtype={"Doc": "int64", "Description": "string"
                          ,"Montant": str, "Cpte": "string", "Ss-Cpte": "string", "Dest": "string"}
                  ,sep=';'
                  ,index_col=1
                  ,parse_dates=True)
"""
data = pd.read_excel('./data/Comptes_Perso_2023_Cloture.xlsm'
                  ,sheet_name="Journal"
                  , usecols=["Date","Doc","Description","Montant","Cpte","Ss-Cpte","Dest"]
                  , dtype={"Doc": "int64", "Description": "string"
                          ,"Montant": float #en lisant depuis Excel le nombre est bien 
                          #numérique, en csv c'est un chaine a ause des blancs et du €
                          , "Cpte": "string", "Ss-Cpte": "string", "Dest": "string"}
                  ,index_col=1
                  ,parse_dates=True)
#print(data.columns)
#print(data.head(6))
#print(data.shape)
#print(data.dtypes)
print(data)


