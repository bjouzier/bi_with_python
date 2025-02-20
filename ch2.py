from decimal import Decimal
import pandas as pd

# Specify the delimiter explicitly
data = pd.read_csv('./data/Comptes_Perso_2023_Cloture.csv'
                  , usecols=["Date","Doc","Description","Montant","Cpte","Ss-Cpte","Dest"]
                  , dtype={"Date": "datetim64", "Doc": "int64", "Description": "string"
                          ,"Montant": "float64", "Cpte": "string", "Ss-Cpte": "string", "Dest": "string"}
                  ,sep=';'
                  ,index_col=1)

print(data.columns)
print(data.head(5))
print(data.shape)
print(data.index)
print(data.dtypes)


