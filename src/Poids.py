import pandas as pd
import locale


df = pd.read_csv('data/Poids.csv', sep=';', decimal=',')
#Dans le format python %A est le jour de la semaine, %B le nom du mois
current_locale = locale.getlocale(locale.LC_TIME)

try:
    # Définir temporairement la locale en français
    #les dates dans le fichier étant 'mardi 19 décembre 2019'
    #la locale fr_FR.UTF-8 ne fonctionne pas sur décembre (elle fonctionne sur novembre)
    #la locale fra fonctionne sur décembre aussi
    #locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')
    locale.setlocale(locale.LC_TIME, 'fra')
    # Exemple de données avec les dates
    #dt.normalize met l'heure à 00:00:00
    df['Date'] = pd.to_datetime(df['Date'], format='%A %d %B %Y').dt.normalize()
finally:
    # Restaurer la locale initiale
    locale.setlocale(locale.LC_TIME, current_locale)
df=df.set_index('Date')
#A partir de là il n'y a plus de colonne Date c'est l'index
df['year'] = df.index.year
df['month'] = df.index.month
df['day_of_week'] = df.index.day_name()
print(df.info())
print(df.head(20))
print(df.loc['2025-02-01':'2025-02-28'])
#gaps identifie les trous dans la série.
#C'est une série qui vaut True si la différence par rapport à la date précédente est > 1
gaps=df.index.to_series().diff().dt.days > 1 
print(gaps)
print(df[(df['Poids Matin'] < 75) & (df['Poids Soir'] > 75)]) #pour le OU c'est |
print(df[df['Poids Matin'] - df['Poids Soir'] > 1]) #Jours ou la différence est > 1
print(df[-(df['Poids Matin'] - df['Poids Soir'] > 1)]) #- ou ~ pour le not	
print(df[df['month'].isin([2,3])].head()) #Le in direct ne marche pas
print(df.sort_values(by='Poids Soir', ascending=False).head())
#Tri par la différence entre deux colonnes
df_sorted = df.loc[(df['Poids Soir'] - df['Poids Matin']).sort_values(ascending=False).index]
df.groupby('day_of_week').mean()
# Regrouper par 'day_of_week' et calculer les statistiques demandées
df['Prise poids'] = df['Poids Soir'] - df['Poids Matin']
df_grouped = df.groupby("day_of_week").agg(
    nombre_lignes=("Poids Soir", "count"),
    premiere_date=("day_of_week",lambda x: df.loc[df["day_of_week"] == x.iloc[0]].index.min()),
    derniere_date=("Poids Soir", "mean"),
    prise_poids_moyenne=("Prise poids","mean"),
    poids_moyen=("Poids Soir", "mean"),
    poids_min=("Poids Soir", "min"),
    poids_max=("Poids Soir", "max"),
).reset_index()
print(df_grouped.sort_values(by='prise_poids_moyenne', ascending=False)[['day_of_week','prise_poids_moyenne']])
